def meow(n):
    i = 0

    while i < n:
        print("meow")
        i += 1


def greet():
    name = input("what is your name? ")
    print(f"Hello, {name}")


def search(item, list):
    for i in list:
        if (item == i):
            return f"Found {i}!"
        else:
            return f"404 not found!"


def get_height():
    while True:
        try:
            height = int(input("Enter height: "))
            if height > 0:
                return height
        except ValueError:
            print("Not an integer")
