FIN = "motion_paths.txt"

DPAD = {'U': [0, 1], 'D': [0, -1], 'R': [1, 0], 'L': [-1, 0]}
SPOTS_VISITED = [[0, 0]]
HEAD = [0, 0]
TAIL = [0, 0]

def coord_check():
    if TAIL not in SPOTS_VISITED:
        SPOTS_VISITED.append(TAIL.copy())

def move_snake(direction, distance):
    global HEAD, TAIL
    for i in range(0, int(distance)):
        HEAD[0] += DPAD[direction][0]
        HEAD[1] += DPAD[direction][1]

        x_diff = abs(HEAD[0] - TAIL[0])
        y_diff = abs(HEAD[1] - TAIL[1])
        if x_diff > 1 or y_diff > 1:
            if direction == 'U' or direction == 'D':
                TAIL[0] = HEAD[0]
                TAIL[1] += DPAD[direction][1]
            else:
                TAIL[0] += DPAD[direction][0]
                TAIL[1] = HEAD[1]
            coord_check()

def main():
    with open(FIN) as fin:
        line = fin.readline().strip('\n').split()
        while line:
            move_snake(line[0], line[1])
            line = fin.readline().strip('\n').split()

    print(f"answer: {len(SPOTS_VISITED)}")

if __name__ == "__main__":
    main()
