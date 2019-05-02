from UI.grid import Grid
from UI.window import Window


def main():
    # initialize grid
    grid = Grid(20, 10)
    # initialize window (grid, start,end,mode)
    #mode 1 - random obstacles
    #mode 2 - board obstacles
    app = Window(grid,(0,0))
    app.Start()

if __name__ == "__main__":
    main()
