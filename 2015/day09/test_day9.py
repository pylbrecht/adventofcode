from day9 import calc_possible_routes, build_graph

import pytest


@pytest.fixture
def distances():
    return [
        "London to Dublin = 464",
        "London to Belfast = 518",
        "Dublin to Belfast = 141",
    ]


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


def test_build_graph(distances):
    expected_graph = {
        ("London", "Dublin"): 464,
        ("Dublin", "London"): 464,
        ("London", "Belfast"): 518,
        ("Belfast", "London"): 518,
        ("Dublin", "Belfast"): 141,
        ("Belfast", "Dublin"): 141,
    }

    graph = build_graph(distances)

    assert graph == expected_graph
