'''represents a basic game character''' 
from typing import Protocol 



class GameCharacter(Protocol):
    ''' implement game character must-have function'''


    def make_a_noise(self):
        ''' let the character make a noise'''


