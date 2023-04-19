import pygame
from Orc_L import *
from Orc_R import *
from Barracks import *

class Game:

    def __init__(self):
        #base gauche 
        self.group_base_l = pygame.sprite.GroupSingle()
        #base droite 
        self.group_base_r = pygame.sprite.GroupSingle()
        #Générer les deux base au lancement du jeu
        self.spawn_barracks()
        self.spawn_orc_l
        #groupe orc gauche
        self.all_orcs_l = pygame.sprite.Group()
        #groupe orc droit
        self.all_orcs_r = pygame.sprite.Group()
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
            orcs_l = Orc_L(self, (200,200))
            self.all_orcs_l.add(orcs_l)
            # récupérer l'instance de Barracks de la base gauche
            barracks.buy_orc()

    def spawn_orc_r(self):
        barracks1 = self.group_base_r.sprites()[0]
        if barracks1.gold >= 50:
            orcs_r = Orc_R(self, (200,200))
            self.all_orcs_r.add(orcs_r)
            barracks1.buy_orc()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
    
    def update_gold_text(self,screen):
        # mettre à jour le texte affiché sur l'écran pour chaque base
        base_l = self.group_base_l.sprites()[0]
        base_r = self.group_base_r.sprites()[0]
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

    