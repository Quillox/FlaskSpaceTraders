"""The universe is made up of many systems, each with a set of waypoints. Every waypoint has a symbol such as X1-DF55-20250Z made up of the sector, system, and location of the waypoint. For example, X1 is the sector, X1-DF55 is the system, and X1-DF55-20250Z is the waypoint."""

from time import sleep
import requests
import json
import random

from app import db

SYSTEM_TYPE = (
    'NEUTRON_STAR',
    'RED_STAR',
    'ORANGE_STAR',
    'BLUE_STAR',
    'YOUNG_STAR',
    'WHITE_DWARF',
    'BLACK_HOLE',
    'HYPERGIANT',
    'NEBULA',
    'UNSTABLE'
)

SYSTEM_TYPE_ENUM = db.Enum(
    *SYSTEM_TYPE,
    name='system_type'
)

WAYPOINT_TYPE = (
    'PLANET',
    'GAS_GIANT',
    'MOON',
    'ORBITAL_STATION',
    'JUMP_GATE',
    'ASTEROID_FIELD',
    'NEBULA',
    'DEBRIS_FIELD',
    'GRAVITY_WELL'
)

WAYPOINT_TYPE_ENUM = db.Enum(
    *WAYPOINT_TYPE,
    name='waypoint_type'
)

WAYPOINT_TRAIT_SYMBOL = (
    'UNCHARTED',
    'MARKETPLACE',
    'SHIPYARD',
    'OUTPOST',
    'SCATTERED_SETTLEMENTS',
    'SPRAWLING_CITIES',
    'MEGA_STRUCTURES',
    'OVERCROWDED',
    'HIGH_TECH',
    'CORRUPT',
    'BUREAUCRATIC',
    'TRADING_HUB',
    'INDUSTRIAL',
    'BLACK_MARKET',
    'RESEARCH_FACILITY',
    'MILITARY_BASE',
    'SURVEILLANCE_OUTPOST',
    'EXPLORATION_OUTPOST',
    'MINERAL_DEPOSITS',
    'COMMON_METAL_DEPOSITS',
    'PRECIOUS_METAL_DEPOSITS',
    'RARE_METAL_DEPOSITS',
    'METHANE_POOLS',
    'ICE_CRYSTALS',
    'EXPLOSIVE_GASES',
    'STRONG_MAGNETOSPHERE',
    'VIBRANT_AURORAS',
    'SALT_FLATS',
    'CANYONS',
    'PERPETUAL_DAYLIGHT',
    'PERPETUAL_OVERCAST',
    'DRY_SEABEDS',
    'MAGMA_SEAS',
    'SUPERVOLCANOES',
    'ASH_CLOUDS',
    'VAST_RUINS',
    'MUTATED_FLORA',
    'TERRAFORMED',
    'EXTREME_TEMPERATURES',
    'EXTREME_PRESSURE',
    'DIVERSE_LIFE',
    'SCARCE_LIFE',
    'FOSSILS',
    'WEAK_GRAVITY',
    'STRONG_GRAVITY',
    'CRUSHING_GRAVITY',
    'TOXIC_ATMOSPHERE',
    'CORROSIVE_ATMOSPHERE',
    'BREATHABLE_ATMOSPHERE',
    'JOVIAN',
    'ROCKY',
    'VOLCANIC',
    'FROZEN',
    'SWAMP',
    'BARREN',
    'TEMPERATE',
    'JUNGLE',
    'OCEAN',
    'STRIPPED'
)

WAYPOINT_TRAIT_SYMBOL_ENUM = db.Enum(
    *WAYPOINT_TRAIT_SYMBOL,
    name='waypoint_trait_symbol'
)

FACTION_SYMBOL = (
    'COSMIC',
    'VOID',
    'GALACTIC',
    'QUANTUM',
    'DOMINION',
    'ASTRO',
    'CORSAIRS',
    'OBSIDIAN',
    'AEGIS',
    'UNITED',
    'SOLITARY',
    'COBALT',
    'OMEGA',
    'ECHO',
    'LORDS',
    'CULT',
    'ANCIENTS',
    'SHADOW',
    'ETHEREAL'
)

FACTION_TRAIT_SYMBOL = (
    'BUREAUCRATIC',
    'SECRETIVE',
    'CAPITALISTIC',
    'INDUSTRIOUS',
    'PEACEFUL',
    'DISTRUSTFUL',
    'WELCOMING',
    'SMUGGLERS',
    'SCAVENGERS',
    'REBELLIOUS',
    'EXILES',
    'PIRATES',
    'RAIDERS',
    'CLAN',
    'GUILD',
    'DOMINION',
    'FRINGE',
    'FORSAKEN',
    'ISOLATED',
    'LOCALIZED',
    'ESTABLISHED',
    'NOTABLE',
    'DOMINANT',
    'INESCAPABLE',
    'INNOVATIVE',
    'BOLD',
    'VISIONARY',
    'CURIOUS',
    'DARING',
    'EXPLORATORY',
    'RESOURCEFUL',
    'FLEXIBLE',
    'COOPERATIVE',
    'UNITED',
    'STRATEGIC',
    'INTELLIGENT',
    'RESEARCH_FOCUSED',
    'COLLABORATIVE',
    'PROGRESSIVE',
    'MILITARISTIC',
    'TECHNOLOGICALLY_ADVANCED',
    'AGGRESSIVE',
    'IMPERIALISTIC',
    'TREASURE_HUNTERS',
    'DEXTEROUS',
    'UNPREDICTABLE',
    'BRUTAL',
    'FLEETING',
    'ADAPTABLE',
    'SELF_SUFFICIENT',
    'DEFENSIVE',
    'PROUD',
    'DIVERSE',
    'INDEPENDENT',
    'SELF_INTERESTED',
    'FRAGMENTED',
    'COMMERCIAL',
    'FREE_MARKETS',
    'ENTREPRENEURIAL'
)

