def main():
    N = int(input())

    countlist = []
    output = []
    value = ""

    for i in range(26):
        countlist.append(0)

    for j in range(N):
        loop = input()
        firststr = ord(loop[0]) - 97
        countlist[firststr] = countlist[firststr] + 1

    for k in range(26):
        if countlist[k] > 4:
            output.append(chr(k+97))

    if len(output) == 0 :
        print("PREDAJA")
    else:
        for loop in output:
            value += loop
        print(value)

if __name__ == '__main__':
    main()
