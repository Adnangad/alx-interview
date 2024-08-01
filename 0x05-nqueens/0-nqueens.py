#!/usr/bin/python3
""" Solves the N-Queens problem using backtracking. """
import sys


def validity(state, board_size):
    """ Check if the state is a valid solution. """
    return len(state) == board_size


def get_val(state, board_size):
    """ Finds possible columns for placing the next queen. """
    if not state:
        return range(board_size)
    pos = len(state)
    cand = set(range(board_size))
    for i, j in enumerate(state):
        cand.discard(j)
        distance = pos - i
        cand.discard(j + distance)
        cand.discard(j - distance)
    return cand


def solve(state, ans, board_size):
    """ Recursively solves the N-Queens problem using backtracking. """
    if validity(state, board_size):
        ans.append([[i, col] for i, col in enumerate(state)])
        return
    for x in get_val(state, board_size):
        state.append(x)
        solve(state, ans, board_size)
        state.pop()


def print_solutions(solutions):
    """ Prints all solutions in the required format. """
    for solution in solutions:
        print(solution)


def main():
    """ Main function """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        board_size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if board_size < 4:
        print("N must be at least 4")
        exit(1)

    state = []
    ans = []
    solve(state, ans, board_size)
    print_solutions(ans)


if __name__ == "__main__":
    main()
