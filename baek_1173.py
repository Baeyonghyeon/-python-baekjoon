def main():
    inputvalue = input().split(" ")
    N = int(inputvalue[0])  # 운동시간
    m = int(inputvalue[1])  # 최소값(시작값)
    M = int(inputvalue[2])  # 최대값
    T = int(inputvalue[3])  # 운동시 증가량
    R = int(inputvalue[4])  # 휴식시 감소량
    count = 0
    time = 0
    pulse = m

    if pulse + T > M:
        print(-1)
    else:
        while time < N:
            if pulse + T <= M:
                pulse += T
                count += 1
                time += 1
            else :
                pulse -= R
                if pulse < m:
                    pulse = m
                count += 1

        print(count)


if __name__ == '__main__':
    main()
