# Get player's name
name = input("Hello, what's your name? ")

# Get board size
board_size = int(input(f"{name}, please choose board size: "))

# Get number of mines
number_of_mines = int(input(f"{name}, for board size {board_size}, choose number of mines to allocate: "))

# Display the information
print(f"{name}, the board size is: {board_size}, number of mines is: {number_of_mines}. ENJOY!")
