def ROBMOV1(xst, yst, xen, yen):
    list = []
    if xst == xen and yst == yen:
        print(0)
    while True:
        if yst < yen:
            yst = yst+1
            list.append("N")
        if yst == yen and xst == xen:
            break

        if yst > yen:
            yst = yst - 1
            list.append("S")
        if yst == yen and xst == xen:
            break

        if xst < xen:
            xst = xst+1
            list.append("E")
        if yst == yen and xst == xen:
            break

        if xst > xen:
            xst = xst - 1
            list.append("W")
        if yst == yen and xst == xen:
            break

    print(len(list))
    for ele in list:
        print(ele, end = "")
    print("")
T = int(input())
for f in range(0, T):
    xst, yst, xen, yen = [int(x) for x in input().split()]
    ROBMOV1(xst, yst, xen, yen)
