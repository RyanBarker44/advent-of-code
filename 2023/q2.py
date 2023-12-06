from aocd import get_data


def p1(data):
    cube_limits = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    total = 0

    for game in data:
        game_num = "".join([x for x in game.split(":")[0] if x.isdigit()])
        rounds = [x for x in (game.split(":")[1]).split(";")]
        failed = False
        for r in rounds:
            cubes = [x.strip() for x in r.split(',')]
            for c in cubes:
                num, colour = c.split(' ')
                if cube_limits[colour] < int(num):
                    failed = True
                    break

        if not failed:
            total += int(game_num) 

    return total


def p2(data):
    game_map = {}

    for game in data:
        game_num = "".join([x for x in game.split(":")[0] if x.isdigit()])
        game_map[game_num] = {"red": 0, "green": 0, "blue": 0}
        rounds = [x for x in (game.split(":")[1]).split(";")]
        for r in rounds:
            cubes = [x.strip() for x in r.split(',')]
            for c in cubes:
                num, colour = c.split(' ')
                game_map[game_num][colour] = max(int(num), game_map[game_num][colour])

    totals = []
    for game in game_map.values():
        total = 1
        for min_cube_count in game.values():
            total *= min_cube_count
        totals.append(total)

    return sum(totals)



def main():
    data = get_data(day=2, year=2023).splitlines()

    print(data, type(data))
    print(f"p1: {p1(data)}")
    print(f"p2: {p2(data)}")


if __name__ == "__main__":
    main()
