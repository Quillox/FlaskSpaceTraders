from flask import Blueprint, render_template

from app.models.agent import Agent, Ship

fleet_bp = Blueprint('fleet', __name__, url_prefix='/fleet')

@fleet_bp.route('/<symbol>')
def show(symbol):
    agent = Agent.query.filter_by(symbol=symbol).first()
    # Ship.add_agent_fleet_to_db(agent_symbol=symbol, token=agent.token)
    fleet = agent.fleet
    return render_template('fleet/show.html', agent=agent, fleet=fleet)