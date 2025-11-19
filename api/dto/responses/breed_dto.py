from dataclasses import dataclass

from api.dto.responses.base_dto import BaseDto
from api.dto.responses.weight_dto import WeightDto


@dataclass
class BreedDto(BaseDto):
    weight: WeightDto
    id: str
    name: str
    temperament: str
    origin: str
    country_codes: str
    country_code: str
    description: str
    life_span: str
    indoor: int
    lap: int
    adaptability: int
    affection_level: int
    child_friendly: int
    dog_friendly: int
    energy_level: int
    grooming: int
    health_issues: int
    intelligence: int
    shedding_level: int
    social_needs: int
    stranger_friendly: int
    vocalisation: int
    experimental: int
    hairless: int
    natural: int
    rare: int
    rex: int
    suppressed_tail: int
    short_legs: int
    hypoallergenic: int
    reference_image_id: str

    # Optional fields (can be empty string)
    vetstreet_url: str = ""
    alt_names: str = ""
    wikipedia_url: str = ""

    @classmethod
    def from_json(cls, data: dict):
        data = dict(data)
        data["weight"] = WeightDto.from_json(data.get("weight", {}))
        return super().from_json(data)