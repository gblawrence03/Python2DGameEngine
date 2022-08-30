import pygame

class Handler():
    def __init__(self):
        self.objects = []

    def addObject(self, obj):
        self.objects.append(obj)

    def deleteObject(self, obj):
        self.objects.remove(obj)
        del obj

    def tick(self):
        for each in self.objects:
            each.tick(pygame.event.get(), pygame.key.get_pressed())

    def render(self, graphics):
        for each in self.objects:
            each.render(graphics)