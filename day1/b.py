if __name__ == '__main__':
    klist = [
        "good ", "good ", "study",
        " good ", "good", "study ",
        "good ", " good", " study",
        " good ", "good", " study ",
        "good ", "good ", "study",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
    ]
    # 创建空列表
    qlist = []
    # 循环去除空格
    for k in klist:
        a = k.strip()
        # 将去完的数据放在空列表中
        qlist.append(a)
    # 创建集合并把列表放入  去重
    qtest = set(qlist)
    # 创建字典
    zd = {}
    # 遍历集合
    for q in qtest:
        # 字典的键     等于每次取出来的值
        zd[q] = q
0
    print(zd)

    # wlist = [k.strip() for k in klist1]
    # lset = set(wlist)
    # vas = {l: l for l in lset}