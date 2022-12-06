from aocd import get_data
import re

expr = re.compile(r"move (\d+) from (\d+) to (\d+)")


def p1(data):
    pos = ' 1   2   3   4   5   6   7   8   9 '
    cols = {
        '1': [],
        '2': [],
        '3': [],
        '4': [],
        '5': [],
        '6': [],
        '7': [],
        '8': [],
        '9': [],
    }

    for row in data:
        if '[' in row:
            
            for i, y in enumerate(row):
                if y.isalpha():
                    cols[pos[i]].insert(0, y)

        if re_exp:= expr.match(row):
            num, to_col, from_col = re_exp.groups()
            for i in range(int(num)):
                val = cols[to_col].pop()
                cols[from_col].append(val)

    return [b[-1] for b in cols.values()]


def p2(data):
    pos = ' 1   2   3   4   5   6   7   8   9 '
    cols = {
        '1': [],
        '2': [],
        '3': [],
        '4': [],
        '5': [],
        '6': [],
        '7': [],
        '8': [],
        '9': [],
    }

    for row in data:
        if '[' in row:
            for i, y in enumerate(row):
                if y.isalpha():
                    cols[pos[i]].insert(0, y)

        if re_exp := expr.match(row):
            num, from_col, to_col = re_exp.groups()
            val = cols[from_col][-int(num):]
            cols[from_col] = cols[from_col][:-int(num)]
            cols[to_col] = cols[to_col] + val

    return [b[-1] for b in cols.values()]


def main():
    data = get_data(day=5, year=2022).splitlines()

    print(data, type(data))
    print()
    print(f"p1: {p1(data)}")
    print(f"p2: {p2(data)}")


if __name__ == "__main__":
    main()