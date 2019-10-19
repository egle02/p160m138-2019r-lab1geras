import sys


def greet(name: str, shout_count: int = 1):
    return f"Hello, {name}{shout_count * '!'}"


if __name__ == '__main__':
    n = 1
    if len(sys.argv) == 3:
        n = int(sys.argv[2])

    te = greet(sys.argv[1], n)
    print(te)
