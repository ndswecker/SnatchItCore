# banding_data_fields.py

CAPTURE_CODES = [
    ('N', '(N) New Bird'),
    ('R', '(R) Recaptured Bird'),
    ('L', '(L) Lost Band'),
    ('D', '(D) Destroyed Band'),
    ('U', '(U) Unbanded Bird'),
    ('C', '(C) Changed band'),
    ('A', '(A) Added Band'),
]

SPECIES_NAMES = [
    ('AMCR', 'AMCR American Crow'),
    ('BRCR', 'BRCR Brown Creeper'),
    ('BCCH', 'BCCH Black-capped Chickadee'),
    ('BUSH', 'BUSH Bushtit'),
    ('CBCH', 'CBCH Chestnut-backed Chickadee'),
    ('ANHU', 'ANHU Anna\'s Hummingbird'),
    ('BEWR', 'BEWR Bewick\'s Wren'),
    ('SWTH', 'SWTH Swainson\'s Thrush'),
    ('WETA', 'WETA Western Tanager'),
    ('WIFL', 'WIFL Willow Flycatcher'),
    ('HUVI', 'Hutton\'s Vireo'),
]
AGE_ANNUAL = [
    ('4', '4 - Local (incapable of sustained flight)'),
    ('2', '2 - Hatch Year (HY)'),
    ('1', '1 - After Hatch Year (AHY)'),
    ('5', '5 - Second Year (SY)'),
    ('6', '6 - After Second Year (ASY)'),
    ('7', '7 - Third Year (TY)'),
    ('8', '8 - After Third Year (ATY)'),
    ('0', '0 - Inderterminable Age'),
    ('9', '9 - Not attempted')
]

AGE_WRP = [
    ('FPJ', '(FPJ) First prejuvenile molt'),
    ('FCJ', '(FCJ) First cycle juvenile plumage'),
    ('FPF', '(FPF) First preformative molt'),
    ('FCF', '(FCF) First cycle formative plumage'),
    ('HFCF', '(HFCF) Hatch year, first cycle formative plumage'),
    ('AFCF', '(AFCF) After hatch year, first cycle formative plumage'),
    ('MFCF', '(MFCF) Minimum first cycle formative'),
    ('FPA', '(FPA) First prealternate molt'),
    ('FCA', '(FCA) First cycle alternate plumage'),
    ('MFCA', '(MFCA) Minimum first cycle alternate'),
    ('SPB', '(SPB) Second prebasic molt'),
    ('MSPB', '(MSPB) Minimum second prebasic molt'),
    ('DCB', '(DCB) Definitive cycle basic plumage'),
    ('DPA', '(DPA) Definitive prealternate molt'),
    ('DCA', '(DCA) Definitive cycle alternate plumage'),
    ('DPB', '(DPB) Definitive prebasic molt'),
    ('FCU', '(FCU) First cycle unknown plumage'),
    ('DCU', '(DCU) Definitive cycle unknown plumage'),
    ('UCU', '(UCU) Unknown cycle unknown plumage'),
]


HOW_AGED_SEXED = [
    ('S', 'S - Skull'),
    ('C', 'C - Cloacal Protuberance'),
    ('B', 'B - Brood Patch'),
    ('F', 'F - Feather Wear'),
    ('J', 'J - Juvenile Body Plumage'),
    ('M', 'M - Molt'),
    ('P', 'P - Plumage (non-juvenile)'),
    ('N', 'N - Non-feather'),
    ('W', 'W - Wing chord'),
    ('L', 'L - Molt Limit'),
    ('I', 'I - Mouth/Bill'),
    ('E', 'E - Eye color'),
    ('W', 'W - Wing length'),
    ('T', 'T - Tail length'),
    ('O', 'O - Other (specify in notes)'),
]

SEX = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('U', 'Unknown'),
]

SKULL = [
    (0, '0 - None'),
    (1, '1 - Trace'),
    (2, '2 - < 1/3'),
    (3, '3 - Half'),
    (4, '4 - > 2/3'),
    (5, '5 - Almost Complete'),
    (6, '6 - Fully Complete'),
    (8, '8 - Unable to Determine'),
]
