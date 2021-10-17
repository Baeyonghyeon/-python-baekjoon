def main():
    while True:
        count = 0
        loop = input()

        if loop == "#":
            break
        else:
            for i in range(len(loop)):
                if loop[i] == "a" or loop[i] == "e" or loop[i] == "i" or loop[i] == "o" or loop[i] == "u"\
                        or loop[i] == "A" or loop[i] == "E" or loop[i] == "I" or loop[i] == "O" or loop[i] == "U":
                    count += 1
        print(count)


if __name__ == '__main__':
    main()
