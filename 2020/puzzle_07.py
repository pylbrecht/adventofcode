import re
import sys
import pprint
from typing import List, Tuple, Optional, Dict


def build_graph(rules) -> Dict[str, List[Tuple[str, int]]]:
    graph = {}
    for rule in rules:
        parent, children = rule.split(' bags contain ')
        graph[parent] = []

        if children == 'no other bags.':
            continue

        pattern = re.compile(r"(?P<count>\d+) (?P<bag>.+) bag(s)?(\.)?")
        bags = []
        for bag_spec in children.split(', '):
            match = pattern.match(bag_spec);

            if not match:
                print(f"unknown bag spec: {repr(bag_spec)}")
                continue

            bag = match.group('bag')
            count = match.group('count')
            graph[parent].append((bag, int(count)))

    return graph


def contains_shiny_gold_bag(bag, graph):
    children = [bag for bag, _ in graph[bag]]

    if "shiny gold" in children:
        return True

    for child in children:
        if not contains_shiny_gold_bag(child, graph):
            continue
        return True

    return False


def total_number_of_bags(bag, graph):
    total = 0
    for child, count in graph[bag]:
        total += count
        total += count * total_number_of_bags(child, graph)

    return total


def part1(graph):
    count = 0
    for bag in graph:
        if not contains_shiny_gold_bag(bag, graph):
            continue
        count += 1

    return count


def part2(graph):
    return total_number_of_bags("shiny gold", graph)


if __name__ == "__main__":
    rules = [line.strip() for line in sys.stdin.readlines()]
    sys.stdin = open('/dev/tty')

    graph = build_graph(rules)

    print(part1(graph))
    print(part2(graph))
