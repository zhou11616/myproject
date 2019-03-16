if __name__ == '__main__':
    m9 = [1,2,3,4,5,6,7,8,9]
    for i in m9:
        for j in m9:
            print(str(i)+"*"+str(j)+"="+str(i*j),end=" ")
            if i == j:
                print()
                break

print('\n'.join([''.join([('Love'[(x - y) % len('Love')] if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (
                x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))

if __name__ == '__main__':
    num=int(input("请输入三角列数"))+1



    def triangles():
        n = [1]
        while True:
            yield n
            n = [x + y for x, y in zip([0] + n, n + [0])]



    n = 0
    for t in triangles():
        print(t)
        n = n + 1
        if n == num:
            break

            rows = input("请输入一个数值：")

            for i in range(0, rows + 1):  # 变量i控制行数
                for j in range(0, rows - i):  # (1,rows-i)
                    print
                    " ",
                    j += 1
                for k in range(0, 2 * i - 1):  # (1,2*i)
                    if k == 0 or k == 2 * i - 2 or i == rows:
                        if i == rows:
                            if k % 2 == 0:  # 因为第一个数是从0开始的，所以要是偶数打印*，奇数打印空格
                                print("*")

                            else:
                                print("*")
                                # 注意这里的","，一定不能省略，可以起到不换行的作用
                        else:
                            print("*")

                    else:
                        print("")

                    k += 1
                print("/n")

                i += 1
        rows = input("请输入一个数值：")

        for i in range(0, rows + 1):  # 变量i控制行数
            for j in range(0, rows - i):  # (1,rows-i)
                print
                " ",
                j += 1
            for k in range(0, 2 * i - 1):  # (1,2*i)
                if k == 0 or k == 2 * i - 2 or i == rows:
                    if i == rows:
                        if k % 2 == 0:  # 因为第一个数是从0开始的，所以要是偶数打印*，奇数打印空格
                            print("*")

                        else:
                            print("*")
                            # 注意这里的","，一定不能省略，可以起到不换行的作用
                    else:
                        print("*")

                else:
                    print("")

                k += 1
            print("/n")

            i += 1
    rows = input("请输入一个数值：")

    for i in range(0, rows + 1):  # 变量i控制行数
        for j in range(0, rows - i):  # (1,rows-i)
            print
            " ",
            j += 1
        for k in range(0, 2 * i - 1):  # (1,2*i)
            if k == 0 or k == 2 * i - 2 or i == rows:
                if i == rows:
                    if k % 2 == 0:  # 因为第一个数是从0开始的，所以要是偶数打印*，奇数打印空格
                        print("*")

                    else:
                        print("*")
                        # 注意这里的","，一定不能省略，可以起到不换行的作用
                else:
                    print("*")

            else:
                print("")

            k += 1
        print("/n")

        i += 1
rows = input("请输入一个数值：")

for i in range(0, rows + 1):  # 变量i控制行数
    for j in range(0, rows - i):  # (1,rows-i)
        print
        " ",
        j += 1
    for k in range(0, 2 * i - 1):  # (1,2*i)
        if k == 0 or k == 2 * i - 2 or i == rows:
            if i == rows:
                if k % 2 == 0:  # 因为第一个数是从0开始的，所以要是偶数打印*，奇数打印空格
                    print("*")

                else:
                    print("*")
                    # 注意这里的","，一定不能省略，可以起到不换行的作用
            else:
                print("*")

        else:
            print("")

        k += 1
    print("/n")

    i += 1
rows = input("请输入一个数值：")

for i in range(0, rows + 1):  # 变量i控制行数
    for j in range(0, rows - i):  # (1,rows-i)
        print
        " ",
        j += 1
    for k in range(0, 2 * i - 1):  # (1,2*i)
        if k == 0 or k == 2 * i - 2 or i == rows:
            if i == rows:
                if k % 2 == 0:  # 因为第一个数是从0开始的，所以要是偶数打印*，奇数打印空格
                    print("*")

                else:
                    print("*")
                    # 注意这里的","，一定不能省略，可以起到不换行的作用
            else:
                print("*")

        else:
            print("")

        k += 1
    print("/n")

    i += 1
