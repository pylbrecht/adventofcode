from collections import defaultdict
from typing import NamedTuple


class Node(NamedTuple):
    city: str
    distance: int


def build_graph(distance_definitions: list[str]) -> dict[str, set[Node]]:
    graph = defaultdict(set)
    for definition in distance_definitions:
        cities, distance = definition.split("=")

        src, dst = cities.split("to")
        distance = int(distance.strip())

        graph[src.strip()].add(Node(dst.strip(), distance))
        graph[dst.strip()].add(Node(src.strip(), distance))

    return graph


def calc_shortest_route(distances: list[str]) -> str:
    raise NotImplementedError


def calc_possible_routes(distances: list[str]) -> list[str]:
    raise NotImplementedError
