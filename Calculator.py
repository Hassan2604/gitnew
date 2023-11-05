def get_user_input(text):
    while True:
        try:
            user_input = input(text)
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a number.")

def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print("What operation do you want to perform?")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    user_choice = input("Enter your choice (1-4): ")
    if user_choice in ["1", "2", "3", "4"]:
        break
    print("Invalid choice. Please enter a number between 1 and 4.")

num1 = get_user_input("Enter your input for number 1: ")
num2 = get_user_input("Enter your input for number 2: ")

if user_choice == "1":
    print(add(num1, num2))
elif user_choice == "2":
    print(sub(num1, num2))
elif user_choice == "3":
    print(mul(num1, num2))
elif user_choice == "4":
    print(divide(num1, num2))