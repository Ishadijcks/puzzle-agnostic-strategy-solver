from puzzles.sudoku.Sudoku import Sudoku


def get_easy1():
    return Sudoku("""
        601 275 930
        302 000 005
        407 096 182

        060 420 010
        015 039 000
        009 000 008

        020 004 000
        000 950 806
        006 000 490
    """.replace(" ", "").replace("\n", "")
                  )
