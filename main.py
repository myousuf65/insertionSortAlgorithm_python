#function that sorts the values (val[], siz (sizeOfArray), commandToExecute)
def sortingalgo(val, siz, command):
    if command == 1:
        for i in range(siz):
            for g in range(siz):
                if val[g] > val[i]:
                    temp = val[g]
                    val[g] = val[i]
                    val[i] = temp
    elif command == 2:
        for i in range(siz):
            for g in range(siz):
                if val[i]>val[g]:
                    temp = val[i]
                    val[i] = val[g]
                    val[g] = temp
#print the values after sorting is done
    for item in val:
        print(item)

#------------------------------------------------
#function for initializing the list
def init():
    value = []
    loop = True
    while loop:
        size = int(input('how many values do u want to input...'))

        for i in range(size):
            value.append(input('Input value.. '))

        print('''
        [1]Ascending Order
        [2]Descending Order
        [3]Nothing
        ''')
        command = int(input('What do you want to do...'))
        sortingalgo(value, size,command)
        #avoid appending of items in next loop over the previous items
        value.clear()
        _loop = True
        #continue the loop until user answers the question correctly
        while _loop:
            _continue = input('Do you want to continue[y][n]...')
            if _continue == 'y':
                loop = True
                _loop = False
            elif _continue == 'n':
                loop = False
                _loop = False
            else:
                _loop = True
                print('Invalid Command')

if __name__ == "__main__":
    init()
