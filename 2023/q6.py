from aocd import get_data


def p1(data):
    times = [x for x in data[0].split(" ") if x.isdigit()]
    distances = [x for x in data[1].split(" ") if x.isdigit()]

    result = {}
    for t, record in zip(times, distances):
        speed = 0
        distance_travelled = 0
        for time_held in range(0, int(t)):
            distance_travelled = (speed * (int(t) - time_held))
            if distance_travelled > int(record):
                result[t] = result.get(t, 0) + 1
            speed += 1

    total = 1
    for x in result.values():
        total *= x

    return total


def p2(data):
    time = "".join([x for x in data[0] if x.isdigit()])
    distance = "".join([x for x in data[1] if x.isdigit()])

    total, speed, distance_travelled = 0, 0, 0
    for time_held in range(0, int(time)):
        distance_travelled = (speed * (int(time) - time_held))
        if distance_travelled > int(distance):
            total += 1
        speed += 1

    return total


def main():
    data = get_data(day=6, year=2023).splitlines()

    print(data, type(data))
    print(f"p1: {p1(data)}")
    print(f"p2: {p2(data)}")


if __name__ == "__main__":
    main()