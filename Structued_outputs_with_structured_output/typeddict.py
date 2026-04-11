from typing import TypeDict

class Person(TypeDict):
    name: str
    age: int


newperson: Person = {"name": "Alice", "age": 30}


print(newperson)

