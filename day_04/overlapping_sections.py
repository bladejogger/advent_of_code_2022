#import string

FIN = "sections.txt"

#low_priority = 26
#upp_priority = 52

def main():
    with open(FIN) as fin:

        index = 0
        overlapping_pairs = 0
        line = fin.readline()
        while line:
            print(f"index: {index}")
            index += 1
            line = line.strip().split(',')
            x = line[0].split('-')
            y = line[1].split('-')
            # first touches second
            if int(x[0]) in range(int(y[0]),int(y[1]) + 1):
                overlapping_pairs += 1
            elif int(x[1]) in range(int(y[0]),int(y[1]) + 1):
                overlapping_pairs += 1
            # second touches first
            elif int(y[0]) in range(int(x[0]),int(x[1]) + 1):
                overlapping_pairs += 1
            elif int(y[1]) in range(int(x[0]),int(x[1]) + 1):
                overlapping_pairs += 1

            line = fin.readline()

        print(f"quantity of overlapping pairs: {overlapping_pairs}")


if __name__ == "__main__":
    main()
