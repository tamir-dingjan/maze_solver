class Point:
    """
    Stores the X and Y values that identify a point on the screen.

    X=0 is the left of the screen.
    Y=0 is the top of the screen.

    Attributes:
        x (int): The horizontal coordinate of the point.
        y (int): The vertical coordinate of the point.
    """

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
