from pydantic import BaseModel
from dataclasses import dataclass, fields

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

    @property
    @classmethod
    def fields(cls):
        return fields(cls)
