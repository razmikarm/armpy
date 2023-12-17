from pydantic import BaseModel
from dataclasses import dataclass, fields, asdict

@dataclass
class Functions:
    input: str
    print: str
    int: str
    str: str
    float: str
    set: str
    list: str
    dict: str
    range: str
    sorted: str
    max: str
    min: str
    sum: str
    round: str

    @classmethod
    def get_fields(cls):
        return fields(cls)

    def items(self):
        return asdict(self).items()
