from maps.maps_reference_data import *  # noqa F403
from maps.models import CaptureRecord


class USGSSerializer:
    def __init__(self, capture_record: CaptureRecord):
        self.capture_record = capture_record

    def get_species(self):
        return SPECIES[self.capture_record.species_number]["alpha_code"]

    def get_condition_code(self):
        return DISPOSTIONS[self.capture_record.capture_code]["usgs"]["code"]

    def get_month(self):
        # format the month to always be 2 digits
        return f"{self.capture_record.capture_time.month:02d}"

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
        return STATION_LOCATIONS[self.capture_record.station]["BBL_location_id"]

    def get_notes(self):
        return self.capture_record.note or ""

    def get_capture_method(self):
        return "Mist net"

    def get_capture_time(self):
        return self.capture_record.capture_time.strftime("%H:%M")

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
            "Banding Year": self.capture_record.capture_time.year,
            "Banding Month": self.get_month(),
            "Banding Day": self.capture_record.capture_time.day,
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


class IBPSerializer:
    def __init__(self, capture_record: CaptureRecord):
        self.capture_record = capture_record

    def get_location(self):
        # Need to ensure that we have the correct location codes
        return self.capture_record.station

    def get_band_size(self):
        return self.capture_record.band_size

    def get_page_number(self):
        # TODO: Implement page number? not sure
        return 1

    def get_bander_initials(self):
        return self.capture_record.bander_initials

    def get_capture_code(self):
        return self.capture_record.capture_code

    def get_band_number(self):
        return self.capture_record.band_number

    def get_speices(self):
        return SPECIES[self.capture_record.species_number]["alpha_code"]

    def get_age_annual(self):
        return self.capture_record.age_annual

    # Handle concatenation of how aged with strings and possible null values
    def get_how_aged(self):
        aged_1 = self.capture_record.how_aged_1 if self.capture_record.how_aged_1 else ""
        aged_2 = self.capture_record.how_aged_2 if self.capture_record.how_aged_2 else ""
        return aged_1 + aged_2

    def get_WRP(self):
        return self.capture_record.age_WRP

    def get_sex(self):
        return self.capture_record.sex

    # Handle concatenation of how aged with strings and possible null values
    def get_how_sexed(self):
        sexed_1 = self.capture_record.how_sexed_1 if self.capture_record.how_sexed_1 else ""
        sexed_2 = self.capture_record.how_sexed_2 if self.capture_record.how_sexed_2 else ""
        return sexed_1 + sexed_2

    def get_cloacal_direction(self):
        direction = self.capture_record.cloacal_direction
        return "Cloacal Direction: " + direction if direction else ""

    def get_skull(self):
        return self.capture_record.skull

    def get_cloacal_protuberance(self):
        return self.capture_record.cloacal_protuberance

    def get_brood_patch(self):
        return self.capture_record.brood_patch

    def get_fat(self):
        return self.capture_record.fat

    def get_body_molt(self):
        return self.capture_record.body_molt

    def get_ff_molt(self):
        return self.capture_record.ff_molt

    def get_ff_wear(self):
        return self.capture_record.ff_wear

    def get_juvenile_body_plumage(self):
        return self.capture_record.juv_body_plumage

    def get_primary_coverts(self):
        return self.capture_record.primary_coverts

    def get_secondary_coverts(self):
        return self.capture_record.secondary_coverts

    def get_primaries(self):
        return self.capture_record.primaries

    def get_secondaries(self):
        return self.capture_record.secondaries

    def get_tertials(self):
        return self.capture_record.tertials

    def get_rectrices(self):
        return self.capture_record.rectrices

    def get_alula(self):
        alula = self.capture_record.alula
        return "Alula: " + alula if alula else ""

    def get_body_plumage(self):
        return self.capture_record.body_plumage

    def get_non_feather(self):
        return self.capture_record.non_feather

    def get_wing_chord(self):
        return self.capture_record.wing_chord

    def get_body_mass(self):
        return self.capture_record.body_mass

    def get_status(self):
        return self.capture_record.status

    def get_date(self):
        return self.capture_record.capture_time.strftime("%m/%d/%Y")

    def get_time(self):
        return self.capture_record.capture_time.strftime("%H%M")

    def get_station(self):
        return self.capture_record.station

    def get_net(self):
        return self.capture_record.net

    def get_disposition(self):
        return self.capture_record.disposition

    def get_note_number(self):
        return self.capture_record.note_number

    def get_feather_pull(self):
        return ""

    def get_notes(self):
        alula = self.get_alula()
        cloacal_direction = self.get_cloacal_direction()
        notes = self.capture_record.note if self.capture_record.note else ""
        if alula:
            notes += ". " + alula if notes else alula
        if cloacal_direction:
            notes += ". " + cloacal_direction if notes else cloacal_direction

        return notes

    def serialize(self) -> dict:
        return {
            "LOC": self.get_location(),
            "BS": self.get_band_size(),
            "PG": self.get_page_number(),
            "BI": self.get_bander_initials(),
            "CODE": self.get_capture_code(),
            "BAND#": self.get_band_number(),
            "SPEC": self.get_speices(),
            "AGE": self.get_age_annual(),
            "HA": self.get_how_aged(),
            "WRP": self.get_WRP(),
            "SEX": self.get_sex(),
            "HS": self.get_how_sexed(),
            "SK": self.get_skull(),
            "CP": self.get_cloacal_protuberance(),
            "BP": self.get_brood_patch(),
            "FAT": self.get_fat(),
            "BMOLT": self.get_body_molt(),
            "FFMOLT": self.get_ff_molt(),
            "FFWEAR": self.get_ff_wear(),
            "J BDY PL": self.get_juvenile_body_plumage(),
            "PPC": self.get_primary_coverts(),
            "SSC": self.get_secondary_coverts(),
            "PPF": self.get_primaries(),
            "SSF": self.get_secondaries(),
            "TT": self.get_tertials(),
            "RR": self.get_rectrices(),
            "BPL": self.get_body_plumage(),
            "NF": self.get_non_feather(),
            "WING": self.get_wing_chord(),
            "WEIGHT": self.get_body_mass(),
            "STATUS": self.get_status(),
            "DATE": self.get_date(),
            "TIME": self.get_time(),
            "STATION": self.get_station(),
            "NET": self.get_net(),
            "DISP": self.get_disposition(),
            "NOTE #": self.get_note_number(),
            "FTHR PULL": self.get_feather_pull(),
            "NOTES": self.get_notes(),
        }
