import sys
from itertools import permutations
from typing import Iterator


Graph = dict[tuple[str, str], int]


def build_graph(distance_definitions: list[str]) -> Graph:
    graph = {}
    for definition in distance_definitions:
        src, _, dst, _, distance = definition.split()
        graph[(src, dst)] = int(distance)
        graph[(dst, src)] = int(distance)

    return graph


def calc_possible_routes(distances: list[str]) -> Iterator[str]:
    graph = build_graph(distances)
    places = {cities[0] for cities in graph}

    for route in permutations(places):
        total_distance = sum(map(lambda src, dst: graph[(src, dst)], route[:-1], route[1:]))
        yield " -> ".join(route) + f" = {total_distance}"


if __name__ == "__main__":
    input_ = [line.strip() for line in sys.stdin.read().split("\n") if line]
    possible_routes = calc_possible_routes(input_)

    distances = [int(route.split()[-1]) for route in possible_routes]

    print(min(distances))
    print(max(distances))
