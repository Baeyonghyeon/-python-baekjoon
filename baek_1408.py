def main():
    outMM = 0
    outmm = 0
    outss = 0

    token = input().split(":") #현재시간
    MM = int(token[0])
    mm = int(token[1])
    ss = int(token[2])

    token = input().split(":") #미션시간
    M = int(token[0])
    m = int(token[1])
    s = int(token[2])

    outMM = M-MM
    if mm > m:
        outMM -= 1
        m += 60
    outmm = m - mm
    if ss > s:
        if outmm == 0:
            outMM -= 1
            outmm += 60
        outmm -= 1
        s += 60
    outss = s - ss

    if(outMM < 0):
        outMM = 24 + outMM
    if (outmm < 0):
        outmm = 60 + outmm
    if (outss < 0):
        outss = 60 + outss


    outMM = str(outMM)
    if (len(outMM))==1:
        outMM = "0"+outMM

    outmm = str(outmm)
    if (len(outmm))==1:
        outmm = "0"+outmm

    outss = str(outss)
    if (len(outss))==1:
        outss = "0"+outss
    print(outMM+":"+outmm+":"+outss)


if __name__ == '__main__':
    main()