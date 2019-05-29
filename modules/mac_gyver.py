import sys
from modules.obj_in_lab.obstacle import Obstacle
from  modules.obj_in_lab.needle import Needle
from  modules.obj_in_lab.pipe import Pipe
from  modules.obj_in_lab.ether import Ether


class MacGyver(Obstacle) :
    """Obstacle are objets that you can find in the laby"""

    name = "MacGiver"
    symbol = "X"
    pix = "res/mac_gyver.png"

    def __init__(self, obstacles):
        self.x, self.y = self.get_random(obstacles)
        self.inventory = []

    def check_victory(self, inventory):
        if len(inventory) == 3 :
            print("Congratulation you can go out :) ! ")
            sys.exit()
        else :
            print("The gate keeper saw you and killed you. Game over :( ! ")
            sys.exit()

    def _check_environnement(self, coordinates, obstacles):

        item = obstacles[coordinates].name

        if item == "Obstacle" :
            can_pass = True
        else :
            if item == "Wall" :
                can_pass = False
            elif item == "Arrival" :
                self.check_victory(self.inventory)
            else :
                self.inventory.append(item)
                can_pass = item
        return can_pass


    def mg_movement (self, direction, mac_gyver, obstacles) :
        """ Ask a direction to move Mac Gyver"""

        begin_x, begin_y = mac_gyver.x, mac_gyver.y

        coordinates = (begin_x, begin_y)

        # print("coordinates : ", type(coordinates))
        # print("obstacles : ", type(obstacles))

        if direction == "N" :
            mac_gyver.x = begin_x
            mac_gyver.y = begin_y -1
        elif direction == "S" :
            mac_gyver.x = begin_x
            mac_gyver.y = begin_y + 1
        elif direction == "W" :
            mac_gyver.x = begin_x - 1
            mac_gyver.y = begin_y
        elif direction == "E" :
            mac_gyver.x = begin_x + 1
            mac_gyver.y = begin_y

        new_coordinates = mac_gyver.x, mac_gyver.y
        can_pass = self._check_environnement(new_coordinates, obstacles)
        if can_pass :
            del obstacles[coordinates]
            obstacles[new_coordinates] = mac_gyver
            obstacles[coordinates] = Obstacle
            if can_pass in ("Needle", "Pipe", "Ether"):
                can_pass = can_pass.lower()
                return obstacles, mac_gyver, can_pass
            return obstacles, mac_gyver
        else :
            print("MG : I can't go, there is a wall ! ")
            mac_gyver.x, mac_gyver.y = begin_x, begin_y

            return False




    def __repr__(self):
        return "<{name}>".format(name=self.name)

    def __str__(self):
        return "{name} ({x}.{y})".format(name=self.name, x=self.x, y=self.y)
