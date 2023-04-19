import pygame
from Orc_L import *
from Button import *
from Game import *
from Barracks import *

pygame.init()

#Générer notre fenetre
pygame.display.set_caption("Age of War")
screen_info = pygame.display.Info()
screen_width, screen_height = screen_info.current_w, screen_info.current_h

#Plein écran
screen = pygame.display.set_mode((screen_width, screen_height))

# Charger l'image de fond et la redimensionner
bg_image = pygame.image.load('Asset/Test/map.png')
bg_image = pygame.transform.scale(bg_image, (1600,880))

# Charger Game
game = Game()

# Charger Button
button_orc = Button('orc', -57, 300, 'Asset/Perso/Orc_l.png' )
button_orc2 = Button('orc2', 1390, 300, 'Asset/Perso/Orc_r.png' )

# Charger time clock
clock = pygame.time.Clock()

# Boucle principale

running = True

while running:

    # Lisser mouvement
    clock.tick(60)

    # Afficher l'image de fond
    screen.blit(bg_image, (0,0))

    # Afficher les bases
    game.group_base_l.draw(screen)
    game.group_base_r.draw(screen)

    # Afficher les golds
    game.update_gold_text(screen)

    # Afficher l'xp
    game.update_xp_text(screen)

    # Afficher les Orcs
    game.all_orcs_l.draw(screen)
    game.all_orcs_r.draw(screen) 

    # Afficher les Strickers  
    game.all_strickers_l.draw(screen)
    game.all_strickers_r.draw(screen)

    # Afficher les Kings
    game.all_kings_l.draw(screen)
    game.all_kings_r.draw(screen)

    # Afficher les Ronins
    game.all_ronins_l.draw(screen)
    game.all_ronins_r.draw(screen)

    # Donner de l'or avec le temps
    game.give_gold_time()
    
    # Afficher base gauche
    for base_l in game.group_base_l:
        base_l.update_hp_bar(screen, 130) 

    # Afficher base droite
    for base_r in game.group_base_r:
        base_r.update_hp_bar(screen, 20)

    # Faire bouger les Orcs
    for orcs_l in game.all_orcs_l:
        orcs_l.move_right()
        orcs_l.update_hp_bar(screen)
        orcs_l.death()
        # Animer orc
        orcs_l.animate()
        if orcs_l.collision_base_r():
            orcs_l.attack_base_r()

    for orcs_r in game.all_orcs_r:
        orcs_r.move_right()
        orcs_r.update_hp_bar(screen)
        orcs_r.death()  
        # Animer orc 
 #       orcs_r.animate()
        if orcs_r.collision_base_l():
            orcs_r.attack_base_l()

    # Faire bouger les Strickers
    for stricker_l in game.all_strickers_l:
        stricker_l.move_right()
        stricker_l.update_hp_bar(screen)
        stricker_l.death()
        # Animer stricker
     #   stricker_l.animate()
        if stricker_l.collision_base_r():
            stricker_l.attack_base_r()

    for stricker_r in game.all_strickers_r:
        stricker_r.move_right()
        stricker_r.update_hp_bar(screen)
        stricker_r.death()
        # Animer stricker
     #   stricker_r.animate()
        if stricker_r.collision_base_l():
            stricker_r.attack_base_l()

    # Faire bouger les Kings
    for king_l in game.all_kings_l:
        king_l.move_right()
        king_l.update_hp_bar(screen)
        king_l.death()
        # Animer king
 #       king_l.animate()
        if king_l.collision_base_r():
            king_l.attack_base_r()

    for king_r in game.all_kings_r:
        king_r.move_right()
        king_r.update_hp_bar(screen)
        king_r.death()
        # Animer king
 #       king_r.animate()
        if king_r.collision_base_l():
            king_r.attack_base_l()

    # Faire bouger les Ronins
    for ronin_l in game.all_ronins_l:
        ronin_l.move_right()
        ronin_l.update_hp_bar(screen)
        ronin_l.death()
        # Animer ronin
  #      ronin_l.animate()
        if ronin_l.collision_base_r():
            ronin_l.attack_base_r()
    
    for ronin_r in game.all_ronins_r:
        ronin_r.move_right()
        ronin_r.update_hp_bar(screen)
        ronin_r.death()
        # Animer ronin
  #      ronin_r.animate()
        if ronin_r.collision_base_l():
            ronin_r.attack_base_l()

    # Afficher les boutons
    screen.blit(button_orc.image, (button_orc.rect))
    screen.blit(button_orc2.image, (button_orc2.rect))
    
    # Actualiser l'image
    pygame.display.flip()

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # Quiter avec echap       
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()

        # Boutons invoquer mob
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                game.spawn_orc_l()
            elif event.key == pygame.K_z:
                game.spawn_king_l()
            elif event.key == pygame.K_e:
                    game.spawn_stricker_l()
            elif event.key == pygame.K_r:
                game.spawn_ronin_l()
            elif event.key == pygame.K_t:
                game.next_age_l()
            elif event.key == pygame.K_1:
                game.spawn_orc_r()
            elif event.key == pygame.K_2:
                game.spawn_king_r()
            elif event.key == pygame.K_3:
                game.spawn_stricker_r()
            elif event.key == pygame.K_4:
                game.spawn_ronin_r()
            elif event.key == pygame.K_5:
                game.next_age_r()
        
