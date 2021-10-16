def main():
    token = input().split(" ")
    S1 = int(token[0])
    S2 = int(token[1])
    S3 = int(token[2])
    value = 0
    max = 0

    countlist = []
    for i in range(S1+S2+S3+1):
        countlist.append(0)

    for j in range(S1):
        first = j+1
        for k in range(S2):
            second = k+1
            for l in range(S3):
                third = l+1
                countlist[first + second + third] += 1

    for loop in range(len(countlist)):
        if countlist[loop] > value:
            value = countlist[loop]
            max = loop

    print(max)

if __name__ == '__main__':
    main()