from functools import cmp_to_key
from collections import Counter
import re

include_joker = False

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
    frequency = Counter(hand)
    # Checking if jokers have to be included (for part2)
    if include_joker:
        #Removing all joker entries and replacing them with most_common card
        joker_count = frequency["J"]
        del frequency["J"]
        #If all cards are jokers, then giving them the highest value i.e 'A'
        if not frequency:
            frequency["A"] = 5
        #Finding most common entry and adding the joker_count
        else:
            most_common, count = frequency.most_common(1)[0] #[(<entry1>:<frequency1>)]
            frequency[most_common] += joker_count

    entries = len(frequency)
    if entries == 1: return "5kind"
    if entries == 2:
        if 4 in frequency.values(): return "4kind"
        else: return "fullhouse"
    if entries == 3:
        if 3 in frequency.values(): return "3kind"
        else: return "2pair"
    if entries == 4: return "1pair"
    return "high"  

def compare_strength(hand1, hand2):
    VALUE = {"A":14, "K":13, "Q":12, "J":11, "T":10, "9":9, "8":8, "7":7, "6":6, "5":5, "4":4, "3":3, "2":2}
    #If joker is included, value of J will fall down
    if include_joker: VALUE["J"] = 1
    for char1, char2 in zip(hand1, hand2):
        if VALUE[char1] > VALUE[char2]:
            return 1
        if VALUE[char1] < VALUE[char2]:
            return -1
    return 0

path = "7.Camel_Cards\input.txt"
CARDS = get_puzzle(path)

# Part 1
print(total_winnings(CARDS))

# Part 2
include_joker = True #including joker for part2
print(total_winnings(CARDS))
