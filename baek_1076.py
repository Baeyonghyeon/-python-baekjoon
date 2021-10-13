def main():
    list = {"black": "0_1",
            "brown": "1_10",
            "red": "2_100",
            "orange": "3_1000",
            "yellow": "4_10000",
            "green": "5_100000",
            "blue": "6_1000000",
            "violet": "7_10000000",
            "grey": "8_100000000",
            "white": "9_1000000000"}
    a = list.get(input()).split("_")[0]
    b = list.get(input()).split("_")[0]
    c = list.get(input()).split("_")[1]

    token = a+b
    value = int(token) * int(c)
    print(value)


if __name__ == '__main__':
    main()
