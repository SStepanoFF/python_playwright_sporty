from dataclasses import dataclass, field
from typing import List, Dict, Optional

from api.dto.responses.base_dto import BaseDto
from api.dto.responses.breed_dto import BreedDto

@dataclass
class CatImage(BaseDto):
    id: str
    url: str
    width: int
    height: int
    breeds: List[BreedDto] = field(default_factory=list)
    favourite: Dict = field(default_factory=dict)

    @classmethod
    def from_json(cls, data: dict):
        data = dict(data)
        data["breeds"] = [BreedDto.from_json(b) for b in data.get("breeds", [])]
        return super().from_json(data)
