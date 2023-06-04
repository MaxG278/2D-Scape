from src.game import Game
import pygame

def main():
    game = Game()
    game.start()
    

    try:
        game.run()
    except KeyboardInterrupt:
        game.exit()

    





if __name__ == "__main__":
    main()


