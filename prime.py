def thirtyTwos(n):
    '''
        >>> thirtyTwos(432601)
        1
        >>> thirtyTwos(132432601)
        2
        >>> thirtyTwos(78)
        0
    '''
    ## YOUR CODE STARTS HERE
    if n < 32:
        return 0
    if n%100 == 32:
        return 1 + thirtyTwos(n//10)
    else:
        return thirtyTwos(n//10)



def flat(aList):
    '''
        >>> x = [3, [[5, 2]], 6, [4]]
        >>> flat(x)
        [3, 5, 2, 6, 4]
        >>> x
        [3, [[5, 2]], 6, [4]]
        >>> flat([1, 2, 3])
        [1, 2, 3]
        >>> flat([1, [], 3])
        [1, 3]
    '''
    ## YOUR CODE STARTS HERE
    if len(aList) == 0:
        return []
    if type(aList[0]) != list:
        return [aList[0]] + flat(aList[1:len(aList)])
    else:
        return flat(aList[0])+ flat(aList[1:len(aList)])

# ############ DO NOT modify the triangle(n) function in any way!
# def triangle(n):
#     return recursiveTriangle(n, n)
# ##################

# def recursiveTriangle(k, n):
#     '''
#         >>> recursiveTriangle(2,4)
#         '  **\\n   *'
#         >>> print(recursiveTriangle(2,4))
#           **
#            *
#         >>> triangle(4)
#         '****\\n ***\\n  **\\n   *'
#         >>> print(triangle(4))
#         ****
#          ***
#           **
#            *
#     '''
#     ## YOUR CODE STARTS HERE
#     spaces = n-k
#     if k == 1:
#        return " "*spaces + "*"
#     return " "*spaces + "*"*k + "\n" + recursiveTriangle(k-1,n)

# '''
#         >>> isPrime(5)
#         True
#         >>> isPrime(1)
#         False
#         >>> isPrime(0)
#         False
#         >>> isPrime(85)
#         False
#         >>> isPrime(1019)
#         True
#         >>> isPrime(2654)
#         False
#         >>> isPrime(6)
#         False
#     '''



def isPrime(num, i=2):
    '''
        >>> isPrime(100000007)
        True
        >>> isPrime(1)
        False
        >>> isPrime(0)
        False
        >>> isPrime(85)
        False
        >>> isPrime(1019)
        True
        >>> isPrime(2654)
        False
    '''
    ## YOUR CODE STARTS HERE
    if num == 0 or num == 1:
        return False
    max = int((num**.5)//1) + 1

    if i >= max:
        return True

    if num  % i == 0:
        return False
    else:
        return isPrime(num, i+1)

