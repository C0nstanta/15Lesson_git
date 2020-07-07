import random


def rand_def(n):
    num = random.randint(0, n)
    return num


def new_function(s: str):
    if len(s) >= 100 :
        print("Hello one")
    else:
        print("Hello two")


if __name__ == "__main__":
    rand_def(10)
    print("Hello world!")