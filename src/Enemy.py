
import pygame

class Enemy():
  def __init__(self):
    """
    description: Initializes the enemy state and sprite. 
    args: None 
    return: None 
    """
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("assets/enemy.png").convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.x = 40 
    self.rect.y = 2 

    self.name = "BOO" 
  
  def update(self):
    pass
