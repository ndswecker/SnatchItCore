import maps.maps_reference_data as REFERENCE_DATA

CAPTURE_CODE_CHOICES = [
    ("N", "(N) New Bird"),
    ("R", "(R) Recaptured Bird"),
    ("L", "(L) Lost Band"),
    ("D", "(D) Destroyed Band (and or dead)"),
    ("U", "(U) Unbanded Bird"),
    ("C", "(C) Changed band"),
    ("A", "(A) Added Band"),
]

SPECIES_CHOICES = [(k, f"{v['alpha_code']} - {v['common_name']}") for k, v in REFERENCE_DATA.SPECIES.items()]

AGE_ANNUAL_CHOICES = [
    (4, "4 - Local (incapable of sustained flight)"),
    (2, "2 - Hatch Year (HY)"),
    (1, "1 - After Hatch Year (AHY)"),
    (5, "5 - Second Year (SY)"),
    (6, "6 - After Second Year (ASY)"),
    (7, "7 - Third Year (TY)"),
    (8, "8 - After Third Year (ATY)"),
    (0, "0 - Inderterminable Age"),
    (9, "9 - Not attempted"),
]

AGE_WRP_CHOICES = [
    ("FPJ", "(FPJ) First prejuvenile molt"),
    ("FCJ", "(FCJ) First cycle juvenile plumage"),
    ("FPF", "(FPF) First preformative molt"),
    ("FCF", "(FCF) First cycle formative plumage"),
    ("HFCF", "(HFCF) Hatch year, first cycle formative plumage"),
    ("AFCF", "(AFCF) After hatch year, first cycle formative plumage"),
    ("MFCF", "(MFCF) Minimum first cycle formative"),
    ("FPA", "(FPA) First prealternate molt"),
    ("FCA", "(FCA) First cycle alternate plumage"),
    ("MFCA", "(MFCA) Minimum first cycle alternate"),
    ("SPB", "(SPB) Second prebasic molt"),
    ("MSPB", "(MSPB) Minimum second prebasic molt"),
    ("SCB", "(SCB) Second cycle basic plumage"),
    ("TPB", "(TPB) Third prebasic molt"),
    ("MSPB", "(MSPB) Minimum second prebasic molt"),
    ("DCB", "(DCB) Definitive cycle basic plumage"),
    ("DPA", "(DPA) Definitive prealternate molt"),
    ("DCA", "(DCA) Definitive cycle alternate plumage"),
    ("DPB", "(DPB) Definitive prebasic molt"),
    ("FCU", "(FCU) First cycle unknown plumage"),
    ("DCU", "(DCU) Definitive cycle unknown plumage"),
    ("UCU", "(UCU) Unknown cycle unknown plumage"),
]

HOW_AGED_SEXED_CHOICES = [
    ("S", "S - Skull"),
    ("C", "C - Cloacal Protuberance"),
    ("B", "B - Brood Patch"),
    ("F", "F - Feather Wear"),
    ("J", "J - Juvenile Body Plumage"),
    ("M", "M - Molt"),
    ("P", "P - Plumage (non-juvenile)"),
    ("N", "N - Non-feather"),
    ("W", "W - Wing chord"),
    ("L", "L - Molt Limit"),
    ("I", "I - Mouth/Bill"),
    ("E", "E - Eye color"),
    ("W", "W - Wing length"),
    ("T", "T - Tail length"),
    ("O", "O - Other (specify in notes)"),
]

SEX_CHOICES = [
    ("M", "Male"),
    ("F", "Female"),
    ("U", "Unknown"),
    ("X", "Not Attempted"),
]

SKULL_CHOICES = [
    (0, "0 - None"),
    (1, "1 - Trace"),
    (2, "2 - < 1/3"),
    (3, "3 - Half"),
    (4, "4 - > 2/3"),
    (5, "5 - Almost Complete"),
    (6, "6 - Fully Complete"),
    (8, "8 - Unable to Determine"),
]

CLOACAL_PROTUBERANCE_CHOICES = [
    (0, "0 - None"),
    (1, "1 - Small (pyramidal)"),
    (2, "2 - Medium (columnar)"),
    (3, "3 - Large (bulbous)"),
]

