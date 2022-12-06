from aocd import get_data


def chunk_list(data):
    N = 3
    return [data[i:i+N] for i in range(0, len(data), N)]


def p1(data):
    characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r', 's', 't','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R', 'S', 'T','U','V','W','X','Y','Z']
    score = 0
    for x in data:
        a, b = x[:len(x)//2], x[len(x)//2:]
        score += sum(
            [characters.index(i)+1 for i in list(set(a).intersection(b))]
        )

    return score


def p2(data):
    data = chunk_list(data)

    characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r', 's', 't','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R', 'S', 'T','U','V','W','X','Y','Z']
    score = 0
    for group in data:    
        a, b, c = group
        score += sum(
            [characters.index(i)+1 for i in list(set(a).intersection(b).intersection(c))]
        )

    return score


def main():
    data = get_data(day=3, year=2022).splitlines()

    print(data, type(data))
    print(f"p1: {p1(data)}")
    print(f"p2: {p2(data)}")


if __name__ == "__main__":
    main()