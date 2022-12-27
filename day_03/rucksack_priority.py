import string

FIN = "sack_contents.txt"

low_priority = 26
upp_priority = 52

def main():
    with open(FIN) as fin:
        ruck_sum = 0
        ruck_val = 0

        #line = fin.readline()
        #while line:
        for line in fin:
            #print(f"{line}")
            mid_pt = int((len(line) - 1 ) / 2) # 'len' is counting the new line
            #print(f"mid_pt type: {type(mid_pt)}")
            #print(f"{mid_pt}")
            first_half = line[ 0 : mid_pt ]
            #print(f"{first_half}")
            secon_half = line[ mid_pt : -1 ]
            #print(f"{secon_half}")
            for char in first_half:
                if char in secon_half:
                    x = string.ascii_lowercase.index(char.lower()) + 1
                    if char.islower():
                        ruck_val += x
                    else:
                        ruck_val += (x + 26)

                    ruck_sum += ruck_val
                    ruck_val = 0
                    break

        print(f"sum of ruck priorities: {ruck_sum}")


if __name__ == "__main__":
    main()
