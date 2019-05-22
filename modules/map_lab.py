from modules.labyrinthe import from_content_to_lab

class Map:

    """Object to create the lab.

    1/ main.py gives a content from a file
    2/ map.py creates an object that can create the lab

    """

    def __init__(self, name, content):
        self.name = name
        self.labyrinthe = from_content_to_lab(content)

    def __repr__(self):
        return "<Map {}>".format(self.name)
