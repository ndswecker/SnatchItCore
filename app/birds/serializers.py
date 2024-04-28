import csv
import re

def parse_agewrps_from_csv(csv_file_path):
    age_wrps = []
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
                        "annuals": [int(annual_id.strip()) for annual_id in row.get("annuals", "").split(",") if annual_id.strip()],
                    }
                    age_wrps.append(age_wrp_data)
                except ValueError as e:
                    errors.append(f"Error parsing AgeWRP data in row {reader.line_num}: {e}")
                except KeyError as e:
                    errors.append(f"Error parsing AgeWRP data in row {reader.line_num}: Missing expected column {e}")
                
    except FileNotFoundError as e:
        print(f"File {csv_file_path} was not found: {e}")
    except csv.Error as e:
        print(f"An error occurred while reading and parsing the CSV file: {e}")

    if errors:
        print("The following errors occurred while parsing AgeWRP data:")
        for error in errors:
            print(error)

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
    errors = []

    try:
        with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    age_wrp_ids = [
                        clean_id.strip()
                        for clean_id in row.get("ages", "").split(",")
                        if clean_id.strip()
                    ]
                    group_wrp_data = {
                        "number": int(row["number"]),
                        "explanation": row["explanation"],
                        "ages": age_wrp_ids,
                    }
                    group_wrps.append(group_wrp_data)
                except ValueError as e:
                    errors.append(f"Error parsing group WRP data in row {reader.line_num}: {e}")
                except KeyError as e:
                    errors.append(f"Error parsing group WRP data in row {reader.line_num}: Missing expected column {e}")
    
    except FileNotFoundError as e:
        print(f"While attempting to parse group WRP data, file {csv_file_path} was not found: {e}")
    except csv.Error as e:
        print(f"A CSV error occurred while parsing group WRP data: {e}")

    if errors:
        print("The following errors occurred while parsing group WRP data:")
        for error in errors:
            print(error)

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

def parse_band_sizes(species_number, alpha, band_sizes):
    bands = []
    last_sex = None  # Track the last processed sex

    # Split into lines assuming M: and F: are on separate lines
    lines = band_sizes.split("\n")
    for line in lines:
        line = line.strip()  # Ensure there's no leading/trailing whitespace
        if line.startswith("M:") or line.startswith("F:"):
            sex = line[:1].lower()  # Correctly get 'm' or 'f'
            sizes = line[2:].split(",")  # Extract sizes after 'M: ' or 'F: '
            # Reset priority if sex changes
            if sex != last_sex:
                priority = 0
                last_sex = sex
        else:
            sex = "u"  # Unisex
            sizes = line.split(",")
            if sex != last_sex:
                priority = 0
                last_sex = sex

        for size in sizes:
            size = size.strip()
            if size:  # Ensure the size is not empty
                bands.append({
                    "bird": species_number,
                    "alpha": alpha,
                    "band": size,
                    "sex": sex,
                    "priority": priority,
                })
                priority += 1
    return bands

def parse_band_allocations_from_csv(csv_file_path):
    band_allocations = []

    try:
        with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                species_number = int(row["number"])
                alpha = row["alpha"]
                band_sizes = row["band_size"]
                species_bands = parse_band_sizes(species_number, alpha, band_sizes)
                band_allocations.extend(species_bands)

    except FileNotFoundError as e:
        print(f"File not found: {csv_file_path} - {e}")
    except csv.Error as e:
        print(f"CSV reading error: {e}")

    return band_allocations
