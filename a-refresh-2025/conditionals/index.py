def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be a least 3 characters long")
    else:
        print("Valid username")
hint_username("salih")


def is_even(num):
    if num % 2 == 0:
        return True
    return False