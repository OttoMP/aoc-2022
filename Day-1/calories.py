import sys
from pprint import pprint

def main():
    file1 = open("input.txt", 'r')

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


    elves = sorted(elves, key=lambda tup: tup[1], reverse=True)
    print("The elf carrying most calories is number {} carrying {} calories total".format(elves[0][0], elves[0][1]))
    final_calories = elves[0][1] + elves[1][1] + elves[2][1]
    print("The three elves carrying most calories are numbers {}, {}, {} carrying {} calories total".format(elves[0][0], elves[1][0], elves[2][0], final_calories))

if __name__ == "__main__":
    main()