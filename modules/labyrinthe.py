#labyrinthe

from modules.obj_in_lab.wall import Wall
from modules.obj_in_lab.arrival import Arrival
from modules.obj_in_lab.obstacle import Obstacle


class Labyrinthe():
    """Create the Labyrinthe object"""

    #size of my laby 15*15
    limite_x = 15
    limite_y = 15
    liste_3_objects=[]

    def __init__(self, obstacles):
        """the Labyrinthe is composed by obstacles and MacGiver """

        self.nom = "Labyrinthe MacGyver"
        self.grid = {}
        for obstacle in obstacles :
            self.grid[obstacle.x, obstacle.y] = obstacle
        # self.mac_gyver =

    def __repr__(self):
        return "Bienvenu dans le {}".format(self.nom)

    def __str__(self):
        return "Bienvenu dans le {}".format(self.nom)

    def display_laby(self, obstacles):
        """ Display the laby object according to x and y properties"""

        y = 1
        grid = "\n\n\n\n\n\n\n\t\t"
        while y <= self.limite_y :
            #début de ligne
            x = 1
            while x <=  self.limite_x :
                try :
                    grid += obstacles[x,y].symbol
                except :
                    finish = False
                    for coordinate in obstacles:
                        if (x,y) == coordinate[0:2] :
                            grid += coordinate[2].symbol
                            finish = True
                    if not finish :
                        grid += " "
                x += 1
            #fin de ligne,
            grid += "\n\t\t"
            y += 1
        grid += "\n\n\n"
        return grid



def from_content_to_lab(content):
    """Take a content and return a my_lab object.

    1/ create a list of obstacles
    2/ init a x = 0 and y = 0
    3/ for each letter of content create an object 'obstacle' accoding to symbols' letter
    4/ for each new letter x+=1 except '\n' x=0 y+=1
    5/ append the object in the list_obstacles
    """

    list_obstacles = []

    symbols = {
            "0": Wall,
            "U": Arrival
        }

    x = 1
    y = 1

    for letter in content :
        if letter == "\n" :
            x = 1
            y += 1
            continue
        elif letter == " ":
            pass
        elif letter in symbols:
            classe = symbols[letter]
            my_object = classe(x, y)
        else :
            pass #penser à coder une erreur

        list_obstacles.append(my_object)
        x += 1

    my_lab = Labyrinthe(list_obstacles)

    return my_lab