FACTION_SYMBOL_ENUM = db.Enum(
    *FACTION_SYMBOL,
    name='faction_symbol'
)

FACTION_TRAIT_SYMBOL_ENUM = db.Enum(
    *FACTION_TRAIT_SYMBOL,
    name='faction_trait_symbol'
)

TRANSACTION_TYPE = (
    'PURCHASE',
    'SELL'
)

TRANSACTION_TYPE_ENUM = db.Enum(
    *TRANSACTION_TYPE,
    name='transaction_type'
)

MARKET_SUPPLY = (
    'SCARCE',
    'LIMITED',
    'MODERATE',
    'ABUNDANT'
)

MARKET_SUPPLY_ENUM = db.Enum(
    *MARKET_SUPPLY,
    name='market_supply'
)

TRADE_GOOD_SYMBOLS = (
    'PRECIOUS_STONES',
    'QUARTZ_SAND',
    'SILICON_CRYSTALS',
    'AMMONIA_ICE',
    'LIQUID_HYDROGEN',
    'LIQUID_NITROGEN',
    'ICE_WATER',
    'EXOTIC_MATTER',
    'ADVANCED_CIRCUITRY',
    'GRAVITON_EMITTERS',
    'IRON',
    'IRON_ORE',
    'COPPER',
    'COPPER_ORE',
    'ALUMINUM',
    'ALUMINUM_ORE',
    'SILVER',
    'SILVER_ORE',
    'GOLD',
    'GOLD_ORE',
    'PLATINUM',
    'PLATINUM_ORE',
    'DIAMONDS',
    'URANITE',
    'URANITE_ORE',
    'MERITIUM',
    'MERITIUM_ORE',
    'HYDROCARBON',
    'ANTIMATTER',
    'FERTILIZERS',
    'FABRICS',
    'FOOD',
    'JEWELRY',
    'MACHINERY',
    'FIREARMS',
    'ASSAULT_RIFLES',
    'MILITARY_EQUIPMENT',
    'EXPLOSIVES',
    'LAB_INSTRUMENTS',
    'AMMUNITION',
    'ELECTRONICS',
    'SHIP_PLATING',
    'EQUIPMENT',
    'FUEL',
    'MEDICINE',
    'DRUGS',
    'CLOTHING',
    'MICROPROCESSORS',
    'PLASTICS',
    'POLYNUCLEOTIDES',
    'BIOCOMPOSITES',
    'NANOBOTS',
    'AI_MAINFRAMES',
    'QUANTUM_DRIVES',
    'ROBOTIC_DRONES',
    'CYBER_IMPLANTS',
    'GENE_THERAPEUTICS',
    'NEURAL_CHIPS',
    'MOOD_REGULATORS',
    'VIRAL_AGENTS',
    'MICRO_FUSION_GENERATORS',
    'SUPERGRAINS',
    'LASER_RIFLES',
    'HOLOGRAPHICS',
    'SHIP_SALVAGE',
    'RELIC_TECH',
    'NOVEL_LIFEFORMS',
    'BOTANICAL_SPECIMENS',
    'CULTURAL_ARTIFACTS',
    'REACTOR_SOLAR_I',
    'REACTOR_FUSION_I',
    'REACTOR_FISSION_I',
    'REACTOR_CHEMICAL_I',
    'REACTOR_ANTIMATTER_I',
    'ENGINE_IMPULSE_DRIVE_I',
    'ENGINE_ION_DRIVE_I',
    'ENGINE_ION_DRIVE_II',
    'ENGINE_HYPER_DRIVE_I',
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
    'MODULE_SHIELD_GENERATOR_II',
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

TRADE_GOOD_SYMBOL_ENUM = db.Enum(
    *TRADE_GOOD_SYMBOLS,
    name='trade_good_symbol'
)


def get_sector_system_waypoint(symbol):
    if len(symbol.split('-')) == 3:
        sector = symbol.split('-')[0]
        system = symbol.split('-')[0] + '-' + symbol.split('-')[1]
        waypoint = symbol
    elif len(symbol.split('-')) == 2:
        sector = symbol.split('-')[0]
        system = symbol.split('-')[0] + '-' + symbol.split('-')[1]
        waypoint = None
    elif len(symbol.split('-')) == 1:
        sector = symbol
        system = None
        waypoint = None
    else:
        return {'sector': None, 'system': None, 'waypoint': None}
    return {'sector': sector, 'system': system, 'waypoint': waypoint}


def waypoint_add_shipyard(Shipyard, waypoint_data, token):
    shipyard_data = Shipyard.get_shipyard_data_api(
        waypoint_data['symbol'], token)
    Shipyard.add_shipyard_to_db(shipyard_data)


class FactionTraitLink(db.Model):
    __tablename__ = 'faction_trait_link'
    faction_symbol = db.Column(FACTION_SYMBOL_ENUM, db.ForeignKey(
        'faction.symbol'), primary_key=True)
    trait_symbol = db.Column(FACTION_TRAIT_SYMBOL_ENUM, db.ForeignKey(
        'faction_trait.symbol'), primary_key=True)

    @staticmethod
    def add_link_to_db(faction_symbol, trait_symbol):
        if FactionTraitLink.query.filter_by(faction_symbol=faction_symbol, trait_symbol=trait_symbol).first() is None:
            faction_trait_link = FactionTraitLink(
                faction_symbol=faction_symbol, trait_symbol=trait_symbol)
            db.session.add(faction_trait_link)
            db.session.commit()


class Faction(db.Model):
    __tablename__ = 'faction'
    symbol = db.Column(
        FACTION_SYMBOL_ENUM,
        primary_key=True,
        nullable=False
    )
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    headquarters = db.Column(
        db.String(50),
        db.ForeignKey('waypoint.symbol'),
        nullable=True
    )
    is_recruiting = db.Column(db.Boolean, nullable=False)

    traits = db.relationship('FactionTrait', secondary='faction_trait_link', lazy='subquery',
                             primaryjoin='Faction.symbol == FactionTraitLink.faction_symbol', backref=db.backref('factions', lazy=True))
    faction_system = db.relationship('System', secondary='system_faction_link', lazy='subquery',
                                     primaryjoin='Faction.symbol == SystemFactionLink.faction_symbol', backref=db.backref('factions', lazy=True))

    @classmethod
    def get_factions_with_traits(cls):
        return cls.query.join(FactionTraitLink).join(FactionTrait).all()

    @staticmethod
    def get_all_factions_api(token):
        url = "https://api.spacetraders.io/v2/factions?limit=20"
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {token}"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()['data']
        else:
            print("Error getting factions from API: ", end="")
            print(response.json())
            return None

    @staticmethod
    def populate_tables(token):

        if not Faction.validate_token(token):
            token = Faction.get_new_token_api()

        data = Faction.get_all_factions_api(token)
        if data is None:
            print('Error getting factions from API')
        else:
            for faction_data in data:
                # Check if faction already exists in database
                if Faction.query.filter_by(symbol=faction_data['symbol']).first() is not None:
                    print(
                        f'Faction {faction_data["symbol"]} already exists in database')
                    continue
                headquarter = get_sector_system_waypoint(
                    faction_data['headquarters'])
                faction = Faction(
                    symbol=faction_data['symbol'],
                    name=faction_data['name'],
                    description=faction_data['description'],
                    headquarters=None,
                    is_recruiting=faction_data['isRecruiting']
                )
                db.session.add(faction)
                db.session.commit()
                headquarter_system_data = System.get_system_data_api(
                    headquarter['system'], token)
                System.add_system_to_db(headquarter_system_data, token)
                sleep(0.5)
                for trait_data in faction_data['traits']:
                    if FactionTrait.query.filter_by(symbol=trait_data['symbol']).first() is None:
                        trait = FactionTrait(
                            symbol=trait_data['symbol'],
                            name=trait_data['name'],
                            description=trait_data['description']
                        )
                        db.session.add(trait)
                    # Add entry to faction_trait_link table if it doesn't exist
                    if FactionTraitLink.query.filter_by(faction_symbol=faction.symbol, trait_symbol=trait_data['symbol']).first() is None:
                        # Add entry to faction_trait_link table
                        FactionTraitLink.add_link_to_db(
                            faction.symbol, trait_data['symbol'])

            db.session.commit()
            print('Factions table populated')

            # Update the faction headquarters after their waypoints have been added to the database
            for faction_data in data:
                faction = Faction.query.filter_by(
                    symbol=faction_data['symbol']).first()
                faction.headquarters = get_sector_system_waypoint(
                    faction_data['headquarters'])['waypoint']
                db.session.commit()

            # Update the system_faction_link table
            for system in System.query.all():
                # Check to see if links already exist for this system
                if SystemFactionLink.query.filter_by(system_symbol=system.symbol).first() is not None:
                    print(f'\nLinks already exist for system {system.symbol}')
                    continue
                else:
                    symbol = system.symbol
                    system_data = System.get_system_data_api(symbol, token)
                    sleep(0.5)
                    if system_data is None:
                        print(f'Error getting system data for {symbol}')
                        continue
                    else:
                        print(
                            f'Updating system_faction_link table for system {symbol}: adding {len(system_data["factions"])} factions')
                        for faction_data in system_data['factions']:
                            faction_symbol = faction_data['symbol']
                            SystemFactionLink.add_link_to_db(
                                system.symbol, faction_symbol)

    @staticmethod
    def get_faction_data(symbol):
        faction = Faction.query.filter_by(symbol=symbol).first()
        if faction is None:
            return None
        data = {
            'symbol': faction.symbol,
            'name': faction.name,
            'description': faction.description,
            'headquarters': faction.headquarters,
            'is_recruiting': faction.is_recruiting,
            'traits': [],
        }
        for trait in faction.traits:
            trait_data = {
                'symbol': trait.symbol,
                'name': trait.name,
                'description': trait.description,
            }
            data['traits'].append(trait_data)
        return data

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
            return response.json()['data']['token']
        else:
            return 'Error'


class FactionTrait(db.Model):
    __tablename__ = 'faction_trait'
    symbol = db.Column(
        FACTION_TRAIT_SYMBOL_ENUM,
        primary_key=True,
        nullable=False
    )
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=False)


