# 🏃‍♀️ Maze-Runner
A text-based Maze game made with Python.

# 🖋️ Custom Mazes
The mazes in this program are hard-coded. If you would like to create your own mazes with this code exactly, without any further modifications on your end, please be sure to follow these conventions when typing out your custom maze:
- Use `#` for blockers
- Use ` ` for open spaces
- Use `|` for non-open spaces and non-blockers
- Use `\n` to break each row of the maze
- The maze should be a single string
To implement this in the code, be sure to do the following
1. Assign your maze string to a variable. Refer to `lines 5 to 8`.
2. Add your maze variable to the `fetch_blank_maze()` method. Refer to `lines 58 to 54`.
3. Modify the input prompt text in `line 71` to reflect the available mazes.

# 🎮 How to Play
1. Download the maze.py file.
2. In the command line, type `python maze.py` if you have Python 2 and Python 3 installed, or `python3 maze.py` if you have Python 3.
3. Input the number of the level you wanna play!
4. Input a start position (Positions: Level 1 - 0 to 8, Level 2 - 0 to 14, Level 3 - 0 to 24).
5. Input an exit position (Positions: Level 1 - 0 to 8, Level 2 - 0 to 14, Level 3 - 0 to 24).
   **NOTE:** You *can* technically input the same position for both the start and exit positions, but this will immediately result in a victory and terminate the program. You may input an exit position that is higher in number than the start position, and vice versa.
6. Input a move. Available moves will be displayed. Repeat until you reach the exit position.
7. Once you reach the exit position, congratulations! You have beaten the maze.
