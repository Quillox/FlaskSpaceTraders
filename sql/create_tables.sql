-- #########
-- SQL Types For Universe, Agents, and Factions
-- #########

CREATE TYPE system_type AS ENUM (
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
);

CREATE TYPE waypoint_type AS ENUM (
    'PLANET',
    'GAS_GIANT',
    'MOON',
    'ORBITAL_STATION',
    'JUMP_GATE',
    'ASTEROID_FIELD',
    'NEBULA',
    'DEBRIS_FIELD',
    'GRAVITY_WELL'
);

CREATE TYPE waypoint_trait_symbol AS ENUM (
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
);

CREATE TYPE faction_symbol AS ENUM (
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
);

CREATE TYPE faction_trait_symbol AS ENUM (
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
);

CREATE TYPE contract_type AS ENUM (
    'PROCUREMENT',
    'TRANSPORT',
    'SHUTTLE'
);

CREATE TYPE market_supply AS ENUM (
    'SCARCE',
    'LIMITED',
    'MODERATE',
    'ABUNDANT'
);

CREATE TYPE trade_good_symbol AS ENUM (
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
);

-- ########
-- SQL Types For Fleet
-- ########

CREATE TYPE ship_role AS ENUM (
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
);

CREATE TYPE ship_nav_status AS ENUM (
    'IN_TRANSIT',
    'IN_ORBIT',
    'DOCKED'
);

CREATE TYPE ship_flight_mode AS ENUM (
    'DRIFT',
    'STEALTH',
    'CRUISE',
    'BURN'
);

CREATE TYPE ship_crew_rotation AS ENUM (
    'STRICT',
    'RELAXED'
);

CREATE TYPE ship_component_symbol AS ENUM (
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
    'FRAME_CARRIER',
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
);

CREATE TYPE ship_type AS ENUM (
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
);

-- ########
-- Universe and Faction
-- ########

CREATE TABLE system (
    symbol VARCHAR(50) PRIMARY KEY,
    sector_symbol VARCHAR(50) NOT NULL,
    type system_type NOT NULL,
    x INTEGER NOT NULL,
    y INTEGER NOT NULL
);

CREATE TABLE faction (
    symbol faction_symbol PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(500) NOT NULL,
    headquarters VARCHAR(50), -- REFERENCES waypoint(symbol),
    is_recruiting BOOLEAN NOT NULL
);

CREATE TABLE faction_trait (
    symbol faction_trait_symbol PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(500) NOT NULL
);

CREATE TABLE waypoint (
    symbol VARCHAR(50) PRIMARY KEY,
    type waypoint_type NOT NULL,
    x INTEGER NOT NULL,
    y INTEGER NOT NULL,
    system_symbol VARCHAR(50) REFERENCES system(symbol) NOT NULL,
    faction_symbol faction_symbol REFERENCES faction(symbol)
);

CREATE TABLE waypoint_trait (
    symbol waypoint_trait_symbol PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(500) NOT NULL
);

CREATE TABLE chart (
    waypoint_symbol VARCHAR(50) PRIMARY KEY REFERENCES waypoint(symbol) NOT NULL,
    submitted_by_agent VARCHAR(50),
    submitted_on TIMESTAMP
);

CREATE TABLE trade_good (
    symbol trade_good_symbol PRIMARY KEY NOT NULL,
    name VARCHAR(50),
    description VARCHAR(500)
);

CREATE TABLE market (
    symbol VARCHAR(50) PRIMARY KEY REFERENCES waypoint(symbol)
);

CREATE TABLE market_transaction (
    id SERIAL PRIMARY KEY,
    transaction_waypoint VARCHAR(50) REFERENCES waypoint(symbol) NOT NULL,
    ship VARCHAR(50), -- REFERENCES ship(symbol),
    trade_good trade_good_symbol NOT NULL REFERENCES trade_good(symbol),
    type VARCHAR(50) NOT NULL,
    units INTEGER NOT NULL CHECK (units >= 0),
    price_per_unit INTEGER NOT NULL CHECK (price_per_unit >= 0),
    total_price INTEGER NOT NULL CHECK (total_price >= 0),
    timestamp TIMESTAMP NOT NULL
);

