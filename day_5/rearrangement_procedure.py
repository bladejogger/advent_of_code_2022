FIN = "crate_instructions.txt"

def main():
    columns = dict()
    num_columns_found = 0

    with open(FIN) as fin:
        # parse columns
        line = fin.readline()
        while line != "\n":
            count = 1
            inc_val = 0
            for elem in line:
                # NOTE: this builds our crate piles so that the first value for
                # each key is going to be the top of the pile!
                if elem.isalpha():
                    # this 2 throws off the formula cause i'm dumb
                    if count == 2:
                        if '1'  not in columns.keys():
                            columns['1'] = []
                            num_columns_found += 1
                        columns['1'] += [elem]
                    else:
                        # to calculate which column the found value goes into
                        # based off how many characters into a line we are is a
                        # reversal of this:
                        # column_num x 3 + inc_val = count
                        # using the hardcoded value of '6' for the place of the
                        # second value
                        x = (count - 6) / 4
                        y = (count - x) / 3
                        # reminder: division makes a float
                        z = str(int(y))
                        if z not in columns.keys():
                            columns[z] = []
                            num_columns_found += 1
                        columns[z] += [elem]
                count += 1
            line = fin.readline()

        #print(f"num columns: {num_columns_found}")
        #print(f"column 1: {columns['1']}")
        #print(f"column 2: {columns['2']}")
        #print(f"column 3: {columns['3']}")
        #print(f"column 4: {columns['4']}")
        #print(f"column 5: {columns['5']}")
        #print(f"column 6: {columns['6']}")
        #print(f"column 7: {columns['7']}")
        #print(f"column 8: {columns['8']}")
        #print(f"column 9: {columns['9']}")
        #print(f"columns: {columns}")
        #return

        # "move quantity from colA to colB"
        line = fin.readline().split()
        counter = 0
        while line:
            if counter == 10:
                pass
                #return
            #print(f"{line}")
            x = int(line[1])
            #print(f"{columns[line[3]]}")
            #print(f"{columns[line[5]]}")
            while x:
                #print(f"{x}")
                #print(f"before pop col {line[3]}: {columns[line[3]]}")
                y = columns[line[3]].pop(0)
                #print(f"after pop col {line[3]} : {columns[line[3]]}")
                #print(f"before add col {line[5]}: {columns[line[5]]}")
                columns[line[5]].insert(0, y)
                #print(f"after add col {line[5]} : {columns[line[5]]}")
                x -= 1
            line = fin.readline().split()
            counter += 1

        answer = ""
        for i in range(1, num_columns_found + 1):
            last = columns[str(i)][0]
            #print(f"last elem: {last}")
            answer += last
        print(f"ANSWER: {answer}")


if __name__ == "__main__":
    main()
