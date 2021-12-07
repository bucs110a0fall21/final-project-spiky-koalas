
import pygame

class Item(pygame.sprite.Sprite):
  def __init__(self, x, y, itemtype):
    pygame.sprite.Sprite.__init__(self)

    if itemtype == 1:
      self.image = pygame.image.load("assets/Book.png")
      self.image = pygame.transform.scale(self.image, (50,50)) 
      
    elif itemtype == 2:
      self.image = pygame.image.load("assets/potion.png")
      self.image = pygame.transform.scale(self.image, (150,150))

    
   
    self.rect = self.image.get_rect()
    self.type = itemtype
    self.x = x
    self.y = y
    self.rect.inflate_ip(-200, -300)
