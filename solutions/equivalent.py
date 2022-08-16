def divideSort(string):
    if len(string) % 2:
        return string

    a = divideSort(string[:len(string)//2])
    b = divideSort(string[len(string)//2:])

    if (a < b):
        return a + b
    else:
        return b + a

if __name__ == '__main__':
    a = input()
    b = input()

    if divideSort(a) == divideSort(b):
        print('YES')
    else:
        print('NO')