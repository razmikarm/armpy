from dataclasses import dataclass, fields, asdict
from abc import ABC, abstractmethod


class Statement(ABC):
    pass


@dataclass
class Blocks:
    if_block: Statement
    while_block: Statement
    for_block: Statement
    def_block: Statement
    # with_block: Statement

    @classmethod
    def get_fields(cls):
        return fields(cls)

    def items(self):
        return asdict(self).items()
