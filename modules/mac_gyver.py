from modules.obj_in_lab.obstacle import Obstacle
import os

class MacGyver(Obstacle) :
    """Obstacle are objets that you can find in the laby"""

    name = "MacGiver"
    symbol = "X"

    def __init__(self, obstacles):
        self.x, self.y = self.get_random(obstacles)

    def _check_mvt_possible(self, coordinate, obstacles):
        if coordinate not in obstacles.keys():
            can_pass = True
            print("can_pass : ", can_pass)
            return can_pass


    def mg_movement (self, obstacles) :
        """ Ask a direction to move Mac Gyver"""

        direction = input(">")
        can_pass = False
        while can_pass == False and direction not in ("N", "S", "E", "O") :
            print("Aide : Précisez où Mac Gyver doit aller....\n\
             > Nord(N),\n > Sud(S),\n > Est(E),\n > Ouest(O).")
            direction = input(">")
            if direction == "N" :
                self.y += 1
            elif direction == "S" :
                self.y -= 1
            elif direction == "O" :
                self.x -= 1
            elif direction == "E" :
                self.x += 1
            coordinate = self.x, self.y
            print(coordinate)
            can_pass = self._check_mvt_possible(coordinate, obstacles)


    def __repr__(self):
        return "<{name} (x={x}, y={y})>".format(name=self.name,
                x=self.x, y=self.y)

    def __str__(self):
        return "{name} ({x}.{y})".format(name=self.name, x=self.x, y=self.y)
