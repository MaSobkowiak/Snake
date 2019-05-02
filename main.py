from UI.grid import Grid
from UI.window import Window


def main():
    # initialize grid
    grid = Grid(30, 30)
    # initialize window (grid, start,end,mode)
    #mode 1 - random obstacles
    #mode 2 - board obstacles
    Window(grid)


if __name__ == "__main__":
    main()
