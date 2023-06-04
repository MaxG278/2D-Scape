from src.game import Game

def main():
    game = Game()
    game2 = Game()
    game.start()

    try:
        game.run()
    except KeyboardInterrupt:
        game.exit()







if __name__ == "__main__":
    main()


