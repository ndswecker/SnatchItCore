from django.core.validators import ValidationError

from common.validators import FormValidator
from maps.maps_reference_data import SPECIES, WRP_GROUPS

def validate_how_aged_by_plumage(form_data: dict):
    how_aged_1 = form_data.get("how_aged_1")
    how_aged_2 = form_data.get("how_aged_2")

    if 'P' not in [how_aged_1, how_aged_2]:
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
    
def validate_skull_score_for_adults(form_data: dict):
    skull = form_data.get("skull")
    age_annual = form_data.get("age_annual")
    if skull and skull < 5 and age_annual not in [2, 4]:
        raise ValidationError(
            {
                "skull": f"A skull score of {skull} is only valid for HY or Local birds."
            }
        )
    
def validate_skull_score_not_valid_for_hy_or_local(form_data: dict):
    if form_data.get("age_annual") not in [2, 4]:
        return
    
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
    if form_data.get("sex") != "M":
        return
    
    how_sexed_1 = form_data.get("how_sexed_1")
    how_sexed_2 = form_data.get("how_sexed_2")
    male_criteria = ["C", "W", "E", "O", "P"]

    if not any(how_sexed in male_criteria for how_sexed in [how_sexed_1, how_sexed_2]):
        raise ValidationError({
            "sex": "Fill in how sexed as 'C', 'W', 'E', 'P', or 'O'."
        })

def validate_female_how_sexed(form_data: dict):
    if form_data.get("sex") != "F":
        return
    
    how_sexed_1 = form_data.get("how_sexed_1")
    how_sexed_2 = form_data.get("how_sexed_2")
    female_criteria = ["B", "P", "E", "W", "O"]

    if not any(how_sexed in female_criteria for how_sexed in [how_sexed_1, how_sexed_2]):
        raise ValidationError({
            "sex": "Fill in how sexed as 'B', 'P', 'E', 'W', or 'O'."
        })

def validate_cloacal_protuberance_filled_if_sexed_by_cp(form_data: dict):
    if form_data.get("sex") != "M":
        return
    
    how_sexed_1 = form_data.get("how_sexed_1")
    how_sexed_2 = form_data.get("how_sexed_2")
    cloacal_protuberance = form_data.get("cloacal_protuberance")

    if "C" in [how_sexed_1, how_sexed_2] and cloacal_protuberance in [None, 0]:
        raise ValidationError({
            "cloacal_protuberance": "Cloacal protuberance must be filled in for birds sexed by cloacal protuberance."
        })

def validate_cloacal_protuberance_none_or_zero_for_females(form_data: dict):
    if form_data.get("sex") != "F":
        return
    
    cloacal_protuberance = form_data.get("cloacal_protuberance")

    if cloacal_protuberance not in [None, 0]:
        raise ValidationError({
            "cloacal_protuberance": "Cloacal protuberance must be None or 0 for female birds."
        })
    
def validate_brood_patch_indication_to_score(form_data: dict):
    how_sexed_1 = form_data.get("how_sexed_1")
    how_sexed_2 = form_data.get("how_sexed_2")
    how_aged_1 = form_data.get("how_aged_1")
    how_aged_2 = form_data.get("how_aged_2")
    brood_patch = form_data.get("brood_patch")

    sexed_by_bp = "B" in [how_sexed_1, how_sexed_2]
    aged_by_bp = "B" in [how_aged_1, how_aged_2]

    if (sexed_by_bp or aged_by_bp) and brood_patch is None:
        raise ValidationError({
            "brood_patch": "Brood patch must be scored for birds sexed or aged by brood patch."
        })

def validate_species_brood_patch_sexing_for_females(form_data: dict):
    if form_data.get("sex") != "F":
        return
    
    species_number = int(form_data.get("species_number"))
    brood_patch = form_data.get("brood_patch")
    how_sexed_1 = form_data.get("how_sexed_1")
    how_sexed_2 = form_data.get("how_sexed_2")

    bp_limited_reliability = not SPECIES[species_number]["sexing_criteria"]["female_by_BP"]
    bp_indicated = "B" in [how_sexed_1, how_sexed_2]
    bp_used_alone = (how_sexed_1 == "B" and how_sexed_2 is None) or (how_sexed_2 == "B" and how_sexed_1 is None)
    limited_bp = brood_patch not in [3, 4]

    if bp_indicated and bp_used_alone and bp_limited_reliability and limited_bp:
        raise ValidationError(
            {
            "sex": "This species cannot be reliably sexed female by a brood patch alone, unless the brood patch is 3 or 4."
            }
        )
    
def validate_appropriate_male_bp_score(form_data: dict):
    if form_data.get("sex") != "M":
        return
    
    species_number = int(form_data.get("species_number"))
    brood_patch = form_data.get("brood_patch")

    male_bp_viability = not SPECIES[species_number]["sexing_criteria"]["female_by_BP"]
    has_bp = brood_patch not in [None, 0]

    if (has_bp and not male_bp_viability):
        raise ValidationError(
            {
                "sex": "Males of this species should not have brood patches. Could this be juv?"
            }
        )

def validate_wrp_to_molt_score(form_data: dict):
    if 'P' not in form_data.get("age_WRP"):
        return
    
    body_molt = form_data.get("body_molt")
    ff_molt = form_data.get("ff_molt")

    has_molt_score = body_molt not in [None, 0] or ff_molt not in [None, 0]

    if not has_molt_score:
        raise ValidationError(
            {
                "age_WRP": 
                "The WRP code indicates this bird is molting, please indicate so in the body molt or flight feather molt scores"
            }
        )
    
def validate_molt_presence_in_wrp_code(form_data: dict):
    body_molt = form_data.get("body_molt")
    ff_molt = form_data.get("ff_molt")
    wrp_code = form_data.get("age_WRP")

    # Check if there's a molt score indicated without 'P' in the WRP code
    molt_indicated = (body_molt not in [None, 0]) or (ff_molt not in [None, "N", "A"])
    p_not_in_wrp = 'P' not in wrp_code

    if molt_indicated and p_not_in_wrp:
        raise ValidationError({
            "age_WRP": "A molting score is indicated but the WRP code does not contain 'P'. Please correct the WRP code."
        })
  

class CaptureRecordFormValidator(FormValidator):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validators = [
            validate_how_aged_by_plumage,
            validate_juv_aging_plumage_not_p,
            validate_skull_provided_if_aged_by_skull,
            validate_skull_score_for_adults,
            validate_skull_score_not_valid_for_hy_or_local,
            validate_wrp_allowed_for_species,
            validate_female_how_sexed,
            validate_male_how_sexed,
            validate_cloacal_protuberance_filled_if_sexed_by_cp,
            validate_species_brood_patch_sexing_for_females,
            validate_cloacal_protuberance_none_or_zero_for_females,
            validate_brood_patch_indication_to_score,
            validate_appropriate_male_bp_score,
            validate_wrp_to_molt_score,
            validate_molt_presence_in_wrp_code,
        ]
