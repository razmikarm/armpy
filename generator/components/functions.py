from pydantic import BaseModel
from dataclasses import dataclass

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