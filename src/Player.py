
import pygame
import random 

class Player(pygame.sprite.Sprite):
  def __init__ (self):
    """
    description: Function initializes the player state and the sprite.   
    args:
    return: None
    """
    
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("assets/Player/Player_U.png").convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.x = 100
    self.rect.y = 200
    self.rect = pygame.Rect((self.rect.x,self.rect.y),(10,20))
    self.direction = "U"
    self.speed = 15
    self.name = "Boo"
    self.health = 100
    self.attack_ani_R = [pygame.image.load("assets/Player/Player_RA1.png"), pygame.image.load("assets/Player/Player_RA2.png")]
    self.attack_ani_L = [pygame.image.load("assets/Player/Player_LA1.png"), pygame.image.load("assets/Player/Player_LA2.png")]    
    self.attacking = False
    self.attack_frame = 0

  def move(self, direction = None):
    """
    description: Moves Player based on direction
    args: direction
    return: None
    """
    # set limits if outside don't move
    if direction == "U":
      self.direction = "U"
      self.image = pygame.image.load("assets/Player/Player_U.png")
      self.rect.y -= self.speed
    elif direction == "D":
      self.direction = "D"
      self.image = pygame.image.load("assets/Player/Player_D.png")
      self.rect.y += self.speed
    elif direction == "L":
      self.direction = "L"
      self.rect.x -= self.speed
      self.image = pygame.image.load("assets/Player/Player_L.png")
    elif direction == "R":
      self.direction = "R"
      self.rect.x += self.speed
      self.image = pygame.image.load("assets/Player/Player_R.png").convert_alpha()



  def attack(self):
    """
    description: makes the character attack with an animation. also states how much damage it is able to do while also taking damage too.
    args: none.
    return: none.
    """ 
    
    if self.attack_frame > 1:
      self.attack_frame = 0
      self.attacking = False
        
    if self.direction in ["R", "U"]:
      self.image = self.attack_ani_R[self.attack_frame]
    else:
      self.image = self.attack_ani_L[self.attack_frame]
    
    self.attack_frame += 1

    if self.attacking == False:
      self.move()
