import csv
import re

from birds.models import AgeAnnual
from birds.models import AgeWRP
from birds.models import Band
from birds.models import GroupWRP


def parse_agewrps_from_csv(csv_file_path):
    age_wrps = []
    annual_cache = {}  # Cache to store and reuse AgeAnnual objects
    errors = []

    try:
        with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    age_wrp_data = {
                        "code": row["code"],
                        "sequence": int(row["sequence"]),
                        "description": row["description"],
                        "status": row["status"].lower(),
                        "annuals": [],
                    }

                    # Handle annual IDs, assume they are comma-separated
                    annual_ids = row.get("annuals", "")
                    if annual_ids:
                        for annual_id in annual_ids.split(","):
                            annual_id = annual_id.strip()  # Strip whitespace from annual ID
                            if annual_id:  # Proceed if the ID is not empty after stripping
                                if annual_id not in annual_cache:  # Check if the ID is not already cached
                                    annual = AgeAnnual.objects.get(number=int(annual_id))  # Fetch the AgeAnnual object
                                    annual_cache[annual_id] = annual  # Cache it
                                # Append the AgeAnnual object to the data
                                age_wrp_data["annuals"].append(annual_cache[annual_id])

                    age_wrps.append(age_wrp_data)

                except ValueError as e:
                    errors.append(f"Error parsing AgeWRP data in row {reader.line_num}: {e}")
                except KeyError as e:
                    errors.append(f"Error parsing AgeWRP data in row {reader.line_num}: Missing expected column {e}")
                except AgeAnnual.DoesNotExist as e:
                    errors.append(f"Error parsing AgeWRP data in row {reader.line_num} for a non valid age annual: {e}")
                except Exception as e:
                    errors.append(f"Error parsing AgeWRP data in row {reader.line_num}: {e}")

    except FileNotFoundError as e:
        print(f"File {csv_file_path} was not found: {e}")
    except csv.Error as e:
        print(f"An error occurred while reading and parsing the CSV file: {e}")

    if errors:
        print("The following errors occurred while parsing AgeWRP data:")
        for error in errors:
            print(error)
    else:
        print("Successfully parsed all AgeWRP data with no errors found")

    return age_wrps


def parse_ageannuals_from_csv(csv_file_path):
    age_annuals = []
    errors = []

    try:
        with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    age_annual_data = {
                        "number": int(row["number"]),
                        "alpha": row["alpha"],
                        "description": row["description"],
                        "explanation": row["explanation"],
                    }
                    age_annuals.append(age_annual_data)
                except ValueError as e:
                    errors.append(f"Error parsing AgeAnnual data in row {reader.line_num}: {e}")
                except KeyError as e:
                    errors.append(f"Error parsing AgeAnnual data in row {reader.line_num}: Missing expected column {e}")

    except csv.Error as e:
        print(f"An error occurred while reading and parsing the CSV file: {e}")
    except FileNotFoundError as e:
        print(f"File {csv_file_path} was not found: {e}")

    if errors:
        print("The following errors occurred while parsing AgeAnnual data:")
        for error in errors:
            print(error)

    return age_annuals


def parse_bands_from_csv(csv_file_path):
    bands = []

    try:
        with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Prepare data for Band
                band_data = {
                    "size": row["size"],
                    "comment": row["comment"],
                }
                bands.append(band_data)
    except FileNotFoundError as e:
        print(f"While attempting to parse bands sizes, file {csv_file_path} was not found: {e}")

    return bands


def parse_groupwrps_from_csv(csv_file_path):
    group_wrps = []
    age_wrp_cache = {}  # Cache to store and reuse AgeWRP objects
    missing_age_wrps = []  # List to store missing AgeWRP codes

    try:
        with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Prepare data for GroupWRP
                group_wrp_data = {
                    "number": int(row["number"]),
                    "explanation": row["explanation"],
                    "ages": [],
                }

                # Handle age WRP IDs, assume they are comma-separated
                age_wrp_ids = row.get("ages", "")
                if age_wrp_ids:
                    for age_wrp_id in age_wrp_ids.split(","):
                        clean_id = age_wrp_id.strip()  # Strip whitespace from age WRP ID
                        if clean_id:  # Proceed if the ID is not empty after stripping
                            if clean_id not in age_wrp_cache:
                                try:
                                    age_wrp = AgeWRP.objects.get(code=clean_id)
                                    age_wrp_cache[clean_id] = age_wrp
                                except AgeWRP.DoesNotExist:
                                    missing_age_wrps.append(clean_id)
                                    continue  # Skip this ID and move to the next one
                            group_wrp_data["ages"].append(age_wrp_cache[clean_id].id)

                group_wrps.append(group_wrp_data)
    except FileNotFoundError as e:
        print(f"While attempting to parse group WRP data, file {csv_file_path} was not found: {e}")
    except csv.Error as e:
        print(f"A CSV error occurred while parsing group WRP data: {e}")

    if missing_age_wrps:
        print(f"The following AgeWRP codes were not found in the database: {missing_age_wrps}")

    return group_wrps


def parse_species_from_csv(csv_file_path):
    species = []

    try:
        with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    # Prepare data for Species
                    species_data = {
                        "number": int(row["number"]),
                        "alpha": row["alpha"],
                        "common": row["common"].strip().replace("*", ""),
                        "scientific": row["scientific"],
                        "taxonomic_order": int(row["taxonomic_order"]),
                    }
                    species.append(species_data)
                except ValueError as e:
                    print(f"Error parsing species data in row {reader.line_num}: {e}")
    except FileNotFoundError as e:
        print(f"While attempting to parse species data, file {csv_file_path} was not found: {e}")
    except csv.Error as e:
        print(f"A CSV error occurred while parsing species data: {e}")

    return species


def parse_band_allocations_from_csv(csv_file_path):
    band_allocations = []

    # Regex pattern to correctly extract band sizes and differentiate between M and F
    # It captures 'M:' or 'F:' followed by any number of band sizes separated by commas
    band_size_pattern = re.compile(r"(M|F):\s*((?:\d+[A-Z]?(?:, )?)*)")

    try:
        with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                species_number = int(row["number"])
                band_sizes = row["band_size"]
                alpha = row["alpha"]
                priority = 0

                # First, check for and handle specific 'M:' or 'F:' entries
                sex_specific_matches = band_size_pattern.findall(band_sizes)
                if sex_specific_matches:
                    for sex_prefix, bands in sex_specific_matches:
                        for band in bands.split(", "):
                            if band:  # Ensure the band entry is not empty
                                band_allocations.append(
                                    {
                                        "bird": species_number,
                                        "alpha": alpha,
                                        "band": band.strip(),
                                        "sex": sex_prefix.lower(),  # 'm' or 'f'
                                        "priority": priority,
                                    }
                                )
                                priority += 1
                    # Remove the processed parts from the band_sizes string
                    band_sizes = band_size_pattern.sub("", band_sizes)

                # Handle the remaining bands which are unisex
                for band in band_sizes.split(","):
                    band = band.strip()
                    if band:  # Ensure the band entry is not empty
                        band_allocations.append(
                            {
                                "bird": species_number,
                                "alpha": alpha,
                                "band": band,
                                "sex": "u",  # Unisex
                                "priority": priority,
                            }
                        )
                        priority += 1
    except FileNotFoundError as e:
        print(f"While attempting to parse band allocations, file {csv_file_path} was not found: {e}")

    return band_allocations
