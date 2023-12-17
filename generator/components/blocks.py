from dataclasses import dataclass
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

    @property
    @classmethod
    def fields(cls):
        return fields(cls)
