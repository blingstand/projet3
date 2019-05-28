from modules.obj_in_lab.obstacle import Obstacle

class Needle(Obstacle) :
    """Needle is one of the objet mac_gyver has to pick in the labyrinthe
        (not Arya's sword this time)
    """

    name = "Needle"
    symbol = "N"
    pix = "res/box.png"

    def __init__(self, obstacles, *obstacles_added):
        self.x, self.y = self.get_random(obstacles, *obstacles_added)

