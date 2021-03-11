from player import Player

p1 = Player()
print(str(p1))
assert(str(p1) == '11')
p1.add(Player.LEFT, 3)
assert(str(p1) == '14')
print(str(p1))
p1.split(1)
assert(str(p1) == '23')
print(str(p1))
p1.add(Player.LEFT, 5)
assert(str(p1) == '03')
print(str(p1))
