def evenFibonacci(limit):
    sum = 0
    next = 0
    prev = 0
    cur = 1

    while sum <= limit:
        if prev % 2 == 0:
            sum += prev
        next = prev + cur
        prev = cur
        cur = next
    return sum

sum = evenFibonacci(4000000)
print(sum)