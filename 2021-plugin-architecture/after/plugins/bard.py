'''Game extension for a bard character''' 

from dataclasses import dataclass
from game import factory 


@dataclass
class Bard():
    name: str 
    instrument: str 

    def make_a_noise(self) -> None:
        print(f'Bard {self.name} is playing the {self.instrument} ')


def register() -> None: 
    factory.register('bard', Bard)