import pygame
import ConfigParser
from libreria import *

ANCHO=1280
ALTO=608
PIXEL_MURO=32
MAPA_COL=40
MAPA_FIL=18
MOV_RICK=32

class Jugador(Cuadro):
    lista_muros=None
    ls_zombies=None
    ls_murci=None
    ls_puerta=None
    ls_power=None
    ls_metas=None
    def __init__(self, archivo,x,y):
        pygame.sprite.Sprite.__init__(self) #Inicializo.
        self.fondo=self.Recortar(archivo,x,y)
        self.image=self.fondo[1][0]
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.cambiox=0
        self.cambioy=0
        self.nivel_vida=100

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


    def sinVida(self):
        if self.nivel_vida ==100:
            vi3=pygame.image.load('imagen/Vida.png').convert_alpha()
            pantalla.blit(vi3,(384,576))
            pygame.display.flip()
            vi2=pygame.image.load('imagen/Vida.png').convert_alpha()
            pantalla.blit(vi2,(320,576))
            pygame.display.flip()
            vi1=pygame.image.load('imagen/Vida.png').convert_alpha()
            pantalla.blit(vi1,(256,576))
            pygame.display.flip()
        if self.nivel_vida <= 99 and self.nivel_vida>=75:
            co3=pygame.image.load('imagen/SinVida.png').convert_alpha()
            pantalla.blit(co3,(384,576))
            pygame.display.flip()
            vi2=pygame.image.load('imagen/Vida.png').convert_alpha()
            pantalla.blit(vi2,(320,576))
            pygame.display.flip()
            vi1=pygame.image.load('imagen/Vida.png').convert_alpha()
            pantalla.blit(vi1,(256,576))
            pygame.display.flip()
        if self.nivel_vida <= 74 and self.nivel_vida>=50:
            co3=pygame.image.load('imagen/SinVida.png').convert_alpha()
            pantalla.blit(co3,(384,576))
            pygame.display.flip()
            co2=pygame.image.load('imagen/SinVida.png').convert_alpha()
            pantalla.blit(co2,(320,576))
            pygame.display.flip()
            vi1=pygame.image.load('imagen/Vida.png').convert_alpha()
            pantalla.blit(vi1,(256,576))
            pygame.display.flip()
        if self.nivel_vida <= 49:
            co3=pygame.image.load('imagen/SinVida.png').convert_alpha()
            pantalla.blit(co3,(384,576))
            pygame.display.flip()
            co2=pygame.image.load('imagen/SinVida.png').convert_alpha()
            pantalla.blit(co2,(320,576))
            pygame.display.flip()
            co1=pygame.image.load('imagen/SinVida.png').convert_alpha()
            pantalla.blit(co1,(256,576))
            pygame.display.flip()

    def menosVida(self):
        self.nivel_vida=self.nivel_vida-25

    def direccion(self, pos,con):
        if pos==1: #Arriba
            self.image=self.fondo[con][3]
            pantalla.blit(self.image,(self.cambiox,self.cambioy))
            self.cambioy=-MOV_RICK
            self.cambiox=0
        if pos==2: #Abajo
            self.image=self.fondo[con][0]
            pantalla.blit(self.image,(self.cambiox,self.cambioy))
            self.cambioy=MOV_RICK
            self.cambiox=0
        if pos==3: #Derecha
            self.image=self.fondo[con][1]
            pantalla.blit(self.image,(self.cambiox,self.cambioy))
            self.cambiox=-MOV_RICK
            self.cambioy=0
        if pos==4: #Izquierda
            self.image=self.fondo[con][2]
            pantalla.blit(self.image,(self.cambiox,self.cambioy))
            self.cambiox=MOV_RICK
            self.cambioy=0

    def direccionBP(self, pos,con):
        if pos==1: #Arriba
            self.image=self.fondo[con][7]
            pantalla.blit(self.image,(self.cambiox,self.cambioy))
            self.cambioy=-MOV_RICK
            self.cambiox=0
        if pos==2: #Abajo
            self.image=self.fondo[con][4]
            pantalla.blit(self.image,(self.cambiox,self.cambioy))
            self.cambioy=MOV_RICK
            self.cambiox=0
        if pos==3: #Derecha
            self.image=self.fondo[con][5]
            pantalla.blit(self.image,(self.cambiox,self.cambioy))
            self.cambiox=-MOV_RICK
            self.cambioy=0
        if pos==4: #Izquierda
            self.image=self.fondo[con][6]
            pantalla.blit(self.image,(self.cambiox,self.cambioy))
            self.cambiox=MOV_RICK
            self.cambioy=0

    def Recortar(self, archivo, ancho, alto):
        self.imagen=pygame.image.load(archivo).convert_alpha()
        img_ancho, img_alto=self.imagen.get_size()
        tabla_fondos=[]
        for fondo_x in range(0,img_ancho/ancho):
            linea=[]
            tabla_fondos.append(linea)
            for fondo_y in range(0,img_alto/alto):
                cuadro=(fondo_x*ancho,fondo_y*alto,ancho,alto)
                linea.append(self.imagen.subsurface(cuadro))
        return tabla_fondos

