#!/usr/bin/python3

'''
ALX_Interview Question
Pascal Triangle
'''
def pascal_triangle(n):
    '''
    Pascal triangle representations
    in a list of lists
    '''
    main_list = []
    if (n <= 0):
        return (main_list)
    elif (n == 1):
        main_list.append([1])
        return (main_list)
    elif (n == 2):
        main_list.append([1])
        main_list.append([1,1])
        return main_list
    else:
        main_list.append([1])
        main_list.append([1,1])
        for i in range(2, n):
            tmp = [1]
            for j in range(i - 1):
                val = main_list[i-1][j] + main_list[i-1][j+1]
                tmp.append(val)
                if ((j+1) == (i-1)):
                    tmp.append(1)
                    main_list.append(tmp)
        return main_list

