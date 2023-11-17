def factorial_non_tail_recursive(n):
    if n == 0:
        return 1
    else:
        result = n
        while n > 1:
            n -= 1
            result *= n
        return result

# Get input from user
n = int(input("Enter a number: "))
print(factorial_non_tail_recursive(n))