CREATE TABLE market_traded_good (
    market_symbol VARCHAR(50) REFERENCES market(symbol) ON DELETE CASCADE,
    traded_good_symbol trade_good_symbol REFERENCES trade_good(symbol),
    trade_volume INTEGER NOT NULL CHECK (trade_volume >= 0),
    supply market_supply NOT NULL,
    purchase_price INTEGER NOT NULL CHECK (purchase_price >= 0),
    sell_price INTEGER NOT NULL CHECK (sell_price >= 0),
    PRIMARY KEY (market_symbol, traded_good_symbol)
);

CREATE TABLE jump_gate (
    symbol VARCHAR(50) PRIMARY KEY REFERENCES waypoint(symbol),
    jump_range FLOAT NOT NULL,
    faction_symbol faction_symbol REFERENCES faction(symbol)
);


-- ######
-- Agents
-- ######

CREATE TABLE agent (
    token VARCHAR(600) NOT NULL,
    account_id VARCHAR(50) NOT NULL UNIQUE,
    symbol VARCHAR(50) NOT NULL PRIMARY KEY,
    headquarters VARCHAR(50) NOT NULL REFERENCES waypoint(symbol),
    credits INTEGER NOT NULL,
    starting_faction faction_symbol NOT NULL REFERENCES faction(symbol),
    CONSTRAINT agent_token_unique UNIQUE (token),
    CONSTRAINT account_id_unique UNIQUE (account_id)
);


CREATE TABLE contract (
    id VARCHAR(50) PRIMARY KEY,
    faction_symbol faction_symbol NOT NULL REFERENCES faction(symbol),
    type contract_type NOT NULL,
    deadline TIMESTAMP NOT NULL,
    payment_on_accepted INTEGER NOT NULL,
    payment_on_fulfilled INTEGER NOT NULL,
    accepted BOOLEAN DEFAULT FALSE,
    fulfilled BOOLEAN DEFAULT FALSE,
    deadline_to_accept TIMESTAMP NOT NULL
);

-- ###########
-- Link tables For Universe, Agents, and Factions
-- ###########

CREATE TABLE waypoint_trait_link (
    waypoint_symbol VARCHAR(50) NOT NULL REFERENCES waypoint(symbol),
    waypoint_trait_symbol waypoint_trait_symbol NOT NULL REFERENCES waypoint_trait(symbol),
    PRIMARY KEY (waypoint_symbol, waypoint_trait_symbol)
);

CREATE TABLE faction_trait_link (
    faction_symbol faction_symbol REFERENCES faction(symbol),
    trait_symbol faction_trait_symbol REFERENCES faction_trait(symbol),
    PRIMARY KEY (faction_symbol, trait_symbol)
);

CREATE TABLE system_faction_link (
    system_symbol VARCHAR(50) REFERENCES system(symbol),
    faction_symbol faction_symbol REFERENCES faction(symbol),
    PRIMARY KEY (system_symbol, faction_symbol)
);

CREATE TABLE agent_contract_link (
    agent_symbol VARCHAR(50) REFERENCES agent(symbol),
    contract_id VARCHAR(50) REFERENCES contract(id),
    PRIMARY KEY (agent_symbol, contract_id)
);

CREATE TABLE orbital_link (
    waypoint_symbol VARCHAR(50) REFERENCES waypoint(symbol),
    orbital VARCHAR(50) REFERENCES waypoint(symbol),
    PRIMARY KEY (waypoint_symbol, orbital)
);

CREATE TABLE system_waypoint_link (
    system_symbol VARCHAR(50) REFERENCES system(symbol),
    waypoint_symbol VARCHAR(50) REFERENCES waypoint(symbol),
    PRIMARY KEY (system_symbol, waypoint_symbol)
);

