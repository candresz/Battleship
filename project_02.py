import random

# --------------------------
# BATTLESHIP GAME STRUCTURE
# --------------------------

# Global settings
grid_size = 10
num_of_ships = 5

# Initialize empty grid
grid = [[""] * grid_size for _ in range(grid_size)]


# --------------------------
# Draw the game board
# --------------------------
def drawBoard(myBoard):
    print("+" + "---+" * 11)
    header = "|   |" + "".join(f"{str(i):^3}|" for i in range(10))
    print(header)
    print("+" + "---+" * 11)

    for i in range(10):
        row = f"| {i} |" + "".join(f"{cell:^3}|" for cell in myBoard[i])
        print(row)
        print("+" + "---+" * 11)


# --------------------------
# Set up board with ships
# --------------------------
def setupBoard(myBoard):
    # Fill grid with water ('.')
    for i in range(grid_size):
        for j in range(grid_size):
            myBoard[i][j] = "."

    # Place ships randomly
    ships_placed = 0
    while ships_placed < num_of_ships:
        randomRow = random.randint(0, grid_size - 1)
        randomCol = random.randint(0, grid_size - 1)
        if myBoard[randomRow][randomCol] == ".":
            myBoard[randomRow][randomCol] = "S"
            ships_placed += 1


# --------------------------
# Check hit or miss
# --------------------------
def hitOrMiss(myBoard, row, col):
    if myBoard[row][col] == "S":
        myBoard[row][col] = "X"
        return "HIT"
    elif myBoard[row][col] == "X":
        return "HIT"
    else:
        myBoard[row][col] = "O"
        return "MISS"


# --------------------------
# Check if game is over
# --------------------------
def isGameOver(myBoard):
    for i in range(grid_size):
        for j in range(grid_size):
            if myBoard[i][j] == "S":
                return False
    return True


# --------------------------
# Main game loop
# --------------------------
def main(myBoard):
    setupBoard(myBoard)

    while not isGameOver(myBoard):
        drawBoard(myBoard)

        try:
            col = int(input("Enter column (0–9): "))
            if col < 0 or col >= grid_size:
                print("Invalid column")
                continue

            row = int(input("Enter row (0–9): "))
            if row < 0 or row >= grid_size:
                print("Invalid row")
                continue

            result = hitOrMiss(myBoard, row, col)
            print(result)

        except ValueError:
            print("Please enter valid numbers.")

    drawBoard(myBoard)
    print("GAME OVER!")


main(grid)
