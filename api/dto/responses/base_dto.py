from dataclasses import fields, dataclass


@dataclass
class BaseDto:
    #ignore unknown fields
    @classmethod
    def from_json(cls, data: dict):
        allowed = {f.name for f in fields(cls)}
        filtered = {k: v for k, v in data.items() if k in allowed}
        return cls(**filtered)