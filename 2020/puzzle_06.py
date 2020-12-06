from typing import List
from dataclasses import dataclass
import sys


@dataclass
class Person:
    questions: str


@dataclass
class Group:
    people: List[Person]

    @property
    def questions(self) -> List[str]:
        return [person.questions for person in self.people]

    def any_yes(self) -> int:
        questions = set(''.join(self.questions))
        return len(questions)

    def all_yes(self) -> int:
        questions = [set(question) for question in self.questions]
        return len(set.intersection(*questions))


def create_groups(puzzle_input: str) -> List[Group]:
    groups = []
    for group in puzzle_input.split("\n\n"):
        people = [Person(questions=''.join(questions)) for questions in group.split("\n")]
        groups.append(Group(people=people))

    return groups


if __name__ == "__main__":
    puzzle_input = sys.stdin.read().strip()

    groups = create_groups(puzzle_input)

    print(sum([group.any_yes() for group in groups]))
    print(sum([group.all_yes() for group in groups]))
