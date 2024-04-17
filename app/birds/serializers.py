import csv
from birds.models import AgeAnnual
from birds.models import AgeWRP
from birds.models import Band
from birds.models import GroupWRP

def parse_agewrps_from_csv(csv_file_path):
    age_wrps = []
    annual_cache = {}  # Cache to store and reuse AgeAnnual objects

    with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Prepare data for AgeWRP
            age_wrp_data = {
                "code": row["code"],
                "sequence": int(row["sequence"]),
                "description": row["description"],
                "status": row["status"].lower(),
                "annuals": []
            }
            
            # Handle annual IDs, assume they are comma-separated
            annual_ids = row.get("annuals", "")
            if annual_ids:
                for annual_id in annual_ids.split(","):
                    if annual_id.strip():
                        if annual_id not in annual_cache:
                            # Assume AgeAnnual exists, or create a mechanism to handle new entries
                            annual, created = AgeAnnual.objects.get_or_create(number=int(annual_id.strip()))
                            annual_cache[annual_id] = annual
                        age_wrp_data["annuals"].append(annual_cache[annual_id])

            age_wrps.append(age_wrp_data)

    return age_wrps

def parse_ageannuals_from_csv(csv_file_path):
    age_annuals = []

    with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Prepare data for AgeAnnual
            age_annual_data = {
                "number": int(row["number"]),
                "alpha": row["alpha"],
                "description": row["description"],
                "explanation": row["explanation"],
            }
            age_annuals.append(age_annual_data)

    return age_annuals

def parse_bands_from_csv(csv_file_path):
    bands = []

    with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Prepare data for Band
            band_data = {
                "size": row["size"],
                "comment": row["comment"],
            }
            bands.append(band_data)

    return bands

def parse_groupwrps_from_csv(csv_file_path):
    group_wrps = []
    age_wrp_cache = {}  # Cache to store and reuse AgeWRP objects

    with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Prepare data for GroupWRP
            group_wrp_data = {
                "number": int(row["number"]),
                "explanation": row["explanation"],
                "ages": []
            }
            
            # Handle age WRP IDs, assume they are comma-separated
            age_wrp_ids = row.get("ages", "")
            if age_wrp_ids:
                for age_wrp_id in age_wrp_ids.split(","):
                    if age_wrp_id.strip():
                        if age_wrp_id not in age_wrp_cache:
                            # Assume AgeWRP exists, or create a mechanism to handle new entries
                            age_wrp, created = AgeWRP.objects.get_or_create(code=age_wrp_id.strip())
                            age_wrp_cache[age_wrp_id] = age_wrp
                        group_wrp_data["ages"].append(age_wrp_cache[age_wrp_id])

            group_wrps.append(group_wrp_data)

    return group_wrps
