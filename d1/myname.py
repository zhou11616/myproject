def list():
 try:
    print(5 / 0)

 except ZeroDivisionError as e:
    pass

    print("ZeroDivisionError")
    print(e)
    print("good")
def ge():
    mfile = open(r"C:\Users\Dell\PycharmProjects\untitled\day4\c.doc", "rb")
    mbool = mfile.read()
    print(mbool)

    nfile = open(r"C:\Users\Dell\PycharmProjects\untitled\day4\d.doc", "wb")
    nn = nfile.write(mbool)
    print(nn)
def a():
    print()
if __name__ == '__main__':
    list()
