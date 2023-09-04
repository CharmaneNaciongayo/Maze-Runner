# Initialize levels and directions arrays
available_levels = [1, 2, 3]
available_directions = []

# Mazes
maze_one = '#######\n# # | #\n#-#-###\n# | | #\n#-#-###\n# # | #\n#######'
maze_two = '#########\n# | | | #\n#-#####-#\n# | | # #\n#-###-###\n# | # | #\n#---#-#-#\n# | # # #\n#########'
maze_three = '###########\n# | | | # #\n#-###-#-#-#\n# | # # | #\n###-#-#-###\n# | | # | #\n#-#-#####-#\n# # | # # #\n#-###-#-#-#\n# | # # | #\n###########'

# Move Functions
def move(direction):
    global current_position
    moves = {
        'East': 1,
        'West': -1,
        'North': -(maze_level + 2),
        'South': maze_level + 2
    }
    current_position += moves.get(direction, 0)  # Default to no movement if direction is invalid

def render_and_limit(): # Use functions to determine the available directions per space in the maze and renders maze after every move

    # Rendering X on the maze
    ending_position_counter = 0
    ending_space_occurences = -1
    for x in current_maze:
        if x == ' ':
            ending_space_occurences += 1
        if ending_space_occurences == ending_position:
            break
        ending_position_counter += 1
    current_maze[ending_position_counter] = 'X'

    # Rendering O on the maze
    current_position_counter = 0
    position_space_occurences = -1
    for x in current_maze:
        if x == ' ' or x == 'X':
            position_space_occurences +=1
        if position_space_occurences == current_position:
            break
        current_position_counter += 1
    current_maze[current_position_counter] = 'O'

    # Refreshes available directions
    global available_directions
    available_directions.clear()
    directions = [('North', - (6 + 2 * (maze_level))), ('East', 1), ('South', (6 + 2 * (maze_level))), ('West', -1)]
    for direction, offset in directions:
        new_position = current_position_counter + offset
        if (0 <= new_position < len(current_maze) and current_maze[new_position] != '#'):
            available_directions.append(direction)
    rendered_maze = ''.join(current_maze)
    print('\n' + rendered_maze)
    current_maze[current_position_counter] = ' ' # Clears previous rendered move
    current_maze[ending_position_counter] = ' '  # Clears previous ending position marker for index to stay in bounds

def fetch_blank_maze(maze_level):
    mazes = {
        1: maze_one,
        2: maze_two,
        3: maze_three
    }
    return mazes.get(maze_level, None)

# -----------------
# Program Execution
# -----------------

print('Welcome to the Maze!') # Greet the player
maze_level = int(input('Select a level: 1, 2, or 3\n')) # Ask the player to select a level
blank_maze = fetch_blank_maze(maze_level) # Use a function to create the layout of the maze depending on the level selected
current_maze = list(blank_maze) # Represent the maze as a list of spaces
current_position = int(input('Starting point: '))
ending_position = int(input('Exit location: '))
render_and_limit()

# Repeatedly asks player for next move until player reaches exit position
while current_position != ending_position:
    print_directions = ' '.join(available_directions)
    print(f'\nAvailable Directions: {print_directions}')
    next_direction = input('Which direction will you take?\n').capitalize()
    if next_direction == 'Quit':
        print('\nTry again next time.')
        break
    elif next_direction in available_directions:
        move(next_direction)
        render_and_limit()
        if current_position == ending_position:
            print('\nFound the exit!')
            break
    else:
        print('\nPlease choose an available direction.\n')

print('Goodbye.') # Before terminating the program, say goodbye.