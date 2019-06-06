#labyrinthe

from  modules.mac_gyver import MacGyver
from  modules.obj_in_lab.needle import Needle
from  modules.obj_in_lab.pipe import Pipe
from  modules.obj_in_lab.ether import Ether
from modules.obj_in_lab.wall import Wall
from modules.obj_in_lab.arrival import Arrival
from modules.obj_in_lab.obstacle import Obstacle


class Labyrinthe():
    """Create the Labyrinthe object"""

    liste_3_objects = []

    def __init__(self, obstacles):
        """the Labyrinthe is composed by obstacles and MacGiver """

        self.nom = "Labyrinthe MacGyver"
        self.grid = {}
        for obstacle in obstacles:
            self.grid[obstacle.x, obstacle.y] = obstacle

    def __repr__(self):
        return "Bienvenu dans le {}".format(self.nom)

    def __str__(self):
        return "Bienvenu dans le {}".format(self.nom)

    def place_objects(self, obstacles):
        """ Place mac_gyver, needle, pipe, ether

        1/ takes dict obstacles
        2/ creates list of instance name, class, coordinates
        3/ creates 4 instances
        4/ adds instances to dict obstacles
        5/ returns obstacles (to refresh is in interface.py),
        6/ returns return_object (to facilitate access without searching)

        """

        print("\n ", "*"*55)
        list_object = [("mac_giver", MacGyver, "coordinates_mac_gyver"),\
            ("needle", Needle, "coordinates_needle"),\
            ("pipe", Pipe, "coordinates_pipe"),\
            ("ether", Ether, "coordinates_ether")]

        return_object = []

        for my_instance, my_class, coordinates_my_instance in list_object:
            my_instance = my_class(obstacles)
            coordinates_my_instance = (my_instance.x, my_instance.y)
            obstacles[coordinates_my_instance] = my_instance
            return_object.append(my_instance)
            if my_class == Ether:
                print(my_instance, ": ")
                print("\n ", "*"*55, "\n")
            else:
                print(my_instance, end=", ")
        return obstacles, return_object



def from_content_to_lab(content):
    """Take a content and return a my_lab object.


    1/ create a list of obstacles
    2/ init a x = 0 and y = 0
    3/ for each letter of content create an object 'obstacle' accoding to symbols' letter
    4/ for each new letter x+=1 except '\n' x=0 y+=1
    5/ append the object in the list_obstacles
    """

    list_obstacles = []

    symbols = {"0": Wall, "U": Arrival, " ": Obstacle}

    abscissa = 1
    ordinate = 1

    for letter in content:

        if letter == "\n":
            abscissa = 1
            ordinate += 1
            continue

        elif letter in symbols:
            my_class = symbols[letter]
            my_object = my_class(abscissa, ordinate)

        else:
            pass #penser à coder une erreur

        list_obstacles.append(my_object)
        abscissa += 1

    my_lab = Labyrinthe(list_obstacles)
    return my_lab


