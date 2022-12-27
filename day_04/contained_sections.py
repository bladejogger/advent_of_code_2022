#import string

FIN = "sections.txt"

#low_priority = 26
#upp_priority = 52

def main():
    with open(FIN) as fin:

        index = 0
        self_containing_pairs = 0
        line = fin.readline()

        while line:
        #for line in fin:
            line = line.strip().split(',')
            print(f"index: {index}")
            x = line[0].split('-')
            y = line[1].split('-')
            # first elf contains second
            if int(x[0]) <= int(y[0]) and int(x[1]) >= int(y[1]):
                self_containing_pairs += 1
            # second elf contains first 
            elif int(y[0]) <= int(x[0]) and int(y[1]) >= int(x[1]):
                self_containing_pairs += 1
            line = fin.readline()
            index += 1

        print(f"quantity of self containing pairs: {self_containing_pairs}")


if __name__ == "__main__":
    main()
