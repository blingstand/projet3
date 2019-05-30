#labyrinthe

import os
from  modules.mac_gyver import MacGyver
from  modules.obj_in_lab.needle import Needle
from  modules.obj_in_lab.pipe import Pipe
from  modules.obj_in_lab.ether import Ether
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

    def __repr__(self):
        return "Bienvenu dans le {}".format(self.nom)

    def __str__(self):
        return "Bienvenu dans le {}".format(self.nom)

    def place_objects(self, obstacles):
        """ Place mac_gyver, needle, pipe, ether """

        print("\n ", "*"*55)
        list_object = [("mac_giver", MacGyver, "coordinates_mac_gyver"),\
            ("needle", Needle, "coordinates_needle"),\
            ("pipe", Pipe, "coordinates_pipe"),\
            ("ether", Ether, "coordinates_ether")]
        obs = obstacles
        return_object = []
        for instance, j, k in list_object:
            instance = j(obs)
            k = (instance.x, instance.y)
            obs[k] = instance
            return_object.append(instance)
            if j == Ether:
                print(instance, ": ")
                print("\n ", "*"*55, "\n")
            else:
                print(instance, end=", ")
        return obs, return_object




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
            "U": Arrival,
            " ": Obstacle
        }

    x = 1
    y = 1

    for letter in content :
        if letter == "\n" :
            x = 1
            y += 1
            continue
        elif letter in symbols:
            classe = symbols[letter]
            my_object = classe(x, y)
        else :
            pass #penser à coder une erreur

        list_obstacles.append(my_object)
        x += 1

    my_lab = Labyrinthe(list_obstacles)

    return my_lab


