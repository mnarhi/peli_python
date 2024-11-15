#Pelaaja liikuttaa robottia nuolinäppäimillä.
#Ruudulla näkyy kolikko, joka robotin tulee kerätä. 
#Kun robotti saa kolikon, uusi kolikko ilmestyy uuteen paikkaan.
#Ruudulla on myös hirviöitä, joita robotin tulee väistellä. 
#Peli päättyy, mikäli robotti osuu hirviöön. 
#Peli on läpäisty, kun robotti on kerännyt yhteensä kymmenen kolikkoa. 
#Kolikkolaskuri nälyy peliruudun yläreunassa.

import pygame
import random

class Keraily:
    def __init__(self):
        pygame.init()
        
        
        self.uusi_peli()
        self.peli_paattynyt = False
        self.naytto = pygame.display.set_mode((640, 480))
        self.fontti = pygame.font.SysFont("Arial", 24)
        self.leveys = 640
        self.korkeus = 480
        self.robo = pygame.image.load("robo.png")
        self.robo_x = 0
        self.robo_y = 480-self.robo.get_height()
        self.kolikko = pygame.image.load("kolikko.png")
        self.kolikko_x = 0 + 3 * self.robo.get_width()
        self.kolikko_y = random.randint(40, 460)
        self.hirvio1 = pygame.image.load("hirvio.png")
        self.hirvio1_x = random.randint(20, 620)
        self.hirvio1_y = random.randint(40, 460)
        self.hirvio2 = pygame.image.load("hirvio.png")
        self.hirvio2_x = random.randint(20, 620)
        self.hirvio2_y = random.randint(40, 460)
        self.hirvio3 = pygame.image.load("hirvio.png")
        self.hirvio3_x = random.randint(20, 620)
        self.hirvio3_y = random.randint(40, 460)

        self.kello = pygame.time.Clock()

        pygame.display.set_caption("Kerää kymmenen kolikkoa")

        self.silmukka()


    def uusi_peli(self):
        self.peli_paattynyt = False
        self.kolikot = 0

  
    def silmukka(self):
        while True:
            self.hirvio1_x += random.randint(-2, 2)
            self.hirvio1_y += random.randint(-2, 2) 

            self.hirvio2_x += random.randint(-2, 2)
            self.hirvio2_y += random.randint(-2, 2)

            self.hirvio3_x += random.randint(-2, 2)
            self.hirvio3_y += random.randint(-2, 2)

            if self.hirvio1_x < 0:
                self.hirvio1_x = 0
            if self.hirvio1_x > self.leveys - self.hirvio1.get_width():
                self.hirvio1_x = self.leveys - self.hirvio1.get_width()
            if self.hirvio1_y < 0 + self.hirvio1.get_height():
                self.hirvio1_y = 0 + self.hirvio1.get_height()
            if self.hirvio1_y > self.korkeus - self.hirvio1.get_height():
                self.hirvio1_y = self.korkeus - self.hirvio1.get_height()

            if self.hirvio2_x < 0:
                self.hirvio2_x = 0
            if self.hirvio2_x > self.leveys - self.hirvio2.get_width():
                self.hirvio2_x = self.leveys - self.hirvio2.get_width()
            if self.hirvio2_y < 0 + self.hirvio2.get_height():
                self.hirvio2_y = 0 + self.hirvio2.get_height()
            if self.hirvio2_y > self.korkeus - self.hirvio2.get_height():
                self.hirvio2_y = self.korkeus - self.hirvio2.get_height()

            if self.hirvio3_x < 0:
                self.hirvio3_x = 0
            if self.hirvio3_x > self.leveys - self.hirvio3.get_width():
                self.hirvio3_x = self.leveys - self.hirvio3.get_width()
            if self.hirvio3_y < 0 + self.hirvio3.get_height():
                self.hirvio3_y = 0 + self.hirvio3.get_height()
            if self.hirvio3_y > self.korkeus - self.hirvio3.get_height():
                self.hirvio3_y = self.korkeus - self.hirvio3.get_height()

            self.tutki_tapahtumat()
            self.piirra_naytto()

    def tutki_tapahtumat(self):
        if self.peli_paattynyt:
            for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.KEYDOWN:
                    if tapahtuma.key == pygame.K_F2:
                        self.uusi_peli()
                    if tapahtuma.key == pygame.K_ESCAPE:
                        exit()
                if tapahtuma.type == pygame.QUIT:
                    exit()
        else:
            keys = pygame.key.get_pressed()
    
            if keys[pygame.K_LEFT]:
                self.vasemmalle()
            if keys[pygame.K_RIGHT]:
                self.oikealle()
            if keys[pygame.K_UP]:
                self.ylos()
            if keys[pygame.K_DOWN]:
                self.alas()
            for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.KEYDOWN:
                    if tapahtuma.key == pygame.K_F2:
                        self.uusi_peli()
                    if tapahtuma.key == pygame.K_ESCAPE:
                        exit()
                if tapahtuma.type == pygame.QUIT:
                    exit()
    

    def vasemmalle(self):
        self.kolikon_ilmestyminen()
        self.peli_lapi()
        self.game_over()
        if self.robo_x <= 0:
            pass
        else:
            self.robo_x += -2
    
    def oikealle(self):
        self.kolikon_ilmestyminen()
        self.peli_lapi()
        self.game_over()
        if self.robo_x + self.robo.get_width() >= 640:
            pass
        else:
            self.robo_x += 2

    def ylos(self):
        self.kolikon_ilmestyminen()
        self.peli_lapi()
        self.game_over()
        if self.robo_y <= 0 + self.robo.get_width():
            pass
        else:
            self.robo_y += -2
    
    def alas(self):
        self.kolikon_ilmestyminen()
        self.peli_lapi()
        self.game_over()
        if self.robo_y + self.robo.get_height() >= 480:
            pass
        else:
            self.robo_y += 2
    
    def kolikon_ilmestyminen(self): 
        if (self.robo_x < self.kolikko_x + self.kolikko.get_width() and self.robo_x + self.robo.get_width() > self.kolikko_x and self.robo_y < self.kolikko_y + self.kolikko.get_height() and self.robo_y + self.robo.get_height() > self.kolikko_y):
            self.kolikot += 1
            while True:
                uusi_x = random.randint(20, 600)
                uusi_y = random.randint(40, 420)
                collision = False
            
                if (abs(uusi_x - self.robo_x) < self.robo.get_width() and abs(uusi_y - self.robo_y) < self.robo.get_height()):
                    collision = True
                if (abs(uusi_x - self.hirvio1_x) < self.hirvio1.get_width() and abs(uusi_y - self.hirvio1_y) < self.hirvio1.get_height()):
                    collision = True
                if (abs(uusi_x - self.hirvio2_x) < self.hirvio2.get_width() and abs(uusi_y - self.hirvio2_y) < self.hirvio2.get_height()):
                    collision = True
                if (abs(uusi_x - self.hirvio3_x) < self.hirvio3.get_width() and abs(uusi_y - self.hirvio3_y) < self.hirvio3.get_height()):
                    collision = True

                if not collision:
                    self.kolikko_x = uusi_x
                    self.kolikko_y = uusi_y
                    break
            return True

    def game_over(self):
        if ((self.robo_x < self.hirvio1_x + self.hirvio1.get_width() and self.robo_x + self.robo.get_width() > self.hirvio1_x and self.robo_y < self.hirvio1_y + self.hirvio1.get_height() and self.robo_y + self.robo.get_height() > self.hirvio1_y) or (self.robo_x < self.hirvio2_x + self.hirvio2.get_width() and self.robo_x + self.robo.get_width() > self.hirvio2_x and self.robo_y < self.hirvio2_y + self.hirvio2.get_height() and self.robo_y + self.robo.get_height() > self.hirvio2_y) or
        (self.robo_x < self.hirvio3_x + self.hirvio3.get_width() and
        self.robo_x + self.robo.get_width() > self.hirvio3_x and
        self.robo_y < self.hirvio3_y + self.hirvio3.get_height() and
        self.robo_y + self.robo.get_height() > self.hirvio3_y)):
            self.peli_paattynyt = True
            return True
        else:
            return False

    

    def peli_lapi(self):
        if self.kolikot == 10:
            self.peli_paattynyt = True
            return True
        else:
            return False


    def piirra_naytto(self):
        self.naytto.fill((0, 100, 0))
        if self.peli_paattynyt:
            if self.peli_lapi():
                teksti = self.fontti.render("Onnittelut, läpäisit pelin! F2: Uusi peli, Esc: Lopeta", True, (0, 0, 0))
                teksti_x = self.leveys - (teksti.get_width() *1.1)
                teksti_y = self.korkeus / 2
                self.naytto.blit(teksti, (teksti_x, teksti_y))
            elif self.game_over():
                teksti = self.fontti.render("GAME OVER! F2: Uusi peli, Esc: Lopeta", True, (0, 0, 0))
                teksti_x = self.leveys - (teksti.get_width() * 1.3)
                teksti_y = self.korkeus / 2
                self.naytto.blit(teksti, (teksti_x, teksti_y))
        else:
            self.naytto.blit(self.robo, (self.robo_x, self.robo_y))
            self.naytto.blit(self.kolikko, (self.kolikko_x, self.kolikko_y))
            self.naytto.blit(self.hirvio1, (self.hirvio1_x, self.hirvio1_y))
            self.naytto.blit(self.hirvio2, (self.hirvio2_x, self.hirvio2_y))
            self.naytto.blit(self.hirvio3, (self.hirvio3_x, self.hirvio3_y))
        

            teksti = self.fontti.render("Kolikot: " + str(self.kolikot), True, (0, 0, 0))
            self.naytto.blit(teksti, (0, 0))
            
            teksti = self.fontti.render("F2 = uusi peli", True, (0, 0, 0))
            self.naytto.blit(teksti, (self.leveys / 3, 0))

            teksti = self.fontti.render("Esc = sulje peli", True, (0, 0, 0))
            self.naytto.blit(teksti, (self.leveys - teksti.get_width(), 0))
     
        pygame.display.flip()
        self.kello.tick(60)

if __name__ == "__main__":
    Keraily() 

