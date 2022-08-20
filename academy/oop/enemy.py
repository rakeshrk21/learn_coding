import random

class Enemy:

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self._name = name
        self._hit_points = hit_points
        self._lives = lives
        self._alive = True

    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        print(f"{self._name} has {remaining_points} points left")
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print(f'{self._name} took {damage} points damage and have {self._hit_points} left')
        else:
            if self._lives > 0 and self._hit_points <= 0:
                self._lives -= 1
                self._hit_points = self._hit_points
                print(f"you just lost a life and you {self._lives} remaining")
            else:
                print(f"{self._name} is dead")
                self._alive = False

    def __str__(self):
        return f"I'm  {self._name} with {self._hit_points} points and {self._lives} lives left"


class Troll(Enemy):

    def __init__(self, name):
        super().__init__(name, hit_points=25, lives=5)


    def grunt(self):
        print(f'Me {self._name}, {self._name} stomp you')


class Vampire(Enemy):

    def __init__(self, name):
        super().__init__(name=name, hit_points=12, lives=3)

    def dodges(self):
        if random.randint(1,3) == 3:
            print(f'{self._name} dodges the damage ******')
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)


class VampireKing(Vampire):

    def __init__(self, name):
        super().__init__(name=name)
        self._hit_points = 140

    def take_damage(self, damage):
        super().take_damage(damage=damage // 4)
