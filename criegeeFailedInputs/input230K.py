database(
    thermoLibraries = ['primaryThermoLibrary', 'BurkeH2O2', 'FFCM1(-)'],
    reactionLibraries = ['Dooley/methylformate_all_N2bathgas'],
    seedMechanisms = [],
    kineticsDepositories = 'default', 
    kineticsFamilies = 'default',
    kineticsEstimator = 'rate rules',
)

# Constraints on generated species
generatedSpeciesConstraints(
    allowed=['input species','seed mechanisms','reaction libraries'],	
    maximumRadicalElectrons = 2,
    maximumOxygenAtoms = 10,
    maximumCarbonAtoms = 15,		
)

species(
    label='CH2OO',
    reactive=True,
    structure=InChI("InChI=1S/CH2O2/c1-3-2/h1H2"),
)

species(
    label='NO',
    reactive=True,
    structure=InChI("InChI=1S/NO/c1-2"),
)

species(
    label='NO2',
    reactive=True,
    structure=InChI("InChI=1S/NO2/c2-1-3"),
)

species(
    label='SO2',
    reactive=True,
    structure=InChI("InChI=1S/O2S/c1-3-2"),
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
    label='O2',
    reactive=True,
    structure=SMILES("[O][O]"),
)

species(
    label='N2',
    reactive=False,
    structure=InChI("InChI=1/N2/c1-2"),
)

simpleReactor(
    temperature=(230,'K'),
    pressure=(1.0,'bar'),
    initialMoleFractions={
        "CH2OO": 5e-10,
        "NO": 5e-7,
        "NO2": 5e-5,
        "SO2": 5e-5,
        "OH": 5e-13,
        "O2": 0.2,
        "N2": 0.8,
    },
    terminationConversion={
        'OH': 0.99,
    },
    terminationTime=(86400, 's'),
)

model(
    toleranceKeepInEdge=0.0,
    toleranceMoveToCore=0.01,
    toleranceInterruptSimulation=0.02,
    maximumEdgeSpecies=100000,
    filterReactions = True,
)

simulator(
    atol=1e-16,
    rtol=1e-8,
)

options(
    units='si',
    generateOutputHTML = True,
    generatePlots=False,
    saveSimulationProfiles = True,
    saveEdgeSpecies = True,
)
