FIN = "elves_calories.txt"

def main():
    with open(FIN) as fin:
        first_calories = 0
        secon_calories = 0
        third_calories = 0
        elf_calories = 0

        line = fin.readline()
        while line:
            if line == '\n': # checks for 'blank'
                if elf_calories > first_calories:
                    third_calories = secon_calories
                    secon_calories = first_calories
                    first_calories = elf_calories
                elif elf_calories > secon_calories:
                    third_calories = secon_calories
                    secon_calories = elf_calories
                elif elf_calories > third_calories:
                    third_calories = elf_calories
                elf_calories = 0
                line = fin.readline()
            else:
                elf_calories += int(line)
                line = fin.readline()

        total_calories = first_calories + secon_calories + third_calories
        print(f"the top 3 elves have {total_calories} calories!!")


if __name__ == "__main__":
    main()
