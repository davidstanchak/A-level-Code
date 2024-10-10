class Game:
    def __init__(self, highscore: int, diffuculty, attemps: int, level: int, experience):
        self.highscore = highscore
        self.difficulty = diffuculty
        self.attemps = attemps
        self.level = level
        self.experience = experience

    def set_highscore(self, highscore):
        self.highscore = highscore

    def get_highscore(self):
        return self.highscore
    
    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    def get_difficulty(self):
        return self.difficulty
    
    def add_experience(self, exp):
        self.experience += exp

def main():
    game = Game()

    highscore = int(input("Set high score: "))

    game.set_highscore(highscore)

    print(Game.get_highscore)

if __name__ == "__main__":
    main()