import pygame
from libreria import *

class Jugador(Cuadro):
    ls_muros=None
    ls_mod=None
    vel=0
    def __init__(self, archivo,x,y):
        pygame.sprite.Sprite.__init__(self) #Inicializo.
        self.image=pygame.image.load(archivo).convert_alpha() #Atributo.
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.cambiox=0
        self.cambioy=0

    def update(self):
        self.rect.x+=self.cambiox
        ls_golpes = pygame.sprite.spritecollide(self,self.ls_muros,False)
        for m in ls_golpes:
            if self.cambiox > 0:
                self.rect.right=m.rect.left
            else:
                self.rect.left=m.rect.right

        self.rect.y+=self.cambioy
        ls_golpes = pygame.sprite.spritecollide(self,self.ls_muros,False)
        for m in ls_golpes:
            if self.cambioy > 0:
                self.rect.bottom=m.rect.top
            else:
                self.rect.top=m.rect.bottom

        ls_captura=pygame.sprite.spritecollide(self,self.ls_mod,True)
        for md in ls_captura:
            self.vel=5

class Muro(Cuadro):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([x,y])
        self.image.fill(CHOCOLATE)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.cambiox=0
        self.cambioy=0

class Velocidad(Cuadro):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([15,15])
        self.image.fill(VERDE)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y


if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    jp=Jugador('imagen/ship.png',100,100)
    todos=pygame.sprite.Group()
    todos.add(jp)

    muros=pygame.sprite.Group()
    '''
    for i in range(5):
        x=random.randrange(10,ANCHO-40)
        y=random.randrange(10,ALTO-40)
        m=Muro(x,y)
        muros.add(m)
        todos.add(m)
    '''
    m=Muro(100,100)
    muros.add(m)
    todos.add(m)

    reloj=pygame.time.Clock()

    mods=pygame.sprite.Group()
    comida=Velocidad(300,100)
    todos.add(comida)
    mods.add(comida)

    jp.ls_muros=muros
    jp.ls_mod=mods

    font = pygame.font.Font(None,36)
    texto=font.render("mensaje",True,NEGRO)


    fin=False
    while not fin:
    #CIclo de control de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    jp.cambioy=-2-jp.vel
                    jp.cambiox=0
                if event.key == pygame.K_DOWN:
                    jp.cambioy=2+jp.vel
                    jp.cambiox=0
                if event.key == pygame.K_LEFT:
                    jp.cambiox=-2-jp.vel
                    jp.cambioy=0
                if event.key == pygame.K_RIGHT:
                    jp.cambiox=2+jp.vel
                    jp.cambioy=0
                if event.key ==pygame.K_s:
                    jp.cambiox=0
                    jp.cambioy=0
            '''if event.type == pygame.KEYUP:
                jp.cambiox=0
                jp.cambioy=0
'''
        pantalla.fill(BLANCO)
        pantalla.blit(texto,[400,300])
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
