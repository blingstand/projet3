from modules.obj_in_lab.obstacle import Obstacle

class MacGiver(Obstacle) :
    """Obstacle are objets that you can find in the laby"""

    name = "MacGiver"
    symbol = "X"

    def __init__(self, obstacles):
        self.x, self.y = self.get_random(obstacles)


    def __repr__(self):
        return "<{name} (x={x}, y={y})>".format(name=self.name,
                x=self.x, y=self.y)

    def __str__(self):
        return "{name} ({x}.{y})".format(name=self.name, x=self.x, y=self.y)
