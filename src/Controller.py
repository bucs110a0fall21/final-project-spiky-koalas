
from src import Player
from src import Enemy

import pygame 
import random
import sys

class Controller:

  def __init__(self): 
    """
    description: sets up pygame and window
    args: None
    return: None
    """
    self.window_width = 800
    self.window_height = 800
    pygame.display.init()
    self.screen = pygame.display.set_mode((self.window_width, self.window_height))
    self.background = pygame.Surface((self.window_width,self.window_height))
    self.background.fill((0,0,0))
    self.player = Player.Player()
    self.enemy = Enemy.Enemy()
    self.state = "GAME"
    #image for background

  def mainLoop(self):
    """
    If game is still running, runs gameLoop; if game is over, runs gameover
    args: None
    return: None
    """
    while True:
        if(self.state == "GAME"):
            self.gameLoop()
        elif(self.state == "GAMEOVER"):
            self.gameOver()

  def gameLoop(self):
    """
    player moves based on what key is pressed, if player collides with enemy starts a fight
    args: (None)
    return: (None)
    """
    while self.state == "GAME":
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        if event.type == pygame.KEYDOWN:
          if(event.key == pygame.K_UP):
            self.player.move("U")
          elif(event.key == pygame.K_DOWN):
            self.player.move("D")
          elif(event.key == pygame.K_LEFT):
            self.player.move("L")
          elif(event.key == pygame.K_RIGHT):
            self.player.move("R")
          elif(event.key == pygame.K_SPACE):
            self.player.attack("later")
            
      # fight = pygame.sprite.spritecollide(self.player, self.enemy, True)
      # if fight:
      #   print("Wow a fight")
      #   #NEED MATH
