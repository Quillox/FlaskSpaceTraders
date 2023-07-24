import requests
from time import sleep

from app import db
from app.models.universe import System, get_sector_system_waypoint, Faction, Waypoint
from app.models.universe import TRADE_GOOD_SYMBOL_ENUM, TradeGood

SHIP_ROLE = (
    'FABRICATOR',
    'HARVESTER',
    'HAULER',
    'INTERCEPTOR',
    'EXCAVATOR',
    'TRANSPORT',
    'REPAIR',
    'SURVEYOR',
    'COMMAND',
    'CARRIER',
    'PATROL',
    'SATELLITE',
    'EXPLORER',
    'REFINERY'
)

SHIP_ROLE_ENUM = db.Enum(
    *SHIP_ROLE,
    name='ship_role'
)

SHIP_NAV_STATUS = (
    'IN_TRANSIT',
    'IN_ORBIT',
    'DOCKED'
)

SHIP_NAV_STATUS_ENUM = db.Enum(
    *SHIP_NAV_STATUS,
    name='ship_nav_status'
)

SHIP_FLIGHT_MODE = (
    'DRIFT',
    'STEALTH',
    'CRUISE',
    'BURN'
)

SHIP_FLIGHT_MODE_ENUM = db.Enum(
    *SHIP_FLIGHT_MODE,
    name='ship_flight_mode'
)

SHIP_CREW_ROTATION = (
    'STRICT',
    'RELAXED'
)

SHIP_CREW_ROTATION_ENUM = db.Enum(
    *SHIP_CREW_ROTATION,
    name='ship_crew_rotation'
)

SHIP_FRAME_SYMBOL = (
    'FRAME_PROBE',
    'FRAME_DRONE',
    'FRAME_INTERCEPTOR',
    'FRAME_RACER',
    'FRAME_FIGHTER',
    'FRAME_FRIGATE',
    'FRAME_SHUTTLE',
    'FRAME_EXPLORER',
    'FRAME_MINER',
    'FRAME_LIGHT_FREIGHTER',
    'FRAME_HEAVY_FREIGHTER',
    'FRAME_TRANSPORT',
    'FRAME_DESTROYER',
    'FRAME_CRUISER',
    'FRAME_CARRIER'
)

SHIP_FRAME_SYMBOL_ENUM = db.Enum(
    *SHIP_FRAME_SYMBOL,
    name='ship_frame_symbol'
)

SHIP_REACTOR_SYMBOL = (
    'REACTOR_SOLAR_I',
    'REACTOR_FUSION_I',
    'REACTOR_FISSION_I',
    'REACTOR_CHEMICAL_I',
    'REACTOR_ANTIMATTER_I'
)

SHIP_REACTOR_SYMBOL_ENUM = db.Enum(
    *SHIP_REACTOR_SYMBOL,
    name='ship_reactor_symbol'
)

SHIP_ENGINE_SYMBOL = (
    'ENGINE_IMPULSE_DRIVE_I',
    'ENGINE_ION_DRIVE_I',
    'ENGINE_ION_DRIVE_II',
    'ENGINE_HYPER_DRIVE_I'
)

SHIP_ENGINE_SYMBOL_ENUM = db.Enum(
    *SHIP_ENGINE_SYMBOL,
    name='ship_engine_symbol'
)

SHIP_MODULE_SYMBOL = (
    'MODULE_MINERAL_PROCESSOR_I',
    'MODULE_CARGO_HOLD_I',
    'MODULE_CREW_QUARTERS_I',
    'MODULE_ENVOY_QUARTERS_I',
    'MODULE_PASSENGER_CABIN_I',
    'MODULE_MICRO_REFINERY_I',
    'MODULE_ORE_REFINERY_I',
    'MODULE_FUEL_REFINERY_I',
    'MODULE_SCIENCE_LAB_I',
    'MODULE_JUMP_DRIVE_I',
    'MODULE_JUMP_DRIVE_II',
    'MODULE_JUMP_DRIVE_III',
    'MODULE_WARP_DRIVE_I',
    'MODULE_WARP_DRIVE_II',
    'MODULE_WARP_DRIVE_III',
    'MODULE_SHIELD_GENERATOR_I',
    'MODULE_SHIELD_GENERATOR_II'
)

SHIP_MODULE_SYMBOL_ENUM = db.Enum(
    *SHIP_MODULE_SYMBOL,
    name='ship_module_symbol'
)

SHIP_MOUNT_SYMBOL = (
    'MOUNT_GAS_SIPHON_I',
    'MOUNT_GAS_SIPHON_II',
    'MOUNT_GAS_SIPHON_III',
    'MOUNT_SURVEYOR_I',
    'MOUNT_SURVEYOR_II',
    'MOUNT_SURVEYOR_III',
    'MOUNT_SENSOR_ARRAY_I',
    'MOUNT_SENSOR_ARRAY_II',
    'MOUNT_SENSOR_ARRAY_III',
    'MOUNT_MINING_LASER_I',
    'MOUNT_MINING_LASER_II',
    'MOUNT_MINING_LASER_III',
    'MOUNT_LASER_CANNON_I',
    'MOUNT_MISSILE_LAUNCHER_I',
    'MOUNT_TURRET_I'
)

SHIP_MOUNT_SYMBOL_ENUM = db.Enum(
    *SHIP_MOUNT_SYMBOL,
    name='ship_mount_symbol'
)

SHIP_COMPONENT_SYMBOL = (
    *SHIP_FRAME_SYMBOL,
    *SHIP_REACTOR_SYMBOL,
    *SHIP_ENGINE_SYMBOL,
    *SHIP_MODULE_SYMBOL,
    *SHIP_MOUNT_SYMBOL
)

SHIP_COMPONENT_SYMBOL_ENUM = db.Enum(
    *SHIP_COMPONENT_SYMBOL,
    name='ship_component_symbol'
)

SHIP_MOUNT_DEPOSIT_SYMBOL = (
    'QUARTZ_SAND',
    'SILICON_CRYSTALS',
    'PRECIOUS_STONES',
    'ICE_WATER',
    'AMMONIA_ICE',
    'IRON_ORE',
    'COPPER_ORE',
    'SILVER_ORE',
    'ALUMINUM_ORE',
    'GOLD_ORE',
    'PLATINUM_ORE',
    'DIAMONDS',
    'URANITE_ORE',
    'MERITIUM_ORE'
)

SHIP_MOUNT_DEPOSIT_SYMBOL_ENUM = db.Enum(
    *SHIP_MOUNT_DEPOSIT_SYMBOL,
    name='ship_mount_deposit_symbol'
)

