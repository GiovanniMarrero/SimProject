import random
#pip install pandas
import pandas as pd

players_hand_value = 0
dealers_hand_value = 0
data = []

BlackjackTotal = 0
WinTotal = 0
LossTotal = 0
PushTotal = 0

for each in range(100000):
    cards_in_deck = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                     'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                     'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                     'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                     'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                     'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                     'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                     'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

    players_hand_value = 0
    dealers_hand_value = 0

    print("\n\n\nThese are cards_in_deck before any dealing:", cards_in_deck)

    players_hand = random.sample(cards_in_deck, 2)

    print("\nThis is players_hand:", players_hand)

    for each in players_hand:
        cards_in_deck.remove(each)

    print("\nThese are cards_in_deck after dealing to player:", cards_in_deck)

    dealers_hand = random.sample(cards_in_deck, 2)

    print("\nThis is dealers_hand:", dealers_hand)

    for each in dealers_hand:
        cards_in_deck.remove(each)

    print("\nThese are cards_in_deck after dealing to dealer:", cards_in_deck)

    # Need to figure out how to make the values from face cards / ace change

    for each in range(len(players_hand)):
        if players_hand[each] == 2:
            players_hand_value = players_hand_value + 2
        if players_hand[each] == 3:
            players_hand_value = players_hand_value + 3
        if players_hand[each] == 4:
            players_hand_value = players_hand_value + 4
        if players_hand[each] == 5:
            players_hand_value = players_hand_value + 5
        if players_hand[each] == 6:
            players_hand_value = players_hand_value + 6
        if players_hand[each] == 7:
            players_hand_value = players_hand_value + 7
        if players_hand[each] == 8:
            players_hand_value = players_hand_value + 8
        if players_hand[each] == 9:
            players_hand_value = players_hand_value + 9
        if players_hand[each] == 10:
            players_hand_value = players_hand_value + 10
        if players_hand[each] == 'Ace':
            players_hand_value = players_hand_value + 11
        if players_hand[each] == 'J':
            players_hand_value = players_hand_value + 10
        if players_hand[each] == 'Q':
            players_hand_value = players_hand_value + 10
        if players_hand[each] == 'K':
            players_hand_value = players_hand_value + 10

    if players_hand_value == 22:
        players_hand_value = 12

    print("\nThis is players_hand_value after dealing:", players_hand_value)

    for each in range(len(dealers_hand)):
        if dealers_hand[each] == 2:
            dealers_hand_value = dealers_hand_value + 2
        if dealers_hand[each] == 3:
            dealers_hand_value = dealers_hand_value + 3
        if dealers_hand[each] == 4:
            dealers_hand_value = dealers_hand_value + 4
        if dealers_hand[each] == 5:
            dealers_hand_value = dealers_hand_value + 5
        if dealers_hand[each] == 6:
            dealers_hand_value = dealers_hand_value + 6
        if dealers_hand[each] == 7:
            dealers_hand_value = dealers_hand_value + 7
        if dealers_hand[each] == 8:
            dealers_hand_value = dealers_hand_value + 8
        if dealers_hand[each] == 9:
            dealers_hand_value = dealers_hand_value + 9
        if dealers_hand[each] == 10:
            dealers_hand_value = dealers_hand_value + 10
        if dealers_hand[each] == 'Ace':
            dealers_hand_value = dealers_hand_value + 11
        if dealers_hand[each] == 'J':
            dealers_hand_value = dealers_hand_value + 10
        if dealers_hand[each] == 'Q':
            dealers_hand_value = dealers_hand_value + 10
        if dealers_hand[each] == 'K':
            dealers_hand_value = dealers_hand_value + 10

    if dealers_hand_value == 22:
        dealers_hand_value = 12

    print("\nThis is dealers_hand_value after dealing:", dealers_hand_value)

    players_hand_after_hit = players_hand[:]
    players_hand_after_hit_value = 0

    for each in range(len(players_hand_after_hit)):         #This is to set another variable to the initial hand, we actually add the hits next step!
        if players_hand_after_hit[each] == 2:
            players_hand_after_hit_value = players_hand_after_hit_value + 2
        if players_hand_after_hit[each] == 3:
            players_hand_after_hit_value = players_hand_after_hit_value + 3
        if players_hand_after_hit[each] == 4:
            players_hand_after_hit_value = players_hand_after_hit_value + 4
        if players_hand_after_hit[each] == 5:
            players_hand_after_hit_value = players_hand_after_hit_value + 5
        if players_hand_after_hit[each] == 6:
            players_hand_after_hit_value = players_hand_after_hit_value + 6
        if players_hand_after_hit[each] == 7:
            players_hand_after_hit_value = players_hand_after_hit_value + 7
        if players_hand_after_hit[each] == 8:
            players_hand_after_hit_value = players_hand_after_hit_value + 8
        if players_hand_after_hit[each] == 9:
            players_hand_after_hit_value = players_hand_after_hit_value + 9
        if players_hand_after_hit[each] == 10:
            players_hand_after_hit_value = players_hand_after_hit_value + 10
        if players_hand_after_hit[each] == 'Ace':
            players_hand_after_hit_value = players_hand_after_hit_value + 11
        if players_hand_after_hit[each] == 'J':
            players_hand_after_hit_value = players_hand_after_hit_value + 10
        if players_hand_after_hit[each] == 'Q':
            players_hand_after_hit_value = players_hand_after_hit_value + 10
        if players_hand_after_hit[each] == 'K':
            players_hand_after_hit_value = players_hand_after_hit_value + 10

    if players_hand_after_hit_value == 22:
        players_hand_after_hit_value = 12

    players_hit = []

    for each in range(10):                                              #for 10 iterations
        if players_hand_after_hit_value < 15:                           #only if current hand value is <15
            players_hit = random.sample(cards_in_deck, 1)               #players_hit is a random sampling of 1 card that remains in the deck
            print("\nThis is players_hit:", players_hit)
            print("\nThis is players_hit[-1]:", players_hit[-1])
            cards_in_deck.remove(players_hit[-1])                       #remove the last item (aka most recent) in players_hit
            players_hand_after_hit.append(players_hit[-1])              #add the latest item to our hand
            if players_hand_after_hit[-1] == 2:
                players_hand_after_hit_value = players_hand_after_hit_value + 2
            if players_hand_after_hit[-1] == 3:
                players_hand_after_hit_value = players_hand_after_hit_value + 3
            if players_hand_after_hit[-1] == 4:
                players_hand_after_hit_value = players_hand_after_hit_value + 4
            if players_hand_after_hit[-1] == 5:
                players_hand_after_hit_value = players_hand_after_hit_value + 5
            if players_hand_after_hit[-1] == 6:
                players_hand_after_hit_value = players_hand_after_hit_value + 6
            if players_hand_after_hit[-1] == 7:
                players_hand_after_hit_value = players_hand_after_hit_value + 7
            if players_hand_after_hit[-1] == 8:
                players_hand_after_hit_value = players_hand_after_hit_value + 8
            if players_hand_after_hit[-1] == 9:
                players_hand_after_hit_value = players_hand_after_hit_value + 9
            if players_hand_after_hit[-1] == 10:
                players_hand_after_hit_value = players_hand_after_hit_value + 10
            if players_hand_after_hit[-1] == 'Ace':
                players_hand_after_hit_value = players_hand_after_hit_value + 11
            if players_hand_after_hit[-1] == 'J':
                players_hand_after_hit_value = players_hand_after_hit_value + 10
            if players_hand_after_hit[-1] == 'Q':
                players_hand_after_hit_value = players_hand_after_hit_value + 10
            if players_hand_after_hit[-1] == 'K':
                players_hand_after_hit_value = players_hand_after_hit_value + 10
            if players_hand_after_hit_value > 21 and 'Ace' in players_hand_after_hit:
                players_hand_after_hit_value = players_hand_after_hit_value - 10
        else:
            continue





    dealers_hand_after_hit = dealers_hand[:]
    dealers_hand_after_hit_value = 0

    for each in range(len(dealers_hand_after_hit)):
        if dealers_hand_after_hit[each] == 2:
            dealers_hand_after_hit_value = dealers_hand_after_hit_value + 2
        if dealers_hand_after_hit[each] == 3:
            dealers_hand_after_hit_value = dealers_hand_after_hit_value + 3
        if dealers_hand_after_hit[each] == 4:
            dealers_hand_after_hit_value = dealers_hand_after_hit_value + 4
        if dealers_hand_after_hit[each] == 5:
            dealers_hand_after_hit_value = dealers_hand_after_hit_value + 5
        if dealers_hand_after_hit[each] == 6:
            dealers_hand_after_hit_value = dealers_hand_after_hit_value + 6
        if dealers_hand_after_hit[each] == 7:
            dealers_hand_after_hit_value = dealers_hand_after_hit_value + 7
        if dealers_hand_after_hit[each] == 8:
            dealers_hand_after_hit_value = dealers_hand_after_hit_value + 8
        if dealers_hand_after_hit[each] == 9:
            dealers_hand_after_hit_value = dealers_hand_after_hit_value + 9
        if dealers_hand_after_hit[each] == 10:
            dealers_hand_after_hit_value = dealers_hand_after_hit_value + 10
        if dealers_hand_after_hit[each] == 'Ace':
            dealers_hand_after_hit_value = dealers_hand_after_hit_value + 11
        if dealers_hand_after_hit[each] == 'J':
            dealers_hand_after_hit_value = dealers_hand_after_hit_value + 10
        if dealers_hand_after_hit[each] == 'Q':
            dealers_hand_after_hit_value = dealers_hand_after_hit_value + 10
        if dealers_hand_after_hit[each] == 'K':
            dealers_hand_after_hit_value = dealers_hand_after_hit_value + 10

    if dealers_hand_after_hit_value == 22:
        dealers_hand_after_hit_value = 12

    dealers_hit = []

    for each in range(10):
        if players_hand_after_hit_value > dealers_hand_after_hit_value and players_hand_after_hit_value < 22 and dealers_hand_after_hit_value < 22:
            dealers_hit = random.sample(cards_in_deck, 1)
            print("\nThis is dealers_hit:", dealers_hit)
            print("\nThis is dealers_hit[-1]:", dealers_hit[-1])
            cards_in_deck.remove(dealers_hit[-1])
            dealers_hand_after_hit.append(dealers_hit[-1])
            if dealers_hand_after_hit[-1] == 2:
                dealers_hand_after_hit_value = dealers_hand_after_hit_value + 2
            if dealers_hand_after_hit[-1] == 3:
                dealers_hand_after_hit_value = dealers_hand_after_hit_value + 3
            if dealers_hand_after_hit[-1] == 4:
                dealers_hand_after_hit_value = dealers_hand_after_hit_value + 4
            if dealers_hand_after_hit[-1] == 5:
                dealers_hand_after_hit_value = dealers_hand_after_hit_value + 5
            if dealers_hand_after_hit[-1] == 6:
                dealers_hand_after_hit_value = dealers_hand_after_hit_value + 6
            if dealers_hand_after_hit[-1] == 7:
                dealers_hand_after_hit_value = dealers_hand_after_hit_value + 7
            if dealers_hand_after_hit[-1] == 8:
                dealers_hand_after_hit_value = dealers_hand_after_hit_value + 8
            if dealers_hand_after_hit[-1] == 9:
                dealers_hand_after_hit_value = dealers_hand_after_hit_value + 9
            if dealers_hand_after_hit[-1] == 10:
                dealers_hand_after_hit_value = dealers_hand_after_hit_value + 10
            if dealers_hand_after_hit[-1] == 'Ace':
                dealers_hand_after_hit_value = dealers_hand_after_hit_value + 11
            if dealers_hand_after_hit[-1] == 'J':
                dealers_hand_after_hit_value = dealers_hand_after_hit_value + 10
            if dealers_hand_after_hit[-1] == 'Q':
                dealers_hand_after_hit_value = dealers_hand_after_hit_value + 10
            if dealers_hand_after_hit[-1] == 'K':
                dealers_hand_after_hit_value = dealers_hand_after_hit_value + 10
            if dealers_hand_after_hit_value > 21 and 'Ace' in dealers_hand_after_hit:
                dealers_hand_after_hit_value = dealers_hand_after_hit_value - 10
        else:
            continue







    print("\nThis is players_hand_after_hit:", players_hand_after_hit)

    print("\nThis is players_hand_after_hit_value", players_hand_after_hit_value)

    print("\nThis is players_hit:", players_hit)

    print("\nThese are cards_in_deck after hitting the player:", cards_in_deck)

    print("\n\nThis is dealers_hand_after_hit:", dealers_hand_after_hit)

    print("\nThis is dealers_hand_after_hit_value", dealers_hand_after_hit_value)

    print("\nThis is dealers_hit:", dealers_hit)

    print("\nThese are cards_in_deck after hitting the dealer:", cards_in_deck)

    if players_hand_value == 21:
        BlackjackTotal = BlackjackTotal + 1
    elif players_hand_after_hit_value > 21:
        LossTotal = LossTotal + 1
    elif (players_hand_after_hit_value < 22 and players_hand_after_hit_value > dealers_hand_after_hit_value) or (
            dealers_hand_after_hit_value > 21):
        WinTotal = WinTotal + 1
    elif (dealers_hand_after_hit_value > players_hand_after_hit_value and dealers_hand_after_hit_value < 22) or (
            players_hand_after_hit_value > 21):
        LossTotal = LossTotal + 1
    elif (players_hand_after_hit_value == dealers_hand_after_hit_value) and (dealers_hand_after_hit_value < 22) and (
            players_hand_after_hit_value < 22):
        PushTotal = PushTotal + 1





    d = {'Players Initital Hand:': players_hand_value, 'Dealers Hand:': dealers_hand_value, "Players Hit:": players_hit, "Players Final Hand:": players_hand_after_hit_value, "Dealers Final Hand:": dealers_hand_after_hit_value,  "Blackjack Total:": BlackjackTotal, "Win Total:": WinTotal, "Loss Total:": LossTotal, "Push Total:": PushTotal}
    data.append(d)

hey1 = pd.DataFrame(data)

hey1.to_excel("HitUntil15.xlsx")