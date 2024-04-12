import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CaptureRecord",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        db_index=True, default=uuid.uuid4, editable=False, unique=True
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("scribe_initials", models.CharField(max_length=3)),
                (
                    "capture_code",
                    models.CharField(
                        choices=[
                            ("N", "(N) New Bird"),
                            ("R", "(R) Recaptured Bird"),
                            ("L", "(L) Lost Band"),
                            ("D", "(D) Destroyed Band (and or dead)"),
                            ("U", "(U) Unbanded Bird"),
                            ("C", "(C) Changed band"),
                            ("A", "(A) Added Band"),
                        ],
                        default="N",
                        max_length=1,
                    ),
                ),
                (
                    "species_number",
                    models.IntegerField(
                        choices=[
                            (3120, "BTPI - Band-tailed Pigeon"),
                            (3159, "ECDO - Eurasian Collared-Dove"),
                            (3160, "MODO - Mourning Dove"),
                            (3250, "TUVU - Turkey Vulture"),
                            (3320, "SSHA - Sharp-shinned Hawk"),
                            (3330, "COHA - Cooper's Hawk"),
                            (3370, "RTHA - Red-tail Hawk"),
                            (3520, "BAEA - Bald Eagle"),
                            (3600, "AMKE - American Kestrel"),
                            (3640, "OSPR - Osprey"),
                            (3650, "BANO - Barn Owl"),
                            (3750, "GHOW - Great Horned Owl"),
                            (3790, "NOPO - Northern Pygmy-Owl"),
                            (3900, "BEKI - Belted Kingfisher"),
                            (3930, "HAWO - Hairy Woodpecker"),
                            (3940, "DOWO - Downy Woodpecker"),
                            (4030, "RBSA - Red-breasted Sapsucker"),
                            (4050, "PIWO - Pileated Woodpecker"),
                            (4130, "RSFL - Red-shafted Flicker"),
                            (4200, "CONI - Common Nighthawk"),
                            (4240, "VASW - Vaux's Swift"),
                            (4310, "ANHU - Anna's Hummingbird"),
                            (4330, "RUHU - Rufous Hummingbird"),
                            (4590, "OSFL - Olive-sided Flycatcher"),
                            (4620, "WEWP - Western Wood-Pewee"),
                            (4649, "WEFL - Western Flycatcher"),
                            (4660, "WIFL - Willow Flycatcher"),
                            (4680, "HAFL - Hammond's Flycatcher"),
                            (4780, "STJA - Steller's Jay"),
                            (4813, "CASJ - California Scrub-Jay"),
                            (4860, "CORA - Common Raven"),
                            (4880, "AMCR - American Crow"),
                            (4930, "EUST - European Starling"),
                            (4950, "BHCO - Brown-headed Cowbird"),
                            (4980, "RWBL - Red-winged Blackbird"),
                            (5080, "BUOR - Bullock's Oriole"),
                            (5100, "BRBL - Brewer's Blackbird"),
                            (5140, "EVGR - Evening Grosbeak"),
                            (5170, "PUFI - Purple Finch"),
                            (5190, "HOFI - House Finch"),
                            (5210, "RECR - Red Crossbill"),
                            (5290, "AMGO - American Goldfinch"),
                            (5330, "PISI - Pine Siskin"),
                            (5420, "SAVS - Savannah Sparrow"),
                            (5540, "WCSP - White-crowned Sparrow"),
                            (5547, "PSWS - Puget Sound White-crowned Sparrow"),
                            (5550, "GWCS - Gambel's White-crowned Sparrow"),
                            (5570, "GCSP - Golden-crowned Sparrow"),
                            (5600, "CHSP - Chipping Sparrow"),
                            (5671, "ORJU - Oregon Junco"),
                            (5810, "SOSP - Song Sparrow"),
                            (5830, "LISP - Lincoln's Sparrow"),
                            (5850, "FOSP - Fox Sparrow"),
                            (5880, "SPTO - Spotted Towhee"),
                            (5960, "BHGR - Black-headed Grosbeak"),
                            (5990, "LAZB - Lazuli Bunting"),
                            (6070, "WETA - Western Tanager"),
                            (6110, "PUMA - Purple Martin"),
                            (6120, "CLSW - Cliff Swallow"),
                            (6130, "BARS - Barn Swallow"),
                            (6140, "TRES - Tree Swallow"),
                            (6150, "VGSW - Violet-green Swallow"),
                            (6170, "NRWS - Northern Rough-winged Swallow"),
                            (6190, "CEDW - Cedar Waxwing"),
                            (6240, "REVI - Red-eyed Vireo"),
                            (6270, "WAVI - Warbling Vireo"),
                            (6292, "CAVI - Cassin's Vireo"),
                            (6320, "HUVI - Hutton's Vireo"),
                            (6450, "NAWA - Nashville Warbler"),
                            (6460, "OCWA - Orange-crowned Warbler"),
                            (6520, "YEWA - Yellow Warbler"),
                            (6550, "MYWA - Myrtle Warbler"),
                            (6556, "MYWA - Yellow-rumped Warbler"),
                            (6560, "AUWA - Audubon's Warbler"),
                            (6650, "BTYW - Black-throated Gray Warbler"),
                            (6800, "MGWA - MacGillivray's Warbler"),
                            (6810, "COYE - Common Yellowthroat"),
                            (6850, "WIWA - Wilson's Warbler"),
                            (7190, "BEWR - Bewick's Wren"),
                            (7210, "HOWR - House Wren"),
                            (7221, "PAWR - Pacific Wren"),
                            (7250, "MAWR - Marsh Wren"),
                            (7260, "BRCR - Brown Creeper"),
                            (7280, "RBNU - Red-breasted Nuthatch"),
                            (7350, "BCCH - Black-capped Chickadee"),
                            (7410, "CBCH - Chestnut-backed Chickadee"),
                            (7430, "BUSH - Bushtit"),
                            (7480, "GCKI - Golden-crowned Kinglet"),
                            (7490, "RCKI - Ruby-crowned Kinglet"),
                            (7580, "SWTH - Swainson's Thrush"),
                            (7590, "HETH - Hermit Thrush"),
                            (7610, "AMRO - American Robin"),
                            (7630, "VATH - Varied Thrush"),
                            (7670, "WEBL - Western Bluebird"),
                        ],
                        default=5810,
                    ),
                ),
                (
                    "band_size",
                    models.CharField(
                        choices=[
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
                            ("U", "Unbanded"),
                        ],
                        default="1B",
                        max_length=2,
                    ),
                ),
                (
                    "band_number",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(
                                100000000,
                                message="Band number must be at least 9 digits long.",
                            ),
                            django.core.validators.MaxValueValidator(
                                999999999,
                                message="Band number must be less than 10 digits.",
                            ),
                        ],
                    ),
                ),
                ("alpha_code", models.CharField(max_length=4)),
                (
                    "age_annual",
                    models.IntegerField(
                        choices=[
                            (4, "4 - Local (incapable of sustained flight)"),
                            (2, "2 - Hatch Year (HY)"),
                            (1, "1 - After Hatch Year (AHY)"),
                            (5, "5 - Second Year (SY)"),
                            (6, "6 - After Second Year (ASY)"),
                            (7, "7 - Third Year (TY)"),
                            (8, "8 - After Third Year (ATY)"),
                            (0, "0 - Inderterminable Age"),
                            (9, "9 - Not attempted"),
                        ],
                        default=1,
                    ),
                ),
                (
                    "how_aged_1",
                    models.CharField(
                        blank=True,
                        choices=[
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
                        ],
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "how_aged_2",
                    models.CharField(
                        blank=True,
                        choices=[
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
                        ],
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "age_WRP",
                    models.CharField(
                        choices=[
                            ("FPJ", "(FPJ) First prejuvenile molt"),
                            ("FCJ", "(FCJ) First cycle juvenile plumage"),
                            ("FPF", "(FPF) First preformative molt"),
                            ("FCF", "(FCF) First cycle formative plumage"),
                            ("MFCF", "(M-FCF) Minimum first cycle formative"),
                            ("FPA", "(FPA) First prealternate molt"),
                            ("MFPA", "(M-FPA) Minimum first cycle prealternate"),
                            ("FCA", "(FCA) First cycle alternate plumage"),
                            ("MFCA", "(M-FCA) Minimum first cycle alternate"),
                            ("SPB", "(SPB) Second prebasic molt"),
                            ("MSPB", "(M-SPB) Minimum second prebasic molt"),
                            ("SCB", "(SCB) Second cycle basic plumage"),
                            ("DPB", "(DPB) Definitive prebasic molt"),
                            ("DCB", "(DCB) Definitive cycle basic plumage"),
                            ("DPA", "(DPA) Definitive prealternate molt"),
                            ("DCA", "(DCA) Definitive cycle alternate plumage"),
                            ("TPB", "(TPB) Third prebasic molt"),
                            ("FCU", "(FCU) First cycle unknown plumage"),
                            ("DCU", "(DCU) Definitive cycle unknown plumage"),
                            ("UCU", "(UCU) Unknown cycle unknown plumage"),
                        ],
                        default="MFCF",
                        max_length=4,
                    ),
                ),
                (
                    "sex",
                    models.CharField(
                        choices=[
                            ("M", "Male"),
                            ("F", "Female"),
                            ("U", "Unknown"),
                            ("X", "Not Attempted"),
                        ],
                        default="U",
                        max_length=1,
                    ),
                ),
                (
                    "how_sexed_1",
                    models.CharField(
                        blank=True,
                        choices=[
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
                        ],
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "how_sexed_2",
                    models.CharField(
                        blank=True,
                        choices=[
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
                        ],
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "cloacal_direction",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("M", "Male"),
                            ("F", "Female"),
                            ("U", "Unknown"),
                            ("X", "Not Attempted"),
                        ],
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "skull",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (0, "0 - None"),
                            (1, "1 - Trace"),
                            (2, "2 - < 1/3"),
                            (3, "3 - Half"),
                            (4, "4 - > 2/3"),
                            (5, "5 - Almost Complete"),
                            (6, "6 - Fully Complete"),
                            (8, "8 - Unable to Determine"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "cloacal_protuberance",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (0, "0 - None"),
                            (1, "1 - Small (pyramidal)"),
                            (2, "2 - Medium (columnar)"),
                            (3, "3 - Large (bulbous)"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "brood_patch",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (0, "0 - None"),
                            (1, "1 - Smooth"),
                            (2, "2 - Vascularized"),
                            (3, "3 - Heavy"),
                            (4, "4 - Wrinkled"),
                            (5, "5 - Molting in"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "fat",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (0, "0 - None"),
                            (1, "1 - Trace (<5%)"),
                            (2, "2 - Light (<1/3)"),
                            (3, "3 - Moderate (half)"),
                            (4, "4 - Filled (full)"),
                            (5, "5 - Bulging"),
                            (6, "6 - Fat under wings & on abdomen"),
                            (7, "7 - Excessive (Over almost all ventral surfaces)"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "body_molt",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (0, "0 - None"),
                            (1, "1 - Trace"),
                            (2, "2 - Light"),
                            (3, "3 - Medium"),
                            (4, "4 - Heavy"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "ff_molt",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("N", "N - None"),
                            ("A", "A - Adventitious"),
                            ("S", "S - Symmetric"),
                            ("J", "J - Juvenile"),
                        ],
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "ff_wear",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (0, "0 - None (pale halo)"),
                            (1, "1 - Slight"),
                            (2, "2 - Light (little fraying & vey nicks)"),
                            (3, "3 - Moderate (some fraying & chipping)"),
                            (4, "4 - Heavy (worn & frayed, tips worn off)"),
                            (5, "5 - Excessive (ragged, torn, broken rachis)"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "juv_body_plumage",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (3, "3 - All body feather juv, FCJ."),
                            (
                                2,
                                "2 - Greater than 1/2 juv body plumage remains, start FPF.",
                            ),
                            (1, "1 - Less than 1/2 juv body plamage remains, FPF."),
                            (0, "0 - HY bird with no juv body plumage, FCF"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "primary_coverts",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("J", "J - Juvenile (OR Juv & Alternate)"),
                            ("L", "L - Limit of Juv & Formative"),
                            ("F", "F - Formative (OR Formative & Alternate)"),
                            ("B", "B - Basic (OR Basic & Alternate)"),
                            ("R", "R - Retained (Juv & Basic)"),
                            ("M", "M - Mixed Basic (woodpecker generally)"),
                            ("A", "A - Alternate (some or all)"),
                            (
                                "N",
                                "N - Non-juv (definitely no juv feathers, but Formative or Basic)",
                            ),
                            ("U", "U - Unknown"),
                        ],
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "secondary_coverts",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("J", "J - Juvenile (OR Juv & Alternate)"),
                            ("L", "L - Limit of Juv & Formative"),
                            ("F", "F - Formative (OR Formative & Alternate)"),
                            ("B", "B - Basic (OR Basic & Alternate)"),
                            ("R", "R - Retained (Juv & Basic)"),
                            ("M", "M - Mixed Basic (woodpecker generally)"),
                            ("A", "A - Alternate (some or all)"),
                            (
                                "N",
                                "N - Non-juv (definitely no juv feathers, but Formative or Basic)",
                            ),
                            ("U", "U - Unknown"),
                        ],
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "primaries",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("J", "J - Juvenile (OR Juv & Alternate)"),
                            ("L", "L - Limit of Juv & Formative"),
                            ("F", "F - Formative (OR Formative & Alternate)"),
                            ("B", "B - Basic (OR Basic & Alternate)"),
                            ("R", "R - Retained (Juv & Basic)"),
                            ("M", "M - Mixed Basic (woodpecker generally)"),
                            ("A", "A - Alternate (some or all)"),
                            (
                                "N",
                                "N - Non-juv (definitely no juv feathers, but Formative or Basic)",
                            ),
                            ("U", "U - Unknown"),
                        ],
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "secondaries",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("J", "J - Juvenile (OR Juv & Alternate)"),
                            ("L", "L - Limit of Juv & Formative"),
                            ("F", "F - Formative (OR Formative & Alternate)"),
                            ("B", "B - Basic (OR Basic & Alternate)"),
                            ("R", "R - Retained (Juv & Basic)"),
                            ("M", "M - Mixed Basic (woodpecker generally)"),
                            ("A", "A - Alternate (some or all)"),
                            (
                                "N",
                                "N - Non-juv (definitely no juv feathers, but Formative or Basic)",
                            ),
                            ("U", "U - Unknown"),
                        ],
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "tertials",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("J", "J - Juvenile (OR Juv & Alternate)"),
                            ("L", "L - Limit of Juv & Formative"),
                            ("F", "F - Formative (OR Formative & Alternate)"),
                            ("B", "B - Basic (OR Basic & Alternate)"),
                            ("R", "R - Retained (Juv & Basic)"),
                            ("M", "M - Mixed Basic (woodpecker generally)"),
                            ("A", "A - Alternate (some or all)"),
                            (
                                "N",
                                "N - Non-juv (definitely no juv feathers, but Formative or Basic)",
                            ),
                            ("U", "U - Unknown"),
                        ],
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "rectrices",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("J", "J - Juvenile (OR Juv & Alternate)"),
                            ("L", "L - Limit of Juv & Formative"),
                            ("F", "F - Formative (OR Formative & Alternate)"),
                            ("B", "B - Basic (OR Basic & Alternate)"),
                            ("R", "R - Retained (Juv & Basic)"),
                            ("M", "M - Mixed Basic (woodpecker generally)"),
                            ("A", "A - Alternate (some or all)"),
                            (
                                "N",
                                "N - Non-juv (definitely no juv feathers, but Formative or Basic)",
                            ),
                            ("U", "U - Unknown"),
                        ],
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "body_plumage",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("J", "J - Juvenile (OR Juv & Alternate)"),
                            ("L", "L - Limit of Juv & Formative"),
                            ("F", "F - Formative (OR Formative & Alternate)"),
                            ("B", "B - Basic (OR Basic & Alternate)"),
                            ("R", "R - Retained (Juv & Basic)"),
                            ("M", "M - Mixed Basic (woodpecker generally)"),
                            ("A", "A - Alternate (some or all)"),
                            (
                                "N",
                                "N - Non-juv (definitely no juv feathers, but Formative or Basic)",
                            ),
                            ("U", "U - Unknown"),
                        ],
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "alula",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("J", "J - Juvenile (OR Juv & Alternate)"),
                            ("L", "L - Limit of Juv & Formative"),
                            ("F", "F - Formative (OR Formative & Alternate)"),
                            ("B", "B - Basic (OR Basic & Alternate)"),
                            ("R", "R - Retained (Juv & Basic)"),
                            ("M", "M - Mixed Basic (woodpecker generally)"),
                            ("A", "A - Alternate (some or all)"),
                            (
                                "N",
                                "N - Non-juv (definitely no juv feathers, but Formative or Basic)",
                            ),
                            ("U", "U - Unknown"),
                        ],
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "non_feather",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("J", "J - Juvenile (OR Juv & Alternate)"),
                            ("L", "L - Limit of Juv & Formative"),
                            ("F", "F - Formative (OR Formative & Alternate)"),
                            ("B", "B - Basic (OR Basic & Alternate)"),
                            ("R", "R - Retained (Juv & Basic)"),
                            ("M", "M - Mixed Basic (woodpecker generally)"),
                            ("A", "A - Alternate (some or all)"),
                            (
                                "N",
                                "N - Non-juv (definitely no juv feathers, but Formative or Basic)",
                            ),
                            ("U", "U - Unknown"),
                        ],
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "wing_chord",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(
                                10, message="Wing chord must be at least 0."
                            ),
                            django.core.validators.MaxValueValidator(
                                300, message="Wing chord must be less than 300."
                            ),
                        ],
                    ),
                ),
                (
                    "body_mass",
                    models.DecimalField(
                        blank=True,
                        decimal_places=1,
                        max_digits=4,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(
                                0, message="Mass must be at least 0."
                            ),
                            django.core.validators.MaxValueValidator(
                                999.9, message="Mass must be less than 10000."
                            ),
                        ],
                    ),
                ),
                (
                    "status",
                    models.IntegerField(
                        choices=[
                            (300, "300 - Normal, banded, released"),
                            (301, "301 - Color banded"),
                            (500, "500 - injured, see Disposition"),
                            (0, "000 - Unbanded OR Died prior to release"),
                        ],
                        default=300,
                        validators=[
                            django.core.validators.MinValueValidator(
                                0, message="Status must be at least 000."
                            ),
                            django.core.validators.MaxValueValidator(
                                999, message="Status must be less than 1000."
                            ),
                        ],
                    ),
                ),
                (
                    "capture_time",
                    models.DateTimeField(
                        blank=True, default=django.utils.timezone.now, null=True
                    ),
                ),
                (
                    "hold_time",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        help_text="Minutes held in hand.",
                        max_digits=5,
                        null=True,
                    ),
                ),
                (
                    "station",
                    models.CharField(
                        choices=[
                            ("MORS", "MORS - Morse Preserve MAPS"),
                            ("GHPR", "Glacial Heritage Preserve MAPS"),
                        ],
                        default="MORS",
                        max_length=4,
                    ),
                ),
                ("net", models.IntegerField()),
                (
                    "disposition",
                    models.CharField(
                        blank=True,
                        choices=[
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
                        ],
                        max_length=1,
                        null=True,
                    ),
                ),
                ("note_number", models.CharField(blank=True, max_length=2, null=True)),
                ("note", models.TextField(blank=True, null=True)),
                ("bander_initials", models.CharField(max_length=3)),
                ("discrepancies", models.TextField(blank=True, null=True)),
                (
                    "is_validated",
                    models.BooleanField(
                        default=True, help_text="Apply validations to this record"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
