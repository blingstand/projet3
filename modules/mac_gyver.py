from random import choice
class MacGiver() :
    """Obstacle are objets that you can find in the laby"""

    name = "MacGiver"
    symbol = "X"
    x_max = 15
    y_max = 15

    def __init__(self, obstacles):
        self.x, self.y = self.get_random(obstacles)


    def get_random(self, obstacles) :
        """ From a list of coordinate(tuple), the function choose with random module, one of them)

        1/ Create the list of coordinate from chain where letter == ""
        2/ Choose a tuple from this list
        3/ Return it
        """
        x = 1
        y = 1

        y = 1
        list_tuples = []
        while y <= self.y_max :
            #début de ligne
            x = 1
            while x <=  self.x_max :
                try :
                    obstacles[x,y] in obstacles
                    pass

                except :
                    list_tuples.append((x,y))
                x += 1
            y += 1

        coordinate = choice(list_tuples)
        return coordinate



    def __repr__(self):
        return "<{name} (x={x}, y={y})>".format(name=self.name,
                x=self.x, y=self.y)

    def __str__(self):
        return "{name} ({x}.{y})".format(name=self.name, x=self.x, y=self.y)
