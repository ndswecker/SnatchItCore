from django.core.validators import ValidationError

from common.validators import FormValidator
from maps.maps_reference_data import SPECIES, WRP_GROUPS


def validate_juv_aging_plumage_not_p(form_data: dict):
    if form_data.get("age_annual") in [4, 2] and form_data.get("how_aged_1") == "P":
        raise ValidationError(
            {
                "age_annual": f"How aged cannot be P for HY or Local birds. Please choose J.",
            },
        )
    
def validate_skull_provided_if_aged_by_skull(form_data: dict):
    if ("S" in [form_data.get("how_aged_1"), form_data.get("how_aged_2")]) and not form_data.get("skull"):
        raise ValidationError(
            {
                "skull": "A skull score must be provided if how aged is by skull."
            }
        )
    
def validate_skull_score_for_hy_or_local_birds(form_data: dict):
    skull = form_data.get("skull")
    age_annual = form_data.get("age_annual")
    if skull and skull < 5 and age_annual not in [2, 4]:
        raise ValidationError(
            {
                "skull": f"A skull score of {skull} is only valid for HY or Local birds."
            }
        )
    
def validate_skull_score_not_valid_for_hy_or_local(form_data: dict):
    skull = form_data.get("skull")
    age_annual = form_data.get("age_annual")
    if skull in [5, 6] and age_annual in [2, 4]:
        raise ValidationError(
            {
                "skull": f"A skull score of {skull} is not valid for HY or Local birds."
            }
        )

def validate_wrp_allowed_for_species(form_data: dict):
    target_species = SPECIES[int(form_data.get("species_number"))]
    wrp_groups = target_species["WRP_groups"]
    age_wrp = form_data.get("age_WRP")

    allowed_codes = []
    for group_number in wrp_groups:
        allowed_codes.extend(WRP_GROUPS[group_number]["codes_allowed"])

    if age_wrp not in allowed_codes:
        raise ValidationError(
            {
                "age_WRP": 
                f"The age_WRP {age_wrp} is not allowed for the species {target_species['common_name']} with WRP_groups {wrp_groups}.",  # noqa E501
            },
        )

def validate_male_how_sexed(form_data: dict):
    sex = form_data.get("sex")
    how_sexed_1 = form_data.get("how_sexed_1")
    how_sexed_2 = form_data.get("how_sexed_2")
    male_criteria = ["C", "W", "E", "O", "P"]

    if sex == "M" and not any(how_sexed in male_criteria for how_sexed in [how_sexed_1, how_sexed_2]):
        raise ValidationError({
            "sex": "Fill in how sexed as 'C', 'W', 'E', 'P', or 'O'."
        })

def validate_female_how_sexed(form_data: dict):
    sex = form_data.get("sex")
    how_sexed_1 = form_data.get("how_sexed_1")
    how_sexed_2 = form_data.get("how_sexed_2")
    female_criteria = ["B", "P", "E", "W", "O"]

    if sex == "F" and not any(how_sexed in female_criteria for how_sexed in [how_sexed_1, how_sexed_2]):
        raise ValidationError({
            "sex": "Fill in how sexed as 'B', 'P', 'E', 'W', or 'O'."
        })

def validate_cloacal_protuberance_filled_if_sexed_by_cp(form_data: dict):
    how_sexed_1 = form_data.get("how_sexed_1")
    how_sexed_2 = form_data.get("how_sexed_2")
    cloacal_protuberance = form_data.get("cloacal_protuberance")

    if "C" in [how_sexed_1, how_sexed_2] and cloacal_protuberance in [None, 0]:
        raise ValidationError({
            "cloacal_protuberance": "Cloacal protuberance must be filled in for birds sexed by cloacal protuberance."
        })

def validate_cloacal_protuberance_none_or_zero_for_females(form_data: dict):
    sex = form_data.get("sex")
    cloacal_protuberance = form_data.get("cloacal_protuberance")

    if sex == "F" and cloacal_protuberance not in [None, 0]:
        raise ValidationError({
            "cloacal_protuberance": "Cloacal protuberance must be None or 0 for female birds."
        })

def validate_species_brood_patch_sexing_for_females(form_data: dict):
    species_number = int(form_data.get("species_number"))
    brood_patch = form_data.get("brood_patch")
    how_sexed_1 = form_data.get("how_sexed_1")
    how_sexed_2 = form_data.get("how_sexed_2")
    sex = form_data.get("sex")
    reliable_bp_sexing = SPECIES[species_number]["sexing_criteria"]["female_by_BP"]

    # Check if the species can be reliably sexed by brood patch or if brood patch is 3 or 4,
    # indicating it can be sexed as female regardless of the species' general reliability for sexing by brood patch.
    if sex == "F" and ("B" in [how_sexed_1, how_sexed_2]) and not reliable_bp_sexing and brood_patch not in [3, 4]:
        raise ValidationError({
            "sex": "This species cannot be reliably sexed female by a brood patch alone, unless the brood patch is 3 or 4."
        })




class CaptureRecordFormValidator(FormValidator):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validators = [
            validate_juv_aging_plumage_not_p,
            validate_skull_provided_if_aged_by_skull,
            validate_skull_score_for_hy_or_local_birds,
            validate_skull_score_not_valid_for_hy_or_local,
            validate_wrp_allowed_for_species,
            validate_female_how_sexed,
            validate_male_how_sexed,
            validate_species_brood_patch_sexing_for_females,
        ]
