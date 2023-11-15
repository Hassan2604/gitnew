def factorial_non_tail_recursive(n):
    if n == 0:
        return 1
    else:
        result = n
        while n > 1:
            n -= 1
            result *= n
        return result

def linear_recursion(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return linear_recursion(n - 1) + linear_recursion(n - 2)
