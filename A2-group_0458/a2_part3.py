"""CSC111 Winter 2021 Assignment 2: Trees, Chess, and Artificial Intelligence (Part 3)

Instructions (READ THIS FIRST!)
===============================

This Python module contains the start of functions and/or classes you'll define
for Part 3 of this assignment. You should NOT make any changes to a2_minichess.py.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 David Liu and Isaac Waller.
"""
import random
from typing import Optional

import a2_game_tree
import a2_minichess


class ExploringPlayer(a2_minichess.Player):
    """A Minichess player that plays greedily some of the time, and randomly some of the time.

    See assignment handout for details.
    """
    # Private Instance Attributes:
    #   - _game_tree:
    #       The GameTree that this player uses to make its moves. If None, then this
    #       player just makes random moves.
    _game_tree: Optional[a2_game_tree.GameTree]
    _exploration_probability: float

    def __init__(self, game_tree: a2_game_tree.GameTree, exploration_probability: float) -> None:
        """Initialize this player."""
        self._game_tree = game_tree
        self._exploration_probability = exploration_probability

    def make_move(self, game: a2_minichess.MinichessGame, previous_move: Optional[str]) -> str:
        """Make a move given the current game.

        previous_move is the opponent player's most recent move, or None if no moves
        have been made.

        Preconditions:
            - There is at least one valid move for the given game
        """
        if self._game_tree is not None and previous_move is not None:
            result = self._game_tree.find_subtree_by_move(previous_move)
            self._game_tree = result

        if self._game_tree is None or self._game_tree.get_subtrees() == []:
            pick = random.choice(game.get_valid_moves())
            self._game_tree = None
            return pick
        else:
            rand = random.uniform(0, 1)
            valid_move = game.get_valid_moves()
            # if rand < self._exploration_probability and valid_move == []:
            #     self._game_tree = None
            if rand < self._exploration_probability:
                pick = random.choice(valid_move)
                self._game_tree = self._game_tree.find_subtree_by_move(pick)

            elif self._game_tree.is_white_move is True:
                temp = self._game_tree.get_subtrees()[0]
                for subtree in self._game_tree.get_subtrees():
                    if subtree.white_win_probability >= temp.white_win_probability:
                        temp = subtree
                self._game_tree = temp
                pick = temp.move

            else:
                temp = self._game_tree.get_subtrees()[0]
                for subtree in self._game_tree.get_subtrees():
                    if subtree.white_win_probability <= temp.white_win_probability:
                        temp = subtree
                self._game_tree = temp
                pick = temp.move
            return pick


def run_learning_algorithm(exploration_probabilities: list[float],
                           show_stats: bool = True) -> a2_game_tree.GameTree:
    """Play a sequence of Minichess games using an ExploringPlayer as the White player.

    This algorithm first initializes an empty GameTree. All ExploringPlayers will use this
    SAME GameTree object, which will be mutated over the course of the algorithm!
    Return this object.

    There are len(exploration_probabilities) games played, where at game i (starting at 0):
        - White is an ExploringPlayer (using the game tree) whose exploration probability
            is equal to exploration_probabilities[i]
        - Black is a RandomPlayer
        - AFTER the game, the move sequence from the game is inserted into the game tree,
          with a white win probability of 1.0 if White won the game, and 0.0 otherwise.

    Implementation note:
        - A NEW ExploringPlayer instance should be created for each loop iteration.
          However, each one should use the SAME GameTree object.
        - You should call run_game, NOT run_games, from a2_minichess. This is because you
          need more control over what happens after each game runs, which you can get by
          writing your own loop that calls run_game. However, you can base your loop on
          the implementation of run_games.
        - Note that run_game from a2_minichess returns both the winner and the move sequence
          after the game ends.
        - You may call print in this function to report progress made in each game.
        - Note that this function returns the final GameTree object. You can inspect the
          white_win_probability of its nodes, calculate its size, or and use it in a
          RandomTreePlayer or GreedyTreePlayer to see how they do with it.
    """
    # Start with a GameTree in the initial state
    game_tree = a2_game_tree.GameTree()

    # Play games using the GreedyRandomPlayer and update the GameTree after each one
    results_so_far = []

    # Write your loop here, according to the description above.
    for i in range(0, len(exploration_probabilities)):
        white = ExploringPlayer(game_tree, exploration_probabilities[i])
        black = a2_minichess.RandomPlayer()
        winner, move_sequence = a2_minichess.run_game(white, black)
        results_so_far.append(winner)

        if winner == "White":
            game_tree.insert_move_sequence(move_sequence, 1.0)
        else:
            game_tree.insert_move_sequence(move_sequence, 0.0)

        print(f'Game {i} winner: {winner}')

    if show_stats:
        a2_minichess.plot_game_statistics(results_so_far)

    return game_tree


def part3_runner() -> a2_game_tree.GameTree:
    """Run example for Part 3.

    Please note that unlike part1_runner and part2_runner, this function is NOT graded.
    We encourage you to experiment with different exploration probability sequences
    to see how quickly you can develop a "winning" GameTree!
    """
    # probabilities = [0.0] * 700
    # probabilities = [1.0] * 700
    probabilities = []
    n = 700
    for i in range(0, n):
        probabilities.append(1 - 1 / n * (i - 1))
    m = 1000 - n
    after = [0.0] * m
    probabilities.extend(after)

    return run_learning_algorithm(probabilities)


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'max-line-length': 100,
        'max-nested-blocks': 4,
        'disable': ['E1136'],
        'extra-imports': ['random', 'a2_minichess', 'a2_game_tree'],
        'allowed-io': ['run_learning_algorithm']
    })

    part3_runner()
