from flask import Blueprint, render_template, flash
from app.models.agent import Agent

from app.models.fleet import Shipyard
from app.models.universe import JumpGate

agent_bp = Blueprint('agent', __name__, url_prefix='/agent')

@agent_bp.route('/')
def index():
    agents = Agent.query.all()
    return render_template('agent/index.html', agents=agents)

@agent_bp.route('/<symbol>')
def show(symbol):
    agent_data = Agent.get_agent_data(symbol)
    if agent_data is None:
        return 'Agent not found', 404
    return render_template('agent/show.html', agent_data=agent_data)

@agent_bp.route('/<symbol>/delete', methods=['POST'])
def delete(symbol):
    success = Agent.delete_agent_from_db(symbol)
    if success:
        flash(f'Agent {symbol} deleted from database', 'success')
    else:
        flash(f'Agent {symbol} not found in database', 'danger')
    agents = Agent.query.all()
    return render_template('agent/index.html', agents=agents)