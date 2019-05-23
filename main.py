from  modules.map_lab import Map
from  modules.mac_gyver import MacGiver
from  modules.obj_in_lab.needle import Needle
from  modules.obj_in_lab.pipe import Pipe
from  modules.obj_in_lab.ether import Ether
import os

#############################################################################
## Pour la prochaine fois :
## 1/ gérer l'affichage du labyrinthe, done
## 2/ coordonnées aléatoires de mac_gyver, done
## 3/ positionner mac_gyver done
## 4/ coordonnées aléatoires des 3 objets done
## 5/ le positionnement des 3 objets done
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

def main() :
    """display the game """

    # create labyrinthe from datafile
    laby = launch_laby("laby1.txt")

    # display
    liste_coordinates = []

        #mac_gyver
    mac_gyver = MacGiver(laby.grid)
    coordinates_mac_gyver = (mac_gyver.x, mac_gyver.y,mac_gyver)
    print("\n\t\t", mac_gyver, "\n")
    liste_coordinates.append(coordinates_mac_gyver)
        #needle
    needle = Needle(laby.grid)
    coordinates_needle = (needle.x, needle.y,needle)
    print("\n\t\t", needle)
    liste_coordinates.append(coordinates_needle)

        #pipe
    pipe = Pipe(laby.grid)
    coordinates_pipe = (pipe.x, pipe.y,pipe)
    print("\n\t\t", pipe)
    liste_coordinates.append(coordinates_pipe)

    #ether
    ether = Ether(laby.grid)
    coordinates_ether = (ether.x, ether.y,ether)
    print("\n\t\t", ether, '\n\n')
    liste_coordinates.append(coordinates_ether)

    # coordinates_pipe = Pipe(laby.grid)
    # print("\n\t\t", coordinates_pipe)
    # coordinates_ether = Ether(laby.grid)
    # print("\n\t\t", coordinates_ether, "\n")

    #place mac_gyver
    disp_laby = laby.display_laby(laby.grid, liste_coordinates)
    print(disp_laby)



if __name__ == "__main__":
    main()
