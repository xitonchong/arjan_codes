'''A simple plugin loader '''


import importlib 
from typing import List 
from game import factory 
from dataclasses import dataclass



'''default characters ''' 
@dataclass
class Sorcerer():
    name: str 

    def make_a_noise(self) -> None:
        print(f"{self.name} Aaarrrrrgggghhhh")


@dataclass
class Witcher:
    name: str 

    def make_a_noise(self) -> None: 
        print(f"I am the Witcher {self.name} ")



@dataclass
class Wizard:
    name: str 

    def make_a_noise(self) -> None: 
        print(f"I am the wizard {self.name}")



class ModuleInterface:
    '''represents a plugin interface. A plugin has a single register function'''

    @staticmethod 
    def register(): # this does not enforce checking on the object 
        '''register the character in the game factory'''


def import_module(name: str) -> ModuleInterface:
    '''import package.file from a str path''' 
    return importlib.import_module(name) 


def load_plugin(plugins: List[str]) -> None: 
    """load the plugins defined in the plugin list: plugins.bard """ 
    for plugin_file in plugins: 
        plugin = import_module(plugin_file)
        plugin.register() 

    factory.register("wizard", Wizard)
    factory.register("witcher", Witcher)
    factory.register("sorcerer", Sorcerer)