import pygame 
import time
from windowClass import Window
from handlerClass import Handler
from gameObjectClass import GameObject
import gameObjectClass
from playerClass import Player

class Game():
    def __init__(self):
        self.fpsTime = 0
        self.clock = pygame.time.Clock()
        self.tickTime = 0
        self.fps = 0
        self.tps = 60
        self.msPerTick = 1000 / self.tps
        self.running = False
        self.window = Window(640, 480, "Game", self)
        self.graphics = self.window.SCREEN
        self.handler = Handler()
        gameObjectClass.init(self.window.getWidth(), self.window.getHeight(), self.handler)
        self.handler.addObject(Player(200, 200, "Player"))

    def start(self):
        self.running = True
        
    def tick(self):
        self.handler.tick()

    def run(self):
        if self.running:
            current = self.clock.tick()
            self.fpsTime += current
            self.tickTime += current
            self.fps += 1
            if self.fpsTime >= 1000:
                self.fpsTime = self.fpsTime - 1000
                print("FPS: " + str(self.fps))
                self.fps = 0
            if self.tickTime >= self.msPerTick:
                self.tickTime = self.tickTime - self.msPerTick
                self.tick()
            self.window.exit()
            self.render()

    def render(self):
        self.graphics.fill((0, 0, 0))
        self.handler.render(self.graphics)
        pygame.display.update()

game = Game()

while True:
    game.run()