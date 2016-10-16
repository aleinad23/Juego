import pygame
import ConfigParser
from libreria import *

ANCHO=1344
ALTO=680

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

class Nivel:
    def __init__(self, infomapa):
        self.interprete=ConfigParser.ConfigParser()
        self.interprete.read(infomapa)
        self.origen=self.interprete.get("nivel","origen")
        self.alto=int(self.interprete.get("nivel","alto"))
        self.ancho=int(self.interprete.get("nivel","ancho"))
        self.fondo=self.Recortar(self.origen,self.alto,self.ancho)
        self.mapa=[]
        self.mapa=self.interprete.get("nivel","mapa").split("\n")

    def Recortar(self,archivo, ancho, alto):
        imagen=pygame.image.load(archivo).convert_alpha()
        img_ancho, img_alto=imagen.get_size()
        print img_ancho, ' ',img_alto
        tabla_fondos=[]
        for fondo_x in range(0,img_ancho/ancho):
            linea=[]
            tabla_fondos.append(linea)
            for fondo_y in range(0,img_alto/alto):
                cuadro=(fondo_x*ancho,fondo_y*alto,ancho,alto)
                linea.append(imagen.subsurface(cuadro))
        return tabla_fondos

    def Dibujar(self,pantalla):
        var_x=self.ancho
        var_y=self.alto
        con_y=0
        for fila in self.mapa:
            con_x=0
            for c in fila:
                x=int(self.interprete.get(c,"x"))
                y=int(self.interprete.get(c,"y"))
                print x, ' ',y
                cuadro_sel=self.fondo[x][y]
                pantalla.blit(cuadro_sel,[con_x,con_y])
                con_x+=var_x
            con_y+=var_y


if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pantalla.fill(BLANCO)
    fondo = pygame.image.load("imagen/gris.jpg").convert()
    pantalla.blit(fondo, (0, 0))
    nivel1=Nivel('niveles.map')
    nivel1.Dibujar(pantalla)
    pygame.display.flip()
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
                    jp.cambioy-=10
                    pantalla.blit(gato,(jp.cambiox,jp.cambioy))
                    pygame.display.flip()
                if event.key == pygame.K_DOWN:
                    if con < 2:
                        con+=1
                    else:
                        con=0
                    gato=jp.fondo[con][0]
                    jp.cambioy+=10
                    pantalla.blit(gato,(jp.cambiox,jp.cambioy))
                    pygame.display.flip()
                if event.key == pygame.K_LEFT:
                    if con < 2:
                        con+=1
                    else:
                        con=0
                    gato=jp.fondo[con][1]
                    jp.cambiox-=10
                    pantalla.blit(gato,(jp.cambiox,jp.cambioy))
                    pygame.display.flip()
                if event.key == pygame.K_RIGHT:
                    if con < 2:
                        con+=1
                    else:
                        con=0
                    gato=jp.fondo[con][2]
                    jp.cambiox+=10
                    pantalla.blit(gato,(jp.cambiox,jp.cambioy))
                    pygame.display.flip()
                fondo = pygame.image.load("imagen/gris.jpg").convert()
                pantalla.blit(fondo, (0, 0))
                nivel1=Nivel('niveles.map')
                nivel1.Dibujar(pantalla)
                pygame.display.flip()
                pantalla.blit(gato,(jp.cambiox,jp.cambioy))
                pygame.display.flip()
