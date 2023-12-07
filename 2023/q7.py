from aocd import get_data
from collections import Counter

order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

def sorter(r):
    if r[1] == 5:
        return 1
    elif r[1] == 4:
        return 2
    elif r[1] == 3:
        return 3
    elif r[1] == 2:
        return 4
    else:
        return 5

def p1(data):
    map = {
        "five of a kind": [],
        "four of a kind": [],
        "full house": [],
        "three of a kind": [],
        "two pair": [],
        "pair": [],
        "high card": [],
    }

    hands = []
    for hand in data:
        cards, _ = hand.split()
        counter = Counter(cards)
        hands.append((counter, hand))
    
    for hand in hands:
        common = hand[0].most_common()
        most_common_letter = common[0][1]
        if len(common) > 1:
            second_common = common[1][1]

        if most_common_letter == 5:
            map["five of a kind"].append(hand[1].split())
        elif most_common_letter == 4:
            map["four of a kind"].append(hand[1].split())
        elif most_common_letter == 3 and second_common == 2:
            map["full house"].append(hand[1].split())
        elif most_common_letter == 3:
            map["three of a kind"].append(hand[1].split())
        elif most_common_letter == 2 and second_common == 2:
            map["two pair"].append(hand[1].split())
        elif most_common_letter == 2:
            map["pair"].append(hand[1].split())
        else:
            map["high card"].append(hand[1].split())

    for k, v in map.items():
        map[k] = sorted(v, key=lambda x: (order.index(x[0][0]), order.index(x[0][1]), order.index(x[0][2]), order.index(x[0][3]), order.index(x[0][4])), reverse=False)

    map["high card"].reverse()
    map["pair"].reverse()
    map["two pair"].reverse()
    map["three of a kind"].reverse()
    map["full house"].reverse()
    map["four of a kind"].reverse()
    map["five of a kind"].reverse()
    total_list = map["high card"] + map["pair"] + map["two pair"] + map["three of a kind"] + map["full house"] + map["four of a kind"] + map["five of a kind"]

    end = []
    for i, a in enumerate(total_list):
        end.append([i + 1, a])

    total = 0
    for e in end:
        total += (e[0] * int(e[1][1]))

    return total


def p2(data):
    hands = []
    for hand in data:
        cards, bid = hand.split()
        counter = Counter(cards)
        sorted_by_pairs = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        hands.append((sorted_by_pairs, hand))
    
    map = {
        "five of a kind": [],
        "four of a kind": [],
        "full house": [],
        "three of a kind": [],
        "two pair": [],
        "pair": [],
        "high card": [],
    }
    
    for hand in hands:
        # Find Jokers
        j_count = 0
        for c in hand[0]:
            if c[0] == 'J':
                j_count = c[1]
                break
        
        # Add Jokers to max card
        max_card = hand[0][0][1] + j_count

        # Pull second highest card
        if len(hand[0]) > 1:
            second_card = hand[0][1][1]

        if j_count:
            # If Joker is in the highest card, add it to the second card
            if hand[0][0][0] == 'J' and len(hand[0]) > 1:
                max_card = hand[0][1][1] + j_count
            # All are Jokers
            elif hand[0][0][0] == 'J' and len(hand[0]) == 1:
                max_card = j_count
            # if Joker is in the second card, select the 3rd as the second highest card
            elif len(hand[0]) > 2 and hand[0][1][0] == 'J':
                second_card = hand[0][1][1]   
        
        if  max_card == 5:
            map["five of a kind"].append(hand[1].split())
        elif max_card == 4:
            map["four of a kind"].append(hand[1].split())
        elif max_card == 3 and second_card == 2:
            map["full house"].append(hand[1].split())
        elif max_card == 3:
            map["three of a kind"].append(hand[1].split())
        elif max_card == 2 and second_card == 2:
            map["two pair"].append(hand[1].split())
        elif max_card == 2:
            map["pair"].append(hand[1].split())
        else:
            map["high card"].append(hand[1].split())

    for k, v in map.items():
        map[k] = sorted(v, key=lambda x: (order.index(x[0][0]), order.index(x[0][1]), order.index(x[0][2]), order.index(x[0][3]), order.index(x[0][4])), reverse=False)

    map["high card"].reverse()
    map["pair"].reverse()
    map["two pair"].reverse()
    map["three of a kind"].reverse()
    map["full house"].reverse()
    map["four of a kind"].reverse()
    map["five of a kind"].reverse()
    total_list = map["high card"] + map["pair"] + map["two pair"] + map["three of a kind"] + map["full house"] + map["four of a kind"] + map["five of a kind"]

    end = []
    for i, a in enumerate(total_list):
        end.append([i + 1, a])

    total = 0
    for e in end:
        total += (e[0] * int(e[1][1]))

    return total


def main():
    data = get_data(day=7, year=2023).splitlines()

    print(data, type(data))
    print(f"p1: {p1(data)}")
    print(f"p2: {p2(data)}")


if __name__ == "__main__":
    main()