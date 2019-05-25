from modules.obj_in_lab.obstacle import Obstacle
import sys

class MacGyver(Obstacle) :
    """Obstacle are objets that you can find in the laby"""

    name = "MacGiver"
    symbol = "X"

    def __init__(self, obstacles):
        self.x, self.y = self.get_random(obstacles)

    def _check_mvt_possible(self, coordinate, obstacles):
        if coordinate not in obstacles.keys():
            can_pass = True
        else :
            can_pass = False
        return can_pass


    def mg_movement (self, obstacles,mac_gyver) :
        """ Ask a direction to move Mac Gyver"""

        begin_x = mac_gyver.x
        begin_y = mac_gyver.y


        coordinates = (begin_x, begin_y)
        print("Where {} has to go ?\n".format(mac_gyver),\
                "> North(N),South(S), East(E), West(W).\n > Finish(F) ")
        del obstacles[coordinates]

        print("coordinates : ", type(coordinates))
        print("obstacles : ", type(obstacles))

        direction = ""
        while True :
            direction = input(">")
            if direction not in ("N", "S", "E", "W", "F") :
                print("'N','S','E','W' or 'F'")
                continue
            elif direction == "N" :
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
            elif direction == "F" :
                sys.exit()
            new_coordinates = mac_gyver.x, mac_gyver.y
            can_pass = self._check_mvt_possible(new_coordinates, obstacles)
            if can_pass :
                obstacles[new_coordinates] = mac_gyver
                print("return un ", type(obstacles))
                return obstacles, mac_gyver
            else :
                print("You can't go, there is a wall ! ")




    def __repr__(self):
        return "<{name}>".format(name=self.name)

    def __str__(self):
        return "{name} ({x}.{y})".format(name=self.name, x=self.x, y=self.y)
