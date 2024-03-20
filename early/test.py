from meow import get_height


def mario():
    h = get_height()
    for i in range(h):
        for j in range(h):
            print("#", end="")
        print()


mario()
