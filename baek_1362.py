def main():
    list = []
    check = True
    while True:
        token1 = input().split(" ")
        o = int(token1[0])
        w = int(token1[1])

        if o == 0 and w == 0:
            break

        while True:
            token2 = input().split(" ")
            scenario1 = token2[0]
            scenario2 = int(token2[1])

            if scenario1 == "#" and scenario2 == 0:
                break
            elif scenario1 == "F": #보충 체중증가
                w += scenario2
            elif scenario1 == "E": #운동 체중감소
                w -= scenario2
                if w <= 0:
                    check = False

        if check == False:
            list.append("RIP")
            check = True
        elif o/2 < w < o*2:
            list.append(":-)")
        else:
            list.append(":-(")

    for loop in range(len(list)):
        print(loop+1, list[loop])


if __name__ == '__main__':
    main()