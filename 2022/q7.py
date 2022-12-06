from aocd import get_data


def p1(data):
    return


def p2(data):
    return


def main():
    data = get_data(day=7, year=2022).splitlines()

    print(data, type(data))
    print(f"p1: {p1(data)}")
    print(f"p2: {p2(data)}")


if __name__ == "__main__":
    main()