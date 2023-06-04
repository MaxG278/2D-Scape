import pygame
import time

class Game:
    running = False
    _instance = False
    

    @staticmethod
    def get():
        if not Game._instance:
            Game()
        return Game._instance

    def __init__(self):
        if Game._instance:
            raise Exception("This class is a singleton")
        else:
            Game._instance = self

    
    def start(self):
        print("Game started")
        self.running = True
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("2D-Scape")
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.screen.fill("purple")
    

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            pygame.display.flip()
            self.dt = self.clock.tick(60) / 1000

    def exit(self):
        print("Game Stop")
        self.running = False


    