''' factory to load game character, 

given a str, should load the corresponding class, 
register(), unregister(), create()
'''

from typing import Callable, Any, Dict
from game.character import GameCharacter


character_creation_funcs : Dict[str, Callable[..., GameCharacter]] = {} 


def register(character_type: str, creator_fn: Callable[..., GameCharacter]) ->None:
    ''' register a character from plugin'''
    character_creation_funcs[character_type] = creator_fn 


def unregister(character_type) -> None:
    '''unregister a character'''
    character_creation_funcs.pop(character_type, None )


def create(arguments: Dict[str, Any]) -> GameCharacter:
    '''create a game character given a JSON data''' 
    args_copy = arguments.copy() 

    character_type = args_copy.pop("type")
    try:
        creator_fn = character_creation_funcs[character_type]
    except KeyError:
        raise ValueError(f"unknow character type {character_type!r}") from None 
    return creator_fn(**args_copy)