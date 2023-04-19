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

    def add_gold_orc(self):
        self.gold += 65
    
    def add_xp_orc(self):
        self.xp += 5

    def add_gold_age1(self):
        self.gold += 15

    def damage(self, amount):
        self.hp -= amount
    
    def evolve(self):
        self.age += 1
        self.image = pygame.image.load("le lien vers l'image de la base lvl 2")