import pygame

ANCHO=640
ALTO=480
BLANCO=(255,255,255)
ROJO=(255,0,0)
AZUL=(0,0,255)
NEGRO=(0,0,0)
VERDE=(0,255,0)
CHOCOLATE=(210,105,30)

class Cuadro(pygame.sprite.Sprite):
    def __init__(self, alto, ancho, color):
        pygame.sprite.Sprite.__init__(self)
        self.alto=alto
        self.ancho=ancho
        self.image=pygame.Surface([self.ancho,self.alto])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.rect.x=0
        self.rect.y=0
