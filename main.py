
from src import Controller
import pygame

def main():
    pygame.init()
    game = Controller.Controller()
    game.mainLoop()
	
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 2 LINES OF CODE ######
main()
