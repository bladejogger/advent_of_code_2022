FIN = "motion_paths.txt"

SPOTS_VISITED = []
snake = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0],\
        [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

def coord_check():
    if snake[9] not in SPOTS_VISITED:
        SPOTS_VISITED.append(snake[9].copy())

def move_snake():
    for count in range(0, 9):
        # vert
        if abs(snake[count][1] - snake[count + 1][1]) > 1:
            snake[count + 1][0] = snake[count][0]
            # up
            if snake[count][1] > snake[count + 1][1]:
                snake[count + 1][1] += 1
            # down
            else:
                snake[count + 1][1] -= 1
        # horiz
        elif abs(snake[count][0] - snake[count + 1][0]) > 1:
            # right
            if snake[count][0] > snake[count + 1][0]:
                snake[count + 1][0] += 1
            # left
            else:
                snake[count + 1][0] -= 1
            snake[count + 1][1] = snake[count][1]
        else:
            return

def main():
    with open(FIN) as fin:
        line = fin.readline().strip('\n').split()
        while line:
            dist = int(line[1])
            match line[0]:
                # up
                case 'U':
                    while dist > 0:
                        dist -= 1
                        snake[0][1] += 1
                        move_snake()
                # down
                case 'D':
                    while dist > 0:
                        dist -= 1
                        snake[0][1] -= 1
                        move_snake()
                # right
                case 'R':
                    while dist > 0:
                        dist -= 1
                        snake[0][0] += 1
                        move_snake()
                # left
                case 'L':
                    while dist > 0:
                        dist -= 1
                        snake[0][0] -= 1
                case _:
                    print("ruh roh!\nerror: '{line[0]} {line[1]}'")
                    return
            coord_check()

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
