def main():
    input = open("input_day2_puzzle1.txt", "r")
    count = 0
    for line in input.readlines():
        (pos1, pos2, character, _, password) = line.strip().replace(" ", ":").replace("-", ":").split(":")
        str = password[int(pos1) - 1] + password[int(pos2) - 1]
        if character in str and str != character + character:
            count += 1

    print(count)


if __name__ == '__main__':
    main()
