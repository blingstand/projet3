from modules.obj_in_lab.obstacle import Obstacle
import sys

class MacGyver(Obstacle) :
    """Obstacle are objets that you can find in the laby"""

    name = "MacGiver"
    symbol = "X"

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

    def _check_environnement(self, coordinate, obstacles):
        if coordinate not in obstacles.keys():
            can_pass = True
        else :
            item = obstacles[coordinate].name
            if item == "Wall" :
                can_pass = False
            elif item == "Arrival" :
                self.check_victory(self.inventory)
            else :
                self.inventory.append(item)
                can_pass = True
        return can_pass


    def mg_movement (self, obstacles,mac_gyver) :
        """ Ask a direction to move Mac Gyver"""

        begin_x = mac_gyver.x
        begin_y = mac_gyver.y


        coordinates = (begin_x, begin_y)
        del obstacles[coordinates]

        # print("coordinates : ", type(coordinates))
        # print("obstacles : ", type(obstacles))

        direction = ""
        while True :

            print("*"*55)
            if len(self.inventory) == 0:
                print("MG : I need to find how to go out !")
            elif 1 <= len(self.inventory) < 3 :
                print("Inventory : ", self.inventory)
            elif len(self.inventory) == 3:
                print("MG : I can go out ! ")
            direction = input(">")


            if direction not in ("Z", "S", "D", "Q", "F") :
                print("Where {} has to go ?\n".format(mac_gyver),\
                "> North(Z),South(S), East(D), West(Q).\n > Finish(F) ")
                continue
            elif direction == "Z" :
                mac_gyver.x = begin_x
                mac_gyver.y = begin_y -1
            elif direction == "S" :
                mac_gyver.x = begin_x
                mac_gyver.y = begin_y + 1
            elif direction == "Q" :
                mac_gyver.x = begin_x - 1
                mac_gyver.y = begin_y
            elif direction == "D" :
                mac_gyver.x = begin_x + 1
                mac_gyver.y = begin_y
            elif direction == "F" :
                sys.exit()

            new_coordinates = mac_gyver.x, mac_gyver.y
            can_pass = self._check_environnement(new_coordinates, obstacles)
            if can_pass :
                obstacles[new_coordinates] = mac_gyver
                return obstacles, mac_gyver
            else :
                print("MG : I can't go, there is a wall ! ")




    def __repr__(self):
        return "<{name}>".format(name=self.name)

    def __str__(self):
        return "{name} ({x}.{y})".format(name=self.name, x=self.x, y=self.y)
