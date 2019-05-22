import modules.obj_in_lab.obstacle as Obstacle

class Wall(Obstacle) :
    """Obstacle are objets that you can find in the laby"""

    nom = "wall"
    peut_traverser = False
    symbole = "0"