BROOD_PATCH_CHOICES = [
    (0, "0 - None"),
    (1, "1 - Smooth"),
    (2, "2 - Vascularized"),
    (3, "3 - Heavy"),
    (4, "4 - Wrinkled"),
    (5, "5 - Molting in"),
]

FAT_CHOICES = [
    (0, "0 - None"),
    (1, "1 - Trace (<5%)"),
    (2, "2 - Light (<1/3)"),
    (3, "3 - Moderate (half)"),
    (4, "4 - Filled (full)"),
    (5, "5 - Bulging"),
    (6, "6 - Fat under wings & on abdomen"),
    (7, "7 - Excessive (Over almost all ventral surfaces)"),
]

BODY_MOLT_CHOICES = [
    (0, "0 - None"),
    (1, "1 - Trace"),
    (2, "2 - Light"),
    (3, "3 - Medium"),
    (4, "4 - Heavy"),
]

FLIGHT_FEATHER_MOLT_CHOICES = [
    ("N", "N - None"),
    ("A", "A - Adventitious"),
    ("S", "S - Symmetric"),
    ("J", "J - Juvenile"),
]

FLIGHT_FEATHER_WEAR_CHOICES = [
    (0, "0 - None (pale halo)"),
    (1, "1 - Slight"),
    (2, "2 - Light (little fraying & vey nicks)"),
    (3, "3 - Moderate (some fraying & chipping)"),
    (4, "4 - Heavy (worn & frayed, tips worn off)"),
    (5, "5 - Excessive (ragged, torn, broken rachis)"),
]

JUVENILE_BODY_PLUMAGE_CHOICES = [
    (3, "3 - All body feather juv, FCJ."),
    (2, "2 - Greater than 1/2 juv body plumage remains, start FPF."),
    (1, "1 - Less than 1/2 juv body plamage remains, FPF."),
    (0, "0 - HY bird with no juv body plumage, FCF"),
]

MOLT_LIMIT_PLUMAGE_CHOICES = [
    ("J", "J - Juvenile (OR Juv & Alternate)"),
    ("L", "L - Limit of Juv & Formative"),
    ("F", "F - Formative (OR Formative & Alternate)"),
    ("B", "B - Basic (OR Basic & Alternate)"),
    ("R", "R - Retained (Juv & Basic)"),
    ("M", "M - Mixed Basic (woodpecker generally)"),
    ("A", "A - Alternate (some or all)"),
    ("N", "N - Non-juv (definitely no juv feathers, but Formative or Basic)"),
    ("U", "U - Unknown"),
]

STATION_CHOICES = [
    ("MORS", "MORS - Morse Preserve MAPS"),
    ("GHPR", "Glacial Heritage Preserve MAPS"),
]

BAND_SIZE_CHOICES = [
    ("0A", "0A"),
    ("0", "0"),
    ("1", "1"),
    ("1A", "1A"),
    ("1B", "1B"),
    ("1D", "1D"),
    ("2", "2"),
    ("3", "3"),
    ("3A", "3A"),
    ("3B", "3B"),
    ("4", "4"),
    ("R", "Recap"),
]

DISPOSITION_CHOICES = [
    ("B", "B - Body Injury"),
    ("D", "Death (not from predation)"),
    ("E", "E - Eye Injury"),
    ("F", "F - Fouled feathers"),
    ("I", "I - Ill or diseased"),
    ("L", "L - Leg Injury"),
    ("M", "M - Malformed (i.e. crossed bill)"),
    ("O", "O - Old healed injury"),
    ("P", "P - Predation"),
    ("B", "B - Band removed"),
    ("S", "S - Stress or shock"),
    ("T", "T - Tongue injury"),
    ("W", "W - Wing injury"),
]

STATUS_CHOICES = [
    (300, "300 - Normal, banded, released"),
    (301, "301 - Color banded"),
    (500, "500 - injured, see Disposition"),
    (000, "000 - Unbanded OR Died prior to release"),
]
