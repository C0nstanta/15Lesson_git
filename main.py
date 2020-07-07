import random


def rand_def(n):
    num = random.randint(0, n)
    return num


if __name__ == "__main__":
    rand_def(10)
    print("Hello world!")