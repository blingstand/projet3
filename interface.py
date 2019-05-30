""" Main.py is my main module that load the game using class objects

    interface now displays messages
    """

import os
import pygame
from  modules.map_lab import Map

###################################################### VARIABLES
RESOLUTION = 680, 680
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
LAB = "laby2.txt"


###################################################### PYGAME
pygame.init()
ROOT = pygame.display.set_mode(RESOLUTION)
FONT = pygame.font.SysFont("Arial", 25)


###################################################### FUNCTIONS
def message_to_screen(msg, color):
    """ displays a BLACK rect then a message in the top left corner """

    pygame.draw.rect(ROOT, BLACK, [0, 0, 680, 38]) #rect
    screen_text = FONT.render(msg, True, color) #msg
    ROOT.blit(screen_text, (0, 0))


def launch_laby(datafile):
    """open the datafile to show the lab.
    1/ create the my_map
    2/ display the lab
    """
    directory = os.path.dirname(__file__)
    path_to_file = os.path.join(directory, "carte", datafile)
    card_name = datafile[:-3].lower()
    with open(path_to_file, "r") as file:
        content = file.read()
        my_map = Map(card_name, content)
        laby = my_map.labyrinthe
        return laby

def mg_can_move(mac_gyver, can_move, mac_gyver_pix, ground, mac_pos):
    """ regroupe all the informations to move Mac Gyver

        1/ display ground to old Mac Gyver position
        2/ refresh obstacles, mac_gyver and mac_pos in order to return them
        3/ display the objectives based on Mac Gyver movement/position
        4/ manage the inventory when Mac Gyver picks up an item
        5/ flip everything
    """

    ROOT.blit(ground, mac_pos)

    obstacles = can_move[0]
    mac_gyver = can_move[1]
    mac_pos = mac_gyver.x *40, mac_gyver.y *40
    ROOT.blit(mac_gyver_pix, mac_pos)


    len_inventory = len(mac_gyver.inventory)
    if len_inventory == 3:
        my_msg = "Objectives : Now you can face the guard ! "
    else:
        my_msg = "Objectives : Avoid the guard as long as you do not have all the items. "
    message_to_screen(my_msg, BLUE)

    try:
        item = can_move[2]
        file = 'res/' + item + '.png'
        item_pix = pygame.image.load(file)
        ROOT.blit(item_pix, (len_inventory*40, 15*40))
        my_msg = "MG : Good point, I've found an item, {}.".format(item)
        message_to_screen(my_msg, RED)
    except :
        pass
    finally:
        pygame.display.flip()
    return mac_gyver, obstacles, mac_pos

###################################################### MAIN
def main():
    """display the game """

    message_to_screen("MG : I need to go out ! ", RED)
    # create labyrinthe from datafile
    laby = launch_laby(LAB)

    #create dictionnary with obstacles of my lab
    obstacles = laby.grid

    #add items and mac_gyver in the dictionnary
    return_place_items = laby.place_objects(obstacles)
    obstacles, list_items = return_place_items[0], return_place_items[1]
    mac_gyver = list_items[0]# create mac_gyver object

    #display background
    background = pygame.image.load("res/background.png")
    ROOT.blit(background, (40, 40))

    for cle in obstacles:
        cle_pixel = (cle[0]*40, cle[1]*40)
        if obstacles[cle] == mac_gyver:
            mac_gyver_pix = pygame.image.load(obstacles[cle].pix)
            mac_gyver_pix.set_colorkey(WHITE)
            ROOT.blit(mac_gyver_pix, cle_pixel)
            mac_pos = mac_gyver_pix.get_rect()
            mac_pos.x, mac_pos.y = cle_pixel
        else:
            pix = pygame.image.load(obstacles[cle].pix)
            pix.set_colorkey(WHITE)
            ROOT.blit(pix, cle_pixel)
        #refresh ROOT
        pygame.display.flip()

        #for later
        ground = pygame.image.load("res/ground.png").convert()
    # infinite loop
    continuer = 1
    while continuer:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                can_move = ""
                if event.key == pygame.K_DOWN:
                    can_move = mac_gyver.mg_movement("S", mac_gyver, obstacles)
                elif event.key == pygame.K_UP:
                    can_move = mac_gyver.mg_movement("N", mac_gyver, obstacles)
                elif event.key == pygame.K_LEFT:
                    can_move = mac_gyver.mg_movement("W", mac_gyver, obstacles)
                elif event.key == pygame.K_RIGHT:
                    can_move = mac_gyver.mg_movement("E", mac_gyver, obstacles)
                if can_move:
                    mac_gyver, obstacles, mac_pos = mg_can_move(mac_gyver,\
                     can_move, mac_gyver_pix, ground, mac_pos)
                else:
                    message_to_screen("MG : I can't there is a wall.", RED)
                    pygame.display.flip()
            if event.type == pygame.QUIT:
                continuer = 0


if __name__ == "__main__":
    main()
