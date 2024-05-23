from django.core.management.base import BaseCommand
import csv
from decimal import Decimal
from datetime import datetime

from maps.models import CaptureRecord


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="The CSV file to load data from")

    def handle(self, *args, **options):
        data = self.parse_capture_records_from_csv(options["csv_file"])
        capture_records = [CaptureRecord(**record) for record in data]

        CaptureRecord.objects.bulk_create(capture_records)
        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully loaded {len(capture_records)} CaptureRecord objects",
            ),
        )

    def parse_capture_records_from_csv(self, csv_file_path):
        with open(csv_file_path) as csv_file:
            reader = csv.DictReader(csv_file)
            capture_records = []
            for row in reader:
                if not any(value.strip() for value in row.values()):
                    break
                try:
                    capture_record = {
                        "user_id": int(row["user_id"]) if row["user_id"].strip() else 1,
                        "scribe_initials": row["scribe_initials"].strip(),
                        "capture_code": row["capture_code"].strip(),
                        "species_number": int(row["species_number"]),
                        "band_size": row["band_size"].strip() or None,
                        "band_number": int(row["band_number"]) if row["band_number"].strip() else None,
                        "alpha_code": row["alpha_code"].strip(),
                        "age_annual": int(row["age_annual"]) if row["age_annual"].strip() else None,
                        "how_aged_1": row["how_aged_1"].strip() or None,
                        "how_aged_2": row["how_aged_2"].strip() or None,
                        "age_WRP": row["age_WRP"].strip(),
                        "sex": row["sex"].strip() or None,
                        "how_sexed_1": row["how_sexed_1"].strip() or None,
                        "how_sexed_2": row["how_sexed_2"].strip() or None,
                        "cloacal_direction": row["cloacal_direction"].strip() or None,
                        "skull": int(row["skull"]) if row["skull"].strip() else None,
                        "cloacal_protuberance": (
                            int(row["cloacal_protuberance"])
                            if row["cloacal_protuberance"].strip()
                            else None  # noqa E501
                        ),
                        "brood_patch": int(row["brood_patch"]) if row["brood_patch"].strip() else None,
                        "fat": int(row["fat"]) if row["fat"].strip() else None,
                        "body_molt": int(row["body_molt"]) if row["body_molt"].strip() else None,
                        "ff_molt": row["ff_molt"].strip() or None,
                        "ff_wear": int(row["ff_wear"]) if row["ff_wear"].strip() else None,
                        "juv_body_plumage": int(row["juv_body_plumage"]) if row["juv_body_plumage"].strip() else None,
                        "primary_coverts": row["primary_coverts"].strip() or None,
                        "secondary_coverts": row["secondary_coverts"].strip() or None,
                        "primaries": row["primaries"].strip() or None,
                        "secondaries": row["secondaries"].strip() or None,
                        "tertials": row["tertials"].strip() or None,
                        "rectrices": row["rectrices"].strip() or None,
                        "body_plumage": row["body_plumage"].strip() or None,
                        "alula": row["alula"].strip() or None,
                        "non_feather": row["non_feather"].strip() or None,
                        "wing_chord": int(row["wing_chord"]) if row["wing_chord"].strip() else None,
                        "body_mass": Decimal(row["body_mass"]) if row["body_mass"].strip() else None,
                        "status": int(row["status"]) if row["status"].strip() else None,
                        "capture_time": (
                            datetime.strptime(row["capture_time"], "%Y-%m-%d %H:%M:%S%z")
                            if row["capture_time"].strip()
                            else None
                        ),
                        "hold_time": Decimal(row["hold_time"]) if row["hold_time"].strip() else None,
                        "station": row["station"].strip(),
                        "net": int(row["net"]) if row["net"].strip() else None,
                        "disposition": row["disposition"].strip() or None,
                        "note_number": int(row["note_number"]) if row["note_number"].strip() else None,
                        "note": row["note"].strip() or None,
                        "bander_initials": row["bander_initials"].strip(),
                        "discrepancies": row["discrepancies"].strip() or None,
                        "is_validated": row["is_validated"].strip().upper() == "TRUE",
                    }
                    capture_records.append(capture_record)
                except Exception as e:
                    continue

        return capture_records
