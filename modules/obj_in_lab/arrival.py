from  modules.obj_in_lab.obstacle import  Obstacle

class Arrival(Obstacle) :
    """Obstacle are objets that you can find in the laby"""

    name = "arrival"
    can_pass = True
    symbol = "U"

