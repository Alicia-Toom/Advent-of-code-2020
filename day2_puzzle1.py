def main():
    input = open("input_day2_puzzle1.txt", "r")
    count = 0
    for line in input.readlines():
        (min, max, character, _, password) = line.strip().replace(" ", ":").replace("-", ":").split(":")
        matches = len(list(filter(lambda c: c == character, password)))
        if (matches >= int(min) and matches <= int(max)):
            count += 1

    print(count)


if __name__ == '__main__':
    main()
