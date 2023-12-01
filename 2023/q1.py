from aocd import get_data
import re


def p1(data):
    sum = 0
    for row in data:
        total = 0
        r = re.sub(r'[^0-9]', '', row)
        r1 = r[0]
        r2 = r[-1]
        total = r1 + r2
        sum += int(total)

    return sum

map = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five':5,
    'six':6,
    'seven':7,
    'eight':8,
    'nine':9,
}

def replace(r):
    for i, _ in enumerate(r):
        for word in map:
            if len(word) > len(r[i:]):
                continue
            if r[i:i + len(word)] == word:
                r = r[:i] + str(map[word]) + r[i + len(word) - 1:]
                break
        if i > len(r) - 1:
            break
    return r

def p2(data):
    sum = 0

    for row in data:
        total = 0
        row = replace(row)
        r = re.sub(r'[^0-9]', '', row)
        r1 = r[0]
        r2 = r[-1]
        total = r1 + r2
        sum += int(total)

    return sum


def main():
    data = get_data(day=1, year=2023).splitlines()

    print(data, type(data))
    print(f"p1: {p1(data)}")
    print(f"p2: {p2(data)}")


if __name__ == "__main__":
    main()