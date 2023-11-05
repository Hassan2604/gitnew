def get_user_input(text):
    while True:
        try:
            user_input = input(text)
            return user_input
        except ValueError:
            print("Invalid input, please try again.")

while True:
    user_input = get_user_input("Enter your input: ")    
    if user_input == "exit":
        break
    for i in range(1, 11):
        print(f"{user_input} x {i} = {int(user_input) * i}")