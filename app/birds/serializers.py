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
                                    },
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
                            },
                        )
                        priority += 1
    except FileNotFoundError as e:
        print(f"While attempting to parse band allocations, file {csv_file_path} was not found: {e}")

    return band_allocations