class SystemFactionLink(db.Model):
    __tablename__ = 'system_faction_link'
    system_symbol = db.Column(db.String(50), db.ForeignKey(
        'system.symbol'), primary_key=True)
    faction_symbol = db.Column(FACTION_TRAIT_SYMBOL_ENUM, db.ForeignKey(
        'faction.symbol'), primary_key=True)

    @staticmethod
    def add_link_to_db(system_symbol, faction_symbol):
        print(
            f'Adding link for system {system_symbol} and faction {faction_symbol} to system_faction_link table')
        if SystemFactionLink.query.filter_by(system_symbol=system_symbol, faction_symbol=faction_symbol).first() is None:
            system_faction_link = SystemFactionLink(
                system_symbol=system_symbol, faction_symbol=faction_symbol)
            db.session.add(system_faction_link)
            db.session.commit()
            print(
                f'Added {faction_symbol} to system_faction_link table for system {system_symbol}')
        else:
            print(
                f'Link already exists for system {system_symbol} and faction {faction_symbol}')


class System(db.Model):
    __tablename__ = 'system'
    symbol = db.Column(db.String(50), primary_key=True, nullable=False)
    sector_symbol = db.Column(db.String(50), nullable=False)
    type = db.Column(SYSTEM_TYPE_ENUM, nullable=False)
    x = db.Column(db.Integer, nullable=False)
    y = db.Column(db.Integer, nullable=False)
    system_factions = db.relationship(
        'Faction',
        secondary='system_faction_link',
        primaryjoin='System.symbol == SystemFactionLink.system_symbol',
        backref='systems',
        lazy='subquery')
    waypoints = db.relationship(
        'Waypoint',
        secondary='system_waypoint_link',
        lazy='subquery',
        backref=db.backref('systems', lazy=True)
    )

    @staticmethod
    def get_system_data_api(symbol, token):
        url = f"https://api.spacetraders.io/v2/systems/{symbol}"
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {token}"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()['data']
        else:
            print(response)
            return None

    @staticmethod
    def add_system_to_db(system_data, token):
        # Check if system already exists in database
        if System.query.filter_by(symbol=system_data['symbol']).first() is not None:
            print(f'System {system_data["symbol"]} already exists in database')
            return None

        system = System(
            symbol=system_data['symbol'],
            sector_symbol=system_data['sectorSymbol'],
            type=system_data['type'],
            x=system_data['x'],
            y=system_data['y']
        )

        db.session.add(system)
        db.session.commit()
        print(f'System {system.symbol} added to database')

        for waypoint in system_data['waypoints']:
            waypoint_symbol = waypoint['symbol']
            Waypoint.add_waypoint_to_db(waypoint_symbol, token)
            sleep(0.5)

        for faction_data in system_data['factions']:
            faction_symbol = faction_data['symbol']
            # Check to see if faction exists in database
            if Faction.query.filter_by(symbol=faction_symbol).first() is None:
                print(
                    f'Faction {faction_symbol} does not yet exist in database, can not add to system_faction_link table')
                continue
            if SystemFactionLink.query.filter_by(system_symbol=system.symbol, faction_symbol=faction_symbol).first() is None:
                # Add entry to system_faction_link table
                SystemFactionLink.add_link_to_db(system.symbol, faction_symbol)
                print(
                    f'Added {faction_symbol} to system_faction_link table for system {system.symbol}')

        return system

    @staticmethod
    def populate_tables(token):
        # If the file already exists, load the data from the file
        try:
            with open('data/universe/systems.json', 'r') as f:
                systems = json.load(f)
            print('Loaded systems from file')
        # If the file does not exist, get the data from the API
        except FileNotFoundError:
            print('Systems file not found, getting data from API')
            response_data = [*range(21)]
            page = 1
            systems = []
            while len(response_data) > 19:
                url = "https://api.spacetraders.io/v2/systems"
                querystring = {"page":f"{page}","limit":"20"}
                headers = {
                    "Accept": "application/json",
                    "Authorization": f"Bearer {token}"
                }
                response = requests.get(url, headers=headers, params=querystring)
                sleep(0.5)
                if response.status_code != 200:
                    print(f'Error getting systems from API: {response.json()}')
                    break
                response_data = response.json()['data']
                for system_data in response_data:
                    systems.append(system_data)
                if page % 20 == 0:
                    with open('data/universe/systems.json', 'w') as f:
                        json.dump(systems, f)
                    print(f'Saved {len(systems)} systems to file at page {page}')
                page += 1

            with open('data/universe/systems.json', 'w') as f:
                json.dump(systems, f)

        random.shuffle(systems)
        for system_data in systems:
            System.add_system_to_db(system_data, token)
        print('Systems table populated')


