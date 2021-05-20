## chopsticks

Chopsticks is a childhood game played with the hands, between two players. Each
step of the way, players take turns to give each other (or themselves) chopstick
points. Hitting or exceeding five points on one hand will "kill" that hand. The
goal of the game is to kill both your opponents' hands.

In this project, I first write a game engine that models the players and game
states. Then, I generated a game theoretic graph of all states that can be
achieved in the game. The graph shows that when both players use an optimal
strategy, the game always ends in a tie (i.e. it never ends since both players
never die).
