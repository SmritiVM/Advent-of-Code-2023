from collections import defaultdict

def parse_input(file):
    Cards = {} #Cards = {<Card no>:[[<winning numbers>], [<numbers possessed>], count: 1]}
    for line in file:
        card, numbers = line.split(':')
        card_number = int(card[5:])
        winning, having = numbers.strip().split('|')
        Cards[card_number] = [winning.strip().split(), having.strip().split(), 1]
    return Cards
        
def sum_of_wins(Cards):
    total_points = 0
    for card_number in Cards:
        matches = count_matches(Cards[card_number]) #send Cards[card_number]
        if matches:
            total_points += 2 ** (matches - 1)
    return total_points

def count_matches(card_details):
    matches = 0
    winning, having = card_details[:2]
    for win in winning:
        if win in having:
            matches += 1
    return matches

#Part 2
def total_scratchcards(Cards):
    for card_number in Cards:
        points = count_matches(card_number, Cards)
        count = Cards[card_number][2]
        while count > 0:
            next_card = card_number + 1
            for _ in range(points):
                Cards[next_card][2] += 1
                next_card += 1
            count -= 1
    return sum([Cards[card_number][2] for card_number in Cards])


with open ("04.Scratchcards\input.txt") as file:
    Cards = parse_input(file)
    print(sum_of_wins(Cards))
    print(total_scratchcards(Cards))
