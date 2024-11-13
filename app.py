def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def login(username, password):
    if not username:
        raise ValueError("Username cannot be empty.")
    if len(password) < 6:
        raise ValueError("Password must be at least 6 characters long.")
    return "Login successful"
