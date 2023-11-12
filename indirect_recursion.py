def even(n):
    if n == 0:
        return True
    else:
        return odd(n-1 )

def odd(n):
    if n == 0:
        return False
    else:
        return even(n-1)

# Example usage
number = int(input("Enter a number: "))

if even(number):
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
