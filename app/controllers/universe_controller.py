from flask import Blueprint, render_template, request, redirect, url_for
from app.models.universe import Faction, Shipyard, System, Waypoint
from app.models.agent import Agent

universe_bp = Blueprint('universe', __name__, url_prefix='/universe')

# TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGlmaWVyIjoiUFNZTU9OIiwidmVyc2lvbiI6InYyIiwicmVzZXRfZGF0ZSI6IjIwMjMtMDctMTUiLCJpYXQiOjE2ODk4MzI2MTQsInN1YiI6ImFnZW50LXRva2VuIn0.ZjrcqkmxpdR1pkMe4qd1fcbhlRAZ4tlKB0e6R3aVC59hswC2knw5PIH6Dq_KYMaSHHSc0Yx71htZV9VQVn-2AoUtpfoMNvYavKC2wpw4MtaugU1dsvqliTC4TJPBs_XLLMMQ3hfEuFR8f0FszhqajrZPWiPSkyp1y7Vw4qe2k7G9lGlevWVZBa68CDatlhFjMobM0eVcfJU8ONfyeVP3LNVVQRAZJVAMicToY7UoJAmf6mHCqHSdLP8VkY44hze5tyxhuwexsWbApSq_DOLGYPQpXcmvU3QqHwCdHd02EU7LDHKJisbbgpjPxW6vFRfmpnHiVrUOLod_4VN33_vi0g'
# if not Agent.validate_token(TOKEN):
#     TOKEN = Agent.get_new_token_api()

@universe_bp.route('/')
def index():
    return render_template('universe/index.html')


@universe_bp.route('/factions')
def faction_index():
    factions = Faction.query.all()
    return render_template('universe/faction/index.html', factions=factions)

@universe_bp.route('factions/<symbol>')
def faction_show(symbol):
    faction_data = Faction.get_faction_data(symbol)
    if faction_data is None:
        return 'Faction not found', 404
    return render_template('universe/faction/show.html', faction_data=faction_data)

@universe_bp.route('/', methods=['POST'])
def populate_tables_api():
    if Agent.query.first() is None:
        token = Agent.get_new_token_api()
    else:
        token = Agent.query.first().token
        if not Agent.validate_token(token):
            token = Agent.get_new_token_api()
    if 'populate_factions' in request.form:
        Faction.populate_tables(token)
    if 'populate_jump_gates' in request.form:
        Waypoint.add_jump_gates_api(token)
    elif 'populate_systems' in request.form:
        System.populate_tables(token)
    return render_template('universe/index.html')

@universe_bp.route('/systems')
def system_index():
    max_x = System.query.order_by(System.x.desc()).first().x
    max_y = System.query.order_by(System.y.desc()).first().y
    min_x = System.query.order_by(System.x.asc()).first().x
    min_y = System.query.order_by(System.y.asc()).first().y
    systems = System.query.all()
    return render_template('universe/system/index.html', systems=systems, max_x=max_x, max_y=max_y, min_x=min_x, min_y=min_y)

@universe_bp.route('/<symbol>')
def system_show(symbol):
    system = System.query.filter_by(symbol=symbol).first()
    if system is None:
        return 'System not found', 404
    return render_template('universe/system/show.html', system=system)


@universe_bp.route('/shipyard')
def shipyard_index():
    shipyards = Shipyard.query.all()
    return render_template('universe/shipyard/index.html', shipyards=shipyards)
