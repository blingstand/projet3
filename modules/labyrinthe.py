#labyrinthe
import pygame
from pygame.locals import *
import os
from modules.obj_in_lab.wall import Wall
from modules.obj_in_lab.arrival import Arrival
from modules.obj_in_lab.obstacle import Obstacle


class Labyrinthe():
    """Create the Labyrinthe object"""

    #size of my laby 15*15
    limite_x = 15
    limite_y = 15
    liste_3_objects=[]

    def __init__(self, obstacles):
        """the Labyrinthe is composed by obstacles and MacGiver """

        self.nom = "Labyrinthe MacGyver"
        self.grid = {}
        for obstacle in obstacles :
            self.grid[obstacle.x, obstacle.y] = obstacle
        self.resolution = 680,680

    def __repr__(self):
        return "Bienvenu dans le {}".format(self.nom)

    def __str__(self):
        return "Bienvenu dans le {}".format(self.nom)

    def display_laby_pygame(self, obstacles):
        """ Display the laby object according to x and y properties"""

        #basics pygame
        pygame.init()

        #Ouverture de la fenêtre Pygame
        root = pygame.display.set_mode(self.resolution)

        #background
        background = pygame.image.load("res/background.png")
        root.blit(background, (40,40))

        for cle in obstacles:
            cle_pixel = (cle[0]*40, cle[1]*40)
            pix = pygame.image.load(obstacles[cle].pix)
            pix.set_colorkey((255,255,255))
            root.blit(pix, cle_pixel)

        #refresh root
        pygame.display.flip()

        # infinite loop
        continuer = 1
        while continuer:
            for event in pygame.event.get():    #Attente des événements
                if event.type == QUIT:
                    continuer = 0





def from_content_to_lab(content):
    """Take a content and return a my_lab object.

    1/ create a list of obstacles
    2/ init a x = 0 and y = 0
    3/ for each letter of content create an object 'obstacle' accoding to symbols' letter
    4/ for each new letter x+=1 except '\n' x=0 y+=1
    5/ append the object in the list_obstacles
    """

    list_obstacles = []

    symbols = {
            "0": Wall,
            "U": Arrival
        }

    x = 1
    y = 1

    for letter in content :
        if letter == "\n" :
            x = 1
            y += 1
            continue
        elif letter == " ":
            pass
        elif letter in symbols:
            classe = symbols[letter]
            my_object = classe(x, y)
        else :
            pass #penser à coder une erreur

        list_obstacles.append(my_object)
        x += 1

    my_lab = Labyrinthe(list_obstacles)

    return my_lab


