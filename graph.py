from player import Player
from game import Game

from collections import deque

add_combinations = (
    (Player.LEFT, Player.LEFT),
    (Player.LEFT, Player.RIGHT),
    (Player.RIGHT, Player.LEFT),
    (Player.RIGHT, Player.RIGHT)
)

TURN1 = 'r'
TURN2 = 'b'

def get_next_turn(turn):
    if turn == TURN1:
        return TURN2
    else:
        return TURN1

def main():
    graph = dict()
    q = deque()
    q.append(Game().get_state())

    turn = TURN1
    while len(q) > 0:
        source = q.pop()
        g = Game(source)
        source_str = turn+str(g)
        print('**** Iterating **** \n', source_str)
        if g.is_end():
            continue

        if source in graph:
            continue
        graph[source] = set()

        # Get all possible states from here
        next_turn = get_next_turn(turn)

        for c in add_combinations:
            success = g.add(c[0], c[1])
            if not success:
                continue

            if g.is_end():
                target_str = turn   # winner
            else:
                q.append(g.get_state())
                target_str = next_turn+str(g)

            print('# Found Target: ', target_str)
            graph[source].add(target_str)
            g = Game(source)
            
        # split
        for i in range(1, 4):
            success = g.split(i)
            if not success:
                break

            q.append(g.get_state())
            target_str = next_turn+str(g)
            print('# Found Target: ', target_str)
            graph[source].add(target_str)
            g = Game(source)



if __name__ == '__main__':
    main()
