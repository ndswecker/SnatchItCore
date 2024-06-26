from django.core.validators import ValidationError

from common.validators import FormValidator
from maps.maps_reference_data import AGES_ANNUAL
from maps.maps_reference_data import SPECIES
from maps.maps_reference_data import STATION_LOCATIONS
from maps.maps_reference_data import WRP_GROUPS


def validate_how_aged_by_plumage(form_data: dict):
    how_aged_1 = form_data.get("how_aged_1")
    how_aged_2 = form_data.get("how_aged_2")

    if "P" not in [how_aged_1, how_aged_2]:
        return

    primary_coverts = form_data.get("primary_coverts")
    secondary_coverts = form_data.get("secondary_coverts")
    primaries = form_data.get("primaries")
    secondaries = form_data.get("secondaries")
    tertials = form_data.get("tertials")
    rectrices = form_data.get("rectrices")
    body_plumage = form_data.get("body_plumage")

    plumage_scores = [primary_coverts, secondary_coverts, primaries, secondaries, tertials, rectrices, body_plumage]

    if all([score in [None, 0] for score in plumage_scores]):
        raise ValidationError(
            {
                "age_annual": "Plumage cannot be used to age a bird without any plumage indicators.",
            },
        )


def validate_juv_aging_plumage_not_p(form_data: dict):
    if form_data.get("age_annual") in [4, 2] and form_data.get("how_aged_1") == "P":
        raise ValidationError(
            {
                "age_annual": "How aged cannot be P for HY or Local birds. Please choose J.",
            },
        )


def validate_skull_provided_if_aged_by_skull(form_data: dict):
    if ("S" in [form_data.get("how_aged_1"), form_data.get("how_aged_2")]) and not form_data.get("skull"):
        raise ValidationError(
            {
                "skull": "A skull score must be provided if how aged is by skull.",
            },
        )


def validate_skull_score_for_adults(form_data: dict):
    skull = form_data.get("skull")
    age_annual = form_data.get("age_annual")
    if skull and skull < 5 and age_annual not in [2, 4]:
        raise ValidationError(
            {
                "skull": f"A skull score of {skull} is only valid for HY or Local birds.",
            },
        )


def validate_skull_score_not_valid_for_hy_or_local(form_data: dict):
    if form_data.get("age_annual") not in [2, 4]:
        return

    skull = form_data.get("skull")
    age_annual = form_data.get("age_annual")
    if skull in [5, 6] and age_annual in [2, 4]:
        raise ValidationError(
            {
                "skull": f"A skull score of {skull} is not valid for HY or Local birds.",
            },
        )


def validate_wrp_allowed_for_species(form_data: dict):
    target_species: dict = SPECIES[int(form_data.get("species_number"))]
    wrp_groups: list[int] = target_species["WRP_groups"]
    age_wrp = form_data.get("age_WRP")

    allowed_codes: list[str] = []
    for group_number in wrp_groups:
        allowed_codes.extend(WRP_GROUPS[group_number]["codes_allowed"])

    if age_wrp not in allowed_codes:
        raise ValidationError(
            {
                "age_WRP": f"The age_WRP {age_wrp} is not allowed for the species {target_species['common_name']} with WRP_groups {wrp_groups}.",  # noqa E501
            },
        )


def validate_male_how_sexed(form_data: dict):
    if form_data.get("sex") != "M":
        return

    how_sexed_1 = form_data.get("how_sexed_1")
    how_sexed_2 = form_data.get("how_sexed_2")
    male_criteria = ["C", "W", "E", "O", "P"]

    if not any(how_sexed in male_criteria for how_sexed in [how_sexed_1, how_sexed_2]):
        raise ValidationError(
            {
                "sex": "Fill in how sexed as 'C', 'W', 'E', 'P', or 'O'.",
            },
        )


def validate_female_how_sexed(form_data: dict):
    if form_data.get("sex") != "F":
        return

    how_sexed_1 = form_data.get("how_sexed_1")
    how_sexed_2 = form_data.get("how_sexed_2")
    female_criteria = ["B", "P", "E", "W", "O"]

    if not any(how_sexed in female_criteria for how_sexed in [how_sexed_1, how_sexed_2]):
        raise ValidationError(
            {
                "sex": "Fill in how sexed as 'B', 'P', 'E', 'W', or 'O'.",
            },
        )


def validate_cloacal_protuberance_filled_if_sexed_by_cp(form_data: dict):
    if form_data.get("sex") != "M":
        return

    how_sexed_1 = form_data.get("how_sexed_1")
    how_sexed_2 = form_data.get("how_sexed_2")
    cloacal_protuberance = form_data.get("cloacal_protuberance")

    if "C" in [how_sexed_1, how_sexed_2] and cloacal_protuberance in [None, 0]:
        raise ValidationError(
            {
                "cloacal_protuberance": "Cloacal protuberance must be filled in for birds sexed by cloacal protuberance.",  # noqa E501
            },
        )


