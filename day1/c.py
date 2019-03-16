def ling(n):
    nstr = range(1, 2 * n)
    for i in nstr[0:n]:
        for j in nstr[n - i : 0 : - 1]:
            print(" ", end=" ")
        for j in nstr[0 : 2 * i - 1]:
            print("*", end=" ")
        print("")
    for i in nstr[0:n-1]:
        for j in nstr[0:i]:
            print(" ", end=" ")
        for j in nstr[2*(n-i)-1:0:-1]:
            print("*", end=" ")
        print("")
def huan():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print("%dX%d=%-2d " % (j, i, i * j), end=" ")
        print()
if __name__ == '__main__':
    ling(9)
