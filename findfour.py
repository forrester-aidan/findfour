def get_initial_board(rows: int, columns: int): # Initializes a game board
    board = ([["." for i in range(columns)] for j in range(rows)])
    return board


def print_board(board: list[list[str]]): # Prints the current board to the console
    numberOfLines = (len(board) * 2) - 1
    toplines = " "
    bottomlines = " "

    while numberOfLines > 0:
        toplines += "_"
        bottomlines += "-"
        numberOfLines -= 1
    print(toplines)

    for i in range(len(board)):
        row = "|"
        for j in range(len(board[i])):
            row += board[i][j] + " "
        print(row.rstrip() + "|")

    print(bottomlines + "\n")


def is_win_state(chip: str, board: list[list[str]], row: int, column: int) -> bool: # Checks if the player has won
    rows = len(board)
    columns = len(board[0])
    rowCounter = 0
    columnCounter = 0

    for i in range(rows):
        for j in range(columns):
            if board[i][j] == chip:
                rowCounter += 1
                if rowCounter == 4 and i != 0:
                    return True
            else:
                rowCounter = 0

    for j in range(columns):
        for i in range(rows):
            if board[i][j] == chip:
                columnCounter += 1
                if columnCounter == 4 and i != 0:
                    return True
            else:
                columnCounter = 0

    print_board(board)


def insert_chip(board: list[list[str]], column: int, chip: str): # Inserts a chip into the game board
    for i in range(len(board)):
        row = len(board) - 1 - i
        if row == 0 and (board[row][column] == "x" or board[row][column] == "o"):
            print("Error: column is full!")
            return -1
        elif board[row][column] == ".":
            board[row][column] = chip
            return row
    print_board(board)


def is_board_full(board: list[list[str]]): # Checks if the game board is full
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ".":
                return False

    return True


def begin_game(board: list[list[str]]): # Begins the game
    x = 0
    playerOneChip = "x"
    playerTwoChip = "o"
    playerTurn = 1

    print_board(board)
    print("Player 1: x")
    print("Player 2: o\n")

    while x < 1:
        if playerTurn == 1:
            selectedColumn = input("Player 1 - Select a Column: ")
            if not selectedColumn.isnumeric() and str(selectedColumn).find("-") == -1:
                print("Error: not a number!")
                continue
            elif not selectedColumn.isnumeric() and str(selectedColumn).find("-") != -1:
                print("Error: no such column!")
                continue
            elif int(selectedColumn) > len(board):
                print("Error: no such column!")
                continue

            row = insert_chip(board, int(selectedColumn), playerOneChip)
            if row == -1:
                continue
            if is_win_state(playerOneChip, board, row, int(selectedColumn)):
                print_board(board)
                print("\nPlayer 1 won the game!")
                quit()
            playerTurn = 2
        else:
            selectedColumn = input("Player 2 - Select a Column: ")
            if not selectedColumn.isnumeric() and str(selectedColumn).find("-") == -1:
                print("Error: not a number!")
                continue
            elif not selectedColumn.isnumeric() and str(selectedColumn).find("-") != -1:
                print("Error: no such column!")
                continue
            elif int(selectedColumn) > len(board):
                print("Error: no such column!")
                continue

            row = insert_chip(board, int(selectedColumn), playerTwoChip)
            if row == -1:
                continue
            if is_win_state(playerTwoChip, board, row, int(selectedColumn)):
                print_board(board)
                print("\nPlayer 2 won the game!")
                quit()
            playerTurn = 1

        if is_board_full(board):
            print("Draw Game! Players tied.")
            quit()


if __name__ == '__main__': # Main Method
    x = 0
    y = 0
    height = ""
    width = ""

    print("Welcome to Find Four!\n---------------------")

    while x < 1:
        height = input("Enter height of board (rows): ")
        if not height.isnumeric() and str(height).find("-") == -1:
            print("Error: not a number!")
            continue
        elif not height.isnumeric() and str(height).find("-") != -1:
            print("Error: height must be at least 4!")
            continue
        elif int(height) < 4:
            print("Error: height must be at least 4!")
            continue
        elif int(height) > 25:
            print("Error: height can be at most 25!")
            continue
        else:
            x = 1

    while y < 1:
        width = input("Enter width of board (columns): ")
        if not width.isnumeric() and str(width).find("-") == -1:
            print("Error: not a number!")
            continue
        elif not width.isnumeric() and str(width).find("-") != -1:
            print("Error: width must be at least 4!")
            continue
        elif int(width) < 4:
            print("Error: width must be at least 4!")
            continue
        elif int(width) > 25:
            print("Error: width can be at most 25!")
            continue
        else:
            y = 1

    gameBoard = get_initial_board(int(height), int(width))
    begin_game(gameBoard)