CREATE TABLE market_export_link (
    market_symbol VARCHAR(50) REFERENCES market(symbol) ON DELETE CASCADE,
    export_good_symbol trade_good_symbol REFERENCES trade_good(symbol),
    PRIMARY KEY (market_symbol, export_good_symbol)
);

CREATE TABLE market_import_link (
    market_symbol VARCHAR(50) REFERENCES market(symbol) ON DELETE CASCADE,
    import_good_symbol trade_good_symbol REFERENCES trade_good(symbol),
    PRIMARY KEY (market_symbol, import_good_symbol)
);

CREATE TABLE market_exchange_link (
    market_symbol VARCHAR(50) REFERENCES market(symbol) ON DELETE CASCADE,
    exchange_good_symbol trade_good_symbol REFERENCES trade_good(symbol),
    PRIMARY KEY (market_symbol, exchange_good_symbol)
);

CREATE TABLE market_transaction_link (
    market_symbol VARCHAR(50) REFERENCES market(symbol) ON DELETE CASCADE,
    transaction_id INTEGER REFERENCES market_transaction(id),
    PRIMARY KEY (market_symbol, transaction_id)
);

CREATE TABLE jump_gate_link (
    jump_gate_symbol VARCHAR(50) REFERENCES jump_gate(symbol),
    system_symbol VARCHAR(50) REFERENCES system(symbol),
    distance INTEGER NOT NULL,
    PRIMARY KEY (jump_gate_symbol, system_symbol)
);

-- #####
-- Fleet
-- #####

CREATE TABLE ship (
    symbol VARCHAR(50) PRIMARY KEY,
    cargo_capacity INTEGER NOT NULL,
    cargo_current_units INTEGER NOT NULL,
    fuel_capacity INTEGER NOT NULL,
    fuel_current INTEGER NOT NULL,
    registration_id INTEGER NOT NULL, -- REFERENCES ship_registration(id),
    nav_id INTEGER NOT NULL, -- REFERENCES ship_nav(id),
    nav_route_id INTEGER NOT NULL, -- REFERENCES ship_nav_route(id),
    crew_id INTEGER NOT NULL -- REFERENCES ship_crew(id),
);

CREATE TABLE ship_registration (
    id SERIAL PRIMARY KEY,
    faction_symbol faction_symbol REFERENCES faction(symbol),
    role ship_role NOT NULL
);

CREATE TABLE ship_nav (
    id SERIAL PRIMARY KEY,
    current_system_symbol VARCHAR(50) REFERENCES system(symbol) NOT NULL,
    current_waypoint_symbol VARCHAR(50) REFERENCES waypoint(symbol) NOT NULL,
    status ship_nav_status NOT NULL,
    flight_mode ship_flight_mode NOT NULL DEFAULT 'CRUISE'
);

CREATE TABLE ship_nav_route (
    id SERIAL PRIMARY KEY,
    destination_waypoint_symbol VARCHAR(50) REFERENCES waypoint(symbol) NOT NULL,
    departure_waypoint_symbol VARCHAR(50) REFERENCES waypoint(symbol) NOT NULL,
    departure_time TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    arrival_time TIMESTAMP WITHOUT TIME ZONE NOT NULL
);

CREATE TABLE ship_crew (
    id SERIAL PRIMARY KEY,
    current INTEGER NOT NULL,
    required INTEGER NOT NULL,
    capacity INTEGER NOT NULL,
    rotation ship_crew_rotation NOT NULL DEFAULT 'STRICT',
    morale INTEGER NOT NULL CHECK (morale >= 0 AND morale <= 100),
    wages INTEGER NOT NULL CHECK (wages >= 0)
);

CREATE TABLE installation_requirements (
    id SERIAL PRIMARY KEY,
    power INTEGER,
    crew INTEGER,
    slots INTEGER
);

CREATE TABLE ship_component (
    symbol ship_component_symbol PRIMARY KEY,
    name VARCHAR(50),
    description VARCHAR(500)
);

