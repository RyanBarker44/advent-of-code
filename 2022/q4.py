from aocd import get_data


def extract_ranges(row):
    a, b = row.split(',')
    a1, a2 = a.split('-')
    b1, b2 = b.split('-')

    return range(int(a1), int(a2)+1), range(int(b1), int(b2)+1)


def p1(data):
    total = 0
    for row in data:
        r1, r2 = extract_ranges(row)
        total += all(item in r1 for item in r2) or all(item in r2 for item in r1)

    return total


def p2(data):
    total = 0
    for row in data:
        r1, r2 = extract_ranges(row)
        total += any(item in r1 for item in r2)

    return total


def main():
    data = get_data(day=4, year=2022).splitlines()

    print(data, type(data))
    print(f"p1: {p1(data)}")
    print(f"p2: {p2(data)}")


if __name__ == "__main__":
    main()