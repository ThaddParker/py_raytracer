"""Light class for providing illumination to a sceen"""
from utils.color import Colors
from utils.vector import Vector


class Light:
    """ Basic light with an origin (where its is located) with what color it is emitting"""

    def __init__(self, origin = Vector(0,0,0), color=Colors.White) -> None:
        """Default camera that is located at <0,0,0> and is a white color"""
        self.origin = origin
        self.color = color
