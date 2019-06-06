
from modules.obj_in_lab.obstacle import Obstacle
from  modules.obj_in_lab.needle import Needle
from  modules.obj_in_lab.pipe import Pipe
from  modules.obj_in_lab.ether import Ether


class MacGyver(Obstacle):
    """Obstacle are objets that you can find in the laby"""

    name = "MacGiver"
    symbol = "X"
    pix = "data/mac_gyver.png"

    def __init__(self, obstacles):
        self.x, self.y = self.get_random(obstacles)
        self.inventory = []
        self.can_finish = False
        self.victory = None


    def mg_movement(self, direction, mac_gyver, obstacles):
        """ Ask a direction to move Mac Gyver"""

        begin_abs, begin_ord = mac_gyver.x, mac_gyver.y

        coordinates = (begin_abs, begin_ord)

        if direction == "N":
            mac_gyver.x = begin_abs
            mac_gyver.y = begin_ord - 1
        elif direction == "S":
            mac_gyver.x = begin_abs
            mac_gyver.y = begin_ord + 1
        elif direction == "W":
            mac_gyver.x = begin_abs - 1
            mac_gyver.y = begin_ord
        elif direction == "E":
            mac_gyver.x = begin_abs + 1
            mac_gyver.y = begin_ord

        new_coordinates = mac_gyver.x, mac_gyver.y
        item = obstacles[new_coordinates] #item = object that will change place with mg or not, depend on class
        #can_pass contains :
        if item.name == "Wall" :
            mac_gyver.x, mac_gyver.y = begin_abs, begin_ord
            return False, None, None, None #a function always returns the same objet, here a tuple with 4 slots

        else :
            del obstacles[coordinates]
            obstacles[new_coordinates] = mac_gyver
            obstacles[coordinates] = Obstacle
            name_item = False
            if item.name in ("Needle", "Pipe", "Ether"):
                name_item = item.name.lower() # I need needle, pipe or ether
                self.inventory.append(item)
            elif item.name == "Arrival":
                name_item = item.name.lower()
            return True, obstacles, mac_gyver, name_item




    def __repr__(self):
        return "<{name}>".format(name=self.name)

    def __str__(self):
        return "{name} ({x}.{y})".format(name=self.name, x=self.x, y=self.y)
