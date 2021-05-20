class Player:

    LEFT = 0
    RIGHT = 1

    def __init__(self, left=1, right=1):
        self.__hand = [left, right]
        self.__is_dead = False

    def __get_other_hand(self, hand):
        return (hand + 1) % 2

    def get(self, target_hand):
        '''
        Retrieves value of target hand
        '''
        return self.__hand[target_hand]

    def add(self, target_hand, value):
        '''
        Adds value to target_hand.
        If target_hand has 5 or more points, target_hand resets to 0 and
        Player is dead.
        '''
        if self.__is_dead:
            return False

        self.__hand[target_hand] += value
        if self.__hand[target_hand] >= 5:
            self.__hand[target_hand] = 0
        self.__hand.sort()

        if self.__hand[Player.RIGHT] == 0:
            self.__is_dead = True
        return True

    def split(self, value):
        '''
        Transfer value from RIGHT hand to LEFT hand.
        '''
        if self.__is_dead:
            return False
        elif self.__hand[Player.RIGHT] - value <= 0:
            return False
        elif self.__hand[Player.LEFT] + value >= 5:
            return False
        elif self.__hand[Player.RIGHT] - self.__hand[Player.LEFT] == value:
            return False

        self.__hand[Player.RIGHT] -= value
        self.__hand[Player.LEFT] += value
        self.__hand.sort()
        return True

    def self_tap(self, source_hand):
        '''
        Add value from source hand to other hand.
        '''
        if self.__is_dead:
            return False

        value = self.__hand[source_hand]
        if value == 0:
            return False
        
        target_hand = self.__get_other_hand(source_hand)
        return self.add(target_hand, value)

    def is_dead(self):
        return self.__is_dead

    def __str__(self):
        return ''.join(list(map(str, self.__hand)))

