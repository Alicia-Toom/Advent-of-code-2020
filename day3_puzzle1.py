def main():
    input = open("input_day3.txt", "r")
    # Skip first line
    input.readline()
    count = 0
    index = 0
    for line in input.readlines():
        if line[index] == "#":
            count += 1

        index += 3
        if index > len(line) - 2:
            index = index - len(line) + 1

    print(count)

if __name__ == '__main__':
    main()
