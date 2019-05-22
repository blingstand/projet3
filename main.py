import modules.labyrinthe as lab
import modules.map_lab as map_lab
import os


def launch_laby(datafile):
    """affiche le labyrinthe"""
    directory = os.path.dirname(__file__)
    path_to_file = os.path.join(directory, "carte", datafile)
    card_name = datafile[:-3].lower()
    with open(path_to_file, "r") as file :
        content = file.read()
        my_map = map_lab.Map(card_name, content)


def main() :
    """à remplir plus tard"""

    launch_laby("laby1.txt")

if __name__ == "__main__":
    main()
