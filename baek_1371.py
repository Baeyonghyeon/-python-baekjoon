import sys

def main():
    printvalue = ""
    inputstr= sys.stdin.read()
    con = []
    for i in range(27):
        con.append(0)

    for loop in range(len(inputstr)):
        if inputstr[loop] == " ":
            continue
        else:
            con[ord(inputstr[loop])-97] += 1

    mai = max(con)
    for j in range(27):
        if con[j] == mai:
            printvalue += chr(j+97)

    print(printvalue)


if __name__ == '__main__':
    main()