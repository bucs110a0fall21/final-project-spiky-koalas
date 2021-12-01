
import pygame

class Player(pygame.sprite.Sprite):
  def __init__ (self):
    """
    description: Function initializes the player state and the sprite.   
    args: x ,y
    return: None
    """
    pygame.sprite.Sprite.__init__(self)

    self.image = pygame.image.load("assets/player.png").convert_alpha()
    #self.sound = pygame.mixer.Sound("assets/...")#need to get a sound effect
    #self.music1 = pygame.mixer.music("assets/...")#need to get background music for menu
    #self.music2 = pygame.mixer.music("assets/...")#need to get background music for the game
    #self.music3 = pygame.mixer.music("assets/...")
    self.rect = self.image.get_rect()
    self.rect.x = 10
    self.rect.y = 0
    self.direction = "R"
    self.speed = 5
    self.name = "YAY"
    self.health = 100

    def move(self, direction):
      """
      description: Moves Player based on direction
      args: direction
      return: None
      """
      if direction == "U":
          self.rect.y -= self.speed
      elif direction == "D":
          self.rect.y += self.speed
      elif direction == "L":
          self.rect.x -= self.speed
      elif direction == "R":
          self.rect.x += self.speed


  def attack(self, enemy):
    """
    description: 
    args:
    return:
    """
