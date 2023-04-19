import pygame
import Animation

class Stricker_r(Animation.animate_sprite):
    
    def __init__(self, Game, size):
        super().__init__("Stricker_r", (230,230))
        self.max_hp = 100
        self.hp = 100
        self.attack_value = 25
        self.speed = 3
        self.attack_speed = 500
        self.rect = self.image.get_rect()
        self.rect.x = 1300
        self.rect.y = 660
        self.visible = False
        self.player = 'player1'
        self.last_attack_time = 0
        self.alive = True
        self.Game = Game
        self.size = size
        self.start_animation()

    def move_right(self):
        if not self.Game.check_collision(self, self.Game.all_orcs_l):
            if not self.Game.check_collision(self, self.Game.all_kings_l):
                if not self.Game.check_collision(self, self.Game.all_strickers_l):
                    if not self.Game.check_collision(self, self.Game.all_ronins_l):   
                        if not self.Game.check_collision(self, self.Game.group_base_l):         
                            self.rect.x -= self.speed
                        else:
                            self.attack_base_l()
                    else:
                        self.attack_ronin()
                else:
                    self.attack_stricker()
            else:
                self.attack_king()
        else:
            self.attack_orc()


    def update_hp_bar(self, surface):
        bar_color = (111, 210, 46)
        back_bar_color = (60,60,60)
        bar_position = [self.rect.x+100, self.rect.y+40, self.hp/3, 5]
        back_bar_position = [self.rect.x+100, self.rect.y +40, self.max_hp/3, 5]
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)
        #update animation

    def update_animation(self):
        self.animate(loop=True)

    def damage(self, amount):
        self.hp -= amount
         # create red circles animation

    def attack_orc(self):
        current_time = pygame.time.get_ticks()
        for orc_r in self.Game.check_collision(self, self.Game.all_orcs_l):
            if current_time - self.last_attack_time >= self.attack_speed:
                orc_r.damage(self.attack_value)
                self.last_attack_time = current_time

    def attack_stricker(self):
        current_time = pygame.time.get_ticks()
        for stricker_r in self.Game.check_collision(self, self.Game.all_strickers_l):
            if current_time - self.last_attack_time >= self.attack_speed:
                stricker_r.damage(self.attack_value)
                self.last_attack_time = current_time

    def attack_ronin(self):
        current_time = pygame.time.get_ticks()
        for ronin_r in self.Game.check_collision(self, self.Game.all_ronins_l):
            if current_time - self.last_attack_time >= self.attack_speed:
                ronin_r.damage(self.attack_value)
                self.last_attack_time = current_time

    def attack_king(self):
        current_time = pygame.time.get_ticks()
        for king in self.Game.check_collision(self, self.Game.all_kings_l):
            if current_time - self.last_attack_time >= self.attack_speed:
                king.damage(self.attack_value)
                self.last_attack_time = current_time

    def attack_base_l(self):
        current_time = pygame.time.get_ticks()
        for base_r in self.Game.check_collision(self, self.Game.group_base_r):
            if current_time - self.last_attack_time >= self.attack_speed:
                base_r.damage(self.attack_value)
                self.last_attack_time = current_time

    def collision_base_l(self):
        if self.Game.check_collision(self, self.Game.group_base_r):
            return True

    def death(self):
        if self.hp <= 0:
            self.alive = False
            self.kill()
            self.Game.group_base_l.sprites()[0].add_gold_stricker()
            self.Game.group_base_l.sprites()[0].add_xp_stricker()
            return True

            