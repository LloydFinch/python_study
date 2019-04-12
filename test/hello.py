print 'hello'
L = []


def sum(list):
    for i in range(1, 100):
        L.append(i)

    sum = 0
    for num in list:
        sum += num * num

    return sum


print sum(L)
