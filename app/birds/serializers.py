import csv
from django.db import transaction
from birds.models import AgeWRP, AgeAnnual

def parse_agewrps_from_csv(csv_file_path):
    age_wrps = []
    annual_cache = {}
    with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            age_wrp = AgeWRP(
                code=row["code"],
                sequence=int(row["sequence"]),
                description=row["description"],
                status=row["status"].lower()
            )
            age_wrps.append(age_wrp)

    # Assuming all AgeWRP objects are ready to be saved without annuals
    AgeWRP.objects.bulk_create(age_wrps)

    # Reopen the file to assign annuals now that all AgeWRPs are persisted
    with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            age_wrp = AgeWRP.objects.get(code=row["code"])  # Retrieve the newly created object
            annual_ids = row.get("annuals", "")
            if annual_ids:
                for annual_id in annual_ids.split(","):
                    if annual_id.strip():
                        if annual_id not in annual_cache:
                            annual, created = AgeAnnual.objects.get_or_create(number=int(annual_id.strip()))
                            annual_cache[annual_id] = annual
                        else:
                            annual = annual_cache[annual_id]
                        age_wrp.annuals.add(annual)

    return AgeWRP.objects.filter(code__in=[wrp.code for wrp in age_wrps])  # Return newly created objects with annuals linked
