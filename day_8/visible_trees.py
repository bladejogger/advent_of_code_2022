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
            #print(f"ROW_INDEX: {row_index}")
            answer += len(row)
        else:
            column_index = 0
            for tree in row:
                # perimeter is visible // first/last column
                if column_index == 0 or column_index == (NUM_COLS - 1):
                    #print(f"COL_INDEX: {column_index}")
                    answer += 1
                else:
                    #print(f"CUR_LOCATION: [{row_index}][{column_index}]")
                    # directional flags to indicate that a tree is visible
                    # false = not visible / true = visible
                    up_flag = False
                    dn_flag = False
                    lt_flag = False
                    rt_flag = False
                    # check vis up
                    cur_row = row_index - 1
                    cur_col = column_index
                    while cur_row >= 0:
                        if int(tree) >= int(tree_grid[cur_row][cur_col]):
                            up_flag = True
                            break
                        cur_row -= 1
                    # check vis down 
                    cur_row = row_index + 1
                    while cur_row < NUM_ROWS:
                        if int(tree) >= int(tree_grid[cur_row][cur_col]):
                            dn_flag = True
                            break
                        cur_row += 1
                    # check vis left
                    cur_row = row_index
                    cur_col = column_index - 1
                    while cur_col >= 0:
                        if int(tree) >= int(tree_grid[cur_row][cur_col]):
                            lt_flag = True
                            break
                        cur_col -= 1
                    # check vis right
                    cur_row = row_index
                    cur_col = column_index + 1
                    while cur_col < NUM_COLS:
                        if int(tree) >= int(tree_grid[cur_row][cur_col]):
                            rt_flag = True
                            break
                        cur_col += 1
                    # if any directional flag is still false, then that tree is
                    # visible from that direction
                    if not up_flag or not dn_flag or not lt_flag or not rt_flag:
                        answer += 1

                column_index += 1
        row_index += 1

    print(f"answer: {answer}")

if __name__ == "__main__":
    main()

# guess 197  - too low
# guess 392  - no response 
# guess 964  - no response
# guess 1150 - no response
# guess 2817 - too high
# guess 9801 - too high
