import pygame
import Animation

class Orc_L(Animation.animate_sprite):
    
    def __init__(self, Game, size):
        super().__init__("Orc_l", (300,300))
        self.max_hp = 100
        self.hp = 100
        self.attack_value = 25
        self.speed = 3
        self.attack_speed = 500
        self.rect = self.image.get_rect()
        self.rect.x = 30
        self.rect.y = 720
        self.visible = False
        self.player = 'player1'
        self.last_attack_time = 0
        self.alive = True
        self.Game = Game
        self.size = size
        self.start_animation()

    def move_right(self):
        if not self.Game.check_collision(self, self.Game.all_orcs_r):
            if not self.Game.check_collision(self, self.Game.group_base_r):
                self.rect.x += self.speed
        elif self.Game.check_collision(self, self.Game.all_orcs_r):
            self.attack_orc()


    def update_hp_bar(self, surface):
        bar_color = (111, 210, 46)
        back_bar_color = (60,60,60)
        bar_position = [self.rect.x+28, self.rect.y - 10, self.hp/3, 5]
        back_bar_position = [self.rect.x+28, self.rect.y - 10, self.max_hp/3, 5]
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)
        #update animation

    def update_animation(self):
        self.animate(loop=True)

    def damage(self, amount):
        self.hp -= amount

    def attack_orc(self):
        current_time = pygame.time.get_ticks()
        for orc_r in self.Game.check_collision(self, self.Game.all_orcs_r):
            if current_time - self.last_attack_time >= self.attack_speed:
                orc_r.damage(self.attack_value)
                self.last_attack_time = current_time

    def attack_base_r(self):
        current_time = pygame.time.get_ticks()
        for base_r in self.Game.check_collision(self, self.Game.group_base_r):
            if current_time - self.last_attack_time >= self.attack_speed:
                base_r.damage(self.attack_value)
                self.last_attack_time = current_time

    def collision_base_r(self):
        if self.Game.check_collision(self, self.Game.group_base_r):
            return True

    def death(self):
        if self.hp <= 0:
            self.alive = False
            self.kill()
            self.Game.group_base_r.sprites()[0].add_gold_orc()
            self.Game.group_base_r.sprites()[0].add_xp_orc()
            return True

            