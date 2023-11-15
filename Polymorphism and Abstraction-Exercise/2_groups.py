from typing import List


class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other: 'Person'):
        return Person(name=self.name, surname=other.surname)


class Group:
    def __init__(self, name: str, people: List[Person]):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other: 'Group'):
        return Group(name=f"{self.name} {other.name}", people=self.people + other.people)

    def __repr__(self):
        return f"Group {self.name} with members {', '.join(repr(p) for p in self.people)}"

    def __getitem__(self, index: int):
        return f"Person {index}: {self.people[index]}"

