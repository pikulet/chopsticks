from game import Game
from player import Player

from collections import deque
import pickle

def get_game(game_str):
    values = [int(x) for x in game_str]

    turn, p1_l, p1_r, p2_l, p2_r = values

    p1 = Player(p1_l, p1_r)
    p2 = Player(p2_l, p2_r)
    return Game(turn, p1, p2)

graph = dict()
queue = deque()
queue.append(str(Game()))

add_combinations = [
(Player.LEFT, Player.LEFT),
(Player.LEFT, Player.RIGHT),
(Player.RIGHT, Player.LEFT),
(Player.RIGHT, Player.RIGHT),
]

tap_combinations = [
    Player.LEFT,
    Player.RIGHT
]
while len(queue) > 0:
    game_str = queue.pop()
    if game_str in graph:
        continue

    neighbours = set()

    game = get_game(game_str)

    for c in add_combinations:
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

    for t in tap_combinations:
        success = game.self_tap(t)
        if not success:
            continue

        target_str = str(game)
        neighbours.add(target_str)
        queue.append(target_str)
        game = get_game(game_str)

    graph[game_str] = list(neighbours)

with open('../graph.out', 'w') as f:
    pickle.dump(graph, f)
