import pygame
import time

ANCHO=640
ALTO=480

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


class Jugador(Cuadro):

    def __init__(self, archivo,x,y):
        pygame.sprite.Sprite.__init__(self) #Inicializo.
        self.image=pygame.image.load(archivo).convert_alpha() #Atributo.
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.cambiox=0
        self.cambioy=0

    def update(self):
        self.rect.x=self.rect.x+self.cambiox
        self.rect.y=self.rect.y+self.cambioy

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

class Enemigo(Cuadro):
    ls_muros=None
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

def linea(p1, p2):
    puntos = []
    dx = (p2[0] - p1[0])
    dy = (p2[1] - p1[1])

    # Determinar que punto usar para empezar y cual para terminar.
    if dy < 0:
        dy = -dy
        stepy = -1
    else:
        stepy = 1
    if dx < 0:
        dx = -dx
        stepx = -1
    else:
        stepx = 1
    x = p1[0]
    y = p1[1]

    # Bucle hasta llegar al otro extremo de la linea.
    if dx > dy:
        p = 2*dy-dx
        while x != p2[0]:
            x += stepx
            if p < 0:
                p += 2*dy
            else:
                y += stepy
                p += 2*(dy-dx)
            puntos.append([x, y])
    else:
        p = 2*dx-dy
        while y != p2[1]:
            y = y + stepy
            if p < 0:
                p += 2*dx
            else:
                x += stepx
                p += 2*(dx-dy)
            puntos.append([x, y])
    return puntos




if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    jpx=200
    jpy=200
    jpos=[jpx,jpy]
    jp=Jugador('imagen/Vida.png',jpx,jpy)
    todos=pygame.sprite.Group()
    todos.add(jp)
    ex=100
    ey=200
    epos=[ex,ey]
    e=Enemigo('imagen/Rick(1).png',ex,ey)
    todos.add(e)
    muros=pygame.sprite.Group()
    m=Muro(100,100)
    muros.add(m)
    todos.add(m)
    e.ls_muros=muros
    #p = [200, 200]
    #q = [100, 50]
    puntos = linea(epos, jpos)
    pygame.draw.lines(pantalla,(255,255,0),False,puntos,1)
    pygame.display.flip()
    for m in puntos:
        print m
    reloj=pygame.time.Clock()
    start_time = time.time()
    end_time = time.time()
    fin=False
    mover=False
    while not fin:
        #CIclo de control de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    jp.cambioy=-2
                    jp.cambiox=0
                if event.key == pygame.K_DOWN:
                    jp.cambioy=2
                    jp.cambiox=0
                if event.key == pygame.K_LEFT:
                    jp.cambiox=-2
                    jp.cambioy=0
                if event.key == pygame.K_RIGHT:
                    jp.cambiox=2
                    jp.cambioy=0
            if event.type == pygame.KEYUP:
                jp.cambiox=0
                jp.cambioy=0

        end_time = time.time()
        mover=True
        if end_time - start_time > 0.5:
            start_time = time.time()
            st=start_time
            puntos=linea([e.rect.x,e.rect.y],[jp.rect.x,jp.rect.y])
            num=0
            for m in puntos:
                num=num+1
                if mover == False:
                    break
                e.rect.x=m[0]
                e.rect.y=m[1]
                time.sleep(0.01)
                if e.rect.x==puntos[len(puntos)-1][0] and e.rect.y==puntos[len(puntos)-1][1]:
                    mover=False
                if num==25:
                    mover=False
                pantalla.fill((0,0,0))
                todos.update()
                todos.draw(pantalla)
                pygame.display.flip()

        pantalla.fill((0,0,0))
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
