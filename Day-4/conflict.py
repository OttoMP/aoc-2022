def main():
    file1 = open("assignment.txt", 'r')

    print("Part 1")
    total = 0
    for line in file1:
        pairs = line.rstrip('\n').split(',')
        sections0 = pairs[0].split('-')
        clean0 = {section for section in range(int(sections0[0]), int(sections0[1])+1)}
        sections1 = pairs[1].split('-')
        clean1 = {section for section in range(int(sections1[0]), int(sections1[1])+1)}

        if (clean0 - clean1 == set()) or (clean1 - clean0 == set()):
            total += 1

    file1.close()
    print("There are a total of {} fully contained assignments".format(total))

    print("Part 2")
    file1 = open("assignment.txt", 'r')
    total = 0
    for line in file1:
        pairs = line.rstrip('\n').split(',')
        sections0 = pairs[0].split('-')
        clean0 = {section for section in range(int(sections0[0]), int(sections0[1])+1)}
        sections1 = pairs[1].split('-')
        clean1 = {section for section in range(int(sections1[0]), int(sections1[1])+1)}

        if (clean0.intersection(clean1) != set()):
            total += 1

    file1.close()
    print("There are a total of {} overlaped assignments".format(total))

if __name__ == "__main__":
    main()