def timestable():
    x = int(input('Choose a number:'))
    n = x + 1
    for i in range(1, n):
        for j in range(1, n):
            print(i * j, end = '\t')
        print('')
if __name__ == '__main__':
    timestable()
    
