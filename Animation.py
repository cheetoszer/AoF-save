import pygame
import os

class animate_sprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name, size):
        super().__init__()
        self.image = pygame.image.load(f'Asset/Perso/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image, size)
        self.size = size
        self.current_image = 0
        self.images = animations.get(sprite_name)
        self.animation = False

    def start_animation(self):
        self.animation = True

    def animate(self, loop=False):
        if self.animation:
            self.current_image += 1
            if self.current_image >= len(self.images):
                self.current_image = 0
                if loop is False:
                    self.animation = False
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)

'''    #methode pour animer le sprite
    def animate(self):
        #passer à l'image suivante
        self.current_image += 1
        #vérifier si on a atteint la fin de l'animation
        if self.current_image >= len(self.images):
            #remettre l'animation au début
                self.current_image = 0
        #modifier l'image du sprite
        self.image = self.images[self.current_image]
        self.image = pygame.transform.scale(self.image, self.size)
        #print(os.path.basename(image_path))   '''     

#fonction charger image sprite
def load_animation_images(sprite_name, nom_anim, num_image):
    #charger les images du d'animation dusprite
    images = []
    #recuperer le chemin du dossier du sprite
    path = f'Asset/Perso/{sprite_name}/{nom_anim}/{sprite_name}  ({num_image}).png'
    #boucle sur les images du dossier
    for num in range(1, num_image+1):
        images.append(pygame.image.load(path))
        print(images)
    return images
    
#definir dictionnaire images chargé sprite
animations = {
    'Orc_l' : load_animation_images('Orc_l', 'Move', 10),
    'Orc_r' : load_animation_images('Orc_r', 'Move', 10)    
}
