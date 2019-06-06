from modules.obj_in_lab.obstacle import Obstacle

class Item(Obstacle) :
    """Needle is one of the objet mac_gyver has to pick in the labyrinthe
        (not Arya's sword this time)
    """

    name = ""
    symbol = ""
    pix = "data/box.png"

    def __init__(self, obstacles):
        self.x, self.y = self.get_random(obstacles)
