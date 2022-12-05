import sys
from pprint import pprint

def main():
    file1 = open("guide.txt", 'r')

    score = 0
    for line in file1:
        his_game = line.split()[0]
        my_game = line.split()[1]
        if my_game == "X":
            score += 1
            if his_game == "A":
                score += 3
            elif his_game == "B":
                score += 0
            elif his_game == "C":
                score += 6
        elif my_game == "Y":
            score += 2
            if his_game == "A":
                score += 6
            elif his_game == "B":
                score += 3
            elif his_game == "C":
                score += 0
        elif my_game == "Z":
            score += 3
            if his_game == "A":
                score += 0
            elif his_game == "B":
                score += 6
            elif his_game == "C":
                score += 3

    # Closing files
    file1.close()
    print("My final score is {}".format(score))

if __name__ == "__main__":
    main()