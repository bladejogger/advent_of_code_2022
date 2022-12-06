FIN = "crate_instructions.txt"

def main():
    columns = dict()

    with open(FIN) as fin:
        # part 1: create crate stacks as lists and use them as values for the
        # column number keys in a dictionary
        line = fin.readline()
        while line != "\n":
            count = 1
            for elem in line:
                # NOTE: this builds our crate piles so that the first value for
                # each key is going to be the top of the pile!
                if elem.isalpha():
                    # this 2 throws off the formula cause i'm dumb
                    if count == 2:
                        if '1'  not in columns.keys():
                            columns['1'] = []
                        columns['1'] += [elem]
                    else:
                        # there is a gap of 4 characters between each crate
                        # value consumed.  the correlation between column
                        # number(col_num) and characters consumed(count) can be
                        # described as:
                        # count = col_num x 3 + inc_val
                        # where inc_val starts at 0 and increases by 1 for
                        # every new column
                        # to calculate which col_num the found value goes into
                        # based off the count, we need a formula which
                        # converts 6 to a inc_val of 0:
                        # 6-6 = 0     ez pz
                        # and 10 to a inc_val of 1, and so on:
                        # 10-6 = 4/4 = 1
                        # 14-6 = 8/4 = 2
                        inc_val = (count - 6) / 4
                        # so now we have both count and inc_val, and order of
                        # operations follows naturally to reverse our
                        # correlation formula
                        col_num  = (count - inc_val) / 3
                        # reminder: division makes a float
                        z = str(int(col_num))
                        if z not in columns.keys():
                            columns[z] = []
                        columns[z] += [elem]
                count += 1
            line = fin.readline()

        # part 2: move ALL crates from one 'stack' to another AT ONCE according
        # to the format:
        # "move quantity from col_A to col_B"
        line = fin.readline().split()
        while line:
            x = int(line[1]) # quantity
            while x:
                y = columns[line[3]].pop(x - 1) # col_A
                columns[line[5]].insert(0, y)   # col_B
                x -= 1
            line = fin.readline().split()

        answer = ""
        for i in range(1, len(columns) + 1):
            last = columns[str(i)][0]
            answer += last
        print(f"ANSWER: {answer}")


if __name__ == "__main__":
    main()
