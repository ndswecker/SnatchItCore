import datetime

from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models

from common.models import BaseModel
from maps.banding_data_fields import *
from maps.birds_info import REFERENCE_GUIDE
from maps.validators import MapsValidator


def rounded_down_datetime():
    now = datetime.datetime.now()
    rounding_down = (now.minute // 10) * 10
    rounded_minute = now.replace(minute=rounding_down, second=0, microsecond=0)
    return rounded_minute


class CaptureRecord(BaseModel):
    def __init__(self):
        super().__init__(self)
        self.validator = MapsValidator(self)

    bander_initials = models.CharField(
        max_length=3,
        default="JSM",
    )

    capture_code = models.CharField(
        max_length=1,
        choices=CAPTURE_CODE_OPTIONS,
        default="N",
    )

    band_number = models.IntegerField(
        validators=[
            MinValueValidator(100000000, message="Band number must be at least 9 digits long."),
            MaxValueValidator(999999999, message="Band number must be less than 10 digits."),
        ],
        default=123456789,
    )

    species_number = models.IntegerField(
        validators=[
            MinValueValidator(1000, message="Species number must be at least 4 digits long."),
            MaxValueValidator(9999, message="Species number must be less than 5 digits."),
        ],
        choices=SPECIES_OPTIONS,
        default=5810,
    )

    alpha_code = models.CharField(max_length=4)

    age_annual = models.CharField(
        max_length=1,
        choices=AGE_ANNUAL_OPTIONS,
        default="1",
    )

    how_aged_1 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        choices=HOW_AGED_SEXED_OPTIONS,
    )

    how_aged_2 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        choices=HOW_AGED_SEXED_OPTIONS,
    )

    age_WRP = models.CharField(
        max_length=4,
        choices=AGE_WRP_OPTIONS,
        default="MFCF",
    )

    sex = models.CharField(
        max_length=1,
        choices=SEX_OPTIONS,
        default="U",
    )
    how_sexed_1 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        choices=HOW_AGED_SEXED_OPTIONS,
    )
    how_sexed_2 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        choices=HOW_AGED_SEXED_OPTIONS,
    )

    skull = models.IntegerField(
        choices=SKULL_SCORES,
        null=True,
        blank=True,
    )

    cloacal_protuberance = models.IntegerField(
        choices=CLOACAL_PROTUBERANCE_SCORES,
        null=True,
        blank=True,
    )

    brood_patch = models.IntegerField(
        choices=BROOD_PATCH_SCORES,
        null=True,
        blank=True,
    )

    fat = models.IntegerField(
        choices=FAT_SCORES,
        null=True,
        blank=True,
    )

    body_molt = models.IntegerField(
        choices=BODY_MOLT_OPTIONS,
        null=True,
        blank=True,
    )

    ff_molt = models.CharField(
        max_length=1,
        choices=FLIGHT_FEATHER_MOLT_OPTIONS,
        null=True,
        blank=True,
    )

    ff_wear = models.IntegerField(
        choices=FLIGHT_FEATHER_WEAR_SCORES,
        null=True,
        blank=True,
    )

    juv_body_plumage = models.IntegerField(
        choices=JUVENILE_BODY_PLUMAGE_OPTIONS,
        null=True,
        blank=True,
    )

    primary_coverts = models.CharField(
        choices=MOLT_LIMIT_PLUMAGE_OPTIONS,
        max_length=1,
        null=True,
        blank=True,
    )

    secondary_coverts = models.CharField(
        choices=MOLT_LIMIT_PLUMAGE_OPTIONS,
        max_length=1,
        null=True,
        blank=True,
    )

    primaries = models.CharField(
        max_length=1,
        choices=MOLT_LIMIT_PLUMAGE_OPTIONS,
        null=True,
        blank=True,
    )

    rectrices = models.CharField(
        max_length=1,
        choices=MOLT_LIMIT_PLUMAGE_OPTIONS,
        null=True,
        blank=True,
    )

    secondaries = models.CharField(
        max_length=1,
        choices=MOLT_LIMIT_PLUMAGE_OPTIONS,
        null=True,
        blank=True,
    )

    tertials = models.CharField(
        max_length=1,
        choices=MOLT_LIMIT_PLUMAGE_OPTIONS,
        null=True,
        blank=True,
    )

    body_plumage = models.CharField(
        max_length=1,
        choices=MOLT_LIMIT_PLUMAGE_OPTIONS,
        null=True,
        blank=True,
    )

    non_feather = models.CharField(
        max_length=1,
        choices=MOLT_LIMIT_PLUMAGE_OPTIONS,
        null=True,
        blank=True,
    )

    wing_chord = models.IntegerField(
        validators=[
            MinValueValidator(10, message="Wing chord must be at least 0."),
            MaxValueValidator(300, message="Wing chord must be less than 300."),
        ],
        null=True,
        blank=True,
    )

    body_mass = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        validators=[
            MinValueValidator(0, message="Mass must be at least 0."),
            MaxValueValidator(999.9, message="Mass must be less than 10000."),
        ],
        null=True,
        blank=True,
    )

    status = models.IntegerField(
        validators=[
            MinValueValidator(0, message="Status must be at least 000."),
            MaxValueValidator(999, message="Status must be less than 1000."),
        ],
        choices=STATUS_OPTIONS,
        default=300,
    )

    date_time = models.DateTimeField(
        default=rounded_down_datetime,
    )

    station = models.CharField(
        max_length=4,
        choices=STATION_OPTIONS,
        default="MORS",
    )

    net = models.CharField(
        max_length=4,
        default="15",
    )

    disposition = models.CharField(
        max_length=1,
        choices=DISPOSITION_OPTIONS,
        null=True,
        blank=True,
    )

    note_number = models.CharField(
        max_length=2,
        null=True,
        blank=True,
    )

    note = models.TextField(
        null=True,
        blank=True,
    )

    band_size = models.CharField(
        max_length=2,
        choices=BAND_SIZE_OPTIONS,
        default="1B",
    )

    scribe = models.CharField(
        max_length=3,
        null=True,
        blank=True,
    )

    location = models.CharField(
        max_length=4,
        choices=STATION_OPTIONS,
        null=True,
        blank=True,
    )

    discrepancies = models.TextField(null=True, blank=True)
    is_flagged_for_review = models.BooleanField(default=False)

    def __str__(self):
        common_name = REFERENCE_GUIDE["species"][self.species_number]["common_name"]
        return f"{common_name} - {self.band_number} - {self.date_time.strftime('%Y-%m-%d %H:%M')}"

    def clean(self):
        super().clean()

        self.validator.validate_initials(self.bander_initials, "bander_initials", mandatory=True)
        self.validator.validate_species_to_wing()
        self.validator.validate_wrp_to_species()
        self.validator.validate_how_sexed_order()
        self.validator.validate_sex_how_sexed()
        self.validator.validate_band_size_to_species()

        if self.scribe:
            self.validator.validate_initials(self.scribe, "scribe", mandatory=False)
    def get_usgs_condition_code(self):
        # Look up the capture_code in the REFERENCE_GUIDE's "dispositions" section
        target_disposition = REFERENCE_GUIDE["dispositions"][self.capture_code]
        
        # Get the "usgs" sub-dictionary
        return target_disposition["usgs"]["code"]
    
    def get_usgs_how_aged_code(self):
        # If how_aged_1 is not set, return a blank string
        if not self.how_aged_1:
            return ""
        
        # Look up the how_aged_1 code in the REFERENCE_GUIDE's "how_aged" section
        target_how_aged = REFERENCE_GUIDE["how_aged"][self.how_aged_1]
        
        # Get the "usgs" sub-dictionary
        return target_how_aged["usgs"]["code"]
    
    def get_usgs_how_sexed_code(self):
        # If how_sexed_1 is not set, return a blank string
        if not self.how_sexed_1:
            return ""
        
        # Look up the how_sexed_1 code in the REFERENCE_GUIDE's "how_sexed" section
        target_how_sexed = REFERENCE_GUIDE["how_aged"][self.how_sexed_1]
        
        # Get the "usgs" sub-dictionary
        return target_how_sexed["usgs"]["code"]
    
    def get_usgs_sex_code(self):
        # Look up the sex code in the REFERENCE_GUIDE's "sex" section
        target_sex = REFERENCE_GUIDE["sex"][self.sex]

        # Get the "usgs" sub-dictionary
        return target_sex["usgs"]["code"]
    
    def get_bbl_location_id(self):
        # Look up the station code in the REFERENCE_GUIDE's "stations" section
        return REFERENCE_GUIDE["site_locations"][self.station]["BBL_location_id"]
    
    def get_notes(self):
        return self.note or ""
    
    def get_capture_method(self):
        # Will support other methods in the future
        return "Mist net"
    
    def get_capture_time(self):
        return self.date_time.strftime("%H:%M")
    
    def get_banded_leg(self):
        # Currently default to left leg for all birds. May support either leg in the future.
        return "L"
        
    def get_fat_score(self):
        # If fat is not set, return a blank string
        return self.fat or ""
    
    def get_skull_score(self):
        # If skull is not set, return a blank string
        return self.skull or ""
    
    def get_body_molt(self):
        # If body_molt is not set, return a blank string
        return self.body_molt or ""
    
    def get_ff_molt(self):
        # If ff_molt is not set, return a blank string
        return self.ff_molt or ""

    def serialize_usgs(self):
        # Your playground
        target_species_alpha = REFERENCE_GUIDE["species"][self.species_number]["alpha_code"]
        return dict(
            band_number=self.band_number,
            species=target_species_alpha,
            dispostion=self.get_usgs_condition_code(),
            year=self.date_time.year,
            month=self.date_time.month,
            day=self.date_time.day,
            age=self.age_annual,
            how_aged=self.get_usgs_how_aged_code(),
            sex=self.get_usgs_sex_code(),
            how_sexed=self.get_usgs_how_sexed_code(),
            status=self.status,
            location=self.get_bbl_location_id(),
            remarks=self.get_notes(),
            replaced_band_number=None,
            reward_band_number=None,
            bander_id=self.bander_initials,
            scribe_id=self.scribe,
            how_capture=self.get_capture_method(),
            capture_time=self.get_capture_time(),
            banded_leg=self.get_banded_leg(),
            wing_chord=self.wing_chord,
            tail_length=None,
            tarsus_length=None,
            culmen_length=None,
            bill_length=None,
            bill_height=None,
            bird_weight=self.body_mass,
            weight_time=None,
            eye_color=None,
            fat_score=self.get_fat_score(),
            skull=self.get_skull_score(),
            brood_patch=self.brood_patch,
            cloacal_protuberance=self.cloacal_protuberance,
            body_molt=self.get_body_molt(),
            ff_molt=self.get_ff_molt(),
            molt_cycle=self.age_WRP,
        )
