def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def login(username, password):
    if username == "admin" and password == "secret":
        return "Login successful"
    return "Invalid credentials"
