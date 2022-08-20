from oop.player import Player
from oop.enemy import Enemy, Troll, Vampire, VampireKing


# https://alex.dzyoba.com/blog/python-import/
# myPlayer = Player("Rakesh")
# print(myPlayer)
#
# myEnemy = Enemy("Monstor", 25, 3)
# print(myEnemy)
#
# troll1 = Troll("crazy")
# print(troll1)
# troll1.grunt()
#
# troll2 = Troll("psycho")
# troll2.grunt()
# troll2.take_damage(13)
# print(troll2)

vampire1 = Vampire("Draculla")

while vampire1._alive:
    vampire1.take_damage(1)
    print(vampire1)

vampireKing1 = VampireKing("King")
vampireKing1.take_damage(12)
print(vampireKing1)


# myPlayer.lives -= 1
# print(myPlayer)
# myPlayer.level = 1 # calling by property name
# print(myPlayer)
# myPlayer.level = 1
# print(myPlayer)
# myPlayer.level = 1
# print(myPlayer)
# myPlayer.level = 1
# print(myPlayer)
# myPlayer.level = 1
# print(myPlayer)
# myPlayer.level = -1
# print(myPlayer)
# myPlayer.level = -1
# print(myPlayer)
# myPlayer.level = 5
# print(myPlayer)
# myPlayer.level = 6
# print(myPlayer)
# myPlayer.level = -9
# print(myPlayer)
# myPlayer.score = 1000
# print(myPlayer)