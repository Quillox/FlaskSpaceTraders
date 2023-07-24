import requests
import random

from app import db
from app.models.universe import FACTION_SYMBOL_ENUM
from app.models.universe import Waypoint
from app.models.universe import TradeGood
from app.models.fleet import TRADE_GOOD_SYMBOL_ENUM
from app.models.fleet import Ship
from app.models.fleet import TRADE_GOOD_SYMBOL_ENUM
from app.models.fleet import AgentShipLink


CONTRACT_TYPE = (
    'PROCUREMENT',
    'TRANSPORT',
    'SHUTTLE'
)

CONTRACT_TYPE_ENUM = db.Enum(
    *CONTRACT_TYPE,
    name='contract_type'
)


class AgentContractLink(db.Model):
    __tablename__ = 'agent_contract_link'
    agent_symbol = db.Column(db.String(50), db.ForeignKey(
        'agent.symbol'), primary_key=True)
    contract_id = db.Column(db.String(50), db.ForeignKey(
        'contract.id'), primary_key=True)

    @staticmethod
    def add_agent_contract_link_to_database(agent_symbol, contract_id):
        if AgentContractLink.query.filter_by(agent_symbol=agent_symbol, contract_id=contract_id).first() is not None:
            return None
        agent_contract_link = AgentContractLink(
            agent_symbol=agent_symbol,
            contract_id=contract_id
        )
        db.session.add(agent_contract_link)
        db.session.commit()
        print(
            f'AgentContractLink {agent_contract_link.agent_symbol} {agent_contract_link.contract_id} added to database')
        return agent_contract_link


class Agent(db.Model):
    token = db.Column(db.String(600), unique=True, nullable=False)
    account_id = db.Column(db.String(50), nullable=False)
    symbol = db.Column(db.String(50), unique=True,
                       nullable=False, primary_key=True)
    headquarters = db.Column(db.String(50), db.ForeignKey(
        'waypoint.symbol'), nullable=False)
    credits = db.Column(db.Integer, unique=True, nullable=False)
    starting_faction = db.Column(
        db.String(50), db.ForeignKey('faction.symbol'), nullable=False)
    contracts = db.relationship(
        'Contract',
        secondary='agent_contract_link',
        primaryjoin=(AgentContractLink.agent_symbol == symbol),
        lazy='subquery',
        backref=db.backref('agents', lazy=True))
    fleet = db.relationship(
        'Ship',
        secondary='agent_ship_link',
        primaryjoin=(AgentShipLink.agent_symbol == symbol),
        lazy='subquery',
        backref=db.backref('agents', lazy=True))

    @staticmethod
    def get_agent_data_api(token):
        agent_response = requests.get('https://api.spacetraders.io/v2/my/agent', headers={
                                      'Authorization': f'Bearer {token}'})
        if agent_response.status_code == 200:
            return agent_response.json()['data']
        else:
            return None
    
    @staticmethod
    def get_agent_contracts_api(token):
        # TODO add page handling
        agent_contracts_response = requests.get('https://api.spacetraders.io/v2/my/contracts?limit=20', headers={
                                      'Authorization': f'Bearer {token}'})
        if agent_contracts_response.status_code == 200:
            return agent_contracts_response.json()['data']
        else:
            return None

    @staticmethod
    def add_agent_to_database(agent_symbol, token):
        agent_data = Agent.get_agent_data_api(token)
        if agent_data is None:
            return None
        agent = Agent(
            account_id=agent_data['accountId'],
            symbol=agent_data['symbol'],
            headquarters=agent_data['headquarters'],
            credits=agent_data['credits'],
            starting_faction=agent_data['startingFaction'],
            token=token
        )
        db.session.add(agent)
        db.session.commit()
        print(f'Agent {agent.symbol} added to database')

        # Add the agent's contracts to the database
        contract_data = Agent.get_agent_contracts_api(token)
        if contract_data is None:
            return None
        for contract in contract_data:
            Contract.add_contract_to_database(contract, agent.symbol, token)
            AgentContractLink.add_agent_contract_link_to_database(
                agent.symbol, contract['id'])

        return agent

    @staticmethod
    def delete_agent_from_db(symbol):
        agent = Agent.query.filter_by(symbol=symbol).first()
        if agent is None:
            return False

        # Delete all contract links for this agent if they exist
        agent_contract_links = AgentContractLink.query.filter_by(
            agent_symbol=agent.account_id).all()
        for agent_contract_link in agent_contract_links:
            db.session.delete(agent_contract_link)
            db.session.commit()
            print(
                f'AgentContractLink {agent_contract_link.agent_symbol} {agent_contract_link.contract_id} deleted from database')
            
        # Delete the agent-ship links
        agent_ship_links = AgentShipLink.query.filter_by(agent_symbol=agent.symbol).all()
        for agent_ship_link in agent_ship_links:
            db.session.delete(agent_ship_link)
            db.session.commit()
            print(f'AgentShipLink {agent_ship_link.agent_symbol} {agent_ship_link.ship_symbol} deleted from database')

        db.session.delete(agent)
        db.session.commit()
        print(f'Agent {agent.symbol} deleted from database')
        return True

    @staticmethod
    def get_agents_with_contracts(self):
        agents = Agent.query.all()
        result = []
        for agent in agents:
            agent_data = {
                'account_id': agent.account_id,
                'symbol': agent.symbol,
                'headquarters': agent.headquarters,
                'credits': agent.credits,
                'starting_faction': agent.starting_faction,
                'contracts': [contract.id for contract in agent.contracts]
            }
            result.append(agent_data)
        return result

    @staticmethod
    def get_agent_data(symbol):
        agent = Agent.query.filter_by(symbol=symbol).first()
        if agent is None:
            return None
        data = {
            'token': agent.token,  # TODO: Remove this line before production
            'account_id': agent.account_id,
            'symbol': agent.symbol,
            'headquarters': agent.headquarters,
            'credits': agent.credits,
            'starting_faction': agent.starting_faction,
            'contracts': [contract.id for contract in agent.contracts]
        }
        return data

    @staticmethod
    def get_agent_fleet_db(symbol):
        agent = Agent.query.filter_by(symbol=symbol).first()
        if agent is None:
            return None
        fleet = []
        for ship in agent.fleet:
            fleet.append(Ship.get_ship_data(ship.symbol))
        return fleet

    @staticmethod
    def validate_token(token):
        url = "https://api.spacetraders.io/v2/my/agent"
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {token}"
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return True
        else:
            return False
    
    @staticmethod
    def get_new_token_api() -> str:
        # Make a random username
        username = ''.join(random.choice('0123456789ABCDEF') for i in range(14))

        url = "https://api.spacetraders.io/v2/register"
        payload = {
            "faction": "COSMIC",
            "symbol": username,
            "email": "string"
        }
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 201:
            Agent.add_agent_to_database(agent_symbol=username, token=response.json()['data']['token'])
            return response.json()['data']['token']
        else:
            return None

