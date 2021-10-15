def main():
    x = int(input("정수 1 :"))
    y = int(input("정수 2 :"))
    print("큰 수 : ",max(x,y))
    print("작은 수 :",min(x,y))
    print("차의 절댓값 : ", abs(x-y))



if __name__ == '__main__':
    main()