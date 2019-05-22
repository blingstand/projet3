from  modules.obj_in_lab.obstacle import  Obstacle

class Arrival(Obstacle) :
    """Obstacle are objets that you can find in the laby"""

    nom = "arrival"
    peut_traverser = True
    symbole = "U"

