'''basic example showing how to create objects from data using a dynamic factory
with reigster/unregister methods.
'''

from dataclasses import dataclass
from game import loader, factory 
import json 


def main():
    '''create game characters from a file containing a level definition'''

    with open("./level.json") as file:
        data = json.load(file)

        loader.load_plugin(data['plugins'])

        # create the characters 
        characters = [factory.create(item) for item in data['characters']]

        for character in characters:
            character.make_a_noise() 



if __name__ == '__main__':
    main() 



