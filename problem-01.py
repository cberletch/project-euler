def multiples35(num):
    sum = 0
    for i in range(num):
        if (i % 3 == 0):
            sum += i
        elif (i % 5 == 0):
            sum += i
    return sum

sum = multiples35(1000)
print(sum)