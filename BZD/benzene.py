# Data sources
database(
    thermoLibraries = ['primaryThermoLibrary', 'BurkeH2O2', 'FFCM1(-)'],
    reactionLibraries = ['Dooley/methylformate_all_N2bathgas'],
    seedMechanisms = [],
    kineticsDepositories = 'default',
    kineticsFamilies = 'default',
    kineticsEstimator = 'rate rules',
)

generatedSpeciesConstraints(
    allowed=['input species','seed mechanisms','reaction libraries'],	
    maximumRadicalElectrons = 2,
    maximumOxygenAtoms = 10,
    maximumCarbonAtoms = 15,		
)

# List of species
species(
    label='toluene',
    reactive=True,
    structure=SMILES("Cc1ccccc1")
)

species(
    label='tolyl',
    reactive=True,
    structure=adjacencyList("""
    multiplicity 2
    1  C u1 p0 c0 {2,S} {8,S} {9,S}
    2  C u0 p0 c0 {1,S} {3,S} {7,D}
    3  C u0 p0 c0 {2,S} {4,D} {10,S}
    4  C u0 p0 c0 {3,D} {5,S} {11,S}
    5  C u0 p0 c0 {4,S} {6,D} {12,S}
    6  C u0 p0 c0 {5,D} {7,S} {13,S}
    7  C u0 p0 c0 {2,D} {6,S} {14,S}
    8  H u0 p0 c0 {1,S}
    9  H u0 p0 c0 {1,S}
    10 H u0 p0 c0 {3,S}
    11 H u0 p0 c0 {4,S}
    12 H u0 p0 c0 {5,S}
    13 H u0 p0 c0 {6,S}
    14 H u0 p0 c0 {7,S}
    """)
)

species(
    label='o-cresol',
    reactive=True,
    structure=adjacencyList("""
    multiplicity 1
    1  C u0 p0 c0 {2,S} {8,S} {9,S} {15,S}
    2  C u0 p0 c0 {1,S} {3,S} {7,D}
    3  C u0 p0 c0 {2,S} {4,D} {10,S}
    4  C u0 p0 c0 {3,D} {5,S} {11,S}
    5  C u0 p0 c0 {4,S} {6,D} {12,S}
    6  C u0 p0 c0 {5,D} {7,S} {13,S}
    7  C u0 p0 c0 {2,D} {6,S} {14,S}
    8  H u0 p0 c0 {1,S}
    9  H u0 p0 c0 {1,S}
    10 O u0 p2 c0 {3,S} {16,S}
    11 H u0 p0 c0 {4,S}
    12 H u0 p0 c0 {5,S}
    13 H u0 p0 c0 {6,S}
    14 H u0 p0 c0 {7,S}
    15 H u0 p0 c0 {1,S}
    16 H u0 p0 c0 {10,S}
    """)
)

species(
    label='MHCHD',
    reactive=True,
    structure=adjacencyList("""
    multiplicity 2
    1  C u0 p0 c0 {2,S} {8,S} {9,S} {14,S}
    2  C u0 p0 c0 {1,S} {3,S} {7,D}
    3  C u0 p0 c0 {2,S} {4,S} {10,S} {17,S}
    4  C u1 p0 c0 {3,S} {5,S} {16,S}
    5  C u0 p0 c0 {4,S} {6,D} {11,S}
    6  C u0 p0 c0 {5,D} {7,S} {12,S}
    7  C u0 p0 c0 {2,D} {6,S} {13,S}
    8  H u0 p0 c0 {1,S}
    9  H u0 p0 c0 {1,S}
    10 O u0 p2 c0 {3,S} {15,S}
    11 H u0 p0 c0 {5,S}
    12 H u0 p0 c0 {6,S}
    13 H u0 p0 c0 {7,S}
    14 H u0 p0 c0 {1,S}
    15 H u0 p0 c0 {10,S}
    16 H u0 p0 c0 {4,S}
    17 H u0 p0 c0 {3,S}
    """)
)

species(
    label='benzaldehyde',
    reactive=True,
    structure=adjacencyList("""
    multiplicity 1
    1  C u0 p0 c0 {2,S} {6,D} {9,S}
    2  C u0 p0 c0 {1,S} {3,D} {10,S}
    3  C u0 p0 c0 {2,D} {4,S} {11,S}
    4  C u0 p0 c0 {3,S} {5,D} {12,S}
    5  C u0 p0 c0 {4,D} {6,S} {13,S}
    6  C u0 p0 c0 {1,D} {5,S} {7,S}
    7  C u0 p0 c0 {6,S} {8,D} {14,S}
    8  O u0 p2 c0 {7,D}
    9  H u0 p0 c0 {1,S}
    10 H u0 p0 c0 {2,S}
    11 H u0 p0 c0 {3,S}
    12 H u0 p0 c0 {4,S}
    13 H u0 p0 c0 {5,S}
    14 H u0 p0 c0 {7,S}
    """)
)