CREATE TABLE frame (
    symbol ship_component_symbol PRIMARY KEY NOT NULL REFERENCES ship_component(symbol),
    condition INTEGER NOT NULL CHECK (condition >= 0 AND condition <= 100),
    module_slots INTEGER NOT NULL CHECK (module_slots >= 0),
    mounting_points INTEGER NOT NULL CHECK (mounting_points >= 0),
    fuel_capacity INTEGER NOT NULL CHECK (fuel_capacity >= 0)
);

CREATE TABLE reactor (
    symbol ship_component_symbol PRIMARY KEY NOT NULL REFERENCES ship_component(symbol),
    condition INTEGER NOT NULL CHECK (condition >= 0 AND condition <= 100),
    power_output INTEGER NOT NULL CHECK (power_output >= 0)
);

CREATE TABLE engine (
    symbol ship_component_symbol PRIMARY KEY NOT NULL REFERENCES ship_component(symbol),
    condition INTEGER NOT NULL CHECK (condition >= 0 AND condition <= 100),
    speed INTEGER NOT NULL CHECK (speed >= 1)
);

CREATE TABLE module (
    symbol ship_component_symbol PRIMARY KEY NOT NULL REFERENCES ship_component(symbol),
    capacity INTEGER CHECK (capacity >= 0),
    range INTEGER CHECK (range >= 0)
);

CREATE TABLE mount (
    symbol ship_component_symbol PRIMARY KEY NOT NULL REFERENCES ship_component(symbol),
    strength INTEGER CHECK (strength >= 0)
);

CREATE TABLE ship_cargo_inventory (
    ship_symbol VARCHAR(50) REFERENCES ship(symbol) NOT NULL,
    trade_good_symbol trade_good_symbol REFERENCES trade_good(symbol) NOT NULL,
    units INTEGER NOT NULL CHECK (units >= 1),
    PRIMARY KEY (ship_symbol)
);

CREATE TABLE fuel_consumed_log (
    id SERIAL PRIMARY KEY,
    ship_symbol VARCHAR(50) REFERENCES ship(symbol) NOT NULL,
    amount INTEGER NOT NULL CHECK (amount >= 0),
    timestamp TIMESTAMP NOT NULL
);

CREATE TABLE contract_deliver_goods (
    contract_id VARCHAR(50) REFERENCES contract(id) NOT NULL,
    trade_good_symbol trade_good_symbol REFERENCES trade_good(symbol) NOT NULL,
    destination_waypoint_symbol VARCHAR(50) REFERENCES waypoint(symbol) NOT NULL,
    units_required INTEGER NOT NULL,
    units_fulfilled INTEGER NOT NULL,
    PRIMARY KEY (contract_id, trade_good_symbol, destination_waypoint_symbol)
);

CREATE TABLE shipyard (
    symbol VARCHAR(50) PRIMARY KEY REFERENCES waypoint(symbol)
);

CREATE TABLE shipyard_transaction (
    transaction_id SERIAL PRIMARY KEY,
    shipyard_symbol VARCHAR(50) REFERENCES shipyard(symbol) ON DELETE CASCADE,
    ship_symbol VARCHAR(50),
    price INTEGER NOT NULL CHECK (price >= 0),
    agent_symbol VARCHAR(50) NOT NULL,
    timestamp TIMESTAMP NOT NULL
);

CREATE TABLE shipyard_ship (
    id SERIAL PRIMARY KEY,
    shipyard_symbol VARCHAR(50) REFERENCES shipyard(symbol) ON DELETE CASCADE,
    ship_type ship_type NOT NULL,
    ship_name VARCHAR(50) NOT NULL,
    ship_description VARCHAR(1000) NOT NULL,
    purchase_price INTEGER NOT NULL CHECK (purchase_price >= 0)
);

-- ########
-- Fleet link tables
-- ########

CREATE TABLE agent_ship_link (
    agent_symbol VARCHAR(50) REFERENCES agent(symbol),
    ship_symbol VARCHAR(50) REFERENCES ship(symbol),
    PRIMARY KEY (agent_symbol, ship_symbol)
);

