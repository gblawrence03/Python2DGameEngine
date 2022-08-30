import pygame

# Window class wrapper allowing easy creation of a window 
class Window():
    def __init__(self, width, height, title, game):
        self.width = width
        self.height = height
        self.SCREEN = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        game.start()

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def exit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()