species(
    label='N2',
    reactive=False,
    structure=SMILES("N#N")
)

species(
    label='O2',
    reactive=True,
    structure=SMILES("[O][O]")
)

species(
    label='tolylperoxy',
    reactive=True,
    structure=SMILES("[O]OCc1ccccc1")
)

species(
    label='OH',
    reactive=True,
    structure=adjacencyList("""
    multiplicity 2
    1 O u1 p2 c0 {2,S}
    2 H u0 p0 c0 {1,S}
    """),
)

species(
    label='1,2 bzd',
    reactive=True,
    structure=adjacencyList("""
    1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
    2  O u0 p2 c0 {1,S} {3,S}
    3  O u0 p2 c0 {2,S} {4,S}
    4  C u0 p0 c0 {3,S} {5,S} {9,D}
    5  C u0 p0 c0 {4,S} {6,D} {12,S}
    6  C u0 p0 c0 {5,D} {7,S} {13,S}
    7  C u0 p0 c0 {6,S} {8,D} {14,S}
    8  C u0 p0 c0 {7,D} {9,S} {15,S}
    9  C u0 p0 c0 {1,S} {4,D} {8,S}
    10 H u0 p0 c0 {1,S}
    11 H u0 p0 c0 {1,S}
    12 H u0 p0 c0 {5,S}
    13 H u0 p0 c0 {6,S}
    14 H u0 p0 c0 {7,S}
    15 H u0 p0 c0 {8,S}
    """),
)

species(
    label='1,3 bzd',
    reactive=True,
    structure=adjacencyList("""
    1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
    2  O u0 p2 c0 {1,S} {3,S}
    3  C u0 p0 c0 {2,S} {4,S} {8,D}
    4  C u0 p0 c0 {3,S} {5,D} {12,S}
    5  C u0 p0 c0 {4,D} {6,S} {13,S}
    6  C u0 p0 c0 {5,S} {7,D} {14,S}
    7  C u0 p0 c0 {6,D} {8,S} {15,S}
    8  C u0 p0 c0 {3,D} {7,S} {9,S}
    9  O u0 p2 c0 {1,S} {8,S}
    10 H u0 p0 c0 {1,S}
    11 H u0 p0 c0 {1,S}
    12 H u0 p0 c0 {4,S}
    13 H u0 p0 c0 {5,S}
    14 H u0 p0 c0 {6,S}
    15 H u0 p0 c0 {7,S}
    """),
)

# Reaction systems
simpleReactor(
    temperature=(298,'K'),
    pressure=(1.0,'bar'),
    initialMoleFractions={
        "N2": 79,
        "O2": 21,
        "OH": 1e-13,
        "toluene": 1e-8,
        "tolyl": 0,
        "tolylperoxy": 0,
        "o-cresol": 0,
        "MHCHD": 0,
        "benzaldehyde": 0,
	"1,3 bzd": 0,
        "1,2 bzd": 0,
    },
    terminationConversion={
        'toluene': 0.99,
    },
    terminationTime=(1e2,'s'),
    sensitivity=['toluene','toluene', 'tolyl', 'tolylperoxy', 'o-cresol', 'benzaldehyde', '1,3 bzd', '1,2 bzd'],
    sensitivityThreshold=0.001,
)

simulator(
    atol=1e-16,
    rtol=1e-8,
)

model(
    toleranceKeepInEdge=0.0,
    toleranceMoveToCore=0.03,
    toleranceInterruptSimulation=0.03,
    maximumEdgeSpecies=100000,
    filterReactions = True,
)

options(
    units='si',
    generateOutputHTML=True,
    generatePlots=True,
    saveEdgeSpecies=True,
    saveSimulationProfiles=True,
)

generatedSpeciesConstraints(
    allowSingletO2 = True
)

uncertainty(
    localAnalysis=True,
    globalAnalysis=False,
    uncorrelated=True,
    localNumber=10,
    globalNumber=5,
    terminationTime=None,
    pceRunTime=1800,
    pceErrorTol=None,
    pceMaxEvals=None,
    logx=True
)
