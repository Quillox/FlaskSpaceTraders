import requests

from flask import Blueprint, render_template, request, redirect, url_for

from app.models.agent import Contract
from app.models.agent import Agent
from app.models.fleet import Ship, AgentShipLink
from app.models.universe import Faction


home_bp = Blueprint('home', __name__)

@home_bp.route('/', methods=['GET', 'POST'])
def add_or_register_agent():
    if request.method == 'POST':
        print(request.form)
        if 'symbol' in request.form:
            symbol = request.form['symbol']
            faction = request.form['faction']
            email = request.form['email']
            response = requests.post('https://api.spacetraders.io/v2/register', json={'symbol': symbol, 'faction': faction, 'email': email})
            print(response.json())
            if response.status_code == 201:
                # Token
                token = response.json()['data']['token']

                # Faction
                # Populate factions table if it is empty
                if len(Faction.query.all()) == 0:
                    Faction.populate_tables(token)

                # Agent
                agent_data = response.json()['data']['agent']
                Agent.add_agent_to_database(agent_data, token)
                agent = Agent.query.filter_by(account_id=agent_data['accountId']).first()

                # Contract
                contract_data = response.json()['data']['contract']
                Contract.add_contract_to_database(contract_data, agent.symbol, token)

                # Ship
                Ship.add_ship_to_db(response.json()['data']['ship'], token)
                AgentShipLink.add_agent_ship_link_to_db(
                    agent_symbol=agent.symbol,
                    ship_symbol=response.json()['data']['ship']['symbol'])


                return redirect(url_for('home.register_success'))
            else:
                return render_template('home/registration_failed.html', error_message=response.json()['error']['message'])
        elif 'agent_token' in request.form:
            token = request.form['agent_token']
            success, error_message = add_new_agent_to_database(token)
            if success:
                return redirect(url_for('home.add_agent_success'))
            else:
                return render_template('home/add_agent_failed.html', error_message=error_message)
        else:
            return render_template('home/add_or_register_agent.html')
    else:
        return render_template('home/add_or_register_agent.html')

@home_bp.route('/register_success')
def register_success():
    return render_template('home/register_success.html')

def add_new_agent_to_database(token):
    agent_response = requests.get('https://api.spacetraders.io/v2/my/agent', headers={'Authorization': f'Bearer {token}'})
    if agent_response.status_code == 200:
        agent_data = agent_response.json()['data']
        if Agent.query.filter_by(account_id=agent_data['accountId']).first() is not None:
            return False, 'Agent already exists in database'
        else:
            # Faction
            # Populate factions table if it is empty
            if len(Faction.query.all()) == 0:
                Faction.populate_tables(token)
            
            # Agent
            Agent.add_agent_to_database(agent_data, token)

            # Fleet
            Ship.add_agent_fleet_to_db(agent_symbol=agent_data['symbol'], token=token)
    else:
        return False, agent_response.json()['error']['message']

    contract_response = requests.get('https://api.spacetraders.io/v2/my/contracts', headers={'Authorization': f'Bearer {token}'})
    if contract_response.status_code == 200:
        for contract_data in contract_response.json()['data']:
            print(contract_data)
            Contract.add_contract_to_database(contract_data, agent_data['symbol'], token)

    return True, None

@home_bp.route('/add_agent_success')
def add_agent_success():
    return render_template('home/add_agent_success.html')

@home_bp.route('/add_agent_failed')
def add_agent_failed():
    return render_template('home/add_agent_failed.html')
