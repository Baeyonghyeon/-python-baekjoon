def main():
    token = input().split(" ")
    A = token[0]
    B = token[1]
    Atemp = 0
    Btemp = 0

    for i in range(len(A)):
        Atemp += int(A[i])
    for j in range(len(B)):
        Btemp += int(B[j])

    print(Atemp * Btemp)
if __name__ == '__main__':
    main()