import os
root, directories, files = next(os.walk('.'))

#CONSTANTS
FROG = "\U0001F438"
OBSTACLE = "X"

def display_and_select_files(files): #Function to sisplay files to the user for them to select
    file_counter = 1
    for file in files:
        if file[-4:] == "frog": #if the file ends with the .frog extension
            print(f"[{file_counter}]    {file}") #Printing each .frog extension file
            file_counter += 1

    file_associations = {"1": "game1.frog", "2": "game2.frog", "3": "game3.frog"} #Associate a number to each file
    option = input("Enter an option or filename: ") #Ask user which file they want to run
    if option in file_associations: #If the user picks a number, we assocate that number to the file name using the dictionary
        option = file_associations[option] #Get that number's (key) value (file name)
        return option #return filename
    return option #If the user instead enter the file name directly, return just the file name.

def load_file_content(filename): #Function to obtain the contents of the file to work with afterwards
    with open(filename, "r") as file: #open the file
        lines = [] #lines list to hold each line's content in the file
        for line in file: 
            lines.append(line.strip()) #Append each line's content to the lines list without any spaces
    first_line = lines[0].split() #Break up the first line into a list and assign to first_line
    rows = int(first_line[0]) #The first element of first_line is the number of rows of the grid
    cols = int(first_line[1]) #The second element of first_line is the number of cols of the grid
    jumps = int(first_line[2]) #The third element of the first_line is the number of jumps allowed
    
    speeds = [] #Each file comes with specific speeds for each row so we store them using a speeds list
    speed_line = lines[1].split() #Speeds are on the second line
    for speed in speed_line:
        speeds.append(int(speed)) #For each speed, we append it to the speeds list

    grid = [[" "] * cols] #This prints the first row, the safe row, where the frog is initialized
    for line in lines[2:]: #For all the rest of the content in lines
        grid.append(list(line)) #Append that to the grid list

    return rows, cols, jumps, speeds, grid

def initialize_frog_position(rows, cols): #Function that sets up the initial position of the frog on the grid.
    frog_row = rows-rows #It starts on the first row
    frog_col = cols // 2 #It's positioned in the center
    return frog_row, frog_col

def display_board(grid, frog_row, frog_col): #Function to display the board/grid
    new_grid = []
    for row in grid:
        new_grid.append(row[:]) #We need to make a copy of the grid to prevent from changing the grid itself.
    if frog_row < len(new_grid): #While the frog is on the grid
        new_grid[frog_row][frog_col] = FROG #We update it's position on the grid
    elif frog_row != len(new_grid):
        print(" " * frog_col + FROG) #Get the frog to show up on the first line

    for row in new_grid:
        print("".join(row)) #"Join" the grid and print

def get_user_move(): #Function to get user input
    move = input("WASDJ >> ").upper() #Ask user what move they want to play
    while move not in ["W", "A", "S", "D", "J"]: #If the user selects any move that is not valid
        move = input("WASDJ >> ").upper() #We prompt them to enter a valid input until they do
    return move

def move_frog(frog_row, frog_col, move, rows, cols): #Function that updates the frog's location depending on the user input
    if move == "W" and frog_row > 0: #If the user enter "W"
        frog_row -= 1 #Move the frog down by 1 row
    elif move == "D" and frog_col < cols - 1: #If the user enters "D"
        frog_col += 1 #Move the frog 1 column to the right
    elif move == "A" and frog_col > 0: #If the user enters "A"
        frog_col -= 1 #Move the frog 1 column to the left
    elif move == "S" and frog_row < rows: #if the user enters "S"
        frog_row += 1 #Move the frog up by 1 row

    return frog_row, frog_col

def move_cars(grid, speeds): #Function that rotates the cars (obstacles)
    for i in range(1, len(grid)): #Rotation occurs on the car rows only so we start 1 to skip the safe row.
        row = grid[i] #Assign the current car row
        speed = speeds[i - 1] #Get the speed of the row (First row has its speed on first index of "speeds" list)

        if speed > 0: #If speed is positive (right shift)
            grid[i] = row[-speed:] + row[:-speed] #Modify the row (rotate). Take the last "speed" elements and move them to the front.  
        elif speed < 0: #if speed is negative (left shift)
            grid[i] = row[speed:] + row[:speed] #Take the first "speed" elements and move them to the end.

def check_collision(frog_row, frog_col, grid): #Function to detect if frog has landed on a car (obstacle)
    if grid[frog_row - 1][frog_col - 1] == OBSTACLE: #If the frog's position on the grid is on obstacle ("X")
        return True
    return False

def main_game_loop(): #Main game loop that executes everything
    all_files = display_and_select_files(files)
    rows, cols, jumps, speeds, grid = load_file_content(all_files)
    
    frog_row, frog_col = initialize_frog_position(rows, cols)
    winning_row = rows #the winning row is the row after the final grid row
    jumps_left = jumps #pre-defined number of jumps
    move_count = 1 #move counter

    play_game = True
    while play_game:
        move_cars(grid, speeds) #Move the cars
        print(move_count)
        display_board(grid, frog_row, frog_col) #Display the board
        print() #New line for better readability
        move = get_user_move() #Get user input and store it in a variable (move) to work with later

        if move == "J": #The jump logic. If the user wants to jump:
            if jumps_left > 0: #If there are jumps left
                target_row = int(input("Enter the row to jump to: ")) #Prompt the user to enter the row
                target_col = int(input("Enter the column to jump to: ")) #Prompt the user to enter the column
                if target_row - frog_row <= 1 and 0 <= target_col < cols: #If the specified row is within bounds and the specified column is greater than 0 but less than number of columns
                    frog_row, frog_col = target_row, target_col #Set that as frog's new position
                    jumps_left -= 1  #Deduct one jump
            else:
                print("No jumps remaining.") #If no jumps remain, print a message saying so.

        else:
            frog_row, frog_col = move_frog(frog_row, frog_col, move, rows + 1, cols) #If user enters any other valid input, use the "move_frog" function to place the frog in the right place

        if frog_row == winning_row + 1: #If the frog reaches the final row + 1 (row after the final row)
            print(move_count + 1)
            display_board(grid, frog_row, frog_col) #Display the current state of the board
            print(" " * frog_col + FROG) #Print the frog being on the winning row
            print("You won, Frog lives to cross another day.") #Print a message saying they won
            play_game = False #The game ends and play_game (flag) becomes false
            continue

        if check_collision(frog_row, frog_col, grid): #Check if a collision between frog and car has occured
            display_board(grid, frog_row, frog_col) #Display the board showing the collision
            print("You lost, Sorry Frog") #Print a message
            play_game = False #change play_game (flag) to false to terminate the program
            continue
        move_count += 1 #Increment move counter after each turn

if __name__ == "__main__":
    main_game_loop()
