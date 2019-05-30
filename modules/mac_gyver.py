import sys
from modules.obj_in_lab.obstacle import Obstacle
from  modules.obj_in_lab.needle import Needle
from  modules.obj_in_lab.pipe import Pipe
from  modules.obj_in_lab.ether import Ether


class MacGyver(Obstacle):
    """Obstacle are objets that you can find in the laby"""

    name = "MacGiver"
    symbol = "X"
    pix = "res/mac_gyver.png"

    def __init__(self, obstacles):
        self.x, self.y = self.get_random(obstacles)
        self.inventory = []


    def check_victory(self):
        """ Manage the victory

            According to the length of inventory and Mac Gyver position
            check_victory manage wether the game is won or lost
        """

        if len(self.inventory) == 3:
            print("Congratulation you can go out :) ! ")
            sys.exit()
        else:
            print("The gate keeper saw you and killed you. Game over :( ! ")
            sys.exit()


    def _check_environnement(self, coordinates, obstacles):
        """ return can_pass wether the item is not a wall, can manage victory """

        item = obstacles[coordinates].name

        if item == "Obstacle":
            can_pass = True

        else:
            if item == "Wall":
                can_pass = False
            elif item == "Arrival":
                self.check_victory()
            else:
                self.inventory.append(item)
                can_pass = item

        return can_pass


    def mg_movement(self, direction, mac_gyver, obstacles):
        """ Ask a direction to move Mac Gyver"""

        begin_abs, begin_ord = mac_gyver.x, mac_gyver.y

        coordinates = (begin_abs, begin_ord)

        if direction == "N":
            mac_gyver.x = begin_abs
            mac_gyver.y = begin_ord -1
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
        can_pass = self._check_environnement(new_coordinates, obstacles)
        if can_pass:
            del obstacles[coordinates]
            obstacles[new_coordinates] = mac_gyver
            obstacles[coordinates] = Obstacle
            if can_pass in ("Needle", "Pipe", "Ether"):
                can_pass = can_pass.lower()
                return obstacles, mac_gyver, can_pass
            return obstacles, mac_gyver
        else:
            print("MG : I can't go, there is a wall ! ")
            mac_gyver.x, mac_gyver.y = begin_abs, begin_ord

            return False


    def __repr__(self):
        return "<{name}>".format(name=self.name)

    def __str__(self):
        return "{name} ({x}.{y})".format(name=self.name, x=self.x, y=self.y)