class WaypointTrait(db.Model):
    __tablename__ = 'waypoint_trait'
    symbol = db.Column(WAYPOINT_TRAIT_SYMBOL_ENUM,
                       primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f"{self.name}: {self.description}"

    @staticmethod
    def add_trait_to_db(trait_data):
        if WaypointTrait.query.filter_by(symbol=trait_data['symbol']).first() is None:
            trait = WaypointTrait(
                symbol=trait_data['symbol'],
                name=trait_data['name'],
                description=trait_data['description']
            )
            db.session.add(trait)
            db.session.commit()


class WaypointTraitLink(db.Model):
    __tablename__ = 'waypoint_trait_link'
    waypoint_symbol = db.Column(db.String(50), db.ForeignKey(
        'waypoint.symbol'), primary_key=True)
    waypoint_trait_symbol = db.Column(WAYPOINT_TRAIT_SYMBOL_ENUM, db.ForeignKey(
        'waypoint_trait.symbol'), primary_key=True)

    @staticmethod
    def add_link_to_db(waypoint_symbol, waypoint_trait_symbol):
        if WaypointTraitLink.query.filter_by(waypoint_symbol=waypoint_symbol, waypoint_trait_symbol=waypoint_trait_symbol).first() is None:
            waypoint_trait_link = WaypointTraitLink(
                waypoint_symbol=waypoint_symbol, waypoint_trait_symbol=waypoint_trait_symbol)
            db.session.add(waypoint_trait_link)
            db.session.commit()


class OrbitalLink(db.Model):
    __tablename__ = 'orbital_link'
    waypoint_symbol = db.Column(db.String(50), db.ForeignKey(
        'waypoint.symbol'), primary_key=True, nullable=False)
    orbital = db.Column(db.String(50), db.ForeignKey(
        'waypoint.symbol'), primary_key=True, nullable=False)

    @staticmethod
    def add_link_to_db(waypoint_symbol, orbital_symbol):
        if OrbitalLink.query.filter_by(waypoint_symbol=waypoint_symbol, orbital=orbital_symbol).first() is None:
            orbital_link = OrbitalLink(
                waypoint_symbol=waypoint_symbol, orbital=orbital_symbol)
            db.session.add(orbital_link)
            db.session.commit()


class Waypoint(db.Model):
    __tablename__ = 'waypoint'
    symbol = db.Column(db.String(50), primary_key=True, nullable=False)
    type = db.Column(WAYPOINT_TYPE_ENUM, nullable=False)
    system_symbol = db.Column(db.String(50), db.ForeignKey(
        'system.symbol'), nullable=False)
    x = db.Column(db.Integer, nullable=False)
    y = db.Column(db.Integer, nullable=False)
    faction_symbol = db.Column(FACTION_SYMBOL_ENUM, db.ForeignKey(
        'faction.symbol'), nullable=True)
    orbitals = db.relationship('Waypoint', secondary='orbital_link', primaryjoin='OrbitalLink.waypoint_symbol == Waypoint.symbol',
                               secondaryjoin=OrbitalLink.orbital == symbol, lazy='subquery', backref=db.backref('orbital_of', lazy=True))
    traits = db.relationship(
        'WaypointTrait',
        secondary='waypoint_trait_link',
        primaryjoin='Waypoint.symbol == WaypointTraitLink.waypoint_symbol',
        lazy='subquery',
        backref=db.backref('waypoints', lazy=True))
    chart = db.relationship('Chart', backref='waypoint', lazy=True)

    def __repr__(self):
        return f"{self.type}: Controlled by {self.faction_symbol} at {self.x}, {self.y}"

    @staticmethod
    def get_waypoint_data_api(symbol, token):
        system_symbol = symbol.split('-')[0] + '-' + symbol.split('-')[1]
        url = f"https://api.spacetraders.io/v2/systems/{system_symbol}/waypoints/{symbol}"
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {token}"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()['data']
        else:
            print(response)
            return None

    @staticmethod
    def add_waypoint_to_db(symbol, token, parent_symbol=None, add_jump_gate=False):
        # Check if waypoint already exists in database
        if Waypoint.query.filter_by(symbol=symbol).first() is not None:
            print(f'Waypoint {symbol} already exists in database')
            return None

        waypoint_data = Waypoint.get_waypoint_data_api(symbol, token)

        if waypoint_data is None:
            print(f'Error getting waypoint data for {symbol}')
            return None

        if 'faction' not in waypoint_data:
            waypoint_data['faction'] = {'symbol': None}
        if 'systemSymbol' not in waypoint_data:
            waypoint_data['systemSymbol'] = get_sector_system_waypoint(symbol)[
                'system']

        waypoint = Waypoint(
            symbol=waypoint_data['symbol'],
            type=waypoint_data['type'],
            system_symbol=waypoint_data['systemSymbol'],
            x=waypoint_data['x'],
            y=waypoint_data['y'],
            faction_symbol=waypoint_data['faction']['symbol']
        )

        db.session.add(waypoint)
        db.session.commit()
        print(f'Waypoint {waypoint.symbol} added to database')

        SystemWaypointLink.add_link_to_db(
            waypoint.system_symbol, waypoint.symbol)

        orbitals = []
        for orbital in waypoint_data['orbitals']:
            if orbital is None:
                continue
            orbital_symbol = orbital['symbol']
            orbital_data = Waypoint.get_waypoint_data_api(
                orbital_symbol, token)
            if orbital_data is not None:
                orbital = Waypoint.add_waypoint_to_db(orbital_data['symbol'], token, waypoint.symbol)
                if orbital is not None:
                    orbitals.append(orbital)
            sleep(0.5)
        # Update orbital_link table
        for orbital in orbitals:
            if orbital is None:
                continue
            if OrbitalLink.query.filter_by(waypoint_symbol=waypoint.symbol, orbital=orbital.symbol).first() is None:
                # Add entry to orbital_link table
                OrbitalLink.add_link_to_db(waypoint.symbol, orbital.symbol)

        if 'chart' not in waypoint_data:
            waypoint_data['chart'] = {'submittedBy': None, 'submittedOn': None}
        chart = Chart(
            waypoint_symbol=waypoint.symbol,
            submitted_by_agent=waypoint_data['chart']['submittedBy'],
            submitted_on=waypoint_data['chart']['submittedOn']
        )
        db.session.add(chart)

        traits = []
        for trait in waypoint_data['traits']:
            trait_symbol = trait['symbol']
            traits.append(trait_symbol)
            # Add trait to waypoint_trait table if it doesn't exist
            if WaypointTrait.query.filter_by(symbol=trait_symbol).first() is None:
                WaypointTrait.add_trait_to_db(trait)

            # Add entry to waypoint_trait_link table if it doesn't exist
            if WaypointTraitLink.query.filter_by(waypoint_symbol=waypoint.symbol, waypoint_trait_symbol=trait_symbol).first() is None:
                # Add entry to waypoint_trait_link table
                WaypointTraitLink.add_link_to_db(waypoint.symbol, trait_symbol)
        # Update waypoint_trait_link table
        for trait in traits:
            if WaypointTraitLink.query.filter_by(waypoint_symbol=waypoint.symbol, waypoint_trait_symbol=trait).first() is None:
                # Add entry to waypoint_trait_link table
                WaypointTraitLink.add_link_to_db(waypoint.symbol, trait)

        db.session.commit()

        # Add entry to orbital_link table for parent waypoint
        if parent_symbol is not None and OrbitalLink.query.filter_by(waypoint_symbol=parent_symbol, orbital=waypoint.symbol).first() is None:
            # Add entry to orbital_link table
            OrbitalLink.add_link_to_db(parent_symbol, waypoint.symbol)

        # Add jump gate to database
        if add_jump_gate:
            if waypoint_data['type'] == 'JUMP_GATE':
                jump_gate_data = JumpGate.get_jump_gate_data_api(
                    waypoint_data['symbol'], token)
                JumpGate.add_jump_gate_to_db(
                    jump_gate_data, waypoint_symbol=waypoint.symbol, token=token)

        if 'MARKETPLACE' in [trait.symbol for trait in waypoint.traits]:
            market_data = Market.get_market_data_api(
                system_symbol=waypoint_data['systemSymbol'], waypoint_symbol=waypoint_data['symbol'], token=token)
            Market.add_market_to_db(market_data)

        if 'SHIPYARD' in [trait.symbol for trait in waypoint.traits]:
            waypoint_add_shipyard(Shipyard, waypoint_data, token)

        return waypoint

    @staticmethod
    def make_system_waypoint_link():
        for waypoint in Waypoint.query.all():
            SystemWaypointLink.add_link_to_db(
                waypoint.system_symbol, waypoint.symbol)

    @staticmethod
    def add_jump_gates_api(token):
        for waypoint in Waypoint.query.all():
            if waypoint.type == 'JUMP_GATE':
                jump_gate_data = JumpGate.get_jump_gate_data_api(
                    waypoint.symbol, token)
                JumpGate.add_jump_gate_to_db(
                    jump_gate_data, waypoint_symbol=waypoint.symbol, token=token)


class SystemWaypointLink(db.Model):
    __tablename__ = 'system_waypoint_link'
    system_symbol = db.Column(
        db.String(50),
        db.ForeignKey('system.symbol'),
        primary_key=True
    )
    waypoint_symbol = db.Column(
        db.String(50),
        db.ForeignKey('waypoint.symbol'),
        primary_key=True
    )

    def __repr__(self):
        system = System.query.filter_by(symbol=self.system_symbol).first()
        waypoint = Waypoint.query.filter_by(symbol=self.waypoint_symbol).first()
        waypoint_traits = [f'{trait.name}: {trait.description}' for trait in waypoint.traits]
        return f'{waypoint.type}: {waypoint_traits}'

    @staticmethod
    def add_link_to_db(system_symbol, waypoint_symbol):
        if SystemWaypointLink.query.filter_by(system_symbol=system_symbol, waypoint_symbol=waypoint_symbol).first() is None:
            system_waypoint_link = SystemWaypointLink(
                system_symbol=system_symbol, waypoint_symbol=waypoint_symbol)
            db.session.add(system_waypoint_link)
            db.session.commit()
            print(
                f'Added {waypoint_symbol} to system_waypoint_link table for system {system_symbol}')
            return system_waypoint_link
        else:
            return SystemWaypointLink.query.filter_by(system_symbol=system_symbol, waypoint_symbol=waypoint_symbol).first()


class Chart(db.Model):
    __tablename__ = 'chart'
    waypoint_symbol = db.Column(db.String(50), db.ForeignKey(
        'waypoint.symbol'), primary_key=True, nullable=False)
    submitted_by_agent = db.Column(
        db.String(50), nullable=True, primary_key=True)
    submitted_on = db.Column(db.DateTime, nullable=True)


class TradeGood(db.Model):
    __tablename__ = 'trade_good'
    symbol = db.Column(TRADE_GOOD_SYMBOL_ENUM,
                       primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=True)
    description = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f"{self.symbol}: {self.name} {self.description}"

    @staticmethod
    def add_trade_good_to_db(trade_good_data):
        if not isinstance(trade_good_data, dict):
            trade_good_data = {
                'symbol': trade_good_data,
                'name': None,
                'description': None
            }
        if TradeGood.query.filter_by(symbol=trade_good_data['symbol']).first() is None:
            # Make dictionary to handel None values
            for data in ['name', 'description']:
                if data not in trade_good_data:
                    trade_good_data[data] = None
            trade_good = TradeGood(
                symbol=trade_good_data['symbol'],
                name=trade_good_data['name'],
                description=trade_good_data['description']
            )
            db.session.add(trade_good)
            db.session.commit()


class Market(db.Model):
    __tablename__ = 'market'
    symbol = db.Column(
        db.String(50),
        db.ForeignKey('waypoint.symbol'),
        primary_key=True
    )
    exports = db.relationship(
        'TradeGood',
        secondary='market_export_link',
        primaryjoin='Market.symbol == MarketExportLink.market_symbol',
        lazy='subquery',
        backref=db.backref('exported_by', lazy=True)
    )
    imports = db.relationship(
        'TradeGood',
        secondary='market_import_link',
        primaryjoin='Market.symbol == MarketImportLink.market_symbol',
        lazy='subquery',
        backref=db.backref('imported_by', lazy=True)
    )

    exchanges = db.relationship(
        'TradeGood',
        secondary='market_exchange_link',
        primaryjoin='Market.symbol == MarketExchangeLink.market_symbol',
        lazy='subquery',
        backref=db.backref('exchanged_by', lazy=True)
    )

    transactions = db.relationship(
        'MarketTransaction',
        secondary='market_transaction_link',
        primaryjoin='Market.symbol == MarketTransactionLink.market_symbol',
        lazy='subquery',
        backref=db.backref('market', lazy=True)
    )

    traded_goods = db.relationship(
        'MarketTradedGood',
        primaryjoin='Market.symbol == MarketTradedGood.market_symbol',
        lazy='subquery',
        backref=db.backref('market', lazy=True)
    )

    def __repr__(self):
        return f"Market at {self.symbol}:\nExports{self.exports}\nImports{self.imports}\nExchanges{self.exchanges}\nTransactions{self.transactions}\nTraded Goods{self.traded_goods}"

    @staticmethod
    def get_market_data_api(system_symbol, waypoint_symbol, token):
        url = f"https://api.spacetraders.io/v2/systems/{system_symbol}/waypoints/{waypoint_symbol}/market"
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {token}"
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()['data']

        else:
            print(response)
            return None

    @staticmethod
    def add_market_to_db(market_data):
        waypoint_symbol = market_data['symbol']
        # Check if market already exists in database
        if Market.query.filter_by(symbol=waypoint_symbol).first() is not None:
            print(f'Market {waypoint_symbol} already exists in database')
            return None

        market = Market(
            symbol=waypoint_symbol
        )
        db.session.add(market)
        db.session.commit()
        print(f'Market {market.symbol} added to database')

        # Add entries to the link tables
        for trade_good_data in market_data['exports']:
            TradeGood.add_trade_good_to_db(trade_good_data)
            MarketExportLink.add_link_to_db(
                market.symbol, trade_good_data['symbol'])

        for trade_good_data in market_data['imports']:
            TradeGood.add_trade_good_to_db(trade_good_data)
            MarketImportLink.add_link_to_db(
                market.symbol, trade_good_data['symbol'])

        for trade_good_data in market_data['exchange']:
            TradeGood.add_trade_good_to_db(trade_good_data)
            MarketExchangeLink.add_link_to_db(
                market.symbol, trade_good_data['symbol'])

        if 'transactions' in market_data:
            for transaction_data in market_data['transactions']:
                transaction = MarketTransaction.add_transaction_to_db(
                    transaction_data)
                MarketTransactionLink.add_link_to_db(
                    market.symbol, transaction.id)
        if 'tradeGoods' in market_data:
            for trade_good_data in market_data['tradeGoods']:
                MarketTradedGood.add_traded_good_to_db(
                    market.symbol, trade_good_data)

        return market


class MarketExportLink(db.Model):
    __tablename__ = 'market_export_link'
    market_symbol = db.Column(
        db.String(50),
        db.ForeignKey('market.symbol'),
        primary_key=True
    )
    export_good_symbol = db.Column(
        TRADE_GOOD_SYMBOL_ENUM,
        db.ForeignKey('trade_good.symbol'),
        primary_key=True
    )

    @staticmethod
    def add_link_to_db(market_symbol, export_good_symbol):
        if MarketExportLink.query.filter_by(market_symbol=market_symbol, export_good_symbol=export_good_symbol).first() is None:
            market_export_link = MarketExportLink(
                market_symbol=market_symbol, export_good_symbol=export_good_symbol)
            db.session.add(market_export_link)
            db.session.commit()


class MarketImportLink(db.Model):
    __tablename__ = 'market_import_link'
    market_symbol = db.Column(
        db.String(50),
        db.ForeignKey('market.symbol'),
        primary_key=True
    )
    import_good_symbol = db.Column(
        TRADE_GOOD_SYMBOL_ENUM,
        db.ForeignKey('trade_good.symbol'),
        primary_key=True
    )

    @staticmethod
    def add_link_to_db(market_symbol, import_good_symbol):
        if MarketImportLink.query.filter_by(market_symbol=market_symbol, import_good_symbol=import_good_symbol).first() is None:
            market_import_link = MarketImportLink(
                market_symbol=market_symbol, import_good_symbol=import_good_symbol)
            db.session.add(market_import_link)
            db.session.commit()


class MarketExchangeLink(db.Model):
    __tablename__ = 'market_exchange_link'
    market_symbol = db.Column(
        db.String(50),
        db.ForeignKey('market.symbol'),
        primary_key=True
    )
    exchange_good_symbol = db.Column(
        TRADE_GOOD_SYMBOL_ENUM,
        db.ForeignKey('trade_good.symbol'),
        primary_key=True
    )

    @staticmethod
    def add_link_to_db(market_symbol, exchange_good_symbol):
        if MarketExchangeLink.query.filter_by(market_symbol=market_symbol, exchange_good_symbol=exchange_good_symbol).first() is None:
            market_exchange_link = MarketExchangeLink(
                market_symbol=market_symbol, exchange_good_symbol=exchange_good_symbol)
            db.session.add(market_exchange_link)
            db.session.commit()


class MarketTransactionLink(db.Model):
    __tablename__ = 'market_transaction_link'
    market_symbol = db.Column(
        db.String(50),
        db.ForeignKey('market.symbol'),
        primary_key=True
    )
    transaction_id = db.Column(
        db.String(50),
        db.ForeignKey('market_transaction.id'),
        primary_key=True
    )

    @staticmethod
    def add_link_to_db(market_symbol, transaction_id):
        if MarketTransactionLink.query.filter_by(market_symbol=market_symbol, transaction_id=transaction_id).first() is None:
            market_transaction_link = MarketTransactionLink(
                market_symbol=market_symbol, transaction_id=transaction_id)
            db.session.add(market_transaction_link)
            db.session.commit()


class MarketTransaction(db.Model):
    __tablename__ = 'market_transaction'
    id = db.Column(db.Integer, primary_key=True,
                   nullable=False, autoincrement=True)
    transaction_waypoint = db.Column(
        db.String(50),
        db.ForeignKey('waypoint.symbol'),
        nullable=False
    )
    ship = db.Column(
        db.String(50),
        db.ForeignKey('ship.symbol'),
        nullable=True
    )
    trade_good = db.Column(
        TRADE_GOOD_SYMBOL_ENUM,
        db.ForeignKey('trade_good.symbol'),
        nullable=False
    )
    type = db.Column(TRANSACTION_TYPE_ENUM, nullable=False)
    units = db.Column(db.Integer, nullable=False)
    price_per_unit = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    __table_args__ = (
        db.CheckConstraint('units >= 0', name='units_positive'),
        db.CheckConstraint('price_per_unit >= 0',
                           name='price_per_unit_positive'),
        db.CheckConstraint('total_price >= 0', name='total_price_positive')
    )

    def __repr__(self):
        return f"{self.id}: {self.type} {self.units} {self.trade_good} at {self.transaction_waypoint} for {self.total_price}"

    @staticmethod
    def add_transaction_to_db(transaction_data):

        known_ships = db.session.execute('SELECT symbol FROM ship').fetchall()
        known_ships = [ship[0] for ship in known_ships]
        if transaction_data['shipSymbol'] not in known_ships:
            # TODO make it so that I can have other agents ships in the database
            transaction_data['shipSymbol'] = None
        if TradeGood.query.filter_by(symbol=transaction_data['tradeSymbol']).first() is None:
            TradeGood.add_trade_good_to_db(transaction_data['tradeSymbol'])

        transaction = MarketTransaction(
            transaction_waypoint=transaction_data['waypointSymbol'],
            ship=transaction_data['shipSymbol'],
            trade_good=transaction_data['tradeSymbol'],
            type=transaction_data['type'],
            units=transaction_data['units'],
            price_per_unit=transaction_data['pricePerUnit'],
            total_price=transaction_data['totalPrice'],
            timestamp=transaction_data['timestamp']
        )
        db.session.add(transaction)
        db.session.commit()
        print(f'Transaction {transaction.id} added to database')

        return transaction


class MarketTradedGood(db.Model):
    __tablename__ = 'market_traded_good'
    market_symbol = db.Column(
        db.String(50),
        db.ForeignKey('market.symbol'),
        primary_key=True
    )
    traded_good_symbol = db.Column(
        TRADE_GOOD_SYMBOL_ENUM,
        db.ForeignKey('trade_good.symbol'),
        primary_key=True
    )
    trade_volume = db.Column(db.Integer, nullable=False)
    supply = db.Column(
        MARKET_SUPPLY_ENUM,
        nullable=False
    )
    purchase_price = db.Column(db.Integer, nullable=False)
    sell_price = db.Column(db.Integer, nullable=False)

    __table_args__ = (
        db.CheckConstraint('trade_volume >= 0', name='trade_volume_positive'),
        db.CheckConstraint('purchase_price >= 0',
                           name='purchase_price_positive'),
        db.CheckConstraint('sell_price >= 0', name='sell_price_positive')
    )

    def __repr__(self):
        return f"{self.traded_good_symbol} at {self.market_symbol}: Volume {self.trade_volume}, Supply {self.supply}, Purchase Price {self.purchase_price}, Sell Price {self.sell_price}"

    @staticmethod
    def add_traded_good_to_db(market_symbol, traded_good_data):
        if MarketTradedGood.query.filter_by(traded_good_symbol=traded_good_data['symbol']).first() is None:
            traded_good = MarketTradedGood(
                market_symbol=market_symbol,
                traded_good_symbol=traded_good_data['symbol'],
                trade_volume=traded_good_data['tradeVolume'],
                supply=traded_good_data['supply'],
                purchase_price=traded_good_data['purchasePrice'],
                sell_price=traded_good_data['sellPrice']
            )
            db.session.add(traded_good)
            db.session.commit()
            print(
                f'Traded good {traded_good.traded_good_symbol} at {traded_good.market_symbol} added to database')


class JumpGate(db.Model):
    __tablename__ = 'jump_gate'
    symbol = db.Column(
        db.String(50),
        db.ForeignKey('waypoint.symbol'),
        primary_key=True
    )
    jump_range = db.Column(db.Float, nullable=False)
    faction_symbol = db.Column(
        FACTION_SYMBOL_ENUM,
        db.ForeignKey('faction.symbol'),
        nullable=False
    )
    connected_systems = db.relationship(
        'JumpGateLink',
        backref='jump_gate',
        lazy=True
    )

    def __repr__(self):
        return f"Jump gate owned by {self.faction_symbol} at {self.symbol} with range {self.jump_range} and connected systems {self.connected_systems}"

    @staticmethod
    def get_jump_gate_data_api(waypoint_symbol, token):
        system_symbol = get_sector_system_waypoint(waypoint_symbol)['system']
        url = f"https://api.spacetraders.io/v2/systems/{system_symbol}/waypoints/{waypoint_symbol}/jump-gate"
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {token}"
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()['data']

        else:
            print(response)
            return None

    @staticmethod
    def add_jump_gate_to_db(jump_gate_data, waypoint_symbol, token):
        # Make sure the waypoint is in the database
        if Waypoint.query.filter_by(symbol=waypoint_symbol).first() is None:
            Waypoint.add_waypoint_to_db(
                symbol=waypoint_symbol, token=token, add_jump_gate=True)
        # Check if jump gate already exists in database
        if JumpGate.query.filter_by(symbol=waypoint_symbol).first() is not None:
            print(f'Jump gate {waypoint_symbol} already exists in database')
            return JumpGate.query.filter_by(symbol=waypoint_symbol).first()

        jump_gate = JumpGate(
            symbol=waypoint_symbol,
            jump_range=jump_gate_data['jumpRange'],
            faction_symbol=jump_gate_data['factionSymbol']
        )
        db.session.add(jump_gate)
        db.session.commit()
        print(f'Jump gate {jump_gate.symbol} added to database')

        for connected_system_data in jump_gate_data['connectedSystems']:
            JumpGateLink.add_link_to_db(
                jump_gate.symbol, connected_system_data, token)
            sleep(0.5)

        return jump_gate


class JumpGateLink(db.Model):
    __tablename__ = 'jump_gate_link'
    jump_gate_symbol = db.Column(
        db.String(50),
        db.ForeignKey('jump_gate.symbol'),
        primary_key=True
    )
    system_symbol = db.Column(
        db.String(50),
        db.ForeignKey('system.symbol'),
        primary_key=True
    )
    distance = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"{self.system_symbol} with distance {self.distance}"

    @staticmethod
    def add_link_to_db(jump_gate_symbol, connected_system_data, token):
        system_symbol = connected_system_data['symbol']
        # Make sure the destination system exists in the database
        if System.query.filter_by(symbol=system_symbol).first() is None:
            system_data = System.get_system_data_api(symbol=system_symbol, token=token)
            System.add_system_to_db(system_data, token)
        if JumpGateLink.query.filter_by(jump_gate_symbol=jump_gate_symbol, system_symbol=system_symbol).first() is None:
            jump_gate_link = JumpGateLink(
                jump_gate_symbol=jump_gate_symbol,
                system_symbol=system_symbol,
                distance=connected_system_data['distance']
            )
            db.session.add(jump_gate_link)
            db.session.commit()
            print(
                f'Jump gate link for {jump_gate_symbol} to {system_symbol} added to database')

            return jump_gate_link


from app.models.fleet import Shipyard