class Gobernador(Cuadro):
    def __init__(self, archivo,x,y):
        pygame.sprite.Sprite.__init__(self) #Inicializo.
        self.fondo=self.Recortar(archivo,32,32)
        self.image=self.fondo[0][1]
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.var_y=2

    def Recortar(self, archivo, ancho, alto):
        self.imagen=pygame.image.load(archivo).convert_alpha()
        img_ancho, img_alto=self.imagen.get_size()
        self.tabla_fondos=[]
        for fondo_x in range(0,img_ancho/ancho):
            linea=[]
            self.tabla_fondos.append(linea)
            for fondo_y in range(0,img_alto/alto):
                cuadro=(fondo_x*ancho,fondo_y*alto,ancho,alto)
                linea.append(self.imagen.subsurface(cuadro))
        return self.tabla_fondos

    def update(self):
        self.rect.y+=self.var_y
        if self.rect.y>512:
            self.image=self.fondo[0][1]
            self.var_y=-2
        elif self.rect.y <= 448:
            self.image=self.fondo[0][1]
            self.var_y=2

class Bala(Cuadro):
    def __init__(self, x, y):
        Cuadro.__init__(self, 5, 10, ROJO)
        self.rect.x=x
        self.rect.y=y
        self.dir=0

    def update(self):
        if self.dir==0:
            self.rect.x+=20
            #self.rect.y+=10

class EnemigoZ(Cuadro):
    def __init__(self, archivo,x,y,varx,vary,v,ran_su,ran_inf,band):
        pygame.sprite.Sprite.__init__(self) #Inicializo.
        self.fondo=self.Recortar(archivo,32,32)
        self.image=self.fondo[0][0]
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.var_y=vary
        self.var_x=varx
        self.ran_su=ran_su
        self.ran_inf=ran_inf
        self.v=v
        self.band=band

    def Recortar(self, archivo, ancho, alto):
        self.imagen=pygame.image.load(archivo).convert_alpha()
        img_ancho, img_alto=self.imagen.get_size()
        self.tabla_fondos=[]
        for fondo_x in range(0,img_ancho/ancho):
            linea=[]
            self.tabla_fondos.append(linea)
            for fondo_y in range(0,img_alto/alto):
                cuadro=(fondo_x*ancho,fondo_y*alto,ancho,alto)
                linea.append(self.imagen.subsurface(cuadro))
        return self.tabla_fondos

    def update(self):
        if(self.band==1):
            self.rect.y+=self.var_y
            if self.rect.y>self.ran_inf:
                self.image=self.fondo[0][2]
                self.var_y=-self.v
            if self.rect.y <= self.ran_su:
                self.image=self.fondo[0][0]
                self.var_y=self.v
        if (self.band==0):
            self.rect.x+=self.var_x
            if self.rect.x>self.ran_inf:
                self.image=self.fondo[0][2]
                self.var_x=-self.v
            if self.rect.x <= self.ran_su:
                self.image=self.fondo[0][0]
                self.var_x=self.v

