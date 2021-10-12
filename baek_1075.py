def main():
    N = int(input())
    F = int(input())

    out = (int)(N / 100)
    out = out * 100

    token = out % F

    if token == 0:
        print("00")
    else:
        token = F-token
        if token < 10:
            print("0"+str(token))
        else:
            print(token)

if __name__ == '__main__':
    main()
