#!/usr/bin/env python3

from brain_games.engine import run_game
from brain_games.games.prime import game_logic
from brain_games.game_constants import GAME_INSTRUCTIONS


def main():
    run_game(game_logic, GAME_INSTRUCTIONS["prime"])


if __name__ == '__main__':
    main()
