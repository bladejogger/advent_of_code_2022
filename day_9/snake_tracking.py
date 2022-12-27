FIN = "motion_paths.txt"

DPAD = {'U': [0, 1], 'D': [0, -1], 'R': [1, 0], 'L': [-1, 0]}
SNAKE = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0],\
        [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
SPOTS_VISITED = [[0, 0]]

def coord_check():
    if SNAKE[9] not in SPOTS_VISITED:
        SPOTS_VISITED.append(SNAKE[9].copy())

def move_snake(direction):
    for i in range(1, 10):
        x_diff = abs(SNAKE[i][0] - SNAKE[i - 1][0])
        y_diff = abs(SNAKE[i][1] - SNAKE[i - 1][1])
        if x_diff > 1 or y_diff > 1:
            if direction == 'U' or direction == 'D':
                SNAKE[i][0] += int((SNAKE[i - 1][0] - SNAKE[i][0]) / 2)
                SNAKE[i][1] += DPAD[direction][1]
            elif direction == 'R' or direction == 'L':
                SNAKE[i][0] += DPAD[direction][0]
                SNAKE[i][1] += int((SNAKE[i - 1][1] - SNAKE[i][1]) / 2)
        else:
            break

    coord_check()

def move_head(direction, distance):
    for i in range(0, int(distance)):
        SNAKE[0][0] += DPAD[direction][0]
        SNAKE[0][1] += DPAD[direction][1]
        move_snake(direction)

def main():
    with open(FIN) as fin:
        line = fin.readline().strip('\n').split()
        while line:
            move_head(line[0], line[1])
            line = fin.readline().strip('\n').split()

    print(f"answer: {len(SPOTS_VISITED)}")

if __name__ == "__main__":
    main()
