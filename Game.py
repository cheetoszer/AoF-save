import pygame
from Orc_L import *
from Orc_R import *
from Barracks import *
from Stricker_L import *
from Stricker_R import *
from King_L import *
from Ronin_L import *
from Ronin_R import *
from King_R import *
from Animation import *


class Game:

    def __init__(self):
        #base gauche 
        self.group_base_l = pygame.sprite.GroupSingle()
        #base droite 
        self.group_base_r = pygame.sprite.GroupSingle()
        #Générer les deux base au lancement du jeu
        self.spawn_barracks()
        #groupe orc gauche
        self.all_orcs_l = pygame.sprite.Group()
        #groupe orc droit
        self.all_orcs_r = pygame.sprite.Group()
        #groupe stricker gauche
        self.all_strickers_l = pygame.sprite.Group()
        #groupe stricker droit
        self.all_strickers_r = pygame.sprite.Group()
        #groupe king gauche
        self.all_kings_l = pygame.sprite.Group()
        #groupe king droit
        self.all_kings_r = pygame.sprite.Group()
        #groupe ronin gauche
        self.all_ronins_l = pygame.sprite.Group()
        #groupe ronin droit
        self.all_ronins_r = pygame.sprite.Group()
        #Typo pour texte
        self.font = pygame.font.Font(None, 30)
        #Dernier don gold
        self.last_give_time = 0

    def spawn_barracks(self):
        base_l = Barracks(-110, 630, 'Asset\Base\cave.png')
        self.group_base_l.add(base_l)
        base_r = Barracks(1290, 630,'Asset\Base\cave1.png')
        self.group_base_r.add(base_r)

    def spawn_orc_l(self):
        barracks = self.group_base_l.sprites()[0]
        # vérifier si le joueur a assez d'argent
        if barracks.gold >= 50:
            orcs_l = Orc_L(self, (230,230))
            self.all_orcs_l.add(orcs_l)
            # récupérer l'instance de Barracks de la base gauche
            barracks.buy_orc()

    def spawn_orc_r(self):
        barracks1 = self.group_base_r.sprites()[0]
        if barracks1.gold >= 50:
            orcs_r = Orc_R(self, (230,230))
            self.all_orcs_r.add(orcs_r)
            barracks1.buy_orc()

    def spawn_king_l(self):
        barracks = self.group_base_l.sprites()[0]
        if barracks.gold >= 50:
            king_l = King_l(self, (230,230))
            self.all_kings_l.add(king_l)
            barracks.buy_king()

    def spawn_king_r(self):
        barracks1 = self.group_base_r.sprites()[0]
        if barracks1.gold >= 50:
            king_r = King_r(self, (230,230))
            self.all_kings_r.add(king_r)
            barracks1.buy_king()

    def spawn_ronin_l(self):
        barracks = self.group_base_l.sprites()[0]
        if barracks.gold >= 50:
            ronin_l = Ronin_l(self, (230,230))
            self.all_ronins_l.add(ronin_l)
            barracks.buy_ronin()

    def spawn_ronin_r(self):
        barracks1 = self.group_base_r.sprites()[0]
        if barracks1.gold >= 50:
            ronin_r = Ronin_r(self, (230,230))
            self.all_ronins_r.add(ronin_r)
            barracks1.buy_ronin()
    
    def spawn_stricker_r(self):
        barracks1 = self.group_base_r.sprites()[0]
        if barracks1.gold >= 50:
            stricker_r = Stricker_r(self, (230,230))
            self.all_strickers_r.add(stricker_r)
            barracks1.buy_stricker()

    def spawn_stricker_l(self):
        barracks = self.group_base_l.sprites()[0]
        if barracks.gold >= 50:
            stricker_l = Stricker_l(self, (230,230))
            self.all_strickers_l.add(stricker_l)
            barracks.buy_stricker()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
    
    def update_gold_text(self,screen):
        # mettre à jour le texte affiché sur l'écran pour chaque base
        base_l = self.group_base_l.sprites()[0]
        base_r = self.group_base_r.sprites()[0]
        # ajouter des rectangle gris derrière le texte
        #pygame.draw.rect(screen, (0, 0, 0), (20, 20, 150, 60))
        #pygame.draw.rect(screen, (0, 0, 0), (1420, 20, 100, 30))
        # générer le texte à afficher
        gold_l_text = self.font.render("Gold: {}".format(base_l.gold), True, (255, 255, 255))
        gold_r_text = self.font.render("{} :Gold".format(base_r.gold), True, (255, 255, 255))
        # afficher le texte sur l'écran
        screen.blit(gold_l_text, (20, 20))
        screen.blit(gold_r_text, (1420, 20))

    def update_xp_text(self, screen):
        # mettre à jour le texte affiché sur l'écran pour chaque base
        base_l = self.group_base_l.sprites()[0]
        base_r = self.group_base_r.sprites()[0]
        xp_l_text = self.font.render("Xp: {}".format(base_l.xp), True, (255, 255, 255))
        xp_r_text = self.font.render("{} :Xp".format(base_r.xp), True, (255, 255, 255))
        # afficher le texte sur l'écran
        screen.blit(xp_l_text, (20, 50))
        screen.blit(xp_r_text, (1462, 50))

    def give_gold_time(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_give_time >= 2000:
            self.last_give_time = current_time
            barracks = self.group_base_l.sprites()[0]
            barracks1 = self.group_base_r.sprites()[0]
            if barracks.age == 1:
                barracks.add_gold_age1()
            if barracks1.age == 1:
                barracks1.add_gold_age1()

    def next_age_l(self):
        barracks = self.group_base_l.sprites()[0]
        if barracks.xp >= 100:
            barracks.evolve_l()

    def next_age_r(self):
        barracks1 = self.group_base_r.sprites()[0]
        if barracks1.xp >= 100:
            barracks1.evolve_r()
    