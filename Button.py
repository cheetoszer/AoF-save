import pygame
# a class to create black squares of 50 px

class Button():
    def __init__(self, name, x, y, image):
        self.name = name
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (200,200))
        self.rect = self.image.get_rect(center=(x,y))
        self.rect.x = x
        self.rect.y = y

    def add_button(self, name, image_path, rect):
        Button = Button(name, image_path, rect)
        return Button
    

