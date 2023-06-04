"""
eine klasse mit dem namen game, die soll eine funktion run eine funktion start und exit
 haben
die sollten erst einmal leer sein. Die soll eine variable running haben, 
und diese sollen in der run.py initialisiert werden.
"""
import time

class Game:
    running = False
    


    
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

