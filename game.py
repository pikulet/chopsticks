from player import Player

class Game:

    PLAYER = 0
    OPPONENT = 1

    def __init__(self, players=(Player(), Player())):
        self.__players = players
        self.__end = False

    def __change_turn(self):
        self.__players = tuple(reversed(self.__players))

    def is_end(self):
        return self.__end

    def add(self, source_hand, target_hand):
        if self.is_end():
            return False

        value = self.__players[Game.PLAYER].get_hand()[source_hand]
        print('Adding value of %d\n' % value)
        if value == 0:
            return False

        print('Initial value of self %s\n' %
              str(self.__players[Game.PLAYER]))
        success = self.__players[Game.OPPONENT].add(target_hand, value)
        if not success:
            return False

        print('Final value of opponent %s\n' %
              str(self.__players[Game.OPPONENT]))
        print('Final value of self %s\n' %
              str(self.__players[Game.PLAYER]))

        if self.__players[Game.OPPONENT].is_dead():
            self.__end = True
        self.__change_turn()
        return True

    def split(self, value):
        if self.is_end():
            return False

        success = self.__players[Game.PLAYER].split(value)
        if not success:
            return False
        self.__change_turn()
        return True

    def get_state(self):
        return self.__players

    def __str__(self):
        return ''.join(list(map(str, self.__players)))
