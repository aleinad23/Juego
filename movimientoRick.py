import pygame
import random
from libreria import *

ANCHO=600
ALTO=468

class Jugador(Cuadro):
    vel=0
    def __init__(self, archivo,x,y):
        pygame.sprite.Sprite.__init__(self) #Inicializo.
        self.fondo=self.Recortar(archivo,x,y)
        self.cambiox=0
        self.cambioy=0

    def Recortar(self, archivo, ancho, alto):
        self.imagen=pygame.image.load(archivo).convert_alpha()
        img_ancho, img_alto=self.imagen.get_size()
        print img_ancho, ' ',img_alto
        tabla_fondos=[]
        for fondo_x in range(0,img_ancho/ancho):
            linea=[]
            tabla_fondos.append(linea)
            for fondo_y in range(0,img_alto/alto):
                cuadro=(fondo_x*ancho,fondo_y*alto,ancho,alto)
                linea.append(self.imagen.subsurface(cuadro))
        return tabla_fondos

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pantalla.fill(NEGRO)
    jp=Jugador('imagen/Rick.png',32,32)
    todos=pygame.sprite.Group()
    todos.add(jp)
    con=0
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if con < 2:
                        con+=1
                    else:
                        con=0
                    gato=jp.fondo[con][3]
                    jp.cambioy-=2
                    pantalla.blit(gato,(jp.cambiox,jp.cambioy))
                    pygame.display.flip()
                if event.key == pygame.K_DOWN:
                    if con < 2:
                        con+=1
                    else:
                        con=0
                    gato=jp.fondo[con][0]
                    jp.cambioy+=2
                    pantalla.blit(gato,(jp.cambiox,jp.cambioy))
                    pygame.display.flip()
                if event.key == pygame.K_LEFT:
                    if con < 2:
                        con+=1
                    else:
                        con=0
                    gato=jp.fondo[con][1]
                    jp.cambiox-=2
                    pantalla.blit(gato,(jp.cambiox,jp.cambioy))
                    pygame.display.flip()
                if event.key == pygame.K_RIGHT:
                    if con < 2:
                        con+=1
                    else:
                        con=0
                    gato=jp.fondo[con][2]
                    jp.cambiox+=2
                    pantalla.blit(gato,(jp.cambiox,jp.cambioy))
                    pygame.display.flip()
        pantalla.fill(NEGRO)