class EnemigoM(Cuadro):
    def __init__(self, archivo,x,y):
        pygame.sprite.Sprite.__init__(self) #Inicializo.
        self.fondo=self.Recortar(archivo,32,32)
        self.image=self.fondo[0][0]
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.var_x=5

    def Recortar(self, archivo, ancho, alto):
        self.imagen=pygame.image.load(archivo).convert_alpha()
        img_ancho, img_alto=self.imagen.get_size()
        self.tabla_fondos=[]
        for fondo_x in range(0,img_ancho/ancho):
            linea=[]
            self.tabla_fondos.append(linea)
            for fondo_y in range(0,img_alto/alto):
                cuadro=(fondo_x*ancho,fondo_y*alto,ancho,alto)
                linea.append(self.imagen.subsurface(cuadro))
        return self.tabla_fondos

    def update(self):
        self.rect.x+=self.var_x
        if self.rect.x>1216:
            self.image=self.fondo[1][0]
            self.var_x=-5
        elif self.rect.x <= 832:
            self.image=self.fondo[0][0]
            self.var_x=5

class EnemigoM2(Cuadro):
    def __init__(self, archivo,x,y):
        pygame.sprite.Sprite.__init__(self) #Inicializo.
        self.fondo=self.Recortar(archivo,32,32)
        self.image=self.fondo[0][0]
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.var_x=10

    def Recortar(self, archivo, ancho, alto):
        self.imagen=pygame.image.load(archivo).convert_alpha()
        img_ancho, img_alto=self.imagen.get_size()
        self.tabla_fondos=[]
        for fondo_x in range(0,img_ancho/ancho):
            linea=[]
            self.tabla_fondos.append(linea)
            for fondo_y in range(0,img_alto/alto):
                cuadro=(fondo_x*ancho,fondo_y*alto,ancho,alto)
                linea.append(self.imagen.subsurface(cuadro))
        return self.tabla_fondos

    def update(self):
        self.rect.x+=self.var_x
        if self.rect.x>1216:
            self.image=self.fondo[1][0]
            self.var_x=-10
        elif self.rect.x <= 832:
            self.image=self.fondo[0][0]
            self.var_x=10

class Muro(Cuadro):
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
                muro=int(self.interprete.get(c,"muros"))
                cuadro_sel=self.fondo[x][y]
                self.lss_muros.append([x,y])
                pantalla.blit(cuadro_sel,[con_x,con_y])
                con_x+=var_x
            con_y+=var_y
        return self.lss_muros

class Power(Cuadro):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

