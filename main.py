from  modules.map_lab import Map
from  modules.mac_gyver import MacGyver
from  modules.obj_in_lab.needle import Needle
from  modules.obj_in_lab.pipe import Pipe
from  modules.obj_in_lab.ether import Ether
import os

#############################################################################
## Pour la prochaine fois :
## 1/ coder le déplacement de mac_gyver ok
#############################################################################

def launch_laby(datafile):
    """open the datafile to show the lab.
    1/ create the my_map
    2/ display the lab
    """
    directory = os.path.dirname(__file__)
    path_to_file = os.path.join(directory, "carte", datafile)
    card_name = datafile[:-3].lower()
    with open(path_to_file, "r") as file :
        content = file.read()
        my_map = Map(card_name, content)
        laby = my_map.labyrinthe
        return laby

def place_objects(obstacles):
    """ Place mac_gyver, needle, pipe, ether """

    print("\n ", "*"*55)
    list_object = [("mac_giver", MacGyver, "coordinates_mac_gyver"),
        ("needle", Needle, "coordinates_needle"),
        ("pipe", Pipe, "coordinates_pipe"),
        ("ether", Ether, "coordinates_ether")]
    obs = obstacles
    return_object = []
    for i, j, k in list_object :
        i = j(obs)
        k = (i.x, i.y)
        obs[k] = i
        return_object.append(i)
        if j == Ether :
            print(i, ": ")
            print("\n ", "*"*55, "\n")
        else :
            print(i, end = ", ")
    return obs, return_object

def main() :
    """display the game """

    # create labyrinthe from datafile
    laby = launch_laby("laby1.txt")

    obstacles = laby.grid

    # place the new objects in dico obstacle
    obstacles = place_objects(obstacles)
    list_object = obstacles[1]

    obstacles = obstacles[0] #refresh obstacles with 4 news
    mac_gyver = list_object[0]
    needle = list_object[1]
    pipe = list_object[2]
    ether = list_object[3]

    disp_laby = laby.display_laby(obstacles)
    print(disp_laby)

    #Mac Gyver movement
    mac_gyver.mg_movement(laby.grid,mac_gyver)
    disp_laby = laby.display_laby(obstacles)
    print(disp_laby)

    # os.system("pause")
if __name__ == "__main__":
    main()
