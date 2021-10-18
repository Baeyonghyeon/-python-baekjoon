def main():
    N = int(input())
    token = input().split(" ")
    cluster = int(input())
    count = N

    for i in range(N):
        loop = int(token[i])

        if loop > cluster:
            count += (loop-1)//cluster
        elif loop==0:
            count -=1
    print(cluster*count)

if __name__ == '__main__':
    main()