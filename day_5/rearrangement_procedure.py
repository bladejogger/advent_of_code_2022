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
                    # column number and char count increase linearly like so:
                    # col_num = count/4 + 1/2
                    z = str(int((.25 * count) + .5))
                    if z not in columns.keys():
                        columns[z] = []
                    columns[z] += [elem]
                count += 1
            line = fin.readline()

        # part 2: move crates from one 'stack' to another according to the format:
        # "move quantity from col_A to col_B"
        line = fin.readline().split()
        while line:
            x = int(line[1]) # quantity
            while x:
                y = columns[line[3]].pop(0)   # col_A
                columns[line[5]].insert(0, y) # col_B
                x -= 1
            line = fin.readline().split()

        answer = ""
        for i in range(1, len(columns) + 1):
            last = columns[str(i)][0]
            answer += last
        print(f"ANSWER: {answer}")


if __name__ == "__main__":
    main()
