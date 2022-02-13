import json
from typing import List 

from dataclasses import dataclass


from game.character import GameCharacter



@dataclass 
class Sorcerer:
    name: str

    def make_a_noise(self) -> None:
        print("Aaarrrrgg")



@dataclass
class Wizard:
    name: str

    def make_a_noise(self) -> None:
        print("Booh")



@dataclass
class Witcher:
    name: str 


    def make_a_noise(self) -> None:
        print("Hhhmmmmm")


def main():

    with open("level.json") as file:
        data = json.load(file)


    # create the characters
    characters : List[GameCharacter] = []

    for item in data["characters"]:
        item_copy = item.copy()  # why copy is needed 
        character_type = item_copy.pop("type")
        if character_type == 'sorcerer':
            characters.append(Sorcerer(**item_copy))
        elif character_type == 'wizard':
            characters.append(Wizard(**item_copy))
        elif character_type == 'witcher':
            characters.append(Witcher(**item_copy))
        else:
            raise NotImplementedError(f"class is not impelemented: {character_type}")


    #print(data["characters"])
    # do something with the characters
    for character in characters:
        print(character, end='\t')
        character.make_a_noise()


if __name__ == '__main__':
    main() 