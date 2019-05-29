""" Main.py is my main module that load the game using class objects

    mac_gyver can move and let a ground rect behind him,
    he is blocked by wall
    """

import os
from  modules.map_lab import Map
import pygame
from pygame.locals import *
from  modules.mac_gyver import MacGyver

resolution = 680,680

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

def main():
    """display the game """

    # create labyrinthe from datafile
    laby = launch_laby("laby1.txt")

    #dico with obstacles of my lab
    obstacles = laby.grid

    # add items and mac_gyver in the dictionnary
    return_place_items = laby.place_objects(obstacles)
    list_items = return_place_items[1]

    # refresh obstacles with 4 news mg, n, p, e
    obstacles = return_place_items[0]

    # create mac_gyver object
    mac_gyver = list_items[0]

    #basics pygame
    pygame.init()
    root = pygame.display.set_mode(resolution)

    #background
    background = pygame.image.load("res/background.png")
    root.blit(background, (40,40))

    for cle in obstacles:
        cle_pixel = (cle[0]*40, cle[1]*40)
        if obstacles[cle] == mac_gyver :
            mac_gyver_pix = pygame.image.load(obstacles[cle].pix)
            mac_gyver_pix.set_colorkey((255,255,255))
            root.blit(mac_gyver_pix, cle_pixel)
            mac_pos = mac_gyver_pix.get_rect()
            mac_pos.x, mac_pos.y = cle_pixel
        else :
            pix = pygame.image.load(obstacles[cle].pix)
            pix.set_colorkey((255,255,255))
            root.blit(pix, cle_pixel)
        #refresh root
        pygame.display.flip()

        #for later
        ground = pygame.image.load("res/ground.png").convert()
    # infinite loop
    continuer = 1
    while continuer:
        for event in pygame.event.get():    #Attente des événements
            if event.type == KEYDOWN:
                old_mac_pos = mac_pos
                can_move = ""
                if event.key == K_DOWN:
                    can_move = mac_gyver.mg_movement("S", mac_gyver, obstacles)
                elif event.key == K_UP:
                    can_move = mac_gyver.mg_movement("N", mac_gyver, obstacles)
                elif event.key == K_LEFT:
                    can_move = mac_gyver.mg_movement("W", mac_gyver, obstacles)
                elif event.key == K_RIGHT:
                    can_move = mac_gyver.mg_movement("E", mac_gyver, obstacles)

                if can_move:
                    print("ok", mac_gyver)
                    obstacles = can_move[0]
                    mac_gyver = can_move[1]
                    mac_pos = mac_gyver.x *40, mac_gyver.y *40
                    root.blit(mac_gyver_pix, mac_pos)
                    root.blit(ground, old_mac_pos)

                else :
                    continue
            pygame.display.flip()
            if event.type == QUIT:
                continuer = 0


if __name__ == "__main__":
    main()
