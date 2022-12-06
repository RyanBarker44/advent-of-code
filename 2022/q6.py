from aocd import get_data


def p1(data):
    n = 4
    for i in range(len(data[0])):
        if len(set(data[0][i: i+n])) == n:
            return i


def p2(data):
    n = 14
    for i in range(len(data[0])):
        if len(set(data[0][i: i+n])) == n:
            return i

# One liners
def p1_2(data):
    return [i for i in range(len(data[0])) if len(set(data[0][i: i+4])) == 4][0]


def p2_2(data):
    return [i for i in range(len(data[0])) if len(set(data[0][i: i+14])) == 14][0]


def main():
    data = get_data(day=6, year=2022).splitlines()

    print(data, type(data), len(data))
    print(f"p1: {p1(data)}")
    print(f"p2: {p2(data)}")


if __name__ == "__main__":
    main()