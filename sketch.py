# You are given a Game and a list of Agents.
# The goal is to play num_games random games between the agents and produce a trueskill rating of the agents.
# Only use the Game interface for evaluating the agents; your program should utilize multiple networked machines for evaluation.
# You are not required to keep the exact interface of this function, but please do not modify the other files.

import random


def evaluate(game, agents, num_games):
    for i in range(num_games):
        i1 = random.randint(0, len(agents) - 1)
        i2 = random.randint(0, len(agents) - 1)
        result = game.play(agents[i1], agents[i2])
        # TODO: record the game result
    # TODO: complete the trueskill evaluation
    raise NotImplementedError
