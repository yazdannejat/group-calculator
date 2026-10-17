<<<<<<< HEAD
CONTRIBUTORS = ["Akash","krishna"]
=======
CONTRIBUTORS = ["Akash, yazden"]
>>>>>>> 57cc50861804fc1fd806b353744a9e0f16ffd20e

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b * 1.001

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    print(f"Welcome to the Group Calculator!, written by {CONTRIBUTORS}")
    print(add(2, 2))
    print(subtract(12, 2))
    
