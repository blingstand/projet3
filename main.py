import modules.labyrinthe as lab
import modules.map_lab as map_lab
import os

#############################################################################
## Pour la prochaine fois :
## 1/ gérer l'affichage du labyrinthe, done
## 2/ coordonnées aléatoires de mac_gyver
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
        my_map = map_lab.Map(card_name, content)
        laby = my_map.labyrinthe
        disp_laby = laby.display_laby(laby.grid)
        print(disp_laby)

def main() :
    """à remplir plus tard"""

    launch_laby("laby1.txt")

if __name__ == "__main__":
    main()
