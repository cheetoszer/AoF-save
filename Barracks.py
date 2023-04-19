import pygame
from Game import *

class Barracks(pygame.sprite.Sprite):
    
    def __init__(self, x, y, image_path):
        super().__init__()
        self.max_hp = 1000
        self.hp = 1000
        self.attack_speed = 500
        self.gold = 500
        self.xp = 0
        self.age = 1
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image ,(350,220))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update_hp_bar(self, surface, x):
        bar_color = (111, 210, 46)
        back_bar_color = (60,60,60)
        bar_position = [self.rect.x+x, self.rect.y - 30, self.hp/5, 10]
        back_bar_position = [self.rect.x+x, self.rect.y - 30, self.max_hp/5, 10]
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def buy_orc(self):
        self.gold -= 50

    def buy_king(self):
        self.gold -= 100

    def buy_stricker(self):
        self.gold -= 200

    def buy_ronin(self):
        self.gold -= 400

    def add_gold_orc(self):
        self.gold += 25

    def add_gold_king(self):
        self.gold += 50

    def add_gold_stricker(self):
        self.gold += 100

    def add_gold_ronin(self):
        self.gold += 200
    
    def add_xp_orc(self):
        self.xp += 10

    def add_xp_king(self):
        self.xp += 20

    def add_xp_stricker(self):
        self.xp += 40
        
    def add_xp_ronin(self):
        self.xp += 80

    def add_gold_age1(self):
        self.gold += 15

    def add_gold_age2(self):
        self.gold += 50

    def damage(self, amount):
        self.hp -= amount
    
    def evolve_l(self):
        self.age += 1
        self.hp += 2000
        self.image = pygame.image.load("Asset\Base\cottage.png")
        self.image = pygame.transform.scale(self.image,(350,320))

    def evolve_r(self):
        self.age += 1
        self.hp += 2000
        self.image = pygame.image.load("Asset\Base\cottage1.png")
        self.image = pygame.transform.scale(self.image,(350,320))