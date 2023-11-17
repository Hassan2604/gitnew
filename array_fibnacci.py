
n = int(input("Enter the number of Fibonacci numbers to generate: "))

fib = [0, 1]
for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])

print("The first", n, "Fibonacci numbers are:", end=" ")
for i in range(n):
    print(fib[i], end=" ")