SHIP_TYPE = (
    'SHIP_PROBE',
    'SHIP_MINING_DRONE',
    'SHIP_INTERCEPTOR',
    'SHIP_LIGHT_HAULER',
    'SHIP_COMMAND_FRIGATE',
    'SHIP_EXPLORER',
    'SHIP_HEAVY_FREIGHTER',
    'SHIP_LIGHT_SHUTTLE',
    'SHIP_ORE_HOUND',
    'SHIP_REFINING_FREIGHTER'
)

SHIP_TYPE_ENUM = db.Enum(
    *SHIP_TYPE,
    name='ship_type'
)


class AgentShipLink(db.Model):
    __tablename__ = 'agent_ship_link'
    agent_symbol = db.Column(db.String(50), db.ForeignKey(
        'agent.symbol'), primary_key=True)
    ship_symbol = db.Column(db.String(50), db.ForeignKey(
        'ship.symbol'), primary_key=True)

    @staticmethod
    def add_agent_ship_link_to_db(agent_symbol, ship_symbol):
        # Check if the link is already in the database
        if AgentShipLink.query.filter_by(agent_symbol=agent_symbol, ship_symbol=ship_symbol).first() is None:
            agent_ship_link = AgentShipLink(
                agent_symbol=agent_symbol,
                ship_symbol=ship_symbol
            )
            db.session.add(agent_ship_link)
            db.session.commit()
            print(
                f"Added agent ship link {agent_ship_link.agent_symbol} - {agent_ship_link.ship_symbol} to database")
            return agent_ship_link
        else:
            print(
                f"Agent ship link {agent_symbol} - {ship_symbol} is already in the database")
            return AgentShipLink.query.filter_by(agent_symbol=agent_symbol, ship_symbol=ship_symbol).first()


class Ship(db.Model):
    __tablename__ = 'ship'
    # [AGENT_SYMBOL]-[HEX_ID]
    symbol = db.Column(db.String(50), primary_key=True)
    cargo_capacity = db.Column(db.Integer, nullable=False)
    cargo_current_units = db.Column(db.Integer, nullable=False)
    fuel_capacity = db.Column(db.Integer, nullable=False)
    fuel_current = db.Column(db.Integer, nullable=False)
    registration_id = db.Column(db.Integer, db.ForeignKey(
        'ship_registration.id'), nullable=False)
    registration = db.relationship('ShipRegistration', foreign_keys=[
                                   registration_id], backref='ships')
    nav_id = db.Column(db.Integer, db.ForeignKey(
        'ship_nav.id'), nullable=False)
    nav = db.relationship('ShipNav', foreign_keys=[nav_id], backref='ships')
    nav_route_id = db.Column(db.Integer, db.ForeignKey(
        'ship_nav_route.id'), nullable=False)
    nav_route = db.relationship('ShipNavRoute', foreign_keys=[
                                nav_route_id], backref='ships')
    crew_id = db.Column(db.Integer, db.ForeignKey(
        'ship_crew.id'), nullable=False)
    crew = db.relationship('ShipCrew', foreign_keys=[crew_id], backref='ships')
    main_component = db.relationship('ShipMainComponentLink', backref='ships')
    modules = db.relationship('ShipModuleLink', backref='ship')
    mounts = db.relationship('ShipMountLink', backref='ship')
    inventory = db.relationship('ShipCargoInventory', backref='ship')
    fuel_logs = db.relationship('FuelConsumedLog', backref='ship')

    def __repr__(self):
        return f"<{self.symbol} {self.registration_id} {self.nav_id} {self.nav_route_id} {self.crew_id}>"

    @staticmethod
    def get_ship_data_api(symbol, token):
        url = f"https://api.spacetraders.io/v2/my/ships/{symbol}"

        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {token}"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()['ship']
        else:
            print("Error getting ship from API: ", end="")
            print(response.json())
            return None

    @staticmethod
    def get_agent_fleet_api(token):
        # TODO add page handling
        url = "https://api.spacetraders.io/v2/my/ships"

        querystring = {"page": "1", "limit": "20"}

        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {token}"
        }

        response = requests.get(url, headers=headers, params=querystring)

        if response.status_code == 200:
            return response.json()['data']
        else:
            print("Error getting ships from API: ", end="")
            print(response.json())
            return None

    @staticmethod
    def add_agent_fleet_to_db(agent_symbol, token):
        fleet_data = Ship.get_agent_fleet_api(token)
        if fleet_data is None:
            return None
        else:
            for ship_data in fleet_data:
                Ship.add_ship_to_db(ship_data, token)
                # Link the agent to the ship
                AgentShipLink.add_agent_ship_link_to_db(
                    agent_symbol, ship_data['symbol'])
            return fleet_data

    @staticmethod
    def add_ship_to_db(ship_data, token):
        # Check if the ship is already in the database
        if Ship.query.filter_by(symbol=ship_data['symbol']).first() is None:
            print(f"Adding ship {ship_data['symbol']} to database")

            registration_id = ShipRegistration.add_ship_registration_to_db(
                ship_data)
            ship_nav_id = ShipNav.add_ship_nav_to_db(ship_data)
            ship_nav_route_id = ShipNavRoute.add_ship_nav_route_to_db(
                ship_data, token)
            ship_crew_id = ShipCrew.add_ship_crew_to_db(ship_data)

            ship = Ship(
                symbol=ship_data['symbol'],
                cargo_capacity=ship_data['cargo']['capacity'],
                cargo_current_units=ship_data['cargo']['units'],
                fuel_capacity=ship_data['fuel']['capacity'],
                fuel_current=ship_data['fuel']['current'],
                registration_id=registration_id,
                nav_id=ship_nav_id,
                nav_route_id=ship_nav_route_id,
                crew_id=ship_crew_id,
            )

            db.session.add(ship)
            db.session.commit()

            # Add all of the links to the database
            ShipMainComponentLink.set_ship_main_component_link_in_db(ship_data)
            ShipModuleLink.set_ship_module_link_in_db(ship_data)
            ShipMountLink.set_ship_mount_link_in_db(ship_data)

            # Cargo and fuel
            ShipCargoInventory.set_ship_cargo_inventory_in_db(ship_data)
            FuelConsumedLog.add_fuel_consumed_log_to_db(ship_data)

            db.session.commit()

            print(f"Added ship {ship.symbol} to database")

            return ship
        else:
            print(f"Ship {ship_data['symbol']} is already in the database")
            return ship_data