if __name__ == '__main__':
    #Pantalla
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pantalla.fill(BLANCO)

    #Fuentes
    font = pygame.font.Font('fuente/zombie.otf', 100)
    pausa = font.render("P A U S E", True, BLANCO)

    font2 = pygame.font.Font('fuente/zombie.otf', 30)
    pres = font2.render("Press 'P' to continue...", True, BLANCO)

    font3 = pygame.font.Font('fuente/zombie.otf', 15)
    lif = font3.render("L i f e : ", True, NEGRO)

    font4 = pygame.font.Font('fuente/zombie.otf', 30)
    ap = font4.render("Z O M B I E", True, NEGRO)

    font5 = pygame.font.Font('fuente/zombie.otf', 30)
    dawn = font5.render(" R A C E", True, NEGRO)

    font6 = pygame.font.Font('fuente/zombie.otf', 100)
    you = font6.render("Y O U  W I N", True, BLANCO)

    font7 = pygame.font.Font('fuente/zombie.otf', 100)
    over = font7.render("GAME OVER", True, BLANCO)
    #Fondo
    fondo = pygame.image.load("imagen/gris1.png").convert()
    pantalla.blit(fondo, (0, 0))
    nivel1=Nivel('niveles.map')
    ls_muros=nivel1.Dibujar(pantalla)
    pygame.display.flip()

    #Grupo Jugador
    rick2=pygame.image.load('imagen/Rick(1).png').convert_alpha()
    pantalla.blit(rick2,(32,32))
    pygame.display.flip()
    jp=Jugador('imagen/RickBox.png',32,32)
    jugador=pygame.sprite.Group()
    jugador.add(jp)
    todos=pygame.sprite.Group()
    todos.add(jp)

    #Grupo Gobernador
    JefeFinal=pygame.sprite.Group()
    gober=Gobernador('imagen/gobernador.png',608,480)
    JefeFinal.add(gober)
    todos.add(gober)


    #Grupos
    muros=pygame.sprite.Group()
    barrera=pygame.sprite.Group()
    balas=pygame.sprite.Group()
    metas=pygame.sprite.Group()
    puertas=pygame.sprite.Group()
    cajas=pygame.sprite.Group()
    zombies=pygame.sprite.Group()
    murcielagos=pygame.sprite.Group()


    #Grupo Enemigo(zombie)
    zo=EnemigoZ('imagen/Zombie.png',288,32,0,5,10,32,352,1)
    zombies.add(zo)
    todos.add(zo)

    zo2=EnemigoZ('imagen/Zombie.png',192,416,0,2,2,416,448,1)
    zombies.add(zo2)
    todos.add(zo2)

    zo3=EnemigoZ('imagen/Zombie.png',256,448,0,-2,2,416,448,1)
    zombies.add(zo3)
    todos.add(zo3)

    zo4=EnemigoZ('imagen/Zombie.png',320,416,0,2,2,416,448,1)
    zombies.add(zo4)
    todos.add(zo4)
    ##
    zo7=EnemigoZ('imagen/Zombie.png',32,96,2,0,2,32,64,0)
    zombies.add(zo7)
    todos.add(zo7)

    zo5=EnemigoZ('imagen/Zombie.png',352,256,-2,0,2,352,416,0)
    zombies.add(zo5)
    todos.add(zo5)

    zo6=EnemigoZ('imagen/Zombie.png',416,160,2,0,2,352,416,0)
    zombies.add(zo6)
    todos.add(zo6)

    #Grupo Enemigo(murcielago)
    #enemigos2=pygame.sprite.Group()
    mu=EnemigoM('imagen/Murciela.png',864,224)
    murcielagos.add(mu)
    todos.add(mu)

    #Grupo Enemigo(murcielago)
    mu2=EnemigoM2('imagen/Murciela.png',1216,320)
    murcielagos.add(mu2)
    todos.add(mu2)

    ca=Power('imagen/guante.png',128,416)
    cajas.add(ca)
    todos.add(ca)

    j=0
    while j<ALTO:
        i=0
        while i<ANCHO:
            yjp=(j/PIXEL_MURO)
            xjp=(i/PIXEL_MURO)+(MAPA_COL*yjp)
            if(ls_muros[xjp][0]==2 and ls_muros[xjp][1]==0):
                m=Muro(i,j,2,0)
                muros.add(m)
                todos.add(m)
            if(ls_muros[xjp][0]==3 and ls_muros[xjp][1]==0):
                m=Muro(i,j,3,0)
                muros.add(m)
                todos.add(m)
            if(ls_muros[xjp][0]==0 and ls_muros[xjp][1]==0):
                m=Muro(i,j,0,0)
                muros.add(m)
                todos.add(m)
            if(ls_muros[xjp][0]==1 and ls_muros[xjp][1]==0):
                m=Muro(i,j,1,0)
                muros.add(m)
                todos.add(m)
            if(ls_muros[xjp][0]==0 and ls_muros[xjp][1]==2):
                m=Muro(i,j,0,2)
                muros.add(m)
                todos.add(m)
            if(ls_muros[xjp][0]==1 and ls_muros[xjp][1]==2):
                m=Muro(i,j,1,2)
                muros.add(m)
                todos.add(m)
            if(ls_muros[xjp][0]==0 and ls_muros[xjp][1]==1):
                m=Muro(i,j,0,1)
                muros.add(m)
                todos.add(m)
            if(ls_muros[xjp][0]==1 and ls_muros[xjp][1]==1):
                m=Muro(i,j,1,1)
                muros.add(m)
                todos.add(m)
            if(ls_muros[xjp][0]==9 and ls_muros[xjp][1]==0):
                ba=Muro(i,j,9,0)
                barrera.add(ba)
                todos.add(ba)
            if(ls_muros[xjp][0]==9 and ls_muros[xjp][1]==1):
                ba1=Muro(i,j,9,1)
                barrera.add(ba1)
                todos.add(ba1)
            if(ls_muros[xjp][0]==9 and ls_muros[xjp][1]==2):
                ba2=Muro(i,j,9,2)
                barrera.add(ba2)
                todos.add(ba2)
            if(ls_muros[xjp][0]==4 and ls_muros[xjp][1]==1):
                me=Muro(i,j,4,1)
                metas.add(me)
                todos.add(me)
            if(ls_muros[xjp][0]==5 and ls_muros[xjp][1]==2):
                pu=Muro(i,j,5,2)
                puertas.add(pu)
                todos.add(pu)
            i=i+PIXEL_MURO
        j=j+PIXEL_MURO

    jp.lista_muros=muros
    jp.ls_murci=murcielagos
    jp.ls_zombies=zombies
    jp.ls_puerta=puertas
    jp.ls_power=cajas
    jp.ls_metas=metas

    reloj=pygame.time.Clock()
    con=0
    fin=False
    BoxPower=False
    texto=False
    vida=0
    conb=0
    META=0
    PAUSE=False
    WIN=False
    GAMEOVER=False

    #########################

    while not fin:
        if jp.nivel_vida < 0:
            GAMEOVER=True
        #Bala Gobernador
        for m in range(600):
            if conb==10000:
                b=Bala(gober.rect.x+10,gober.rect.y+10)
                todos.add(b)
                balas.add(b)
                conb=0
                if b.rect.x>1152:
                    balas.remove(b)
                    todos.remove(b)
            conb+=1

        #Desaparece balas
        for b in balas:
            l_gb2=pygame.sprite.spritecollide(b,barrera,False)
            for m in l_gb2:
                balas.remove(b)
                todos.remove(b)

        if BoxPower == False:

            ls_pue = pygame.sprite.spritecollide(jp,jp.ls_puerta,False)###########33
            for m in ls_pue:
                pygame.mixer.music.load("sonido/knock.wav")
                pygame.mixer.music.play(1)
                if jp.cambioy > 0:
                    jp.rect.bottom=m.rect.top
                else:
                    jp.rect.top=m.rect.bottom

            ls_golpesz = pygame.sprite.spritecollide(jp,jp.ls_zombies,False)
            for m in ls_golpesz:
                if vida==6:
                    jp.menosVida()
                    pygame.mixer.music.load("sonido/zombi.wav")
                    pygame.mixer.music.play(1)
                    vida=0
                vida+=1
                break

            ls_golpesm = pygame.sprite.spritecollide(jp,jp.ls_murci,False)
            for m in ls_golpesm:
                if vida==6:
                    jp.menosVida()
                    pygame.mixer.music.load("sonido/bat.wav")
                    pygame.mixer.music.play(1)
                    vida=0
                vida+=1
                break

            ls_cajas=pygame.sprite.spritecollide(jp,cajas,True)
            for md in ls_cajas:
                jp.image=jp.fondo[1][4]
                BoxPower=True
                pygame.mixer.music.load("sonido/box.wav")
                pygame.mixer.music.play(1)



        if BoxPower == True:

            ls_pue = pygame.sprite.spritecollide(jp,jp.ls_puerta,False)############
            for m in ls_pue:
                pygame.mixer.music.load("sonido/door.wav")
                pygame.mixer.music.play(1)


            ls_golpesz = pygame.sprite.spritecollide(jp,jp.ls_zombies,True)
            for m in ls_golpesz:
                zombies.remove(m)
                todos.remove(m)

            ls_golpesm = pygame.sprite.spritecollide(jp,jp.ls_murci,False)
            for m in ls_golpesm:
                if vida==6:
                    jp.menosVida()
                    pygame.mixer.music.load("sonido/bat.wav")
                    pygame.mixer.music.play(1)
                    vida=0
                vida+=1
                break

            for b in balas:
                l_gb=pygame.sprite.spritecollide(b,jugador,False)
                for m in l_gb:
                    #if vida==1:
                    print "antes", jp.nivel_vida
                    jp.menosVida()
                    print "des", jp.nivel_vida
                #        vida=0
                #    vida+=1
                    balas.remove(b)
                    todos.remove(b)


            ls_me=pygame.sprite.spritecollide(jp,jp.ls_metas,False)
            for m in ls_me:
                META+=1
                jp.rect.x=1216
                jp.rect.y=480
                if META ==3:
                    WIN=True


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if con < 2:
                        con+=1
                    else:
                        con=0
                    if BoxPower == False:
                        jp.direccion(1,con)
                    else:
                        jp.direccionBP(1,con)
                if event.key == pygame.K_DOWN:
                    if con < 2:
                        con+=1
                    else:
                        con=0
                    if BoxPower == False:
                        jp.direccion(2,con)
                    else:
                        jp.direccionBP(2,con)
                if event.key == pygame.K_LEFT:
                    if con < 2:
                        con+=1
                    else:
                        con=0
                    if BoxPower == False:
                        jp.direccion(3,con)
                    else:
                        jp.direccionBP(3,con)
                if event.key == pygame.K_RIGHT:
                    if con < 2:
                        con+=1
                    else:
                        con=0
                    if BoxPower == False:
                        jp.direccion(4,con)
                    else:
                        jp.direccionBP(4,con)
                if event.key == pygame.K_p:
                    if PAUSE == False and WIN== False and GAMEOVER== False:
                        pygame.mixer.music.load("sonido/pause.wav")
                        pygame.mixer.music.play(1)
                        PAUSE = True
                    else:
                        if PAUSE == True:
                            print "quitar pausa"
                            pygame.mixer.music.load("sonido/despause.wav")
                            pygame.mixer.music.play(1)
                            PAUSE = False
            if event.type == pygame.KEYUP:
                jp.cambiox=0
                jp.cambioy=0

        if PAUSE==False and WIN==False and GAMEOVER == False:
            fondo = pygame.image.load("imagen/gris1.png").convert()
            pantalla.blit(fondo, (0, 0))
            pantalla.blit(lif, [160, 576])
            pantalla.blit(ap, [32, 192])
            pantalla.blit(dawn, [64, 256])
            nivel1=Nivel('niveles.map')
            nivel1.Dibujar(pantalla)
            pygame.display.flip()

            todos.update()
            todos.draw(pantalla)
            pygame.display.flip()

        else:
            if PAUSE == True:
                pantalla.blit(pausa, [386, 160])
                pantalla.blit(pres, [450, 416])
                pantalla.blit(lif, [160, 576])
                pygame.display.flip()
            if WIN == True:
                pantalla.blit(you, [322, 160])
            if GAMEOVER==True:
                pygame.mixer.music.stop()
                pantalla.blit(over, [322, 160])


        jp.sinVida()
        reloj.tick(60)
