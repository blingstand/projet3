from  modules.map_lab import Map
from  modules.mac_gyver import MacGiver
import os

#############################################################################
## Pour la prochaine fois :
## 1/ gérer l'affichage du labyrinthe, done
## 2/ coordonnées aléatoires de mac_gyver, done
## 3/ positionner mac_gyver
## 4/ coordonnées aléatoires des 3 objets
## 5/ le positionnement des 3 objets
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

    # display coordinate_mac_gyver
    coordinates_mac_gyver = MacGiver(laby.grid)
    print("\n\t\t", coordinates_mac_gyver, "\n")

    #place mac_gyver
    disp_laby = laby.display_laby(laby.grid, coordinates_mac_gyver)
    print(disp_laby)

if __name__ == "__main__":
    main()