class ShipRegistration(db.Model):
    __tablename__ = 'ship_registration'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    faction_symbol = db.Column(db.String(50), db.ForeignKey('faction.symbol'))
    role = db.Column(SHIP_ROLE_ENUM, nullable=False)

    def __repr__(self):
        faction_name = Faction.query.filter_by(
            symbol=self.faction_symbol).first().name
        return f'Registered to {faction_name} as {self.role}'

    @staticmethod
    def add_ship_registration_to_db(ship_data):
        ship_registration = ShipRegistration(
            faction_symbol=ship_data['registration']['factionSymbol'],
            role=ship_data['registration']['role']
        )
        db.session.add(ship_registration)
        db.session.commit()
        print(f"Added ship registration {ship_registration.id} to database")
        assert ship_registration.id is not None
        return ship_registration.id


class ShipNav(db.Model):
    __tablename__ = 'ship_nav'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    current_system_symbol = db.Column(
        db.String(50), db.ForeignKey('system.symbol'), nullable=False)
    current_waypoint_symbol = db.Column(
        db.String(50), db.ForeignKey('waypoint.symbol'), nullable=False)
    status = db.Column(SHIP_NAV_STATUS_ENUM, nullable=False)
    flight_mode = db.Column(SHIP_FLIGHT_MODE_ENUM,
                            nullable=False, default='CRUISE')

    def __repr__(self):
        if self.status == 'IN_TRANSIT':
            return f'In transit from {self.current_system_symbol} to {self.current_waypoint_symbol}'
        elif self.status == 'IN_ORBIT':
            return f'In orbit around {self.current_waypoint_symbol}'
        elif self.status == 'DOCKED':
            return f'Docked at {self.current_waypoint_symbol}'
        else:
            return f'Unknown status {self.status}'

    @staticmethod
    def add_ship_nav_to_db(ship_data):
        ship_nav = ShipNav(
            current_system_symbol=ship_data['nav']['systemSymbol'],
            current_waypoint_symbol=ship_data['nav']['waypointSymbol'],
            status=ship_data['nav']['status'],
            flight_mode=ship_data['nav']['flightMode']
        )
        db.session.add(ship_nav)
        db.session.commit()
        print(f"Added ship nav {ship_nav.id} to database")
        return ship_nav.id


class ShipNavRoute(db.Model):
    __tablename__ = 'ship_nav_route'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    destination_waypoint_symbol = db.Column(
        db.String(50), db.ForeignKey('waypoint.symbol'), nullable=False)
    departure_waypoint_symbol = db.Column(
        db.String(50), db.ForeignKey('waypoint.symbol'), nullable=False)
    departure_time = db.Column(db.DateTime, nullable=False)
    arrival_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'Route from {self.departure_waypoint_symbol} to {self.destination_waypoint_symbol}. Departed at {self.departure_time} and arrived at {self.arrival_time}'

    @staticmethod
    def add_ship_nav_route_to_db(ship_data, token):
        route_data = ship_data['nav']['route']

        # Make sure that the relevant systems are in the database
        destination_system = get_sector_system_waypoint(
            route_data['destination']['symbol'])['system']
        destination_system_data = System.get_system_data_api(
            destination_system, token)
        System.add_system_to_db(destination_system_data, token)
        departure_system = get_sector_system_waypoint(
            route_data['departure']['symbol'])['system']
        departure_system_data = System.get_system_data_api(
            departure_system, token)
        System.add_system_to_db(departure_system_data, token)

        ship_nav_route = ShipNavRoute(
            destination_waypoint_symbol=route_data['destination']['symbol'],
            departure_waypoint_symbol=route_data['departure']['symbol'],
            departure_time=route_data['departureTime'],
            arrival_time=route_data['arrival']
        )
        db.session.add(ship_nav_route)
        db.session.commit()
        print(f"Added ship nav route {ship_nav_route.id} to database")
        return ship_nav_route.id


