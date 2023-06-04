
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
    

    def run(self):
        while self.running:
            print("Game Running")
            time.sleep(1)

    def exit(self):
        print("Game Stop")
        self.running = False

