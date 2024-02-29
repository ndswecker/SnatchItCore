REFERENCE_GUIDE = {
    "species": {
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
        4124: {
            "common_name": "Northern Flicker",
            "scientific_name": "Colaptes auratus",
            "alpha_code": "NOFL",
            "species_number": 4124,
            "band_sizes": ["1A", "1D", "2"],
            "wing_chord_range": (110, 130),
            "WRP_groups": [3, 5],
            "male_brood_patch": True,
            "pyle_second_edition_page": 202,
        },
    },
    "wrp_groups": {
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
    },
    "dispositions": {
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
    },
    "age_annual": {
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
    },
}
