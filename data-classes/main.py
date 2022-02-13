#https://www.youtube.com/watch?v=vRVVyl9uaZc&t=43s&ab_channel=ArjanCodes



from dataclasses import dataclass, field


## adding decorator simplify init 
@dataclass(order=True, frozen=True)
class Person:
    sort_index: int = field(init=False, repr=False)
    name: str
    age: int
    job: str
    strength: int = 100

    def __post_init__(self):
        #self.sort_index = self.age # cannot assing if frozen is True, instead use setattr method
        object.__setattr__(self, 'sort_index', self.strength)


    def __str__(self):
        return f'{self.name}, {self.job}, {self.age}'


person1 = Person('gerall', 'witcher', 3, 99)
person2 = Person("yennefer", 'sorceress', 25)
person3 = Person("yennefer", 'sorceress', 25)

try:
    person2.age = 12
except:
    print("cannto assign value to atrributes if frozen is set")


print(id(person2))
print(id(person3))
print(person1)


print(person1 > person2)