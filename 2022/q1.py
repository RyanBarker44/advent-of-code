from aocd import get_data


def get_calories_list(data):
    cur_score, scores_list = 0, []

    for x in data:
        if x == '':
            scores_list.append(cur_score)
            cur_score = 0
            continue
        cur_score += int(x)   

    if cur_score:
        scores_list.append(cur_score)

    return scores_list


def p1(data):
    return max(get_calories_list(data))


def p2(data):
    return(sum(sorted(get_calories_list(data))[-3:]))


def main():
    data = get_data(day=1, year=2022).splitlines()

    print(data, type(data))
    print(f"p1: {p1(data)}")
    print(f"p2: {p2(data)}")


if __name__ == "__main__":
    main()