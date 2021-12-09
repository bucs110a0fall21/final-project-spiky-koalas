
import pygame

class Item(pygame.sprite.Sprite):
  def __init__(self, x, y, itemtype):
    """
    description: Creates the book and trophy items.
    args: None
    return: None
    """
    pygame.sprite.Sprite.__init__(self)

    if itemtype == 1:
      self.image = pygame.image.load("assets/Book.png").convert_alpha()
      self.image = pygame.transform.scale(self.image, (50,50)) 
      
    elif itemtype == 2:
      self.image = pygame.image.load("assets/trophy.png").convert_alpha()
      self.image = pygame.transform.scale(self.image, (40,40))

    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.rect = pygame.Rect((self.rect.x,self.rect.y),(15,15))

    self.type = itemtype
