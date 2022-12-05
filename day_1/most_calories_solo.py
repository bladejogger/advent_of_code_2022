FIN = "elves_calories.txt"

def main():
    # STEP 1) get elves_calories.txt
    with open(FIN) as fin:

        # STEP 3) save the number!
        most_calories = 0
        which_elf = 0
        elf_calories = 0

        # STEP 2) add numbers until line is blank (this is for one elf)
        line = fin.readline()
        while line:
            if line == '\n': # checks for 'blank'
                which_elf += 1
                # STEP 5) compare the numbers
                if elf_calories > most_calories:
                    # STEP 6) save the larger number
                    most_calories = elf_calories 
                elf_calories = 0
                line = fin.readline()
                continue

            elf_calories += int(line)
            line = fin.readline()
            # STEP 4) repeat step 2
        # STEP 7) repeat step 4 through 6

        # STEP 8) print the largest number
        print(f"elf number {which_elf} has the most calories!")
        print(f"they have {most_calories} calories!!")


if __name__ == "__main__":
    main()
