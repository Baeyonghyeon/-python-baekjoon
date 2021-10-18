def main():
    token = input().split(" ")
    N = int(token[0])
    Q = int(token[1])
    list = []
    for i in range(N):
        list.append(int(input()))

    for loop in range(Q):
        t = int(input())
        for j in range(N):
            if t < sum(list[:j+1]):
                print(j+1)
                break


if __name__ == '__main__':
    main()