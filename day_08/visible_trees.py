FIN = "tree_grid.txt"

def main():

    # make 2d array
    tree_grid = []
    NUM_ROWS = 0
    NUM_COLS = 0
    with open(FIN) as fin:
        line = fin.readline().strip('\n')
        NUM_COLS = len(line)
        while line:
            NUM_ROWS += 1
            tree_grid.append(line)
            line = fin.readline().strip('\n')

    answer = 0
    row_index = 0
    for row in tree_grid:
        # perimeter is visible // top/bottom rows
        if row_index == 0 or row_index == (NUM_ROWS - 1):
            answer += len(row)
        else:
            column_index = 0
            for tree in row:
                # perimeter is visible // first/last column
                if column_index == 0 or column_index == (NUM_COLS - 1):
                    answer += 1
                else:
                    # tree is visible if it is the same or taller than ANY tree
                    # in the row or column
                    # true = visible / false = invisible 
                    up_flag = True 
                    dn_flag = True 
                    lt_flag = True 
                    rt_flag = True 
                    cur_row = row_index - 1
                    cur_col = column_index
                    # check vis up
                    while cur_row >= 0:
                        if int(tree) <= int(tree_grid[cur_row][cur_col]):
                            up_flag = False
                            break
                        cur_row -= 1
                    # check vis down 
                    cur_row = row_index + 1
                    while cur_row < NUM_ROWS:
                        if int(tree) <= int(tree_grid[cur_row][cur_col]):
                            dn_flag = False
                            break
                        cur_row += 1
                    # check vis left
                    cur_row = row_index
                    cur_col = column_index - 1
                    while cur_col >= 0:
                        if int(tree) <= int(tree_grid[cur_row][cur_col]):
                            lt_flag = False
                            break
                        cur_col -= 1
                    # check vis right
                    cur_row = row_index
                    cur_col = column_index + 1
                    while cur_col < NUM_COLS:
                        if int(tree) <= int(tree_grid[cur_row][cur_col]):
                            rt_flag = False
                            break
                        cur_col += 1
                    # if any directional flag is still false, then that tree is
                    # visible from that direction
                    if up_flag or dn_flag or lt_flag or rt_flag:
                        answer += 1

                column_index += 1
        row_index += 1

    print(f"answer: {answer}")

if __name__ == "__main__":
    main()
