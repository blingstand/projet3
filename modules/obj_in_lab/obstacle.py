from random import choice
class Obstacle:
    """Represent all the obstacles in the labyrinthe. """

    name = "Obstacle"
    symbol = " "
    pix = "data/ground.png"
    x_max = 15
    y_max = 15

    def __init__(self, x, y):
        """initiate the coordinate of the obstacle"""

        self.x = x
        self.y = y

    def get_random(self, obstacles):
        """ From a list of coordinate(tuple), the function choose with random module, one of them)

        1/ Create the list of Obstacles objects
        2/ Choose a tuple from this list
        3/ Return it
        """
        list_tuples = []

        for cle in obstacles :
            if obstacles[cle].name == "Obstacle":
                list_tuples.append((obstacles[cle].x, obstacles[cle].y))


        coordinate = choice(list_tuples)
        return coordinate


    def __repr__(self):
        return "<{name}>".format(name=self.name)

    def __str__(self):
        return "{name} ({x}.{y})".format(name=self.name, x=self.x, y=self.y)
