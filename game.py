from player import Player

class Game:

    P1 = 0
    P2 = 1

    def __init__(self, turn=P1, p1=Player(), p2=Player()):
        self.__players = (p1, p2)
        self.__turn = turn
        self.__is_ended = False

    def __change_turn(self):
        self.__turn = self.__get_opponent()

    def __get_opponent(self):
        return (self.__turn + 1) % 2

    def add(self, source_hand, target_hand):
        if self.__is_ended:
            return False

        source_player = self.__players[self.__turn]
        value = source_player.get(source_hand)
        if value == 0:
            return False

        target_player = self.__players[self.__get_opponent()]
        target_player.add(target_hand, value)

        if target_player.is_dead():
            self.__is_ended = True
            return True
        else:
            self.__change_turn()
            return True

    def split(self, value):
        source_player = self.__players[self.__turn]
        success = source_player.split(value)
        self.__change_turn()
        return success

    def is_ended(self):
        return self.__is_ended

    def __str__(self):
        if self.__is_ended:
            return str(self.__turn)
        else:
            return str(self.__turn) + ''.join(list(map(str, self.__players)))

