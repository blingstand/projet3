class MacGiver() :
    """Obstacle are objets that you can find in the laby"""

    nom = "MacGiver"
    symbole = "X"

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<{nom} (x={x}, y={y})>".format(nom=self.nom,
                x=self.x, y=self.y)

    def __str__(self):
        return "{nom} ({x}.{y})".format(nom=self.nom, x=self.x, y=self.y)
