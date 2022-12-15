FIN = "motion_paths.txt"

SPOTS_VISITED = []

def coord_check(coords):
    if tuple(coords) not in SPOTS_VISITED:
        SPOTS_VISITED.append(tuple(coords))

def main():
    head = [0, 0]
    tail = [0, 0]
    SPOTS_VISITED.append(tuple(tail))
    with open(FIN) as fin:
        line = fin.readline().strip('\n').split()
        while line:
            dist = int(line[1])
            # upwards tracking 
            if line[0] == 'U':
                while dist > 0:
                    dist -= 1
                    head[1] += 1
                    if abs(head[1] - tail[1]) > 1:
                        tail[0] = head[0]
                        tail[1] += 1
                        coord_check(tail)
            # downwards tracking
            elif line[0] == 'D':
                while dist > 0:
                    dist -= 1
                    head[1] -= 1
                    if abs(head[1] - tail[1]) > 1:
                        tail[0] = head[0]
                        tail[1] -= 1
                        coord_check(tail)
            # leftwards tracking
            elif line[0] == 'L':
                while dist > 0:
                    dist -= 1
                    head[0] -= 1
                    if abs(head[0] - tail[0]) > 1:
                        tail[0] -= 1
                        tail[1] = head[1]
                        coord_check(tail)
            # rightwards tracking
            elif line[0] == 'R':
                while dist > 0:
                    dist -= 1
                    head[0] += 1
                    if abs(head[0] - tail[0]) > 1:
                        tail[0] += 1
                        tail[1] = head[1]
                        coord_check(tail)
            else:
                print("ruh roh: found '{line[0]} {line[1]}'")
                return

            line = fin.readline().strip('\n').split()

    answer = len(SPOTS_VISITED)
    print(f"answer: {answer}")

if __name__ == "__main__":
    main()
