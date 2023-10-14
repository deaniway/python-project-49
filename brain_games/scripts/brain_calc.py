#!/usr/bin/env python3

from brain_games.engine import run_game
from brain_games.games.calc import game_logic
from brain_games.game_constants import GAME_INSTRUCTIONS


def main():
    run_game(game_logic, GAME_INSTRUCTIONS["calc"])


if __name__ == '__main__':
    main()
