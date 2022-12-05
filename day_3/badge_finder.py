import string

FIN = "sack_contents.txt"

low_priority = 26
upp_priority = 52

def main():
    with open(FIN) as fin:
        badge_sum = 0
        badge_val = 0

        #for line in fin:
        line_0 = fin.readline()
        while line_0:
            line_1 = fin.readline()
            line_2 = fin.readline()

            for char in line_0:
                if char in line_1:
                    if char in line_2:
                        x = string.ascii_lowercase.index(char.lower()) + 1
                        if char.islower():
                            badge_val += x
                        else:
                            badge_val += (x + 26)
                        break
                    else:
                        continue
                else:
                    continue

            badge_sum += badge_val
            badge_val = 0
            line_0 = fin.readline()

        print(f"sum of badge priorities: {badge_sum}")


if __name__ == "__main__":
    main()
