from game import Game
from player import Player

g = Game()
assert(str(g) == '01111')
g.add(Player.LEFT, Player.RIGHT)
assert(str(g) == '11112')
