FIN = "tree_grid.txt"

def main():

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

    best_view = 0
    row_index = 0
    for row in tree_grid:
        column_index = 0
        for tree in row:
            cur_view = [0, 0, 0, 0]
            cur_row = row_index - 1
            cur_col = column_index
            # check view up
            while cur_row >= 0:
                cur_view[0] += 1
                if int(tree_grid[cur_row][cur_col]) >= int(tree):
                    break
                cur_row -= 1
            # check view down 
            cur_row = row_index + 1
            while cur_row < NUM_ROWS:
                cur_view[1] += 1
                if int(tree_grid[cur_row][cur_col]) >= int(tree):
                    break
                cur_row += 1
            # check view left
            cur_row = row_index
            cur_col = column_index - 1
            while cur_col >= 0:
                cur_view[2] += 1
                if int(tree_grid[cur_row][cur_col]) >= int(tree):
                    break
                cur_col -= 1
            # check view right
            cur_row = row_index
            cur_col = column_index + 1
            while cur_col < NUM_COLS:
                cur_view[3] += 1
                if int(tree_grid[cur_row][cur_col]) >= int(tree):
                    break
                cur_col += 1

            x = cur_view[0] * cur_view[1] * cur_view[2] * cur_view[3]
            if x > best_view:
                best_view = x

            column_index += 1
        row_index += 1

    print(f"answer: {best_view}")

if __name__ == "__main__":
    main()
