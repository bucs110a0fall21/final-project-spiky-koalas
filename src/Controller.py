
from src import Player
from src import Enemy
from src import Item

import pygame
import random
import sys
import json
import numpy


class Controller:
  def __init__(self):
    """
    description: sets up pygame and window.
    args: None
    return: None
    """
    pygame.init()
    self.window_width = 500
    self.window_height = 300
    self.screen = pygame.display.set_mode((self.window_width, self.window_height))
    self.background = pygame.Surface((self.window_width, self.window_height))
    pygame.key.set_repeat(50, 500)
    self.state = "MENU"

    self.book = Item.Item(60, 65, 1)
    self.trophy = Item.Item(370, 65, 2)
    self.player = Player.Player()
    self.enemy = Enemy.Enemy("Ghosty", 310, 160, "assets/enemy_L.png")  
    self.all_sprites = pygame.sprite.Group((self.enemy), (self.player), (self.book), (self.trophy))
    self.trophy.kill()

    self.inside = pygame.image.load("assets/inside_mw.png")
    self.bck_img1 = pygame.image.load("assets/mansion.png")
    self.gameover = pygame.image.load("assets/gameover.png")
    self.balloon = pygame.image.load("assets/balloons.png")
    self.balloons = pygame.transform.scale(self.balloon, (200,150))
    self.real_img1 = pygame.transform.scale(self.bck_img1, (300, 300))
    self.real_inside = pygame.transform.scale(self.inside, (470, 300))
    self.real_gameover = pygame.transform.scale(self.gameover, (470, 300))

    self.button = pygame.image.load("assets/button.png")
    self.rbutton = pygame.transform.scale(self.button, (150, 150))

  def mainLoop(self):
    """
    If game is still running, runs gameLoop; if game is over(player health is at 0), runs gameover; if game is at a savepoint, runs savepoint; if player won(enemy health is at 0), runs win
    args: None
    return: None
    """
    while True:
      if (self.state == "MENU"):
        self.menu()
      elif (self.state == "GAME"):
        self.gameLoop()
      elif (self.state == "GAMEOVER"):
        self.gameOver()
      elif (self.state == "SAVE"):
        self.savePoint()
      elif (self.state == "WIN"):
        self.win()

  def menu(self):
    """
    description: Sets up menu screen with it text, buttons, and images.
    args: None
    return: None
    """
    while self.state == "MENU":
      pygame.font.init()
      font = pygame.font.Font("assets/Stranger back in the Night.ttf", 80)
      font2 = pygame.font.Font('assets/Basking.ttf', 20)
      text = font.render('The Haunted', True, (131, 139, 139))
      text2 = font.render('Mansion', True, (131, 139, 139))
      text3 = font2.render('New Game', True, (131, 139, 139))
      text4 = font2.render('Load Game', True, (131, 139, 139))
      text5 = font2.render('Exit', True, (131, 139, 139))

      button_NG = pygame.Rect((25, 155), (150, 40))
      button_LG = pygame.Rect((25, 200), (150, 40))
      button_Exit = pygame.Rect((25, 235), (150, 40))
      

      self.screen.blit(text, (20, 10))
      self.screen.blit(text2, (40, 75))

      self.screen.blit(self.real_img1, (175, 0))
      self.screen.blit(self.rbutton, (25, 112))
      self.screen.blit(self.rbutton, (25, 160))
      self.screen.blit(self.rbutton, (25, 208))

      self.screen.blit(text3, (50, 159))
      self.screen.blit(text4, (50, 209))
      self.screen.blit(text5, (80, 257))

      click = False
      mx, my = pygame.mouse.get_pos()

      for event in pygame.event.get():
        event.type == pygame.mouse.get_pressed()
        if event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:
            click = True

      if button_NG.collidepoint((mx, my)):
        if click:
          self.newGame()
          self.state = "GAME"

      if button_LG.collidepoint((mx, my)):
        if click:
          self.loadGame()
        

      if button_Exit.collidepoint((mx, my)):
        if click:
          self.exitGame()

      pygame.display.update()

  def gameLoop(self):
    """
    description: player moves based on what key is pressed, if player collides with enemy starts a fight
    args: (None)
    return: (None)
    """
    while self.state == "GAME":
      self.screen.blit(self.real_inside, (0, 0))
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        if event.type == pygame.KEYDOWN:
          if (event.key == pygame.K_UP):
            self.player.move("U")
            self.player.attacking = False
          elif (event.key == pygame.K_DOWN):
            self.player.move("D")
            self.player.attacking = False
          elif (event.key == pygame.K_LEFT):
            self.player.move("L")
            self.player.attacking = False
          elif (event.key == pygame.K_RIGHT):
            self.player.move("R")
            self.player.attacking = False 
          elif (event.key == pygame.K_SPACE):
            self.player.attack()
            self.player.attacking = True


      fight = pygame.Rect.colliderect(self.player.rect, self.enemy.rect)
      if fight:
        if self.player.attacking == True:
          self.enemy.health -= numpy.random.randint(0, 2)
          if self.enemy.health <= 0:
            self.enemy.kill()
            self.all_sprites = pygame.sprite.Group((self.player), (self.book))
     
        elif self.player.attacking == False:
          self.player.health -= random.randrange(0,5)
          print(self.player.attacking == True)
          if self.player.health <= 0:
            self.state = "GAMEOVER"
      else:
        if self.enemy.health <= 0:
          self.trophy = Item.Item(370, 65, 2)
          self.all_sprites.add(self.trophy)
          winning = pygame.Rect.colliderect(self.player.rect, self.trophy)
          if winning:
            print("trophy time")
            self.state = "WIN"

        self.player.move()


      self.all_sprites.draw(self.screen)


      if pygame.Rect.colliderect(self.player.rect, self.book.rect):
        self.state = "SAVE"
        print(self.state)

      pygame.display.flip()

      
    self.all_sprites.draw(self.screen)
    pygame.display.flip()

  def savePoint(self):
    """
    description: Allows the player to save the game after picking up the book.
    args: None
    return: None
    """
    while self.state == "SAVE":
      pygame.font.init()
      self.screen.fill((0, 0, 0))
      font = pygame.font.Font('assets/Basking.ttf', 20)
      text1 = font.render('Save and Continue', True, (131, 139, 139))
      text2 = font.render('Save and Quit', True, (131, 139, 139))
      
      button_SC = pygame.Rect((175, 50), (150, 60))
      button_SQ = pygame.Rect((175, 100), (150, 60))  

      
      thisbutton = self.rbutton
      thisbutton = pygame.transform.scale(thisbutton, (200, 150))

      self.screen.blit(thisbutton, (165, 20))
      self.screen.blit(thisbutton, (165, 70))

      self.screen.blit(text1, (177, 70))
      self.screen.blit(text2, (177, 120))

      click = False
      mx, my = pygame.mouse.get_pos()

      for event in pygame.event.get():
        event.type == pygame.mouse.get_pressed()
        if event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:
            click = True

      if button_SC.collidepoint((mx, my)):
        if click:
          fptr = open("assets/data.json", "w")
          stats = {
            "name" : self.player.name,
            "position_x" : 100,
            "position_y" : 200,
            "health" : self.player.health,
            "enemy" : self.enemy.health,
            "state" : "GAME"
            }
          print(stats)
          json.dump(stats, fptr)
          fptr.flush()
          fptr.close()

          self.loadGame()

      if button_SQ.collidepoint((mx, my)):
        if click:
          fptr = open("assets/data.json", "w")
          stats = {
            "name" : self.player.name,
            "position_x" :100,
            "position_y": 200,
            "health" : self.player.health,
            "enemy" : self.enemy.health,
            "state" : "GAME"
            }
          json.dump(stats, fptr)
          fptr.close()
          self.screen.fill((0,0,0))
          self.state = "MENU"

      pygame.display.update()


  def gameOver(self):
    """
    description: Displays screen for when player is killed by enemy. Has options to retry from the beginning or exit the game.
    args: None
    return: None
    """
    while self.state == "GAMEOVER":
      print(self.state)
      pygame.font.init()
      font = pygame.font.Font('assets/Basking.ttf', 20)
      self.screen.fill((0, 0, 0))
      self.screen.blit(self.real_gameover, (15, 0))
      color17 = (255,0,0)
      
      button_retry = pygame.Rect((25, 234), (150, 40))
      button_exit = pygame.Rect((330, 234), (150,40))
      
      text = font.render('Retry', True, (131, 139, 139))
      text2 = font.render("Exit", True, (131,139,139))

      self.screen.blit(self.rbutton, (25, 194))
      self.screen.blit(self.rbutton, (330, 194))

      self.screen.blit(text, (70, 240))
      self.screen.blit(text2, (380, 240))

      click = False
      mx, my = pygame.mouse.get_pos()

      for event in pygame.event.get():
        event.type == pygame.mouse.get_pressed()
        if event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:
            click = True

          if button_retry.collidepoint((mx, my)):
            if click:
              self.loadGame()

          if button_exit.collidepoint((mx,my)):
            if click:
              self.screen.fill((0,0,0))
              self.state = "MENU"

      pygame.display.flip()
  
  def win(self):
    """
    description: Will display winning screen if player kills the enemy. 
    args: None
    return: None
    """
    while self.state == "WIN":
      self.screen.fill((31,34,52))
      self.screen.blit(self.balloons, (140,15))
      pygame.font.init()
      font = pygame.font.Font('assets/Basking.ttf', 20)
      button_exit = pygame.Rect((205, 235), (150, 60))
      text = font.render ( 'Exit' , True , (131, 139, 139))
      text2 = font.render ('Enemy defeated' , True,(131, 139, 139))
      text3 = font.render ('You win!' , True, (131, 139, 139))

      self.screen.blit(self.rbutton, (175,200))

      self.screen.blit(text2, (175, 150))
      self.screen.blit(text3, (200,200))
      self.screen.blit(text, (230, 250))

      mx,my = pygame.mouse.get_pos()
      for event in pygame.event.get():
        event.type == pygame.mouse.get_pressed()
        if event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:
            click = True

          if button_exit.collidepoint((mx, my)):
            if click:
              self.screen.fill((0,0,0))
              self.state = "MENU"

      pygame.display.flip()
    
  def exitGame(self):
    """
    description: stops running program ("Exits game")
    args: None
    return: None
    """
    pygame.quit()
    sys.exit
    pygame.display.update()

  def newGame(self):
    """
    description: Sets up the menu screen while allowing the player to input their name. 
    args: None
    return: None
    """
    self.enemy = Enemy.Enemy("Ghosty", 310, 160, "assets/enemy_L.png")
    self.all_sprites = pygame.sprite.Group((self.enemy), (self.player), (self.book)) 
    self.enemy.health = 50
    self.player.health = 100
    self.player.direction = "U"
    self.player.rect.x = 100
    self.player.rect.y = 200
    input_box = pygame.Rect((310, 10), (25, 28))
    inside_box = pygame.Rect((313, 10), (200, 32))
    font = pygame.font.Font('assets/Basking.ttf', 20)
    color_inactive = pygame.Color('darkorchid4')
    color_active = pygame.Color('darkorchid3')
    color = color_inactive
    text1 = font.render('Enter Name:', True, (154, 50, 205))
    self.screen.blit(text1, (200, 10))
    text = ""
    active = False
    done = False
    pygame.display.update()

    while not done:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
          if input_box.collidepoint(event.pos):
            active = not active
          else:
            active = False
            color = color_active
          if active:
            color = color_active
          else:
            color = color_inactive
        if event.type == pygame.KEYDOWN:
          if active:
            if event.key == pygame.K_BACKSPACE:
              text = text[:-1]
            elif event.key == pygame.K_RETURN:
              text = ""
              self.state == "GAME"
              self.screen.fill((0, 0, 0))
              done = True
            else:
              text += event.unicode
              self.player.name = text 
      color2 = (0,0,0)
      txt_surface = font.render(text, True, color)
      width = max(150, txt_surface.get_width() + 10)
      input_box.w = width
      pygame.draw.rect(self.screen, color2, inside_box)
      self.screen.blit(txt_surface, (input_box.x + 5, input_box.y + 2))
      pygame.draw.rect(self.screen, color , input_box, 2)
      
      
      pygame.display.flip()

  def loadGame(self):
    """
    description: Loads the save file the player created previously.
    args: None
    return: None
    """
    self.screen.fill((0,0,0))
    fptr = open("assets/data.json", "r")
    stats = json.load(fptr)
    self.player.name = stats["name"]
    self.player.rect.x = stats["position_x"]
    self.player.rect.y = stats["position_y"]
    self.player.health = stats["health"]
    self.enemy.health = stats["enemy"]
    self.state = stats["state"]
    fptr.close()
