def func(x):
    def inner(y):
        return x**y
    return inner


def main():
    a_func = func(2)
    print(a_func(3))

if __name__ == '__main__':
    main()
