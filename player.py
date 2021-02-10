class Player:

    LEFT = 0
    RIGHT = 1

    def __init__(self, hand=[1,1]):
        self.__hand = hand

    def __align(self):
        self.__hand.sort()

    def add(self, hand_index, value):
        if self.is_dead():
            return False

        if value > 4:
            return False
        self.__hand[hand_index] += value
        if self.__hand[hand_index] > 5:
            self.__hand[hand_index] = 0

        self.__align()
        return True

    def split(self, value):
        if self.is_dead():
            return False

        if self.__hand[Player.RIGHT] <= value:
            return False

        self.__hand[Player.RIGHT] -= value
        self.__hand[Player.LEFT] += value
        return True

    def is_dead(self):
        return self.__hand[Player.LEFT] == 0 and \
            self.__hand[Player.RIGHT] == 0

    def get_hand(self):
        return self.__hand

    def __str__(self):
        return ''.join(list(map(str, self.__hand)))
