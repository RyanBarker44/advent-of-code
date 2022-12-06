from aocd import get_data


def p1(data):
    win = 6
    tie = 3
    loss = 0

    shape_scores = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }
    win_map = {
        'X': 'C',
        'Y': 'A',
        'Z': 'B',
    }
    loss_map = {
        'X': 'B',
        'Y': 'C',
        'Z': 'A',
    }
    tie_map = {
        'X': 'A',
        'Y': 'B',
        'Z': 'C',
    }

    total_score = 0

    for x in data:
        a, b = x[0], x[2]

        if win_map.get(b) == a:
            outcome_score = win
        if loss_map.get(b) == a:
            outcome_score = loss
        if tie_map.get(b) == a:
            outcome_score = tie

        total_score += shape_scores.get(b) + outcome_score

    return total_score


def p2(data):
    win = 6
    tie = 3
    loss = 0

    shape_scores = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }
    win_map = {
        'C': 'X',
        'A': 'Y',
        'B': 'Z',
    }
    loss_map = {
        'B': 'X',
        'C': 'Y',
        'A': 'Z',
    }
    tie_map = {
        'A': 'X',
        'B': 'Y',
        'C': 'Z',
    }
    outcome_map = {
        'X': loss_map,
        'Y': tie_map,
        'Z': win_map,
    }

    total_score = 0

    for x in data:
        a, b = x[0], x[2]
        outcome = outcome_map[b]

        if b == 'Z':
            outcome_score = win
        if b == 'X':
            outcome_score = loss
        if b == 'Y':
            outcome_score = tie

        total_score += shape_scores.get(outcome[a]) + outcome_score

    return total_score


def main():
    data = get_data(day=2, year=2022).splitlines()

    print(data, type(data))
    print(f"p1: {p1(data)}")
    print(f"p2: {p2(data)}")


if __name__ == "__main__":
    main()