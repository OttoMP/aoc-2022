import sys

def main():
    if len(sys.argv) > 1:
        # Opening JSON file
        file1 = open(sys.argv[1], 'r')

    elf_index = 0
    elves = []
    total_calories = 0
    for line in file1:
        if line == "\n":
            elves.append((elf_index, total_calories))
            total_calories = 0
            elf_index += 1
            continue
        total_calories += int(line)

    # Closing files
    file1.close()

    elves = sorted(elves, key=lambda tup: tup[1])
    print("The elf carrying most calories is number {} carrying {} calories total".format(elves[0][0], elves[0][1]))


if __name__ == "__main__":
    main()