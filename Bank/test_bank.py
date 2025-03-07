# This file test for the function in bank.py file where function takes the greeting and rate as per the freeting 
import pytest
from bank import value

def test_hello():
    assert value("Hello") == 0
    assert value("hello there") == 0
    assert value("HELLO") == 0

def test_h_start():
    assert value("Hi") == 20
    assert value("Hey there!") == 20
    assert value("Hola!") == 20

def test_other_greetings():
    assert value("Good morning") == 100
    assert value("What's up?") == 100
    assert value("Greetings") == 100

def test_case_insensitivity():
    assert value("hElLo") == 0
    assert value("HeLLo and welcome") == 0
    assert value("hI") == 20

def test_edge_cases():
    assert value("h") == 20
    assert value("hooray!") == 20
    assert value("random text") == 100
