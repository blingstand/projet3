class Obstacle:

    """Classe représentant tous les obstacles.

    Les obstacles sont généralement hérités de cette classe. Elle
    définit plusieurs méthodes et attributs qu'il faudra peut-être modifier
    dans les classes filles.

    """

    name = "obstacle"
    can_pass = True
    symbol = ""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<{name} (x={x}, y={y})>".format(name=self.name,
                x=self.x, y=self.y)

    def __str__(self):
        return "{name} ({x}.{y})".format(name=self.name, x=self.x, y=self.y)
