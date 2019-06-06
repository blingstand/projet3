from  modules.obj_in_lab.item import Item

class Needle(Item) :
    """Needle is one of the objet mac_gyver has to pick in the labyrinthe
        (not Arya's sword this time)
    """

    name = "Needle"
    symbol = "N"

    def __init__(self, obstacles):
        self.x, self.y = self.get_random(obstacles)

