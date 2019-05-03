from UI.grid import Grid
from UI.window import Window


def main():
    # initialize grid
    grid = Grid(20, 10)
    app = Window(grid,(0,0))
    app.start()

if __name__ == "__main__":
    main()
