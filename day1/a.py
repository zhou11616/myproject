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
    nlist = [str(i).strip() for i in klist]

    mset = set(nlist)
    mdict = {}
    for i in mset:
        mdict[i] = nlist.count(i)
        if nlist.count(i) > 1:
            print(i)
    print(mdict)