CREATE TABLE ship_main_component_link (
    ship_symbol VARCHAR(50) REFERENCES ship(symbol) PRIMARY KEY,
    frame_symbol ship_component_symbol REFERENCES frame(symbol) NOT NULL,
    reactor_symbol ship_component_symbol REFERENCES reactor(symbol) NOT NULL,
    engine_symbol ship_component_symbol REFERENCES engine(symbol) NOT NULL
);

CREATE TABLE ship_module_link (
    id SERIAL PRIMARY KEY,
    ship_symbol VARCHAR(50) REFERENCES ship(symbol) NOT NULL,
    module_symbol ship_component_symbol REFERENCES module(symbol) NOT NULL
);

CREATE TABLE ship_mount_link (
    id SERIAL PRIMARY KEY,
    ship_symbol VARCHAR(50) REFERENCES ship(symbol) NOT NULL,
    mount_symbol ship_component_symbol REFERENCES mount(symbol) NOT NULL
);

CREATE TABLE installation_requirements_link (
    component_symbol ship_component_symbol REFERENCES ship_component(symbol) NOT NULL,
    installation_requirements_id INTEGER REFERENCES installation_requirements(id) NOT NULL,
    PRIMARY KEY (component_symbol, installation_requirements_id)
);

CREATE TABLE mount_deposit_link (
    trade_good_symbol trade_good_symbol REFERENCES trade_good(symbol) NOT NULL,
    mount_symbol ship_component_symbol REFERENCES mount(symbol) NOT NULL,
    PRIMARY KEY (trade_good_symbol, mount_symbol)
);

CREATE TABLE shipyard_transaction_link (
    shipyard_symbol VARCHAR(50) REFERENCES shipyard(symbol) ON DELETE CASCADE,
    transaction_id INTEGER REFERENCES shipyard_transaction(transaction_id),
    PRIMARY KEY (shipyard_symbol, transaction_id)
);

CREATE TABLE shipyard_ship_main_component_link (
    shipyard_ship_id INTEGER REFERENCES shipyard_ship(id) PRIMARY KEY,
    frame_symbol ship_component_symbol REFERENCES frame(symbol) NOT NULL,
    reactor_symbol ship_component_symbol REFERENCES reactor(symbol) NOT NULL,
    engine_symbol ship_component_symbol REFERENCES engine(symbol) NOT NULL
);

CREATE TABLE shipyard_ship_module_link (
    shipyard_ship_id INTEGER REFERENCES shipyard_ship(id) NOT NULL,
    module_symbol ship_component_symbol REFERENCES module(symbol) NOT NULL
);

CREATE TABLE shipyard_ship_mount_link (
    shipyard_ship_id INTEGER REFERENCES shipyard_ship(id) NOT NULL,
    mount_symbol ship_component_symbol REFERENCES mount(symbol) NOT NULL
);

CREATE TABLE shipyard_ship_link (
    shipyard_symbol VARCHAR(50) REFERENCES shipyard(symbol) ON DELETE CASCADE,
    shipyard_ship_id INTEGER REFERENCES shipyard_ship(id),
    PRIMARY KEY (shipyard_symbol, shipyard_ship_id)
);

ALTER TABLE faction ADD CONSTRAINT fk_faction_headquarters FOREIGN KEY (headquarters) REFERENCES waypoint(symbol);

ALTER TABLE market_transaction ADD CONSTRAINT fk_market_transaction_ship FOREIGN KEY (ship) REFERENCES ship(symbol);

ALTER TABLE ship ADD CONSTRAINT fk_ship_registration_id FOREIGN KEY (registration_id) REFERENCES ship_registration(id);
ALTER TABLE ship ADD CONSTRAINT fk_ship_nav_id FOREIGN KEY (nav_id) REFERENCES ship_nav(id);
ALTER TABLE ship ADD CONSTRAINT fk_ship_nav_route_id FOREIGN KEY (nav_route_id) REFERENCES ship_nav_route(id);
ALTER TABLE ship ADD CONSTRAINT fk_ship_crew_id FOREIGN KEY (crew_id) REFERENCES ship_crew(id);