def validate_cloacal_protuberance_none_or_zero_for_females(form_data: dict):
    if form_data.get("sex") != "F":
        return

    cloacal_protuberance = form_data.get("cloacal_protuberance")

    if cloacal_protuberance not in [None, 0]:
        raise ValidationError(
            {
                "cloacal_protuberance": "Cloacal protuberance must be None or 0 for female birds.",
            },
        )


def validate_brood_patch_indication_to_score(form_data: dict):
    how_sexed_1 = form_data.get("how_sexed_1")
    how_sexed_2 = form_data.get("how_sexed_2")
    how_aged_1 = form_data.get("how_aged_1")
    how_aged_2 = form_data.get("how_aged_2")
    brood_patch = form_data.get("brood_patch")

    sexed_by_bp = "B" in [how_sexed_1, how_sexed_2]
    aged_by_bp = "B" in [how_aged_1, how_aged_2]

    if (sexed_by_bp or aged_by_bp) and brood_patch is None:
        raise ValidationError(
            {
                "brood_patch": "Brood patch must be scored for birds sexed or aged by brood patch.",
            },
        )


def validate_species_brood_patch_sexing_for_females(form_data: dict):
    if form_data.get("sex") != "F":
        return

    species_number: int = int(form_data.get("species_number"))
    brood_patch = form_data.get("brood_patch")
    how_sexed_1 = form_data.get("how_sexed_1")
    how_sexed_2 = form_data.get("how_sexed_2")

    bp_limited_reliability: bool = not SPECIES[species_number]["sexing_criteria"]["female_by_BP"]
    bp_indicated = "B" in [how_sexed_1, how_sexed_2]
    bp_used_alone = (how_sexed_1 == "B" and how_sexed_2 is None) or (how_sexed_2 == "B" and how_sexed_1 is None)
    limited_bp = brood_patch not in [3, 4]

    if bp_indicated and bp_used_alone and bp_limited_reliability and limited_bp:
        raise ValidationError(
            {
                "sex": "This species cannot be reliably sexed female by a brood patch alone, unless the brood patch is 3 or 4.",  # noqa E501
            },
        )


def validate_appropriate_male_bp_score(form_data: dict):
    if form_data.get("sex") != "M":
        return

    species_number: int = int(form_data.get("species_number"))
    brood_patch = form_data.get("brood_patch")

    male_bp_viability: bool = not SPECIES[species_number]["sexing_criteria"]["female_by_BP"]
    has_bp = brood_patch not in [None, 0]

    if has_bp and not male_bp_viability:
        raise ValidationError(
            {
                "sex": "Males of this species should not have brood patches. Could this be juv?",
            },
        )


def validate_wrp_to_molt_score(form_data: dict):
    if "P" not in form_data.get("age_WRP"):
        return

    body_molt = form_data.get("body_molt")
    ff_molt = form_data.get("ff_molt")

    has_molt_score = body_molt not in [None, 0] or ff_molt not in [None, 0]

    if not has_molt_score:
        raise ValidationError(
            {
                "age_WRP": "The WRP code indicates this bird is molting, please indicate so in the body molt or flight feather molt scores",  # noqa E501
            },
        )


def validate_molt_presence_in_wrp_code(form_data: dict):
    body_molt = form_data.get("body_molt")
    ff_molt = form_data.get("ff_molt")
    wrp_code = form_data.get("age_WRP")

    # Check if there's a molt score indicated without 'P' in the WRP code
    molt_indicated = (body_molt not in [None, 0]) or (ff_molt not in [None, "N", "A"])
    p_not_in_wrp = "P" not in wrp_code

    if molt_indicated and p_not_in_wrp:
        raise ValidationError(
            {
                "age_WRP": "A molting score is indicated but the WRP code does not contain 'P'. Please correct the WRP code.",  # noqa E501
            },
        )


def validate_species_to_band_size(form_data: dict):
    capture_code = form_data.get("capture_code")
    if capture_code in ["R", "U"]:
        return

    species_number = int(form_data.get("species_number"))
    band_size: str = form_data.get("band_size")

    allowed_band_sizes: list[str] = SPECIES[species_number]["band_sizes"]

    if band_size not in allowed_band_sizes:
        raise ValidationError(
            {
                "band_size": f"The band size {band_size} is not allowed for this species.",
            },
        )


