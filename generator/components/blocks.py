from dataclasses import dataclass
from abc import ABC, abstractmethod


class Statement(ABC):
    pass


@dataclass
class Blocks:
    for_block: Statement
    if_block: Statement
    def_block: Statement
    # with_block: Statement
