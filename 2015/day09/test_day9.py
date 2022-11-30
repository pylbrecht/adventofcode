from day9 import calc_shortest_route, calc_possible_routes

import pytest


@pytest.fixture
def distances():
    return [
        "London to Dublin = 464",
        "London to Belfast = 518",
        "Dublin to Belfast = 141",
    ]


def test_shortest_distance(distances):
    assert calc_shortest_route(distances) == "London -> Dublin -> Belfast = 605"


def test_possible_routes(distances):
    possible_routes = [
        "Dublin -> London -> Belfast = 982",
        "London -> Dublin -> Belfast = 605",
        "London -> Belfast -> Dublin = 659",
        "Dublin -> Belfast -> London = 659",
        "Belfast -> Dublin -> London = 605",
        "Belfast -> London -> Dublin = 982",
    ]
    assert sorted(calc_possible_routes(distances)) == sorted(possible_routes)