def validate_species_to_wing_chord(form_data: dict):
    if form_data.get("age_annual") in [2, 4] or form_data.get("wing_chord") is None:
        return

    species_number: int = int(form_data.get("species_number"))
    wing_chord = int(form_data.get("wing_chord"))

    wing_chord_min: int = SPECIES[species_number]["wing_chord_range"][0]
    wing_chord_max: int = SPECIES[species_number]["wing_chord_range"][1]

    if wing_chord < wing_chord_min or wing_chord > wing_chord_max:
        raise ValidationError(
            {
                "wing_chord": f"The wing chord {wing_chord} is not within the expected range for this species.",
            },
        )


def validate_how_sexed_to_wing_chord(form_data: dict):
    if form_data.get("sex") not in ["M", "F"]:
        return

    how_sexed_1 = form_data.get("how_sexed_1")
    how_sexed_2 = form_data.get("how_sexed_2")

    if "W" not in [how_sexed_1, how_sexed_2]:
        return

    wing_chord = form_data.get("wing_chord")

    if wing_chord is None:
        raise ValidationError(
            {
                "wing_chord": "Wing chord must be filled in for birds sexed by wing chord.",
            },
        )


def validate_how_sexed_by_wing_chord_is_possible(form_data: dict):
    if form_data.get("sex") not in ["M", "F"]:
        return

    how_sexed_1 = form_data.get("how_sexed_1")
    how_sexed_2 = form_data.get("how_sexed_2")

    if "W" not in [how_sexed_1, how_sexed_2]:
        return

    species_number = int(form_data.get("species_number"))

    if "wing_chord_range_by_sex" not in SPECIES[species_number]:
        raise ValidationError(
            {
                "how_sexed_1": "This species cannot be sexed by wing chord.",
            },
        )


def validate_how_sexed_by_wing_chord_in_range(form_data: dict):
    sex = form_data.get("sex")

    if sex not in ["M", "F"]:
        return

    how_sexed_1 = form_data.get("how_sexed_1")
    how_sexed_2 = form_data.get("how_sexed_2")

    if "W" not in [how_sexed_1, how_sexed_2]:
        return

    species_number: int = int(form_data.get("species_number"))

    if "wing_chord_range_by_sex" not in SPECIES[species_number]:
        return

    sex_code_mapping = {"M": "male", "F": "female"}

    mapped_sex = sex_code_mapping.get(sex)
    wing_chord = int(form_data.get("wing_chord"))

    wing_chord_min: int = SPECIES[species_number]["wing_chord_range_by_sex"][mapped_sex][0]
    wing_chord_max: int = SPECIES[species_number]["wing_chord_range_by_sex"][mapped_sex][1]

    if wing_chord < wing_chord_min or wing_chord > wing_chord_max:
        raise ValidationError(
            {
                "wing_chord": f"The wing chord {wing_chord} is not within the expected range for a {mapped_sex} of this species.",  # noqa E501
            },
        )


def validate_how_sexed_has_sex(form_data: dict):
    how_sexed_1 = form_data.get("how_sexed_1")
    how_sexed_2 = form_data.get("how_sexed_2")
    sex = form_data.get("sex")

    if (how_sexed_1 is None and how_sexed_2 is None) and sex not in ["U", "X"]:
        raise ValidationError(
            {
                "sex": "How sexed must be blank for birds not sexed.",
            },
        )


def validate_recapture_has_no_band_size(form_data: dict):
    if form_data.get("capture_code") != "R":
        return

    if form_data.get("band_size") != "R":
        raise ValidationError(
            {
                "band_size": "Band size must labeled as 'Recap' for recaptures.",
            },
        )


def validate_recapture_and_new_has_band_number(form_data: dict):
    if form_data.get("capture_code") not in ["R", "N"]:
        return

    if form_data.get("band_number") is None:
        raise ValidationError(
            {
                "band_number": "Band number must be filled in for new birds and recaps.",
            },
        )


def validate_unbanded_has_no_band_size(form_data: dict):
    if form_data.get("capture_code") != "U":
        return

    if form_data.get("band_size") != "U":
        raise ValidationError(
            {
                "band_size": "Band size must labeled as 'Unbanded' for unbanded birds.",
            },
        )


def validate_unbanded_has_no_band_number(form_data: dict):
    if form_data.get("capture_code") != "U":
        return

    if form_data.get("band_number") is not None:
        raise ValidationError(
            {
                "band_number": "Band number must be left blank for unbanded birds.",
            },
        )


def validate_unbanded_status(form_data: dict):
    if form_data.get("capture_code") != "U":
        return

    if int(form_data.get("status")) != 0:
        raise ValidationError(
            {
                "status": "Status must be 000 for unbanded birds.",
            },
        )


