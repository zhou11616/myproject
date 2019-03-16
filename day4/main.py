if __name__ == '__main__':
    mdict = {
        1:"[1]输入用户姓名及性别，然后给出下列的提示",
        2:"[2]输入用户姓名及性别，然后给出下列的提示",
        3:"[3]输入用户姓名及性别，然后给出下列的提示",
        4:"[4]输入用户姓名及性别，然后给出下列的提示"
    }

    while True:

        for cho in mdict.values():
            print(cho)

        sel = input("请选择服务")

        print(mdict[int(sel)])

        import day04.quest1.q1 as q

        if __name__ == '__main__':
            mdict = {
                1: "[1]:输入用户姓名及性别，然后给出下列的提示:XX先生你好 或 XX女士你好",
                2: "[2]:随机生成两个分别包含10和15个整数的列表，并计算输出两个列表的并集",
                3: "[3]:注意一个用户信息，包含EMAIL号，判断信息是否合法，如果合法则输出相关信息（姓名长度不能少于6位，邮件中包含@）",
                4: "[4]:从键盘输入一行字符串，判断是否是回文数",
                0: "[0]退出"
            }
            fdict = {
                1: q.checkSex,
                2: q.two,
                3: q.em,
                4: q.huiwen
            }

            while True:
                for v in mdict.values():
                    print(v)
                num = int(input("请输入编号："))

                for k, v in fdict.items():
                    if num == k:
                        v()
                        break
                    elif num == 0:
                        exit()






