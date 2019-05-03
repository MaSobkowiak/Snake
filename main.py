from UI.grid import Grid
from UI.window import Window
import sys


def main(mode: int):
    # initialize grid
    print(sys.argv[1])
    grid = Grid(20, 10)
    app = Window(grid)
    app.start(mode)

if __name__ == "__main__":
    main(int(sys.argv[1]))
