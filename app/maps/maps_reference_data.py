# Description: Reference data for MAPS and USGS banding codes and descriptions

SITE_LOCATIONS = {
    "MORS": {
        "name": "Morse Preserve MAPS",
        "code": "MORS",
        "BBL_location_id": 223665
    },
    "GHPR": {
        "name": "Glacial Heritage Preserve MAPS",
        "code": "GHPR",
        "BBL_location_id": 0
    },
}

SPECIES = {
    5810: {
        "common_name": "Song Sparrow",
        "scientific_name": "Melospiza melodia",
        "alpha_code": "SOSP",
        "species_number": 5810,
        "band_sizes": ["1B"],
        "wing_chord_range": (50, 90),
        "WRP_groups": [3, 4],
        "male_brood_patch": False,
        "pyle_second_edition_page": 527,
    },
    6460: {
        "common_name": "Orange-crowned Warbler",
        "scientific_name": "Leiothlypis celata",
        "alpha_code": "OCWA",
        "species_number": 6460,
        "band_sizes": ["0", "0A"],
        "wing_chord_range": (50, 70),
        "WRP_groups": [3, 8],
        "male_brood_patch": False,
        "pyle_second_edition_page": 589,
    },
    5880: {
        "common_name": "Spotted Towhee",
        "scientific_name": "Pipilo maculatus",
        "alpha_code": "SPTO",
        "species_number": 5880,
        "band_sizes": ["1D", "1A", "2"],
        "wing_chord_range": (76, 95),
        "WRP_groups": [3],
        "male_brood_patch": False,
        "pyle_second_edition_page": 538,
    },
    7580: {
        "common_name": "Swainson's Thrush",
        "scientific_name": "Catharus ustulatus",
        "alpha_code": "SWTH",
        "species_number": 7580,
        "band_sizes": ["1B"],
        "wing_chord_range": (80, 110),
        "WRP_groups": [3],
        "male_brood_patch": False,
        "pyle_second_edition_page": 422,
    },
    4310: {
        "common_name": "Anna's Hummingbird",
        "scientific_name": "Calypte anna",
        "alpha_code": "ANHU",
        "species_number": 4310,
        "band_sizes": ["0"],
        "wing_chord_range": (46, 52),
        "WRP_groups": [3, 5, 6],
        "male_brood_patch": False,
        "pyle_second_edition_page": 104,
    },
    # New birds added below
    3160: {
        "common_name": "Mourning Dove",
        "scientific_name": "Zenaida macroura",
        "alpha_code": "MODO",
        "species_number": 3160,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    4240: {
        "common_name": "Vaux's Swift",
        "scientific_name": "Chaetura vauxi",
        "alpha_code": "VASW",
        "species_number": 4240,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    4330: {
        "common_name": "Rufous Hummingbird",
        "scientific_name": "Selasphorus rufus",
        "alpha_code": "RUHU",
        "species_number": 4330,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    2120: {
        "common_name": "Virginia Rail",
        "scientific_name": "Rallus limicola",
        "alpha_code": "VIRA",
        "species_number": 2120,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    3320: {
        "common_name": "Sharp-shinned Hawk",
        "scientific_name": "Accipiter striatus",
        "alpha_code": "SSHA",
        "species_number": 3320,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    3330: {
        "common_name": "Cooper's Hawk",
        "scientific_name": "Accipiter cooperii",
        "alpha_code": "COHA",
        "species_number": 3330,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    3650: {
        "common_name": "Barn Owl",
        "scientific_name": "Tyto alba",
        "alpha_code": "BNOW",
        "species_number": 3650,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    3750: {
        "common_name": "Great Horned Owl",
        "scientific_name": "Bubo virginianus",
        "alpha_code": "GHOW",
        "species_number": 3750,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    3900: {
        "common_name": "Belted Kingfisher",
        "scientific_name": "Megaceryle alcyon",
        "alpha_code": "BEKI",
        "species_number": 3900,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    4030: {
        "common_name": "Red-breasted Sapsucker",
        "scientific_name": "Sphyrapicus ruber",
        "alpha_code": "RBSA",
        "species_number": 4030,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    3940: {
        "common_name": "Downy Woodpecker",
        "scientific_name": "Dryobates pubescens",
        "alpha_code": "DOWO",
        "species_number": 3940,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    3930: {
        "common_name": "Hairy Woodpecker",
        "scientific_name": "Dryobates villosus",
        "alpha_code": "HAWO",
        "species_number": 3930,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    4130: {
        "common_name": "Red-shafted Flicker",
        "scientific_name": "Colaptes auratus cafer",
        "alpha_code": "RSFL",
        "species_number": 4130,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    4050: {
        "common_name": "Pileated Woodpecker",
        "scientific_name": "Dryocopus pileatus",
        "alpha_code": "PIWO",
        "species_number": 4050,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    4590: {
        "common_name": "Olive-sided Flycatcher",
        "scientific_name": "Contopus cooperi",
        "alpha_code": "OSFL",
        "species_number": 4590,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    4620: {
        "common_name": "Western Wood-Pewee",
        "scientific_name": "Contopus sordidulus",
        "alpha_code": "WEWP",
        "species_number": 4620,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    4660: {
        "common_name": "Willow Flycatcher",
        "scientific_name": "Empidonax traillii",
        "alpha_code": "WIFL",
        "species_number": 4660,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    4649: {
        "common_name": "Western Flycatcher",
        "scientific_name": "Empidonax difficilis",
        "alpha_code": "WEFL",
        "species_number": 4649,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    4680: {
        "common_name": "Hammond's Flycatcher",
        "scientific_name": "Empidonax hammondii",
        "alpha_code": "HAFL",
        "species_number": 4680,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    6320: {
        "common_name": "Hutton's Vireo",
        "scientific_name": "Vireo huttoni",
        "alpha_code": "HUVI",
        "species_number": 6320,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    6292: {
        "common_name": "Cassin's Vireo",
        "scientific_name": "Vireo cassinii",
        "alpha_code": "CAVI",
        "species_number": 6292,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    6270: {
        "common_name": "Warbling Vireo",
        "scientific_name": "Vireo gilvus",
        "alpha_code": "WAVI",
        "species_number": 6270,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    4780: {
        "common_name": "Steller's Jay",
        "scientific_name": "Cyanocitta stelleri",
        "alpha_code": "STJA",
        "species_number": 4780,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    4880: {
        "common_name": "American Crow",
        "scientific_name": "Corvus brachyrhynchos",
        "alpha_code": "AMCR",
        "species_number": 4880,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    4813: {
        "common_name": "California Scrub-Jay",
        "scientific_name": "Aphelocoma californica",
        "alpha_code": "CASJ",
        "species_number": 4813,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    4860: {
        "common_name": "Common Raven",
        "scientific_name": "Corvus corax",
        "alpha_code": "CORA",
        "species_number": 4860,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    6110: {
        "common_name": "Purple Martin",
        "scientific_name": "Progne subis",
        "alpha_code": "PUMA",
        "species_number": 6110,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    6140: {
        "common_name": "Tree Swallow",
        "scientific_name": "Tachycineta bicolor",
        "alpha_code": "TRES",
        "species_number": 6140,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    6150: {
        "common_name": "Violet-green Swallow",
        "scientific_name": "Tachycineta thalassina",
        "alpha_code": "VGSW",
        "species_number": 6150,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    6120: {
        "common_name": "Cliff Swallow",
        "scientific_name": "Petrochelidon pyrrhonota",
        "alpha_code": "CLSW",
        "species_number": 6120,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    6130: {
        "common_name": "Barn Swallow",
        "scientific_name": "Hirundo rustica",
        "alpha_code": "BARS",
        "species_number": 6130,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    7350: {
        "common_name": "Black-capped Chickadee",
        "scientific_name": "Poecile atricapillus",
        "alpha_code": "BCCH",
        "species_number": 7350,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    7410: {
        "common_name": "Chestnut-backed Chickadee",
        "scientific_name": "Poecile rufescens",
        "alpha_code": "CBCH",
        "species_number": 7410,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    7430: {
        "common_name": "Bushtit",
        "scientific_name": "Psaltriparus minimus",
        "alpha_code": "BUSH",
        "species_number": 7430,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    7280: {
        "common_name": "Red-breasted Nuthatch",
        "scientific_name": "Sitta canadensis",
        "alpha_code": "RBNU",
        "species_number": 7280,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    7260: {
        "common_name": "Brown Creeper",
        "scientific_name": "Certhia americana",
        "alpha_code": "BRCR",
        "species_number": 7260,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    7210: {
        "common_name": "House Wren",
        "scientific_name": "Troglodytes aedon",
        "alpha_code": "HOWR",
        "species_number": 7210,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    7221: {
        "common_name": "Pacific Wren",
        "scientific_name": "Troglodytes pacificus",
        "alpha_code": "PAWR",
        "species_number": 7221,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    7250: {
        "common_name": "Marsh Wren",
        "scientific_name": "Cistothorus palustris",
        "alpha_code": "MAWR",
        "species_number": 7250,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    7190: {
        "common_name": "Bewick's Wren",
        "scientific_name": "Thryomanes bewickii",
        "alpha_code": "BEWR",
        "species_number": 7190,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    7480: {
        "common_name": "Golden-crowned Kinglet",
        "scientific_name": "Regulus satrapa",
        "alpha_code": "GCKI",
        "species_number": 7480,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    7490: {
        "common_name": "Ruby-crowned Kinglet",
        "scientific_name": "Corthylio calendula",
        "alpha_code": "RCKI",
        "species_number": 7490,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    7580: {
        "common_name": "Swainson's Thrush",
        "scientific_name": "Catharus ustulatus",
        "alpha_code": "SWTH",
        "species_number": 7580,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    7610: {
        "common_name": "American Robin",
        "scientific_name": "Turdus migratorius",
        "alpha_code": "AMRO",
        "species_number": 7610,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    7590: {
        "common_name": "Hermit Thrush",
        "scientific_name": "Catharus guttatus",
        "alpha_code": "HETH",
        "species_number": 7590,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    4930: {
        "common_name": "European Starling",
        "scientific_name": "Sturnus vulgaris",
        "alpha_code": "EUST",
        "species_number": 4930,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    6190: {
        "common_name": "Cedar Waxwing",
        "scientific_name": "Bombycilla cedrorum",
        "alpha_code": "CEDW",
        "species_number": 6190,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    5190: {
        "common_name": "House Finch",
        "scientific_name": "Haemorhous mexicanus",
        "alpha_code": "HOFI",
        "species_number": 5190,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    5170: {
        "common_name": "Purple Finch",
        "scientific_name": "Haemorhous purpureus",
        "alpha_code": "PUFI",
        "species_number": 5170,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    5210: {
        "common_name": "Red Crossbill",
        "scientific_name": "Loxia curvirostra",
        "alpha_code": "RECR",
        "species_number": 5210,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    5330: {
        "common_name": "Pine Siskin",
        "scientific_name": "Spinus pinus",
        "alpha_code": "PISI",
        "species_number": 5330,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    5290: {
        "common_name": "American Goldfinch",
        "scientific_name": "Spinus tristis",
        "alpha_code": "AMGO",
        "species_number": 5290,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
        5140: {
        "common_name": "Evening Grosbeak",
        "scientific_name": "Coccothraustes vespertinus",
        "alpha_code": "EVGR",
        "species_number": 5140,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    6460: {
        "common_name": "Orange-crowned Warbler",
        "scientific_name": "Leiothlypis celata",
        "alpha_code": "OCWA",
        "species_number": 6460,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    6800: {
        "common_name": "MacGillivray's Warbler",
        "scientific_name": "Geothlypis tolmiei",
        "alpha_code": "MGWA",
        "species_number": 6800,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    6810: {
        "common_name": "Common Yellowthroat",
        "scientific_name": "Geothlypis trichas",
        "alpha_code": "COYE",
        "species_number": 6810,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    6520: {
        "common_name": "Yellow Warbler",
        "scientific_name": "Setophaga petechia",
        "alpha_code": "YEWA",
        "species_number": 6520,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    6560: {
        "common_name": "Audubon's Warbler",
        "scientific_name": "Setophaga auduboni auduboni",
        "alpha_code": "AUWA",
        "species_number": 6560,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    6650: {
        "common_name": "Black-throated Gray Warbler",
        "scientific_name": "Setophaga nigrescens",
        "alpha_code": "BTYW",
        "species_number": 6650,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    6850: {
        "common_name": "Wilson's Warbler",
        "scientific_name": "Cardellina pusilla",
        "alpha_code": "WIWA",
        "species_number": 6850,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    5880: {
        "common_name": "Spotted Towhee",
        "scientific_name": "Pipilo maculatus",
        "alpha_code": "SPTO",
        "species_number": 5880,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    5600: {
        "common_name": "Chipping Sparrow",
        "scientific_name": "Spizella passerina",
        "alpha_code": "CHSP",
        "species_number": 5600,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    5420: {
        "common_name": "Savannah Sparrow",
        "scientific_name": "Passerculus sandwichensis",
        "alpha_code": "SAVS",
        "species_number": 5420,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    5810: {
        "common_name": "Song Sparrow",
        "scientific_name": "Melospiza melodia",
        "alpha_code": "SOSP",
        "species_number": 5810,
        "band_sizes": ["1B"],
        "wing_chord_range": (50, 90),
        "WRP_groups": [3, 4],
        "male_brood_patch": False,
        "pyle_second_edition_page": 527,
    },
    5547: {
        "common_name": "Puget Sound White-crowned Sparrow",
        "scientific_name": "Zonotrichia leucophrys pugetensis",
        "alpha_code": "PSWS",
        "species_number": 5547,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    5671: {
        "common_name": "Oregon Junco",
        "scientific_name": "Junco hyemalis oreganus",
        "alpha_code": "ORJU",
        "species_number": 5671,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    6070: {
        "common_name": "Western Tanager",
        "scientific_name": "Piranga ludoviciana",
        "alpha_code": "WETA",
        "species_number": 6070,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    5960: {
        "common_name": "Black-headed Grosbeak",
        "scientific_name": "Pheucticus melanocephalus",
        "alpha_code": "BHGR",
        "species_number": 5960,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    4980: {
        "common_name": "Red-winged Blackbird",
        "scientific_name": "Agelaius phoeniceus",
        "alpha_code": "RWBL",
        "species_number": 4980,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    5100: {
        "common_name": "Brewer's Blackbird",
        "scientific_name": "Euphagus cyanocephalus",
        "alpha_code": "BRBL",
        "species_number": 5100,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    4950: {
        "common_name": "Brown-headed Cowbird",
        "scientific_name": "Molothrus ater",
        "alpha_code": "BHCO",
        "species_number": 4950,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    3159: {
        "common_name": "Eurasian Collared-Dove",
        "scientific_name": "Streptopelia decaocto",
        "alpha_code": "ECDO",
        "species_number": 3159,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
        7670: {
        "common_name": "Western Bluebird",
        "scientific_name": "Sialia mexicana",
        "alpha_code": "WEBL",
        "species_number": 7670,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    3790: {
        "common_name": "Northern Pygmy-Owl",
        "scientific_name": "Glaucidium gnoma",
        "alpha_code": "NOPO",
        "species_number": 3790,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    },
    5990: {
        "common_name": "Lazuli Bunting",
        "scientific_name": "Passerina amoena",
        "alpha_code": "LAZB",
        "species_number": 5990,
        "band_sizes": [],
        "wing_chord_range": (),
        "WRP_groups": [],
        "male_brood_patch": None,
        "pyle_second_edition_page": None,
    }




}

WRP_GROUPS = {
    3: {
        "description": "Group 3 - Preformative molt less than complete, prebasic molt complete, and no prealternate molts occur.", 
        "codes_allowed": ["FPJ", "FCJ", "FPF", "FCF", "SPB", "DCB", "DPB", "MFCF", "MSPB"]
    },
    4: {
        "description": "Group 4 - Preformative and prebasic molts complete, and no prealternate molts occur.", 
        "codes_allowed": ["FPJ", "FCJ", "FPF", "FCF", "MFCF", "MSPB"]
    },
    5: {
        "description": "Group 5 - Preformative and prebasic molts less than complet and no prealternate molts occur.", 
        "codes_allowed": ["FPJ", "FCJ", "FPF", "FCF", "SPB", "SCB", "TPB", "DCB", "DPB", "TCB", "4PB"]
    },
    6: {
        "description": "Group 6 - Preformative molt less than complete, prebasic molt less than complete or complete. Prealternate molt occurs in the definative but not the first cylce.", 
        "codes_allowed": ["FPJ", "FCJ", "FPF", "FCF", "SPB", "DPA", "DCA", "DPB", "DCB", "SCB", "SPA", "SCA", "TPB"]
    },
    8: {
        "description": "Group 8 - Preformative molt less than complete, prebasic molt complete, and prealternate molt occur in both first and definative cycles.", 
        "codes_allowed": ["FPJ", "FCJ", "FPF", "FCF", "FPA", "FCA", "SPB", "DPA", "DCA", "DPB", "DCB", "DCU", "FCU"]
    },
}

DISPOSTIONS = {
    "N": {
        "maps": {
            "description": "New Bird",
            "code": "N",
        },
        "usgs": {
            "description": "Add (New Band)",
            "code": "1",
        },
    },
    "R": {
        "maps": {
            "description": "Recaptured Bird",
            "code": "R",
        },
        "usgs": {
            "description": "Added-To",
            "code": "6",
        },
    },
    "L": {
        "maps": {
            "description": "Lost Band",
            "code": "L",
        },
        "usgs": {
            "description": "Band Lost",
            "code": "8",
        },
    },
    "D": {
        "maps": {
            "description": "Destroyed Band (and or dead)",
            "code": "D",
        },
        "usgs": {
            "description": "Destroyed",
            "code": ["4", "X"],
        },
    },
    "U": {
        "maps": {
            "description": "Unbanded Bird",
            "code": "U",
        },
    },
    "C": {
        "maps": {
            "description": "Changed Band",
            "code": "C",
        },
        "usgs": {
            "description": "Replacing Band",
            "code": "5",
        },
    },
}

AGES_ANNUAL = {
    "4": {
        "maps": {
            "code": "4",
            "description": "Local (incapable of sustained flight)"
        },
        "usgs": {
            "code": "L",
            "description": "Local"
        }
    },
    "2": {
        "maps": {
            "code": "2",
            "description": "Hatch Year (HY)"
        },
        "usgs": {
            "code": "HY",
            "description": "Hatching Year"
        }
    },
    "1": {
        "maps": {
            "code": "1",
            "description": "After Hatch Year (AHY)"
        },
        "usgs": {
            "code": "AHY",
            "description": "After Hatching Year"
        }
    },
    "5": {
        "maps": {
            "code": "5",
            "description": "Second Year (SY)"
        },
        "usgs": {
            "code": "SY",
            "description": "Second Year"
        }
    },
    "6": {
        "maps": {
            "code": "6",
            "description": "After Second Year (ASY)"
        },
        "usgs": {
            "code": "ASY",
            "description": "After Second Year"
        }
    },
    "7": {
        "maps": {
            "code": "7",
            "description": "Third Year (TY)"
        },
        "usgs": {
            "code": "TY",
            "description": "Third Year"
        }
    },
    "8": {
        "maps": {
            "code": "8",
            "description": "After Third Year (ATY)"
        },
        "usgs": {
            "code": "ATY",
            "description": "After Third Year"
        }
    },
    "0": {
        "maps": {
            "code": "0",
            "description": "Indeterminable Age"
        },
        "usgs": {
            "code": "U",
            "description": "Unknown"
        }
    },
    "9": {
        "maps": {
            "code": "9",
            "description": "Not attempted"
        },
        "usgs": {
            "code": "U",
            "description": "Unknown"  # Assuming 'U' is equivalent to 'Not attempted'
        }
    },
}

HOW_AGE_DETERMINED = {
    "S": {
        "maps": {
            "code": "S",
            "description": "Skull"
        },
        "usgs": {
            "code": "SK",
            "description": "Skull"
        }
    },
    "C": {
        "maps": {
            "code": "C",
            "description": "Cloacal Protuberance"
        },
        "usgs": {
            "code": "CL",
            "description": "Cloacal Protuberance"
        }
    },
    "B": {
        "maps": {
            "code": "B",
            "description": "Brood Patch"
        },
        "usgs": {
            "code": "BP",
            "description": "Brood Patch"
        }
    },
    "F": {
        "maps": {
            "code": "F",
            "description": "Feather Wear"
        },
        "usgs": {
            "code": "FF",
            "description": "Flight feathers (remiges), condition or color"
        }
    },
    "J": {
        "maps": {
            "code": "J",
            "description": "Juvenile Body Plumage"
        },
        "usgs": {
            "code": "PL",
            "description": "Body Plumage"
        }
    },
    "M": {
        "maps": {
            "code": "M",
            "description": "Molt"
        },
        "usgs": {
            "code": "MR",
            "description": "Flight feathers (remiges), condition or color"
        }
    },
    "P": {
        "maps": {
            "code": "P",
            "description": "Plumage (non-juvenile)"
        },
        "usgs": {
            "code": "PL",
            "description": "Body Plumage"
        }
    },
    "N": {
        "maps": {
            "code": "N",
            "description": "Non-feather"
        },
    },
    "L": {
        "maps": {
            "code": "L",
            "description": "Molt Limit"
        },
        "usgs": {
            "code": "LP",
            "description": "Molt limit present"
        }
    },
    "I": {
        "maps": {
            "code": "I",
            "description": "Mouth/Bill"
        },
        "usgs": {
            "code": "MB",
            "description": "Mouth/Bill"
        }
    },
    "E": {
        "maps": {
            "code": "E",
            "description": "Eye color"
        },
        "usgs": {
            "code": "EY",
            "description": "Eye color"
        }
    },
    "W": {
        "maps": {
            "code": "W",
            "description": "Wing length"
        },
    },
    "T": {
        "maps": {
            "code": "T",
            "description": "Tail length"
        },
    },
    "O": {
        "maps": {
            "code": "O",
            "description": "Other (specify in notes)"
        },
        "usgs": {
            "code": "OT",
            "description": "Other"
        }
    },
}

SEXES = {
    "M": {
        "maps": {
            "code": "M",
            "description": "Male"
        },
        "usgs": {
            "code": "M",
            "description": "Male"
        }
    },
    "F": {
        "maps": {
            "code": "F",
            "description": "Female"
        },
        "usgs": {
            "code": "F",
            "description": "Female"
        }
    },
    "U": {
        "maps": {
            "code": "U",
            "description": "Unknown"
        },
        "usgs": {
            "code": "U",
            "description": "Unknown"
        }
    },
    "X": {
        "maps": {
            "code": "X",
            "description": "Not Attempted"
        },
        "usgs": {
            "code": "U",
            "description": "Unkown"
        }
    },
},