from maps.models import CaptureRecord
from maps.maps_reference_data import *


class USGSSerializer:
    def __init__(self, capture_record: CaptureRecord):
        self.capture_record = capture_record

    def get_species(self):
        return SPECIES[self.capture_record.species_number]["alpha_code"]

    def get_condition_code(self):
        return DISPOSTIONS[self.capture_record.capture_code]["usgs"]["code"]

    def get_how_aged(self):
        if not self.capture_record.how_aged_1:
            return ""
        return HOW_AGE_DETERMINED[self.capture_record.how_aged_1]["usgs"]["code"]

    def get_usgs_how_sexed_code(self):
        if not self.capture_record.how_sexed_1:
            return ""
        return HOW_AGE_DETERMINED[self.capture_record.how_sexed_1]["usgs"]["code"]

    def get_sex(self):
        return self.capture_record.sex

    def get_bbl_location_id(self):
        return SITE_LOCATIONS[self.capture_record.station]["BBL_location_id"]

    def get_notes(self):
        return self.capture_record.note or ""

    def get_capture_method(self):
        return "Mist net"

    def get_capture_time(self):
        return self.capture_record.date_time.strftime("%H:%M")

    def get_banded_leg(self):
        return "L"

    def get_fat_score(self):
        return self.capture_record.fat or ""

    def get_skull_score(self):
        return self.capture_record.skull or ""

    def get_body_molt(self):
        return self.capture_record.body_molt or ""

    def get_ff_molt(self):
        return self.capture_record.ff_molt or ""

    def serialize(self) -> dict:
        """Serialize a CaptureRecord to a dict"""
        return {
            "Band Number": self.capture_record.band_number,
            "Species": self.get_species(),
            "Disposition": self.get_condition_code(),
            "Banding Year": self.capture_record.date_time.year,
            "Banding Month": self.capture_record.date_time.month,
            "Banding Day": self.capture_record.date_time.day,
            "Age": self.capture_record.age_annual,
            "How Aged": self.get_how_aged(),
            "Sex": self.get_sex(),
            "How Sexed": self.get_usgs_how_sexed_code(),
            "Bird Status": self.capture_record.status,
            "Location": self.get_bbl_location_id(),
            "Remarks": self.get_notes(),
            "Replaced Band Number": None,
            "Reward Band Number": None,
            "Bander ID": self.capture_record.bander_initials,
            "Scribe": self.capture_record.scribe,
            "How Captured": self.get_capture_method(),
            "Capture Time Enter or Paste Here": None,
            "Capture Time": self.get_capture_time(),
            "Banded Leg": self.get_banded_leg(),
            "Wing Chord": self.capture_record.wing_chord,
            "Tail Length": None,
            "Tarsus Length": None,
            "Culmen Length": None,
            "Bill Length": None,
            "Bill Width": None,
            "Bill Height": None,
            "Bird Weight": self.capture_record.body_mass,
            "Weight Time Enter or Paste Here": None,
            "Weight Time": None,
            "Eye color": None,
            "Fat Score": self.get_fat_score(),
            "Skull": self.get_skull_score(),
            "Brood Patch": self.capture_record.brood_patch,
            "Cloacal Protuberance": self.capture_record.cloacal_protuberance,
            "Body Molt": self.get_body_molt(),
            "Flight Feather Molt": self.get_ff_molt(),
            "Molt Cycle Code": self.capture_record.age_WRP,
            "Net Nest Cavity Designator": None,
            "Net Nest Cavity Number": None,
            "Plot ID": None,
            "Sweep Number": None,
            "Nest Location": None,
            "Blood sample taken": None,
            "Feather sample taken": None,
            "Genetic sample taken": None,
            "Other tests performed": None,
            "Tracheal Swab": None,
            "Mouth Swab": None,
            "Cloacal Swab": None,
            "Ectoparasites present": None,
            "Ectoparasites collected": None,
            "User Field 1": None,
            "User Field 2": None,
            "User Field 3": None,
            "User Field 4": None,
            "User Field 5": None,
        }