def validate_net_to_station(form_data: dict):
    net: int = int(form_data.get("net"))
    station: str = form_data.get("station")
    net_set: list[int] = STATION_LOCATIONS[station]["net_set"]

    if net not in net_set:
        raise ValidationError(
            {
                "net": f"The net {net} is not at the station {station}.",
            },
        )


def validate_band_number_to_size(form_data: dict):
    # Ensure that the 4th digit of the band number matches the first character of the band size
    band_number: str = form_data.get("band_number")
    band_size: str = form_data.get("band_size")

    if band_number is None or band_size in ["R", "U"]:
        return

    # Convert band_number to string and access the 4th digit (3rd index)
    appropriate_size_band = str(band_number)[3]
    if appropriate_size_band != band_size[0]:
        raise ValidationError(
            {
                "band_size": f"The band number {band_number} does not match the band size {band_size}.",
            },
        )


def validate_status_to_dispostion_for_injury(form_data: dict):
    status = int(form_data.get("status"))
    if status != 500:
        return

    disposition = form_data.get("disposition")
    injury_codes = ["B", "E", "F", "I", "L", "P", "S", "T", "W"]

    if disposition not in injury_codes:
        raise ValidationError(
            {
                "disposition": f"The disposition {disposition} is not a valid injury code for a bird with status {status}.",  # noqa #501
            },
        )


def validate_disposition_to_status_for_injury(form_data: dict):
    disposition = form_data.get("disposition")
    status = int(form_data.get("status", 0))  # Default to 0 if status not provided
    injury_codes = ["B", "E", "F", "I", "L", "P", "S", "T", "W"]

    # If the disposition indicates an injury, ensure status is 500
    if disposition in injury_codes and status != 500:
        raise ValidationError(
            {
                "status": f"With disposition {disposition}, the status must be 500 to indicate injury.",
            },
        )


def validate_injury_has_note(form_data: dict):
    status = int(form_data.get("status"))
    if status != 500:
        return

    note = form_data.get("note")

    if not note:
        raise ValidationError(
            {
                "note": "A note must be provided for injured birds.",
            },
        )


def validate_death_to_status(form_data: dict):
    disposition = form_data.get("disposition")
    if disposition != "D":
        return

    status = int(form_data.get("status"))

    if status != 0:
        raise ValidationError(
            {
                "disposition": "Dead birds must have a status of 000",
            },
        )


def validate_death_has_note(form_data: dict):
    disposition = form_data.get("disposition")
    if disposition != "D":
        return

    note = form_data.get("note")

    if not note:
        raise ValidationError(
            {
                "note": "Dead birds must have a note",
            },
        )


def validate_age_annual_to_allowed_wrp(form_data: dict):
    age_annual = int(form_data.get("age_annual"))
    age_wrp = form_data.get("age_WRP")

    allowed_wrp_codes = AGES_ANNUAL[age_annual]["allowed_wrp_codes"]

    if age_wrp not in allowed_wrp_codes:
        raise ValidationError(
            {
                "age_WRP": f"The age {age_annual} does not correspond to the WRP code {age_wrp}. Allowed codes are {', '.join(allowed_wrp_codes)}.",  # noqa E501
            },
        )


class CaptureRecordFormValidator(FormValidator):
    def __init__(self, cleaned_data):
        super().__init__(cleaned_data)
        self.validators = [
            validate_how_aged_by_plumage,
            validate_juv_aging_plumage_not_p,
            validate_skull_provided_if_aged_by_skull,
            validate_skull_score_for_adults,
            validate_skull_score_not_valid_for_hy_or_local,
            validate_wrp_allowed_for_species,
            validate_age_annual_to_allowed_wrp,
            validate_female_how_sexed,
            validate_male_how_sexed,
            validate_cloacal_protuberance_filled_if_sexed_by_cp,
            validate_species_brood_patch_sexing_for_females,
            validate_cloacal_protuberance_none_or_zero_for_females,
            validate_brood_patch_indication_to_score,
            validate_appropriate_male_bp_score,
            validate_wrp_to_molt_score,
            validate_molt_presence_in_wrp_code,
            validate_species_to_band_size,
            validate_species_to_wing_chord,
            validate_how_sexed_by_wing_chord_in_range,
            validate_how_sexed_to_wing_chord,
            validate_how_sexed_by_wing_chord_is_possible,
            validate_how_sexed_has_sex,
            validate_recapture_has_no_band_size,
            validate_unbanded_has_no_band_size,
            validate_unbanded_has_no_band_number,
            validate_unbanded_status,
            validate_recapture_and_new_has_band_number,
            validate_net_to_station,
            validate_band_number_to_size,
            validate_status_to_dispostion_for_injury,
            validate_disposition_to_status_for_injury,
            validate_injury_has_note,
            validate_death_to_status,
            validate_death_has_note,
        ]
