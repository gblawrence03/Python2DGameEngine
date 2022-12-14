from gameObjectClass import GameObject
import pygame

# Example Player class
class Player(GameObject):
    def __init__(self, x, y, ID):
        super().__init__(x, y, ID)

    def render(self, graphics):
        pygame.draw.rect(graphics, (255, 255, 255), (200, 200, 10, 10))

    def tick(self, *args):
        # User input handling, physics, computation goes here
        pass