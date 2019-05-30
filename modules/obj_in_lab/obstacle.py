from random import choice
class Obstacle:
    """Represent all the obstacles in the labyrinthe. """

    name = "Obstacle"
    symbol = " "
    pix = "res/ground.png"
    x_max = 15
    y_max = 15

    def __init__(self, x, y):
        """initiate the coordinate of the obstacle"""

        self.x = x
        self.y = y

    def get_random(self, obstacles):
        """ From a list of coordinate(tuple), the function choose with random module, one of them)

        1/ Create the list of coordinate from chain where letter == ""
        2/ Choose a tuple from this list
        3/ Return it
        """

        x = 1
        y = 1
        list_tuples = []
        while y <= self.y_max:
            #début de ligne
            x = 1
            while x <=  self.x_max:
                if obstacles[x,y].name == "Obstacle":
                    list_tuples.append((x,y))
                x += 1
            y += 1
        coordinate = choice(list_tuples)
        return coordinate


    def __repr__(self):
        return "<{name}>".format(name=self.name)

    def __str__(self):
        return "{name} ({x}.{y})".format(name=self.name, x=self.x, y=self.y)
