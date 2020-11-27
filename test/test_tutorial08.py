import pytest
from exercises.bubbles import *


class TestBubble:

    def test_bubble_constructor(self):
        try:
            ball = Bubble(100, 100, (200, 200, 200))
            box = Box(100, 100, 600, 600, 800, 800)
        except:
            pytest.fail("Looks like the constructors have not been properly implemented yet.")
            return None


class TestBebble:

    def test_bebble_constructor(self):
        try:
            ball = Bebble(100, 100)

        except:
            pytest.fail(
                "Looks like the constructor of 'Bebble' has not been properly implemented yet.\n It should take "
                "exactly two parameters, x and y.")
            return None


class TestBobble:

    def test_bobble_constructor(self):
        try:
            ball = Bobble(100, 100)
        except:
            pytest.fail(
                "Looks like the constructor of 'Bobble' has not been properly implemented yet.\n It should take "
                "exactly two parameters, x and y.")
            return None
