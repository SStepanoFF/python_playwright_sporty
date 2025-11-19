from dataclasses import dataclass

from api.dto.responses.base_dto import BaseDto


@dataclass
class WeightDto(BaseDto):
    imperial: str
    metric: str

    # @staticmethod
    # def from_json(data: dict):
    #     allowed = {f.name for f in WeightDto.__dataclass_fields__.values()}
    #     filtered = {k: v for k, v in data.items() if k in allowed}
    #     return WeightDto(**filtered)