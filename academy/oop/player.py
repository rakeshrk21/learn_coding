class Player:
    
    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0
        
    def _get_lives(self):
        return self._lives
    
    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("live cannot be negative")
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if self._level + level >= 1:
            self._level += level
            self.score = self.score + level * 1000
        else:
            print("level can't be less than 1")

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    def __str__(self):
        return f'Name: {self.name}, lives: {self._lives}, level: {self._level}, score: {self.score}'

    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)


print(f'player.py module name is {__name__}')

if __name__ == '__main__':
    print("This is the player class")

