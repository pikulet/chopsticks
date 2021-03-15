from game import Game
from player import Player

from collections import deque

def get_game(game_str):
    def get_player(player_str):
        pass
    pass

graph = dict()
queue = deque()
queue.append(str(Game()))

combinations = [
(Player.LEFT, Player.LEFT),
(Player.LEFT, Player.RIGHT),
(Player.RIGHT, Player.LEFT),
(Player.RIGHT, Player.RIGHT),
]

while len(queue) > 0:
    game_str = queue.pop()
    if game_str in graph:
        continue

    neighbours = set()

    print('***** Iterating %s *****' % game_str)
    game = get_game(game_str)

    for c in combinations:
        success = game.add(c[0], c[1])
        if not success:
            continue

        target_str = str(game)
        neighbours.add(target_str)
        if not game.is_ended():
            queue.append(target_str)
        game = get_game(game_str)

    for i in range(1, 4):
        success = game.split(i)
        if not success:
            continue

        target_str = str(game)
        neighbours.add(target_str)
        queue.append(target_str)
        game = get_game(game_str)