class ShipCrew(db.Model):
    __tablename__ = 'ship_crew'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    current = db.Column(db.Integer, nullable=False)
    required = db.Column(db.Integer, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    rotation = db.Column(SHIP_CREW_ROTATION_ENUM,
                         default='STRICT', nullable=False)
    morale = db.Column(db.Integer, nullable=False)
    wages = db.Column(db.Integer, nullable=False)

    __table_args__ = (
        db.CheckConstraint('morale >= 0 AND morale <= 100'),
        db.CheckConstraint('wages >= 0'),
    )

    def __repr__(self):
        return f'Currently {self.current} crew out of {self.required} required. Ship can hold {self.capacity} crew. Crew rotation is {self.rotation}. Morale is {self.morale}. Wages are {self.wages} credits per hour.'

    @staticmethod
    def add_ship_crew_to_db(ship_data):
        ship_crew = ShipCrew(
            current=ship_data['crew']['current'],
            required=ship_data['crew']['required'],
            capacity=ship_data['crew']['capacity'],
            rotation=ship_data['crew']['rotation'],
            morale=ship_data['crew']['morale'],
            wages=ship_data['crew']['wages']
        )
        db.session.add(ship_crew)
        db.session.commit()
        print(f"Added ship crew {ship_crew.id} to database")
        return ship_crew.id


class ShipMainComponentLink(db.Model):
    __tablename__ = 'ship_main_component_link'
    ship_symbol = db.Column(db.String(50), db.ForeignKey(
        'ship.symbol'), primary_key=True, nullable=False)
    frame_symbol = db.Column(SHIP_FRAME_SYMBOL_ENUM,
                             db.ForeignKey('frame.symbol'), nullable=False)
    reactor_symbol = db.Column(SHIP_REACTOR_SYMBOL_ENUM, db.ForeignKey(
        'reactor.symbol'), nullable=False)
    engine_symbol = db.Column(SHIP_ENGINE_SYMBOL_ENUM,
                              db.ForeignKey('engine.symbol'), nullable=False)

    def __repr__(self):
        frame_name = ShipComponent.query.filter_by(
            symbol=self.frame_symbol).first().name
        frame_description = ShipComponent.query.filter_by(
            symbol=self.frame_symbol).first().description
        reactor_name = ShipComponent.query.filter_by(
            symbol=self.reactor_symbol).first().name
        reactor_description = ShipComponent.query.filter_by(
            symbol=self.reactor_symbol).first().description
        engine_name = ShipComponent.query.filter_by(
            symbol=self.engine_symbol).first().name
        engine_description = ShipComponent.query.filter_by(
            symbol=self.engine_symbol).first().description
        return f"{self.ship_symbol} has frame {frame_name}: {frame_description}, reactor {reactor_name}: {reactor_description}, and engine {engine_name}: {engine_description}"

    @staticmethod
    def set_ship_main_component_link_in_db(ship_data):
        # Make sure that the relevant components are in the database
        Frame.add_frame_to_db(ship_data['frame'])
        Reactor.add_reactor_to_db(ship_data['reactor'])
        Engine.add_engine_to_db(ship_data['engine'])

        # Add the link to the database if it doesn't already exist, otherwise update it
        if ShipMainComponentLink.query.filter_by(ship_symbol=ship_data['symbol']).first() is None:
            ship_main_component_link = ShipMainComponentLink(
                ship_symbol=ship_data['symbol'],
                frame_symbol=ship_data['frame']['symbol'],
                reactor_symbol=ship_data['reactor']['symbol'],
                engine_symbol=ship_data['engine']['symbol']
            )
            db.session.add(ship_main_component_link)
            db.session.commit()
            print(
                f"Added ship main component link {ship_main_component_link.ship_symbol} to database")
            return ship_main_component_link
        else:
            ship_main_component_link = ShipMainComponentLink.query.filter_by(
                ship_symbol=ship_data['symbol']).first()
            ship_main_component_link.frame_symbol = ship_data['frame']['symbol']
            ship_main_component_link.reactor_symbol = ship_data['reactor']['symbol']
            ship_main_component_link.engine_symbol = ship_data['engine']['symbol']
            db.session.commit()
            print(
                f"Updated ship main component link {ship_main_component_link.ship_symbol} in database for ship {ship_main_component_link.ship_symbol}")
            return ship_main_component_link


class ShipModuleLink(db.Model):
    __tablename__ = 'ship_module_link'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ship_symbol = db.Column(db.String(50), db.ForeignKey(
        'ship.symbol'), nullable=False)
    module_symbol = db.Column(SHIP_MODULE_SYMBOL_ENUM,
                              db.ForeignKey('module.symbol'), nullable=False)

    def __repr__(self):
        name = ShipComponent.query.filter_by(
            symbol=self.module_symbol).first().name
        description = ShipComponent.query.filter_by(
            symbol=self.module_symbol).first().description
        return f"{self.ship_symbol} has module {name}: {description}"

    @staticmethod
    def set_ship_module_link_in_db(ship_data):
        # Make sure that the relevant modules are in the database
        for module_data in ship_data['modules']:
            Module.add_module_to_db(module_data)

        # Remove all existing links for this ship
        ShipModuleLink.query.filter_by(
            ship_symbol=ship_data['symbol']).delete()

        # Add the links to the database
        ship_module_link = None
        for module_data in ship_data['modules']:
            new_ship_module_link = ShipModuleLink(
                ship_symbol=ship_data['symbol'],
                module_symbol=module_data['symbol']
            )
            db.session.add(new_ship_module_link)
            db.session.commit()
            print(
                f"Added ship module link {new_ship_module_link.id} to database for ship {new_ship_module_link.ship_symbol}")
            ship_module_link = new_ship_module_link

        return ship_module_link


class ShipMountLink(db.Model):
    __tablename__ = 'ship_mount_link'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ship_symbol = db.Column(db.String(50), db.ForeignKey(
        'ship.symbol'), nullable=False)
    mount_symbol = db.Column(SHIP_MOUNT_SYMBOL_ENUM,
                             db.ForeignKey('mount.symbol'), nullable=False)

    def __repr__(self):
        mount_name = ShipComponent.query.filter_by(
            symbol=self.mount_symbol).first().name
        mount_description = ShipComponent.query.filter_by(
            symbol=self.mount_symbol).first().description
        return f"{self.ship_symbol} has mount {mount_name}: {mount_description}"

    @staticmethod
    def set_ship_mount_link_in_db(ship_data):
        # Make sure that the relevant mounts are in the database
        for mount_data in ship_data['mounts']:
            Mount.add_mount_to_db(mount_data)

        # Remove all existing links for this ship
        ShipMountLink.query.filter_by(ship_symbol=ship_data['symbol']).delete()

        # Add the links to the database
        ship_mount_link = None
        for mount_data in ship_data['mounts']:
            ship_mount_link = ShipMountLink(
                ship_symbol=ship_data['symbol'],
                mount_symbol=mount_data['symbol']
            )
            db.session.add(ship_mount_link)
            db.session.commit()
            print(
                f"Added ship mount link {ship_mount_link.id} to database for ship {ship_mount_link.ship_symbol}")
        return ship_mount_link


class InstallationRequirements(db.Model):
    __tablename__ = 'installation_requirements'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    power = db.Column(db.Integer, nullable=True)
    crew = db.Column(db.Integer, nullable=True)
    slots = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"Power: {self.power}, Crew: {self.crew}, Slots: {self.slots}"

    @staticmethod
    def add_installation_requirements_to_db(requirements_data):
        # Make dictionary to handel None values
        for requirement in ['power', 'crew', 'slots']:
            # If the key doesn't exist, add it with a value of None
            if requirement not in requirements_data:
                requirements_data[requirement] = None
        # Check if the requirements are already in the database
        if InstallationRequirements.query.filter_by(
            power=requirements_data['power'],
            crew=requirements_data['crew'],
            slots=requirements_data['slots']
        ).first() is None:
            installation_requirements = InstallationRequirements(
                power=requirements_data['power'],
                crew=requirements_data['crew'],
                slots=requirements_data['slots']
            )
            db.session.add(installation_requirements)
            db.session.commit()
            print(
                f"Added installation requirements {installation_requirements.id} to database")
            return installation_requirements.id
        else:
            print(
                f"Installation requirements {requirements_data['power']}-{requirements_data['crew']}-{requirements_data['slots']} already in database")
            return InstallationRequirements.query.filter_by(
                power=requirements_data['power'],
                crew=requirements_data['crew'],
                slots=requirements_data['slots']
            ).first().id


class InstallationRequirementsLink(db.Model):
    __tablename__ = 'installation_requirements_link'
    component_symbol = db.Column(SHIP_COMPONENT_SYMBOL_ENUM, db.ForeignKey(
        'ship_component.symbol'), primary_key=True, nullable=False)
    installation_requirements_id = db.Column(db.Integer, db.ForeignKey(
        'installation_requirements.id'), primary_key=True, nullable=False)

    @staticmethod
    def set_installation_requirements_link_in_db(component_symbol, requirements_data):
        # Make sure that the relevant requirements are in the database
        InstallationRequirements.add_installation_requirements_to_db(
            requirements_data)

        # Add the link to the database if it doesn't already exist, otherwise update it
        if InstallationRequirementsLink.query.filter_by(component_symbol=component_symbol).first() is None:
            installation_requirements_link = InstallationRequirementsLink(
                component_symbol=component_symbol,
                installation_requirements_id=InstallationRequirements.add_installation_requirements_to_db(
                    requirements_data)
            )
            db.session.add(installation_requirements_link)
            db.session.commit()
            print(
                f"Added installation requirements link {installation_requirements_link.component_symbol} to database")
            return installation_requirements_link
        else:
            installation_requirements_link = InstallationRequirementsLink.query.filter_by(
                component_symbol=component_symbol).first()
            installation_requirements_link.installation_requirements_id = InstallationRequirements.add_installation_requirements_to_db(
                requirements_data)
            db.session.commit()
            print(
                f"Updated installation requirements link {installation_requirements_link.component_symbol} in database")
            return installation_requirements_link


class ShipComponent(db.Model):
    __tablename__ = 'ship_component'
    symbol = db.Column(SHIP_COMPONENT_SYMBOL_ENUM,
                       primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=True)
    description = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f"{self.symbol} {self.name} {self.description}"

    @staticmethod
    def add_ship_component_to_db(component_data):
        # Check if the component is already in the database
        if ShipComponent.query.filter_by(symbol=component_data['symbol']).first() is None:
            # Make dictionary to handel None values
            for key in ['name', 'description']:
                if key not in component_data:
                    component_data[key] = None
            ship_component = ShipComponent(
                symbol=component_data['symbol'],
                name=component_data['name'],
                description=component_data['description']
            )
            db.session.add(ship_component)
            db.session.commit()
            print(f"Added ship component {ship_component.symbol} to database")
            return ship_component.symbol
        else:
            print(
                f"Ship component {component_data['symbol']} already in database")
            return ShipComponent.query.filter_by(symbol=component_data['symbol']).first().symbol


class Frame(db.Model):
    __tablename__ = 'frame'
    symbol = db.Column(SHIP_FRAME_SYMBOL_ENUM, db.ForeignKey(
        'ship_component.symbol'), primary_key=True, nullable=False)
    condition = db.Column(db.Integer, nullable=False)
    module_slots = db.Column(db.Integer, nullable=False)
    mounting_points = db.Column(db.Integer, nullable=False)
    fuel_capacity = db.Column(db.Integer, nullable=False)

    __table_args__ = (
        db.CheckConstraint('condition >= 0 AND condition <= 100'),
        db.CheckConstraint('module_slots >= 0'),
        db.CheckConstraint('mounting_points >= 0'),
        db.CheckConstraint('fuel_capacity >= 0'),
    )

    def __repr__(self):
        return f"{self.symbol}: {self.condition}/100 condition, {self.module_slots} module slots, {self.mounting_points} mounting points, {self.fuel_capacity} fuel capacity"

    @staticmethod
    def add_frame_to_db(frame_data):
        ShipComponent.add_ship_component_to_db(frame_data)
        InstallationRequirementsLink.set_installation_requirements_link_in_db(
            frame_data['symbol'], frame_data['requirements'])

        # Check if the frame is already in the database
        if Frame.query.filter_by(symbol=frame_data['symbol']).first() is None:
            frame = Frame(
                symbol=frame_data['symbol'],
                condition=frame_data['condition'],
                module_slots=frame_data['moduleSlots'],
                mounting_points=frame_data['mountingPoints'],
                fuel_capacity=frame_data['fuelCapacity']
            )
            db.session.add(frame)
            db.session.commit()
            print(f"Added frame {frame.symbol} to database")
            return frame.symbol
        else:
            print(f"Frame {frame_data['symbol']} already in database")
            return Frame.query.filter_by(symbol=frame_data['symbol']).first().symbol


class Reactor(db.Model):
    __tablename__ = 'reactor'
    symbol = db.Column(SHIP_REACTOR_SYMBOL_ENUM, db.ForeignKey(
        'ship_component.symbol'), primary_key=True, nullable=False)
    condition = db.Column(db.Integer, nullable=False)
    power_output = db.Column(db.Integer, nullable=False)

    __table_args__ = (
        db.CheckConstraint('condition >= 0 AND condition <= 100'),
        db.CheckConstraint('power_output >= 0'),
    )

    def __repr__(self):
        return f"{self.symbol}: {self.condition}/100 condition, {self.power_output} power output"

    @staticmethod
    def add_reactor_to_db(reactor_data):
        ShipComponent.add_ship_component_to_db(reactor_data)
        InstallationRequirementsLink.set_installation_requirements_link_in_db(
            reactor_data['symbol'], reactor_data['requirements'])

        # Check if the reactor is already in the database
        if Reactor.query.filter_by(symbol=reactor_data['symbol']).first() is None:
            reactor = Reactor(
                symbol=reactor_data['symbol'],
                condition=reactor_data['condition'],
                power_output=reactor_data['powerOutput']
            )
            db.session.add(reactor)
            db.session.commit()
            print(f"Added reactor {reactor.symbol} to database")
            return reactor.symbol
        else:
            print(f"Reactor {reactor_data['symbol']} already in database")
            return Reactor.query.filter_by(symbol=reactor_data['symbol']).first().symbol


class Engine(db.Model):
    __tablename__ = 'engine'
    symbol = db.Column(SHIP_ENGINE_SYMBOL_ENUM, db.ForeignKey(
        'ship_component.symbol'), primary_key=True, nullable=False)
    condition = db.Column(db.Integer, nullable=False)
    speed = db.Column(db.Integer, nullable=False)

    __table_args__ = (
        db.CheckConstraint('condition >= 0 AND condition <= 100'),
        db.CheckConstraint('speed >= 1'),
    )

    def __repr__(self):
        return f"{self.symbol}: {self.condition}/100 condition, {self.speed} speed"

    @staticmethod
    def add_engine_to_db(engine_data):
        ShipComponent.add_ship_component_to_db(engine_data)
        InstallationRequirementsLink.set_installation_requirements_link_in_db(
            engine_data['symbol'], engine_data['requirements'])

        # Check if the engine is already in the database
        if Engine.query.filter_by(symbol=engine_data['symbol']).first() is None:
            engine = Engine(
                symbol=engine_data['symbol'],
                condition=engine_data['condition'],
                speed=engine_data['speed']
            )
            db.session.add(engine)
            db.session.commit()
            print(f"Added engine {engine.symbol} to database")
            return engine.symbol
        else:
            print(f"Engine {engine_data['symbol']} already in database")
            return Engine.query.filter_by(symbol=engine_data['symbol']).first().symbol


class Module(db.Model):
    __tablename__ = 'module'
    symbol = db.Column(SHIP_MODULE_SYMBOL_ENUM, db.ForeignKey(
        'ship_component.symbol'), primary_key=True, nullable=False)
    capacity = db.Column(db.Integer, nullable=True)
    range = db.Column(db.Integer, nullable=True)

    __table_args__ = (
        db.CheckConstraint('capacity >= 0'),
        db.CheckConstraint('range >= 0'),
    )

    def __repr__(self):
        return f"{self.symbol}: {self.capacity} capacity, {self.range} range"

    @staticmethod
    def add_module_to_db(module_data):
        ShipComponent.add_ship_component_to_db(module_data)
        InstallationRequirementsLink.set_installation_requirements_link_in_db(
            module_data['symbol'], module_data['requirements'])

        # Check if the module is already in the database
        if Module.query.filter_by(symbol=module_data['symbol']).first() is None:
            # Make dictionary to handel None values
            for data in ['capacity', 'range']:
                # If the key doesn't exist, add it with a value of None
                if data not in module_data:
                    module_data[data] = None

            module = Module(
                symbol=module_data['symbol'],
                capacity=module_data['capacity'],
                range=module_data['range']
            )
            db.session.add(module)
            db.session.commit()
            print(f"Added module {module.symbol} to database")
            return module.symbol
        else:
            print(f"Module {module_data['symbol']} already in database")
            return Module.query.filter_by(symbol=module_data['symbol']).first().symbol


class Mount(db.Model):
    __tablename__ = 'mount'
    symbol = db.Column(SHIP_MOUNT_SYMBOL_ENUM, db.ForeignKey(
        'ship_component.symbol'), primary_key=True, nullable=False)
    strength = db.Column(db.Integer, nullable=True)

    __table_args__ = (
        db.CheckConstraint('strength >= 0'),
    )

    def __repr__(self):
        return f"{self.symbol}: {self.strength} strength"

    @staticmethod
    def add_mount_to_db(mount_data):
        ShipComponent.add_ship_component_to_db(mount_data)
        InstallationRequirementsLink.set_installation_requirements_link_in_db(
            mount_data['symbol'], mount_data['requirements'])

        # Check if the mount is already in the database
        if Mount.query.filter_by(symbol=mount_data['symbol']).first() is None:
            # Make dictionary to handel None values
            for data in ['strength']:
                if data not in mount_data:
                    mount_data[data] = None
            mount = Mount(
                symbol=mount_data['symbol'],
                strength=mount_data['strength']
            )
            db.session.add(mount)
            db.session.commit()
            print(f"Added mount {mount.symbol} to database")

            # Add the mount deposit links to the database
            MountDepositLink.set_mount_deposit_link_in_db(mount_data)

            return mount.symbol
        else:
            print(f"Mount {mount_data['symbol']} already in database")
            return Mount.query.filter_by(symbol=mount_data['symbol']).first().symbol


class MountDepositLink(db.Model):
    __tablename__ = 'mount_deposit_link'
    trade_good_symbol = db.Column(SHIP_MOUNT_DEPOSIT_SYMBOL_ENUM, db.ForeignKey(
        'trade_good.symbol'), nullable=False, primary_key=True)
    mount_symbol = db.Column(SHIP_MOUNT_SYMBOL_ENUM, db.ForeignKey(
        'mount.symbol'), nullable=False, primary_key=True)

    @staticmethod
    def set_mount_deposit_link_in_db(mount_data):
        if 'deposits' not in mount_data:
            return None
        # Make sure that the relevant trade goods are in the database
        for trade_good_symbol in mount_data['deposits']:
            TradeGood.add_trade_good_to_db(trade_good_symbol)

        # Remove all existing links for this mount
        MountDepositLink.query.filter_by(
            mount_symbol=mount_data['symbol']).delete()

        # Add the links to the database
        mount_deposit_link = None
        for trade_good_symbol in mount_data['deposits']:
            mount_deposit_link = MountDepositLink(
                trade_good_symbol=trade_good_symbol,
                mount_symbol=mount_data['symbol']
            )
            db.session.add(mount_deposit_link)
            db.session.commit()
            print(
                f"Added mount deposit link {mount_deposit_link.trade_good_symbol} to database for mount {mount_deposit_link.mount_symbol}")
        return mount_deposit_link


class ShipCargoInventory(db.Model):
    __tablename__ = 'ship_cargo_inventory'
    ship_symbol = db.Column(db.String(50), db.ForeignKey(
        'ship.symbol'), nullable=False, primary_key=True)
    trade_good_symbol = db.Column(TRADE_GOOD_SYMBOL_ENUM, db.ForeignKey(
        'trade_good.symbol'), nullable=False)
    units = db.Column(db.Integer, nullable=False)

    __table_args__ = (
        db.CheckConstraint('units >= 1'),
    )

    def __repr__(self):
        return f"{self.ship_symbol}: {self.trade_good_symbol} {self.units} units"

    @staticmethod
    def set_ship_cargo_inventory_in_db(ship_data):
        # Make sure that the relevant trade goods are in the database
        for trade_good_data in ship_data['cargo']['inventory']:
            TradeGood.add_trade_good_to_db(trade_good_data['symbol'])

        # Remove all existing links for this ship
        ShipCargoInventory.query.filter_by(
            ship_symbol=ship_data['symbol']).delete()

        # Add the links to the database
        ship_cargo_inventory = None
        for trade_good_data in ship_data['cargo']['inventory']:
            ship_cargo_inventory = ShipCargoInventory(
                ship_symbol=ship_data['symbol'],
                trade_good_symbol=trade_good_data['symbol'],
                units=trade_good_data['units']
            )
            db.session.add(ship_cargo_inventory)
            db.session.commit()
            print(f"Added {ship_cargo_inventory.units} {ship_cargo_inventory.trade_good_symbol} to database for ship {ship_cargo_inventory.ship_symbol}")
        return ship_cargo_inventory


class FuelConsumedLog(db.Model):
    __tablename__ = 'fuel_consumed_log'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ship_symbol = db.Column(db.String(50), db.ForeignKey(
        'ship.symbol'), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    __table_args__ = (
        db.CheckConstraint('amount >= 0'),
    )

    def __repr__(self):
        return f"{self.ship_symbol}: {self.amount} units consumed at {self.timestamp}"

    @staticmethod
    def add_fuel_consumed_log_to_db(ship_data):
        fuel_consumed_log = FuelConsumedLog(
            ship_symbol=ship_data['symbol'],
            amount=ship_data['fuel']['consumed']['amount'],
            timestamp=ship_data['fuel']['consumed']['timestamp']
        )
        db.session.add(fuel_consumed_log)
        db.session.commit()
        print(
            f"Added fuel consumed log {fuel_consumed_log.id} to database for ship {fuel_consumed_log.ship_symbol}")
        return fuel_consumed_log


class Shipyard(db.Model):
    __tablename__ = 'shipyard'
    symbol = db.Column(
        db.String(50),
        db.ForeignKey('waypoint.symbol'),
        primary_key=True
    )
    ships = db.relationship('ShipyardShipLink', backref='shipyard', lazy=True)
    transactions = db.relationship('ShipyardTransactionLink', backref='shipyard', lazy=True)

    def __repr__(self):
        ships = self.ships
        transactions = self.transactions
        return f"Shipyard at {self.symbol} has {ships} for sale. Recent transactions: {transactions}"

    @staticmethod
    def get_shipyard_data_api(waypoint_symbol, token):
        system = get_sector_system_waypoint(waypoint_symbol)['system']
        url = f"https://api.spacetraders.io/v2/systems/{system}/waypoints/{waypoint_symbol}/shipyard"
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {token}"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()['data']
        else:
            print(
                f"Error getting ship yard data for {waypoint_symbol}: {response.status_code}")
            return None

    @staticmethod
    def add_shipyard_to_db(shipyard_data):
        # Check if the shipyard is already in the database
        if Shipyard.query.filter_by(symbol=shipyard_data['symbol']).first() is None:
            shipyard = Shipyard(
                symbol=shipyard_data['symbol']
            )
            db.session.add(shipyard)
            db.session.commit()
            print(f"Added shipyard {shipyard.symbol} to database")

            # Add the relevant data to the link tables
            if 'ships' in shipyard_data:
                for shipyard_ship_data in shipyard_data['ships']:
                    shipyard_ship = ShipyardShip.add_ship_to_db(
                        shipyard_data['symbol'], shipyard_ship_data)
                    ShipyardShipLink.add_link_to_db(
                        shipyard_data['symbol'], shipyard_ship.id)
            if 'transactions' in shipyard_data:
                for transaction_data in shipyard_data['transactions']:
                    transaction = ShipyardTransaction.add_shipyard_transaction_to_db(
                        shipyard_data['symbol'], transaction_data)
                    ShipyardTransactionLink.add_link_to_db(
                        shipyard_data['symbol'], transaction.transaction_id)

            return shipyard
        else:
            print(f"Shipyard {shipyard_data['symbol']} already in database")
            return Shipyard.query.filter_by(symbol=shipyard_data['symbol']).first()


class ShipyardShip(db.Model):
    __tablename__ = 'shipyard_ship'
    id = db.Column(
        db.Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True
    )
    shipyard_symbol = db.Column(
        db.String(50),
        db.ForeignKey('shipyard.symbol'),
    )
    ship_type = db.Column(
        SHIP_TYPE_ENUM,
        nullable=False
    )
    ship_name = db.Column(
        db.String(50),
        nullable=False
    )
    ship_description = db.Column(
        db.String(1000),
        nullable=False
    )
    purchase_price = db.Column(
        db.Integer,
        nullable=False
    )
    main_components = db.relationship(
        'ShipyardShipMainComponentLink',
        backref='shipyard_ship',
        lazy=True
    )

    modules = db.relationship(
        'ShipyardShipModuleLink',
        backref='shipyard_ship',
        lazy=True
    )
    mounts = db.relationship(
        'ShipyardShipMountLink',
        backref='shipyard_ship',
        lazy=True
    )

    def __repr__(self):
        return f"{self.ship_name} {self.ship_type} for {self.purchase_price} credits. Main components: {self.main_components}, modules: {self.modules}, mounts: {self.mounts}"

    @staticmethod
    def add_ship_to_db(shipyard_symbol, ship_data):
        # Add 'condition' key to all the main components in ship_data
        for key in ['frame', 'reactor', 'engine']:
            if key in ship_data:
                ship_data[key]['condition'] = 100

        shipyard_ship = ShipyardShip(
            shipyard_symbol=shipyard_symbol,
            ship_type=ship_data['type'],
            ship_name=ship_data['name'],
            ship_description=ship_data['description'],
            purchase_price=ship_data['purchasePrice']
        )
        db.session.add(shipyard_ship)
        db.session.commit()
        print(
            f"Added shipyard ship {shipyard_ship.id} to shipyard {shipyard_ship.shipyard_symbol}")

        # Add the relevant data to the link tables
        ShipyardShipMainComponentLink.add_ship_main_component_link_in_db(
            ship_data, shipyard_ship.id)
        ShipyardShipModuleLink.add_ship_module_link_to_db(
            ship_data, shipyard_ship.id)
        ShipyardShipMountLink.add_ship_mount_link_to_db(
            ship_data, shipyard_ship.id)

        return shipyard_ship


class ShipyardShipLink(db.Model):
    __tablename__ = 'shipyard_ship_link'
    shipyard_symbol = db.Column(
        db.String(50),
        db.ForeignKey('shipyard.symbol'),
        primary_key=True
    )
    shipyard_ship_id = db.Column(
        db.Integer,
        db.ForeignKey('shipyard_ship.id'),
        primary_key=True
    )

    def __repr__(self):
        ship = ShipyardShip.query.filter_by(id=self.shipyard_ship_id).first()
        return f"{ship.ship_name} ({ship.ship_type}): {ship.ship_description} for {ship.purchase_price} credits"

    @staticmethod
    def add_link_to_db(shipyard_symbol, shipyard_ship_id):
        # Check if the link is already in the database
        if ShipyardShipLink.query.filter_by(
            shipyard_symbol=shipyard_symbol,
            shipyard_ship_id=shipyard_ship_id
        ).first() is None:
            shipyard_ship_link = ShipyardShipLink(
                shipyard_symbol=shipyard_symbol,
                shipyard_ship_id=shipyard_ship_id
            )
            db.session.add(shipyard_ship_link)
            db.session.commit()
            print(
                f"Added shipyard ship link {shipyard_ship_link.shipyard_symbol} {shipyard_ship_link.shipyard_ship_id} to database")
            return shipyard_ship_link
        else:
            print(
                f"Shipyard ship link {shipyard_symbol} {shipyard_ship_id} already in database")
            return ShipyardShipLink.query.filter_by(
                shipyard_symbol=shipyard_symbol,
                shipyard_ship_id=shipyard_ship_id
            ).first()


class ShipyardTransaction(db.Model):
    __tablename__ = 'shipyard_transaction'
    transaction_id = db.Column(
        db.Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True
    )
    # TODO Is this really the shipyard or just the waypoint of the transaction?
    shipyard_symbol = db.Column(
        db.String(50),
        db.ForeignKey('shipyard.symbol'),
        nullable=False
    )
    # TODO should this reference ship.symbol?
    ship_symbol = db.Column(
        db.String(50),
        nullable=False
    )
    price = db.Column(db.Integer, nullable=False)
    agent_symbol = db.Column(
        db.String(50),
        nullable=False
    )
    timestamp = db.Column(db.DateTime, nullable=False)

    __table_args__ = (
        db.CheckConstraint('price >= 0', name='price_positive'),
    )

    def __repr__(self):
        return f"{self.ship_symbol} for {self.price} credits at {self.timestamp}"

    @staticmethod
    def add_shipyard_transaction_to_db(shipyard_symbol, transaction_data):
        # TODO maybe add getting public agent data here
        # https://spacetraders.stoplight.io/docs/spacetraders/82c819018af91-get-public-agent

        shipyard_transaction = ShipyardTransaction(
            shipyard_symbol=shipyard_symbol,
            ship_symbol=transaction_data['shipSymbol'],
            price=transaction_data['price'],
            agent_symbol=transaction_data['agentSymbol'],
            timestamp=transaction_data['timestamp']
        )
        db.session.add(shipyard_transaction)
        db.session.commit()
        print(
            f"Added shipyard transaction {shipyard_transaction.transaction_id} to shipyard {shipyard_transaction.shipyard_symbol}")
        return shipyard_transaction


class ShipyardTransactionLink(db.Model):
    __tablename__ = 'shipyard_transaction_link'
    shipyard_symbol = db.Column(
        db.String(50),
        db.ForeignKey('shipyard.symbol'),
        primary_key=True
    )
    transaction_id = db.Column(
        db.Integer,
        db.ForeignKey('shipyard_transaction.transaction_id'),
        primary_key=True
    )

    def __repr__(self):
        transaction = ShipyardTransaction.query.filter_by(
            transaction_id=self.transaction_id).first()
        return f"{transaction.ship_symbol} for {transaction.price} credits at {transaction.timestamp}"

    @staticmethod
    def add_link_to_db(shipyard_symbol, transaction_id):
        # Check if the link is already in the database
        if ShipyardTransactionLink.query.filter_by(
            shipyard_symbol=shipyard_symbol,
            transaction_id=transaction_id
        ).first() is None:
            shipyard_transaction_link = ShipyardTransactionLink(
                shipyard_symbol=shipyard_symbol,
                transaction_id=transaction_id
            )
            db.session.add(shipyard_transaction_link)
            db.session.commit()
            print(
                f"Added shipyard transaction link {shipyard_transaction_link.shipyard_symbol} {shipyard_transaction_link.transaction_id} to database")
            return shipyard_transaction_link
        else:
            print(
                f"Shipyard transaction link {shipyard_symbol} {transaction_id} already in database")
            return ShipyardTransactionLink.query.filter_by(
                shipyard_symbol=shipyard_symbol,
                transaction_id=transaction_id
            ).first()


class ShipyardShipMainComponentLink(db.Model):
    __tablename__ = 'shipyard_ship_main_component_link'
    shipyard_ship_id = db.Column(db.Integer, db.ForeignKey(
        'shipyard_ship.id'), primary_key=True)
    frame_symbol = db.Column(SHIP_FRAME_SYMBOL_ENUM,
                             db.ForeignKey('frame.symbol'), nullable=False)
    reactor_symbol = db.Column(SHIP_REACTOR_SYMBOL_ENUM, db.ForeignKey(
        'reactor.symbol'), nullable=False)
    engine_symbol = db.Column(SHIP_ENGINE_SYMBOL_ENUM,
                              db.ForeignKey('engine.symbol'), nullable=False)

    @staticmethod
    def add_ship_main_component_link_in_db(ship_data, shipyard_ship_id):
        # Make sure that the relevant components are in the database
        Frame.add_frame_to_db(ship_data['frame'])
        Reactor.add_reactor_to_db(ship_data['reactor'])
        Engine.add_engine_to_db(ship_data['engine'])

        # Add the links to the database
        shipyard_ship_main_component_link = ShipyardShipMainComponentLink(
            shipyard_ship_id=shipyard_ship_id,
            frame_symbol=ship_data['frame']['symbol'],
            reactor_symbol=ship_data['reactor']['symbol'],
            engine_symbol=ship_data['engine']['symbol']
        )
        db.session.add(shipyard_ship_main_component_link)
        db.session.commit()
        print(
            f"Added ship main component link {shipyard_ship_main_component_link.shipyard_ship_id} to database")
        return shipyard_ship_main_component_link


class ShipyardShipModuleLink(db.Model):
    __tablename__ = 'shipyard_ship_module_link'
    shipyard_ship_id = db.Column(
        db.Integer,
        db.ForeignKey('shipyard_ship.id'),
        primary_key=True
    )
    module_symbol = db.Column(
        SHIP_MODULE_SYMBOL_ENUM,
        db.ForeignKey('module.symbol'),
        primary_key=True
    )

    @staticmethod
    def add_ship_module_link_to_db(ship_data, shipyard_ship_id):
        # Make sure that the relevant modules are in the database
        for module_data in ship_data['modules']:
            Module.add_module_to_db(module_data)
            shipyard_ship_module_link = ShipyardShipModuleLink(
                shipyard_ship_id=shipyard_ship_id,
                module_symbol=module_data['symbol']
            )
            db.session.add(shipyard_ship_module_link)
            db.session.commit()
            print(
                f"Added ship module link {shipyard_ship_module_link.shipyard_ship_id} {shipyard_ship_module_link.module_symbol} to database")
            return shipyard_ship_module_link


class ShipyardShipMountLink(db.Model):
    __tablename__ = 'shipyard_ship_mount_link'
    shipyard_ship_id = db.Column(
        db.Integer,
        db.ForeignKey('shipyard_ship.id'),
        primary_key=True
    )
    mount_symbol = db.Column(
        SHIP_MOUNT_SYMBOL_ENUM,
        db.ForeignKey('mount.symbol'),
        primary_key=True
    )

    @staticmethod
    def add_ship_mount_link_to_db(ship_data, shipyard_ship_id):
        # Make sure that the relevant mounts are in the database
        for mount_data in ship_data['mounts']:
            Mount.add_mount_to_db(mount_data)
            shipyard_ship_mount_link = ShipyardShipMountLink(
                shipyard_ship_id=shipyard_ship_id,
                mount_symbol=mount_data['symbol']
            )
            db.session.add(shipyard_ship_mount_link)
            db.session.commit()
            print(
                f"Added ship mount link {shipyard_ship_mount_link.shipyard_ship_id} {shipyard_ship_mount_link.mount_symbol} to database")
            return shipyard_ship_mount_link
