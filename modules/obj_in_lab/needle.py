import random

class Needle() :
    """Obstacle are objets that you can find in the laby"""

    name = "needle"
    can_pass = True
    symbol = "N"

    def __init__(self):
        self.x = "gérer un x aléatoire compris entre 2 et 14 qui appartiendra à un objet 'obstacle' "
        self.y = "gérer un y aléatoire compris entre 2 et 14 qui appartiendra à un objet 'obstacle'"

    def __repr__(self):
        return "<{nom} (x={x}, y={y})>".format(nom=self.nom,
                x=self.x, y=self.y)

    def __str__(self):
        return "{nom} ({x}.{y})".format(nom=self.nom, x=self.x, y=self.y)
