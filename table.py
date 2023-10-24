def get_user_input(text):
    while True:
        try:
            user_input = input(text)
            return user_input
        except ValueError:
            print("Invalid input, please try again.")