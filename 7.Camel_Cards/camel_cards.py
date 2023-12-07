from functools import cmp_to_key
from collections import defaultdict
import re

def get_puzzle(path):
    with open(path) as file:
        return parse_input(file)

def parse_input(file):
    CARDS = []
    for line in file:
        hand, bid = line.split()
        CARDS.append((hand, int(bid)))
    return CARDS

def total_winnings(CARDS):
    CARDS = sort_cards(CARDS)
    total = 0
    for rank, card in enumerate(CARDS, 1):
        hand, bid = card
        total += rank * bid
    return total

def sort_cards(CARDS):
    return sorted(CARDS, key = cmp_to_key(compare_power))

def compare_power(card1, card2):
    # POWER : {<type>:<power>}
    POWER = {"high":0, "1pair":1, "2pair":2, "3kind":3, "fullhouse":4, "4kind":5, "5kind":6}
    hand1, bid1 = card1
    hand2, bid2 = card2
    type1, type2 = get_type(hand1), get_type(hand2)
    if POWER[type1] == POWER[type2]:
        return compare_strength(hand1, hand2)
    else:
        return 1 if POWER[type1] > POWER[type2] else -1

def get_type(hand):
    frequency = defaultdict(lambda: 0)
    for char in hand:
        frequency[char] += 1
    if len(frequency) == 1:
        return "5kind"
    if len(frequency) == 2:
        if 4 in frequency.values():
            return "4kind"
        else:
            return "fullhouse"
    if len(frequency) == 3:
        if 3 in frequency.values():
            return "3kind"
        else:
            return "2pair"
    if len(frequency) == 4:
        return "1pair"
    return "high"  
    # if re.match(r'(\w)\1{4,}', hand):
    #     print("5kind", hand)
    # if re.match(r'.*(\w).*\1.*\1.*\1', hand):
    #     print("4kind", hand)
    # three_pos = re.match(r'.*(\w).*\1.*\1', hand)
    # if three_pos:
    #     print(three_pos)
    #     if re.match(r'(\w).*\1', hand[:three_pos.start()] + hand[three_pos.end() + 1:]):
    #         print("fullhouse", hand)


def compare_strength(hand1, hand2):
    VALUE = {"A":14, "K":13, "Q":12, "J":11, "T":10, "9":9, "8":8, "7":7, "6":6, "5":5, "4":4, "3":3, "2":2}
    for char1, char2 in zip(hand1, hand2):
        if VALUE[char1] > VALUE[char2]:
            return 1
        if VALUE[char1] < VALUE[char2]:
            return -1
    return 0

path = "7.Camel_Cards\input.txt"
CARDS = get_puzzle(path)
print(total_winnings(CARDS))
