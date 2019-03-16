if __name__ == '__main__':
    for i in range(-4, 5):
        if i < 0:
            j = -i
        else:
            j = i
        print(' ' * j + '*' * (9 - 2 * j))

if __name__ == '__main__':
    mytuple = (1,2,3,4,5,6)
    ntuple = mytuple
    print("id of ntuple->",id(ntuple))
    print("id of mtuple->",id(mytuple))
    ntuple += mytuple
    print("id of += ntuple->",id(ntuple))