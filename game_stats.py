

class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()


    def reset_stats(self):
        self.ships_left = self.settings.number_of_lives
