import pygame
import ConfigParser
from libreria import *

ANCHO=1344
ALTO=680

class Jugador(Cuadro):
    lista_muros=None
    def __init__(self, archivo,x,y):
        pygame.sprite.Sprite.__init__(self) #Inicializo.
        self.fondo=self.Recortar(archivo,x,y)
        self.image=self.fondo[0][0]
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.cambiox=32
        self.cambioy=32

    def update(self):
        self.rect.x+=self.cambiox
        ls_golpes = pygame.sprite.spritecollide(self,self.lista_muros,False)
        for m in ls_golpes:
            if self.cambiox > 0:
                self.rect.right=m.rect.left
            else:
                self.rect.left=m.rect.right

        self.rect.y+=self.cambioy
        ls_golpes = pygame.sprite.spritecollide(self,self.lista_muros,False)
        for m in ls_golpes:
            if self.cambioy > 0:
                self.rect.bottom=m.rect.top
            else:
                self.rect.top=m.rect.bottom

    def direccion(self, pos,con):
        if pos==1: #Arriba
            self.image=self.fondo[con][3]
            pantalla.blit(self.image,(self.cambiox,self.cambioy))
            self.cambioy=-32
            self.cambiox=0
        if pos==2: #Abajo
            self.image=self.fondo[con][0]
            pantalla.blit(self.image,(self.cambiox,self.cambioy))
            self.cambioy=32
            self.cambiox=0
        if pos==3: #Derecha
            self.image=self.fondo[con][1]
            pantalla.blit(self.image,(self.cambiox,self.cambioy))
            self.cambiox=-32
            self.cambioy=0
        if pos==4: #Izquierda
            self.image=self.fondo[con][2]
            pantalla.blit(self.image,(self.cambiox,self.cambioy))
            self.cambiox=32
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

class Muro(Cuadro):
    lista=None
    def __init__(self,x,y,imgx,imgy):
        pygame.sprite.Sprite.__init__(self)
        self.image=nivel1.tabla_fondos[imgx][imgy]
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y


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
        self.imagen=pygame.image.load(archivo).convert_alpha()
        img_ancho, img_alto=self.imagen.get_size()
        #print img_ancho, ' ',img_alto
        self.tabla_fondos=[]
        for fondo_x in range(0,img_ancho/ancho):
            linea=[]
            self.tabla_fondos.append(linea)
            for fondo_y in range(0,img_alto/alto):
                cuadro=(fondo_x*ancho,fondo_y*alto,ancho,alto)
                linea.append(self.imagen.subsurface(cuadro))
        return self.tabla_fondos

    def Dibujar(self,pantalla):
        var_x=self.ancho
        var_y=self.alto
        con_y=0
        self.lss_muros=[]
        for fila in self.mapa:
            con_x=0
            for c in fila:
                x=int(self.interprete.get(c,"x"))
                y=int(self.interprete.get(c,"y"))
                muro=int(self.interprete.get(c,"muro"))
                cuadro_sel=self.fondo[x][y]
                self.lss_muros.append([x,y])
                pantalla.blit(cuadro_sel,[con_x,con_y])
                con_x+=var_x
            con_y+=var_y
        return self.lss_muros


if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pantalla.fill(BLANCO)

    fondo = pygame.image.load("imagen/gris.jpg").convert()
    pantalla.blit(fondo, (0, 0))
    nivel1=Nivel('niveles.map')
    ls_muros=nivel1.Dibujar(pantalla)
    pygame.display.flip()

    jp=Jugador('imagen/Rick.png',32,32)
    todos=pygame.sprite.Group()
    todos.add(jp)

    muros=pygame.sprite.Group()
    print ls_muros
    j=0
    while j<672:
        i=0
        while i<1344:
            print " "
            print "x",i,"y",j
            yjp=(j/32)
            xx=(i/32)
            xjp=(i/32)+(42*yjp)
            if(ls_muros[xjp][0]==2 and ls_muros[xjp][1]==0):
                print "entra: ", i,' ',j
                m=Muro(i,j,2,0)
                muros.add(m)
                todos.add(m)
            if(ls_muros[xjp][0]==3 and ls_muros[xjp][1]==0):
                print "entra: ", i,' ',j
                m=Muro(i,j,3,0)
                muros.add(m)
                todos.add(m)
            if(ls_muros[xjp][0]==0 and ls_muros[xjp][1]==0):
                print "entra: ", i,' ',j
                m=Muro(i,j,0,0)
                muros.add(m)
                todos.add(m)
            if(ls_muros[xjp][0]==1 and ls_muros[xjp][1]==0):
                print "entra: ", i,' ',j
                m=Muro(i,j,1,0)
                muros.add(m)
                todos.add(m)
            if(ls_muros[xjp][0]==0 and ls_muros[xjp][1]==2):
                print "entra: ", i,' ',j
                m=Muro(i,j,0,2)
                muros.add(m)
                todos.add(m)
            if(ls_muros[xjp][0]==1 and ls_muros[xjp][1]==2):
                print "entra: ", i,' ',j
                m=Muro(i,j,1,2)
                muros.add(m)
                todos.add(m)
            if(ls_muros[xjp][0]==0 and ls_muros[xjp][1]==1):
                print "entra: ", i,' ',j
                m=Muro(i,j,0,1)
                muros.add(m)
                todos.add(m)
            if(ls_muros[xjp][0]==1 and ls_muros[xjp][1]==1):
                print "entra: ", i,' ',j
                m=Muro(i,j,1,1)
                muros.add(m)
                todos.add(m)
            i=i+32
        j=j+32
    print "sali"

    jp.lista_muros=muros

    reloj=pygame.time.Clock()

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
                    jp.direccion(1,con)
                if event.key == pygame.K_DOWN:
                    if con < 2:
                        con+=1
                    else:
                        con=0
                    jp.direccion(2,con)
                if event.key == pygame.K_LEFT:
                    if con < 2:
                        con+=1
                    else:
                        con=0
                    jp.direccion(3,con)
                if event.key == pygame.K_RIGHT:
                    if con < 2:
                        con+=1
                    else:
                        con=0
                    jp.direccion(4,con)

                fondo = pygame.image.load("imagen/gris.jpg").convert()
                pantalla.blit(fondo, (0, 0))

                todos.update()
                todos.draw(pantalla)
                pygame.display.flip()

                nivel1=Nivel('niveles.map')
                nivel1.Dibujar(pantalla)
                pygame.display.flip()


                reloj.tick(60)
