FIN = "motion_paths.txt"

DPAD = {'U': [0, 1], 'D': [0, -1], 'R': [1, 0], 'L': [-1, 0]}
SNAKE = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0],\
        [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
SPOTS_VISITED = [[0, 0]]

def coord_check():
    if SNAKE[9] not in SPOTS_VISITED:
        SPOTS_VISITED.append(SNAKE[9].copy())

def move_snake(direction, distance):
    global SNAKE
    for i in range(0, int(distance)):
        SNAKE[0][0] += DPAD[direction][0]
        SNAKE[0][1] += DPAD[direction][1]
    
        for elem in range(0, 9):
            x_diff = abs(SNAKE[elem][0] - SNAKE[elem + 1][0])
            y_diff = abs(SNAKE[elem][1] - SNAKE[elem + 1][1])
            if x_diff > 1 or y_diff > 1:
                if direction == 'U' or direction == 'D':
                    SNAKE[elem + 1][0] = SNAKE[elem][0]
                    SNAKE[elem + 1][1] += DPAD[direction][1]
                else:
                    SNAKE[elem + 1][0] += DPAD[direction][0]
                    SNAKE[elem + 1][1] = SNAKE[elem][1]
        coord_check()
    
def main():
    with open(FIN) as fin:
        line = fin.readline().strip('\n').split()
        while line:
            move_snake(line[0], line[1]);
            line = fin.readline().strip('\n').split()

    print(f"answer: {len(SPOTS_VISITED)}")

if __name__ == "__main__":
    main()

# 1241 - no res
# 1500 - too low
# 1519 - too low
# 1958 - no res 
# 2380 - no res
# 2430 - too high
# 2670 - no res
# 2841 - too high