class Contract(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    faction_symbol = db.Column(FACTION_SYMBOL_ENUM, db.ForeignKey(
        'faction.symbol'), nullable=False)
    type = db.Column(CONTRACT_TYPE_ENUM, nullable=False)
    deadline = db.Column(db.DateTime, nullable=False)
    payment_on_accepted = db.Column(db.Integer, nullable=False)
    payment_on_fulfilled = db.Column(db.Integer, nullable=False)
    accepted = db.Column(db.Boolean, nullable=True, default=False)
    fulfilled = db.Column(db.Boolean, nullable=True, default=False)
    deadline_to_accept = db.Column(db.DateTime, nullable=False)

    @staticmethod
    def add_contract_to_database(contract_data, agent_symbol, token):
        # Add the waypoints and trade goods to the database if they don't already exist
        for delivery in contract_data['terms']['deliver']:
            if Waypoint.query.filter_by(symbol=delivery['destinationSymbol']).first() is None:
                Waypoint.add_waypoint_to_db(
                    delivery['destinationSymbol'], token)
            if TradeGood.query.filter_by(symbol=delivery['tradeSymbol']).first() is None:
                # Make a replacement dictionary for the trade good
                trade_good_data = {
                    'symbol': delivery['tradeSymbol'],
                    'name': None,
                    'description': None
                }
                TradeGood.add_trade_good_to_db(trade_good_data)

        # Add the contract to the database if it doesn't already exist
        if Contract.query.filter_by(id=contract_data['id']).first() is not None:
            return None

        contract = Contract(
            id=contract_data['id'],
            faction_symbol=contract_data['factionSymbol'],
            type=contract_data['type'],
            deadline=contract_data['terms']['deadline'],
            payment_on_accepted=contract_data['terms']['payment']['onAccepted'],
            payment_on_fulfilled=contract_data['terms']['payment']['onFulfilled'],
            accepted=contract_data['accepted'],
            fulfilled=contract_data['fulfilled'],
            deadline_to_accept=contract_data['deadlineToAccept']
        )
        db.session.add(contract)
        db.session.commit()
        print(f'Contract {contract.id} added to database')

        # Add relationship between agent and contract to AgentContractLink table
        agent = Agent.query.filter_by(symbol=agent_symbol).first()
        AgentContractLink.add_agent_contract_link_to_database(
            agent.symbol, contract.id)

        # Add row to ContractDeliverGoods table
        for delivery in contract_data['terms']['deliver']:
            contract_deliver_goods = ContractDeliverGoods(
                contract_id=contract.id,
                trade_good_symbol=delivery['tradeSymbol'],
                destination_waypoint_symbol=delivery['destinationSymbol'],
                units_required=delivery['unitsRequired'],
                units_fulfilled=delivery['unitsFulfilled']
            )
            db.session.add(contract_deliver_goods)
            db.session.commit()
            print(
                f'Added delivery term ({contract_deliver_goods.trade_good_symbol}: {contract_deliver_goods.units_required}) for contract {contract.id} to database')

        return contract


class ContractDeliverGoods(db.Model):
    __tablename__ = 'contract_deliver_goods'
    contract_id = db.Column(db.String(50), db.ForeignKey(
        'contract.id'), primary_key=True)
    trade_good_symbol = db.Column(TRADE_GOOD_SYMBOL_ENUM, db.ForeignKey(
        'trade_good.symbol'), primary_key=True)
    destination_waypoint_symbol = db.Column(
        db.String(50), db.ForeignKey('waypoint.symbol'), primary_key=True)
    units_required = db.Column(db.Integer, nullable=False)
    units_fulfilled = db.Column(db.Integer, nullable=False)
