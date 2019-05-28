""" Main.py is my main module that load the game using class objects

    1/ create a labyrinthe object according to datafile (laby1.txt)
    2/ create a dictionnary with obstacles of my lab
    3/ add items in the dictionnary
    4/ create a mac_gyver object
    5/ display lab
    6/ initiate the loop for mac_gyver movements in the lab

    """

import os
from  modules.map_lab import Map
from  modules.mac_gyver import MacGyver
from  modules.obj_in_lab.needle import Needle
from  modules.obj_in_lab.pipe import Pipe
from  modules.obj_in_lab.ether import Ether


def launch_laby(datafile):
    """open the datafile to show the lab.
    1/ create the my_map
    2/ display the lab
    """
    directory = os.path.dirname(__file__)
    path_to_file = os.path.join(directory, "carte", datafile)
    card_name = datafile[:-3].lower()
    with open(path_to_file, "r") as file:
        content = file.read()
        my_map = Map(card_name, content)
        laby = my_map.labyrinthe
        return laby

def place_objects(obstacles):
    """ Place mac_gyver, needle, pipe, ether """

    print("\n ", "*"*55)
    list_object = [("mac_giver", MacGyver, "coordinates_mac_gyver"),\
        ("needle", Needle, "coordinates_needle"),\
        ("pipe", Pipe, "coordinates_pipe"),\
        ("ether", Ether, "coordinates_ether")]
    obs = obstacles
    return_object = []
    for i, j, k in list_object:
        i = j(obs)
        k = (i.x, i.y)
        obs[k] = i
        return_object.append(i)
        if j == Ether:
            print(i, ": ")
            print("\n ", "*"*55, "\n")
        else:
            print(i, end=", ")
    return obs, return_object

def main():
    """display the game """

    # create labyrinthe from datafile
    laby = launch_laby("laby1.txt")

    #dico with obstacles of my lab
    obstacles = laby.grid

    # add items and mac_gyver in the dictionnary
    return_place_items = place_objects(obstacles)
    list_items = return_place_items[1]

    # refresh obstacles with 4 news mg, n, p, e
    obstacles = return_place_items[0]

    # create mac_gyver object
    mac_gyver = list_items[0]

    # display lab
    disp_laby = laby.display_laby_pygame(obstacles)
    # print(disp_laby)
    """
    #Mac Gyver movement
    while True:
        return_mg_move = mac_gyver.mg_movement(obstacles, mac_gyver)
        obstacles = return_mg_move[0]
        mac_gyver = return_mg_move[1]
        disp_laby = laby.display_laby(obstacles)
        print(disp_laby)
    """

if __name__ == "__main__":
    main()
