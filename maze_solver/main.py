from collections import deque

with open('./input.txt', 'r') as file:
    lines = file.readlines()

mazes = {}
current_maze = []
current_label = None

for line in lines:
    line = line.strip()
    if not line:
        continue
    if line.isalpha() and len(line) == 1:
        if current_label is not None:
            mazes[current_label] = current_maze
        current_label = line
        current_maze = []
    else:
        current_maze.append(list(line.replace(" ", "")))

if current_label is not None:
    mazes[current_label] = current_maze


def solve_maze(maze):
    start = None
    goal = None
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'G':
                goal = (i, j)

    directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    queue = deque([(start, [])])
    visited = set()
    visited.add(start)

    PATH = None
    while queue:
        (current, path) = queue.popleft()

        if current == goal:
            PATH = path

        for direction, (di, dj) in directions.items():
            ni, nj = current[0] + di, current[1] + dj

            if 0 <= ni < len(maze) and 0 <= nj < len(maze[0]) and (ni, nj) not in visited:
                if maze[ni][nj] in ('.', 'G'):
                    queue.append(((ni, nj), path + [direction]))
                    visited.add((ni, nj))

    print("S", " ".join(PATH), "G\n")


for items in mazes:
    print(items)
    solve_maze(mazes[items])

