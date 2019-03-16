if __name__ == '__main__':
        arr = range(1, 101)
        for i in arr:
            print(str(i).rjust(4), end=" ")
            if i % 10 == 0:
                print()

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