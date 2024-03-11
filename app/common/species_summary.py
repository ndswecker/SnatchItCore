from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class SpeciesSummary:
    common_name: str = ""
    scientific_name: str = ""
    alpha_code: str = ""
    species_number: int = 0
    band_sizes: List[str] = field(default_factory=list)
    wing_chord_range: List[int] = field(default_factory=lambda: [0, 0])
    WRP_groups: List[int] = field(default_factory=list)
    sexing_criteria: Dict[str, bool] = field(default_factory=dict)
    pyle_second_edition_page: int = 0

    def __init__(self, species_data: Dict):
        self.common_name = species_data.get("common_name", "")
        self.scientific_name = species_data.get("scientific_name", "")
        self.alpha_code = species_data.get("alpha_code", "")
        self.species_number = species_data.get("species_number", 0)
        self.band_sizes = species_data.get("band_sizes", [])
        self.wing_chord_range = species_data.get("wing_chord_range", [])
        self.WRP_groups = species_data.get("WRP_groups", [])
        self.sexing_criteria = species_data.get("sexing_criteria", {})
        self.pyle_second_edition_page = species_data.get("pyle_second_edition_page", 0)

    def generate_html_snippet(self) -> str:
        # Determine the display for plumage dimorphism based on its value
        if self.sexing_criteria.get('plumage_dimorphism'):
            plumage_dimorphism_display = "<strong>Sex:</strong> &female;&ne;&male; (dimorphic)"
        else:
            plumage_dimorphism_display = "<strong>Sex:</strong> &female;=&male;"

        # Construct the HTML snippet with the updated plumage dimorphism display
        html_snippet = f"""
        <strong>Common Name:</strong> {self.common_name}<br>
        <strong>Scientific Name:</strong> {self.scientific_name}<br>
        <strong>Alpha Code:</strong> {self.alpha_code}<br>
        <strong>Band Sizes:</strong> {', '.join(self.band_sizes)}<br>
        <strong>Wing Chord Range:</strong> {self.wing_chord_range[0]} - {self.wing_chord_range[1]}<br>
        <strong>WRP Groups:</strong> {', '.join(map(str, self.WRP_groups))}<br>
        {plumage_dimorphism_display}<br>
        <strong>Sexing Criteria:</strong> <br>
        Female by BP: {'Yes' if self.sexing_criteria.get('female_by_BP') else 'No'}<br>
        Male by CP: {'Yes' if self.sexing_criteria.get('male_by_CP') else 'No'}<br>
        <strong>Pyle Second Edition Page:</strong> {self.pyle_second_edition_page}
        """
        return html_snippet


