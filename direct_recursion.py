def direct_recursion(n):
    if n <= 0:
        return
    print(n)
    direct_recursion(n-1)

n = int(input("Enter a number: "))
direct_recursion(n)