import csv
import datetime

from maps.models import CaptureRecord
from maps.maps_reference_data import SPECIES

from django.utils import timezone

class IBPDataImporter:
    def __init__(self, csv_file):
        self.csv_file = csv_file
    
    def parse_csv(self):
        reader = csv.DictReader(self.csv_file.read().decode("utf-8").splitlines())
        for row in reader:
            print(row)
            self.create_capture_record(row)

    # A method to get the species number from the SPECIES dict using the alpha code
    def get_species_number(self, alpha_code):
        for species_number, species_info in SPECIES.items():
            if species_info["alpha_code"] == alpha_code:
                return int(species_number)
        return None
    
    # A method to set how_aged_1 and how_aged_2 from the "HA" column.
    # The "HA" column may contain up to 2 characters. If it contains 2 characters, 
    # the first character should be set to how_aged_1 and the second character should be set to how_aged_2.
    def set_how_aged(self, how_aged):
        how_aged_1, how_aged_2 = None, None
        if len(how_aged) >= 1:
            how_aged_1 = how_aged[0]
        if len(how_aged) == 2:
            how_aged_2 = how_aged[1]
        return how_aged_1, how_aged_2
    
    # A method to set how_sexed_1 and how_sexed_2 from the "HS" column.
    # The "HS" column may contain up to 2 characters. If it contains 2 characters,
    # the first character should be set to how_sexed_1 and the second character should be set to how_sexed_2.
    def set_how_sexed(self, how_sexed):
        how_sexed_1, how_sexed_2 = None, None
        if len(how_sexed) >= 1:
            how_sexed_1 = how_sexed[0]
        if len(how_sexed) == 2:
            how_sexed_2 = how_sexed[1]
        return how_sexed_1, how_sexed_2
    
    # A method to parse the date MM/DD/YYYY
    def parse_date(self, date_str):
        month, day, year = date_str.split("/")
        # return a datetime object
        return datetime.date(int(year), int(month), int(day))
    
    def parse_time(self, time_str):
        # Pad the time string to ensure it's always 4 characters, e.g., '740' becomes '0740'
        time_str = time_str.zfill(4)
        hour = int(time_str[:2])
        minute = int(time_str[2:4])
        return datetime.time(hour, minute)


    def create_capture_record(self, row):
        capture_record = CaptureRecord()

        # Map each csv column to the corresponding CaptureRecord field
        capture_record.station = row.get("LOC")
        capture_record.band_size = row.get("BS")
        capture_record.bander_initials = row.get("BI")
        capture_record.capture_code = row.get("CODE")
        capture_record.alpha_code = row.get("SPECIES")
        capture_record.species_number = self.get_species_number(row.get("SPECIES"))
        capture_record.age_annual = int(row.get("AGE"))

        how_aged_1, how_aged_2 = self.set_how_aged(row.get("HA"))
        capture_record.how_aged_1 = how_aged_1
        capture_record.how_aged_2 = how_aged_2

        capture_record.age_WRP = row.get("WRP")
        capture_record.sex = row.get("SEX")

        how_sexed_1, how_sexed_2 = self.set_how_sexed(row.get("HS"))
        capture_record.how_sexed_1 = how_sexed_1
        capture_record.how_sexed_2 = how_sexed_2

        capture_record.skull = int(row.get("SK"))
        capture_record.cloacal_protuberance = int(row.get("CP"))
        capture_record.brood_patch = int(row.get("BP"))
        capture_record.fat = int(row.get("FAT"))
        capture_record.body_molt = int(row.get("BMOLT"))
        capture_record.ff_molt = row.get("FFMOLT")
        capture_record.ff_wear = int(row.get("FFWEAR"))
        capture_record.juv_body_plumage = int(row.get("J BDY PL"))
        capture_record.primary_coverts = row.get("PPC")
        capture_record.secondary_coverts = row.get("SSC")
        capture_record.primaries = row.get("PPF")
        capture_record.secondaries = row.get("SSF")
        capture_record.tertials = row.get("TT")
        capture_record.rectrices = row.get("RR")
        capture_record.body_plumage = row.get("BPL")
        capture_record.non_feather = row.get("NF")
        capture_record.wing_chord = int(row.get("WING"))
        capture_record.status = row.get("STATUS")
        capture_date = self.parse_date(row.get("DATE"))
        capture_time = self.parse_time(row.get("TIME"))
        capture_record.capture_time = timezone.make_aware(
            datetime.datetime.combine(capture_date, capture_time)
        )
        capture_record.net = int(row.get("NET"))
        capture_record.disposition = row.get("DISP")
        capture_record.note_number = row.get("NOTE #")
        capture_record.note = row.get("NOTES")

        # Assume all imported IBP records have already undergone validation
        capture_record.is_validated = True
        # Assume for IBP imports that the bander is also the scribe
        capture_record.scribe_initials = row.get("BI")

        capture_record.save()

        return capture_record
