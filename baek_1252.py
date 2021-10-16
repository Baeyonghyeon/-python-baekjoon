def main():
    token = input().split(" ")
    x = int(token[0],2)
    y = int(token[1],2)
    print(bin(x + y)[2:])


if __name__ == '__main__':
    main()