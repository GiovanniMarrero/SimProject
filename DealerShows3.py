import random
#pip install pandas
import pandas as pd

players_hand_value = 0
dealers_hand_value = 0

data14 = []
data15 = []
data16 = []
data17 = []

BlackjackTotal14 = 0
BlackjackTotal15 = 0
BlackjackTotal16 = 0
BlackjackTotal17 = 0

WinTotal14 = 0
WinTotal15 = 0
WinTotal16 = 0
WinTotal17 = 0

LossTotal14 = 0
LossTotal15 = 0
LossTotal16 = 0
LossTotal17 = 0

PushTotal14 = 0
PushTotal15 = 0
PushTotal16 = 0
PushTotal17 = 0

for each in range(100000):
    cards_in_deck14 = ['Ace', 2, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                     'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                     'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                     'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                     'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                     'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                     'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                     'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

    players_hand_value14 = 0
    dealers_hand_value14 = 3

    print("\n\n\nThese are cards_in_deck before any dealing:", cards_in_deck14)

    players_hand14 = random.sample(cards_in_deck14, 2)

    print("\nThis is players_hand:", players_hand14)

    for each in players_hand14:
        cards_in_deck14.remove(each)

    print("\nThese are cards_in_deck after dealing to player:", cards_in_deck14)

    dealers_hand14 = random.sample(cards_in_deck14, 1)

    print("\nThis is dealers_hand:", dealers_hand14)

    for each in dealers_hand14:
        cards_in_deck14.remove(each)

    print("\nThese are cards_in_deck after dealing to dealer:", cards_in_deck14)

    # Need to figure out how to make the values from face cards / ace change

    for each in range(len(players_hand14)):
        if players_hand14[each] == 2:
            players_hand_value14 = players_hand_value14 + 2
        if players_hand14[each] == 3:
            players_hand_value14 = players_hand_value14 + 3
        if players_hand14[each] == 4:
            players_hand_value14 = players_hand_value14 + 4
        if players_hand14[each] == 5:
            players_hand_value14 = players_hand_value14 + 5
        if players_hand14[each] == 6:
            players_hand_value14 = players_hand_value14 + 6
        if players_hand14[each] == 7:
            players_hand_value14 = players_hand_value14 + 7
        if players_hand14[each] == 8:
            players_hand_value14 = players_hand_value14 + 8
        if players_hand14[each] == 9:
            players_hand_value14 = players_hand_value14 + 9
        if players_hand14[each] == 10:
            players_hand_value14 = players_hand_value14 + 10
        if players_hand14[each] == 'Ace':
            players_hand_value14 = players_hand_value14 + 11
        if players_hand14[each] == 'J':
            players_hand_value14 = players_hand_value14 + 10
        if players_hand14[each] == 'Q':
            players_hand_value14 = players_hand_value14 + 10
        if players_hand14[each] == 'K':
            players_hand_value14 = players_hand_value14 + 10

    if players_hand_value14 == 22:
        players_hand_value14 = 12

    print("\nThis is players_hand_value after dealing:", players_hand_value14)

    for each in range(len(dealers_hand14)):
        if dealers_hand14[each] == 2:
            dealers_hand_value14 = dealers_hand_value14 + 2
        if dealers_hand14[each] == 3:
            dealers_hand_value14 = dealers_hand_value14 + 3
        if dealers_hand14[each] == 4:
            dealers_hand_value14 = dealers_hand_value14 + 4
        if dealers_hand14[each] == 5:
            dealers_hand_value14 = dealers_hand_value14 + 5
        if dealers_hand14[each] == 6:
            dealers_hand_value14 = dealers_hand_value14 + 6
        if dealers_hand14[each] == 7:
            dealers_hand_value14 = dealers_hand_value14 + 7
        if dealers_hand14[each] == 8:
            dealers_hand_value14 = dealers_hand_value14 + 8
        if dealers_hand14[each] == 9:
            dealers_hand_value14 = dealers_hand_value14 + 9
        if dealers_hand14[each] == 10:
            dealers_hand_value14 = dealers_hand_value14 + 10
        if dealers_hand14[each] == 'Ace':
            dealers_hand_value14 = dealers_hand_value14 + 11
        if dealers_hand14[each] == 'J':
            dealers_hand_value14 = dealers_hand_value14 + 10
        if dealers_hand14[each] == 'Q':
            dealers_hand_value14 = dealers_hand_value14 + 10
        if dealers_hand14[each] == 'K':
            dealers_hand_value14 = dealers_hand_value14 + 10

    if dealers_hand_value14 == 22:
        dealers_hand_value14 = 12

    print("\nThis is dealers_hand_value after dealing:", dealers_hand_value14)

    players_hand_after_hit14 = players_hand14[:]
    players_hand_after_hit_value14 = 0

    for each in range(len(players_hand_after_hit14)):         #This is to set another variable to the initial hand, we actually add the hits next step!
        if players_hand_after_hit14[each] == 2:
            players_hand_after_hit_value14 = players_hand_after_hit_value14 + 2
        if players_hand_after_hit14[each] == 3:
            players_hand_after_hit_value14 = players_hand_after_hit_value14 + 3
        if players_hand_after_hit14[each] == 4:
            players_hand_after_hit_value14 = players_hand_after_hit_value14 + 4
        if players_hand_after_hit14[each] == 5:
            players_hand_after_hit_value14 = players_hand_after_hit_value14 + 5
        if players_hand_after_hit14[each] == 6:
            players_hand_after_hit_value14 = players_hand_after_hit_value14 + 6
        if players_hand_after_hit14[each] == 7:
            players_hand_after_hit_value14 = players_hand_after_hit_value14 + 7
        if players_hand_after_hit14[each] == 8:
            players_hand_after_hit_value14 = players_hand_after_hit_value14 + 8
        if players_hand_after_hit14[each] == 9:
            players_hand_after_hit_value14 = players_hand_after_hit_value14 + 9
        if players_hand_after_hit14[each] == 10:
            players_hand_after_hit_value14 = players_hand_after_hit_value14 + 10
        if players_hand_after_hit14[each] == 'Ace':
            players_hand_after_hit_value14 = players_hand_after_hit_value14 + 11
        if players_hand_after_hit14[each] == 'J':
            players_hand_after_hit_value14 = players_hand_after_hit_value14 + 10
        if players_hand_after_hit14[each] == 'Q':
            players_hand_after_hit_value14 = players_hand_after_hit_value14 + 10
        if players_hand_after_hit14[each] == 'K':
            players_hand_after_hit_value14 = players_hand_after_hit_value14 + 10

    if players_hand_after_hit_value14 == 22:
        players_hand_after_hit_value14 = 12

    players_hit14 = []

    for each in range(10):                                              #for 10 iterations
        if players_hand_after_hit_value14 < 14:                           #only if current hand value is <19
            players_hit14 = random.sample(cards_in_deck14, 1)               #players_hit is a random sampling of 1 card that remains in the deck
            print("\nThis is players_hit:", players_hit14)
            print("\nThis is players_hit[-1]:", players_hit14[-1])
            cards_in_deck14.remove(players_hit14[-1])                       #remove the last item (aka most recent) in players_hit
            players_hand_after_hit14.append(players_hit14[-1])              #add the latest item to our hand
            if players_hand_after_hit14[-1] == 2:
                players_hand_after_hit_value14 = players_hand_after_hit_value14 + 2
            if players_hand_after_hit14[-1] == 3:
                players_hand_after_hit_value14 = players_hand_after_hit_value14 + 3
            if players_hand_after_hit14[-1] == 4:
                players_hand_after_hit_value14 = players_hand_after_hit_value14 + 4
            if players_hand_after_hit14[-1] == 5:
                players_hand_after_hit_value14 = players_hand_after_hit_value14 + 5
            if players_hand_after_hit14[-1] == 6:
                players_hand_after_hit_value14 = players_hand_after_hit_value14 + 6
            if players_hand_after_hit14[-1] == 7:
                players_hand_after_hit_value14 = players_hand_after_hit_value14 + 7
            if players_hand_after_hit14[-1] == 8:
                players_hand_after_hit_value14 = players_hand_after_hit_value14 + 8
            if players_hand_after_hit14[-1] == 9:
                players_hand_after_hit_value14 = players_hand_after_hit_value14 + 9
            if players_hand_after_hit14[-1] == 10:
                players_hand_after_hit_value14 = players_hand_after_hit_value14 + 10
            if players_hand_after_hit14[-1] == 'Ace':
                players_hand_after_hit_value14 = players_hand_after_hit_value14 + 11
            if players_hand_after_hit14[-1] == 'J':
                players_hand_after_hit_value14 = players_hand_after_hit_value14 + 10
            if players_hand_after_hit14[-1] == 'Q':
                players_hand_after_hit_value14 = players_hand_after_hit_value14 + 10
            if players_hand_after_hit14[-1] == 'K':
                players_hand_after_hit_value14 = players_hand_after_hit_value14 + 10
            if players_hand_after_hit_value14 > 21 and 'Ace' in players_hand_after_hit14:
                players_hand_after_hit_value14 = players_hand_after_hit_value14 - 10
        else:
            continue

    dealers_hand_after_hit14 = dealers_hand14[:]
    dealers_hand_after_hit_value14 = 3

    for each in range(len(dealers_hand_after_hit14)):
        if dealers_hand_after_hit14[each] == 2:
            dealers_hand_after_hit_value14 = dealers_hand_after_hit_value14 + 2
        if dealers_hand_after_hit14[each] == 3:
            dealers_hand_after_hit_value14 = dealers_hand_after_hit_value14 + 3
        if dealers_hand_after_hit14[each] == 4:
            dealers_hand_after_hit_value14 = dealers_hand_after_hit_value14 + 4
        if dealers_hand_after_hit14[each] == 5:
            dealers_hand_after_hit_value14 = dealers_hand_after_hit_value14 + 5
        if dealers_hand_after_hit14[each] == 6:
            dealers_hand_after_hit_value14 = dealers_hand_after_hit_value14 + 6
        if dealers_hand_after_hit14[each] == 7:
            dealers_hand_after_hit_value14 = dealers_hand_after_hit_value14 + 7
        if dealers_hand_after_hit14[each] == 8:
            dealers_hand_after_hit_value14 = dealers_hand_after_hit_value14 + 8
        if dealers_hand_after_hit14[each] == 9:
            dealers_hand_after_hit_value14 = dealers_hand_after_hit_value14 + 9
        if dealers_hand_after_hit14[each] == 10:
            dealers_hand_after_hit_value14 = dealers_hand_after_hit_value14 + 10
        if dealers_hand_after_hit14[each] == 'Ace':
            dealers_hand_after_hit_value14 = dealers_hand_after_hit_value14 + 11
        if dealers_hand_after_hit14[each] == 'J':
            dealers_hand_after_hit_value14 = dealers_hand_after_hit_value14 + 10
        if dealers_hand_after_hit14[each] == 'Q':
            dealers_hand_after_hit_value14 = dealers_hand_after_hit_value14 + 10
        if dealers_hand_after_hit14[each] == 'K':
            dealers_hand_after_hit_value14 = dealers_hand_after_hit_value14 + 10

    if dealers_hand_after_hit_value14 == 22:
        dealers_hand_after_hit_value14 = 12

    dealers_hit14 = []

    for each in range(10):
        if players_hand_after_hit_value14 > dealers_hand_after_hit_value14 and players_hand_after_hit_value14 < 22 and dealers_hand_after_hit_value14 < 22:
            dealers_hit14 = random.sample(cards_in_deck14, 1)
            print("\nThis is dealers_hit:", dealers_hit14)
            print("\nThis is dealers_hit[-1]:", dealers_hit14[-1])
            cards_in_deck14.remove(dealers_hit14[-1])
            dealers_hand_after_hit14.append(dealers_hit14[-1])
            if dealers_hand_after_hit14[-1] == 2:
                dealers_hand_after_hit_value14 = dealers_hand_after_hit_value14 + 2
            if dealers_hand_after_hit14[-1] == 3:
                dealers_hand_after_hit_value14 = dealers_hand_after_hit_value14 + 3
            if dealers_hand_after_hit14[-1] == 4:
                dealers_hand_after_hit_value14 = dealers_hand_after_hit_value14 + 4
            if dealers_hand_after_hit14[-1] == 5:
                dealers_hand_after_hit_value14 = dealers_hand_after_hit_value14 + 5
            if dealers_hand_after_hit14[-1] == 6:
                dealers_hand_after_hit_value14 = dealers_hand_after_hit_value14 + 6
            if dealers_hand_after_hit14[-1] == 7:
                dealers_hand_after_hit_value14 = dealers_hand_after_hit_value14 + 7
            if dealers_hand_after_hit14[-1] == 8:
                dealers_hand_after_hit_value14 = dealers_hand_after_hit_value14 + 8
            if dealers_hand_after_hit14[-1] == 9:
                dealers_hand_after_hit_value14 = dealers_hand_after_hit_value14 + 9
            if dealers_hand_after_hit14[-1] == 10:
                dealers_hand_after_hit_value14 = dealers_hand_after_hit_value14 + 10
            if dealers_hand_after_hit14[-1] == 'Ace':
                dealers_hand_after_hit_value14 = dealers_hand_after_hit_value14 + 11
            if dealers_hand_after_hit14[-1] == 'J':
                dealers_hand_after_hit_value14 = dealers_hand_after_hit_value14 + 10
            if dealers_hand_after_hit14[-1] == 'Q':
                dealers_hand_after_hit_value14 = dealers_hand_after_hit_value14 + 10
            if dealers_hand_after_hit14[-1] == 'K':
                dealers_hand_after_hit_value14 = dealers_hand_after_hit_value14 + 10
            if dealers_hand_after_hit_value14 > 21 and 'Ace' in dealers_hand_after_hit14:
                dealers_hand_after_hit_value14 = dealers_hand_after_hit_value14 - 10
        else:
            continue

    if players_hand_value14 == 21:
        BlackjackTotal14 = BlackjackTotal14 + 1
    elif players_hand_after_hit_value14 > 21:
        LossTotal14 = LossTotal14 + 1
    elif (players_hand_after_hit_value14 < 22 and players_hand_after_hit_value14 > dealers_hand_after_hit_value14) or (
            dealers_hand_after_hit_value14 > 21):
        WinTotal14 = WinTotal14 + 1
    elif (dealers_hand_after_hit_value14 > players_hand_after_hit_value14 and dealers_hand_after_hit_value14 < 22) or (
            players_hand_after_hit_value14 > 21):
        LossTotal14 = LossTotal14 + 1
    elif (players_hand_after_hit_value14 == dealers_hand_after_hit_value14) and (dealers_hand_after_hit_value14 < 22) and (
            players_hand_after_hit_value14 < 22):
        PushTotal14 = PushTotal14 + 1

    d14 = {'Players Initital Hand:': players_hand_value14, 'Dealers Hand:': dealers_hand_value14, "Players Hit:": players_hit14, "Players Final Hand:": players_hand_after_hit_value14, "Dealers Final Hand:": dealers_hand_after_hit_value14,  "Blackjack Total:": BlackjackTotal14, "Win Total:": WinTotal14, "Loss Total:": LossTotal14, "Push Total:": PushTotal14}
    data14.append(d14)

hey14 = pd.DataFrame(data14)

hey14.to_excel("Dealer3HU14.xlsx")

#START OF HU 15 START OF HU 15 START OF HU 15 START OF HU 15 START OF HU 15 START OF HU 15 START OF HU 15 START OF HU 15 START OF HU 15 v START OF HU 15 START OF HU 15 START OF HU 15

for each in range(100000):
    cards_in_deck15 = ['Ace', 2, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                     'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                     'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                     'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                     'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                     'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                     'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                     'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

    players_hand_value15 = 0
    dealers_hand_value15 = 3

    print("\n\n\nThese are cards_in_deck before any dealing:", cards_in_deck15)

    players_hand15 = random.sample(cards_in_deck15, 2)

    print("\nThis is players_hand:", players_hand15)

    for each in players_hand15:
        cards_in_deck15.remove(each)

    print("\nThese are cards_in_deck after dealing to player:", cards_in_deck15)

    dealers_hand15 = random.sample(cards_in_deck15, 1)

    print("\nThis is dealers_hand:", dealers_hand15)

    for each in dealers_hand15:
        cards_in_deck15.remove(each)

    print("\nThese are cards_in_deck after dealing to dealer:", cards_in_deck15)

    # Need to figure out how to make the values from face cards / ace change

    for each in range(len(players_hand15)):
        if players_hand15[each] == 2:
            players_hand_value15 = players_hand_value15 + 2
        if players_hand15[each] == 3:
            players_hand_value15 = players_hand_value15 + 3
        if players_hand15[each] == 4:
            players_hand_value15 = players_hand_value15 + 4
        if players_hand15[each] == 5:
            players_hand_value15 = players_hand_value15 + 5
        if players_hand15[each] == 6:
            players_hand_value15 = players_hand_value15 + 6
        if players_hand15[each] == 7:
            players_hand_value15 = players_hand_value15 + 7
        if players_hand15[each] == 8:
            players_hand_value15 = players_hand_value15 + 8
        if players_hand15[each] == 9:
            players_hand_value15 = players_hand_value15 + 9
        if players_hand15[each] == 10:
            players_hand_value15 = players_hand_value15 + 10
        if players_hand15[each] == 'Ace':
            players_hand_value15 = players_hand_value15 + 11
        if players_hand15[each] == 'J':
            players_hand_value15 = players_hand_value15 + 10
        if players_hand15[each] == 'Q':
            players_hand_value15 = players_hand_value15 + 10
        if players_hand15[each] == 'K':
            players_hand_value15 = players_hand_value15 + 10

    if players_hand_value15 == 22:
        players_hand_value15 = 12

    print("\nThis is players_hand_value after dealing:", players_hand_value15)

    for each in range(len(dealers_hand15)):
        if dealers_hand15[each] == 2:
            dealers_hand_value15 = dealers_hand_value15 + 2
        if dealers_hand15[each] == 3:
            dealers_hand_value15 = dealers_hand_value15 + 3
        if dealers_hand15[each] == 4:
            dealers_hand_value15 = dealers_hand_value15 + 4
        if dealers_hand15[each] == 5:
            dealers_hand_value15 = dealers_hand_value15 + 5
        if dealers_hand15[each] == 6:
            dealers_hand_value15 = dealers_hand_value15 + 6
        if dealers_hand15[each] == 7:
            dealers_hand_value15 = dealers_hand_value15 + 7
        if dealers_hand15[each] == 8:
            dealers_hand_value15 = dealers_hand_value15 + 8
        if dealers_hand15[each] == 9:
            dealers_hand_value15 = dealers_hand_value15 + 9
        if dealers_hand15[each] == 10:
            dealers_hand_value15 = dealers_hand_value15 + 10
        if dealers_hand15[each] == 'Ace':
            dealers_hand_value15 = dealers_hand_value15 + 11
        if dealers_hand15[each] == 'J':
            dealers_hand_value15 = dealers_hand_value15 + 10
        if dealers_hand15[each] == 'Q':
            dealers_hand_value15 = dealers_hand_value15 + 10
        if dealers_hand15[each] == 'K':
            dealers_hand_value15 = dealers_hand_value15 + 10

    if dealers_hand_value15 == 22:
        dealers_hand_value15 = 12

    print("\nThis is dealers_hand_value after dealing:", dealers_hand_value15)

    players_hand_after_hit15 = players_hand15[:]
    players_hand_after_hit_value15 = 0

    for each in range(len(players_hand_after_hit15)):         #This is to set another variable to the initial hand, we actually add the hits next step!
        if players_hand_after_hit15[each] == 2:
            players_hand_after_hit_value15 = players_hand_after_hit_value15 + 2
        if players_hand_after_hit15[each] == 3:
            players_hand_after_hit_value15 = players_hand_after_hit_value15 + 3
        if players_hand_after_hit15[each] == 4:
            players_hand_after_hit_value15 = players_hand_after_hit_value15 + 4
        if players_hand_after_hit15[each] == 5:
            players_hand_after_hit_value15 = players_hand_after_hit_value15 + 5
        if players_hand_after_hit15[each] == 6:
            players_hand_after_hit_value15 = players_hand_after_hit_value15 + 6
        if players_hand_after_hit15[each] == 7:
            players_hand_after_hit_value15 = players_hand_after_hit_value15 + 7
        if players_hand_after_hit15[each] == 8:
            players_hand_after_hit_value15 = players_hand_after_hit_value15 + 8
        if players_hand_after_hit15[each] == 9:
            players_hand_after_hit_value15 = players_hand_after_hit_value15 + 9
        if players_hand_after_hit15[each] == 10:
            players_hand_after_hit_value15 = players_hand_after_hit_value15 + 10
        if players_hand_after_hit15[each] == 'Ace':
            players_hand_after_hit_value15 = players_hand_after_hit_value15 + 11
        if players_hand_after_hit15[each] == 'J':
            players_hand_after_hit_value15 = players_hand_after_hit_value15 + 10
        if players_hand_after_hit15[each] == 'Q':
            players_hand_after_hit_value15 = players_hand_after_hit_value15 + 10
        if players_hand_after_hit15[each] == 'K':
            players_hand_after_hit_value15 = players_hand_after_hit_value15 + 10

    if players_hand_after_hit_value15 == 22:
        players_hand_after_hit_value15 = 12

    players_hit15 = []

    for each in range(10):                                              #for 10 iterations
        if players_hand_after_hit_value15 < 15:                           #only if current hand value is <19
            players_hit15 = random.sample(cards_in_deck15, 1)               #players_hit is a random sampling of 1 card that remains in the deck
            print("\nThis is players_hit:", players_hit15)
            print("\nThis is players_hit[-1]:", players_hit15[-1])
            cards_in_deck15.remove(players_hit15[-1])                       #remove the last item (aka most recent) in players_hit
            players_hand_after_hit15.append(players_hit15[-1])              #add the latest item to our hand
            if players_hand_after_hit15[-1] == 2:
                players_hand_after_hit_value15 = players_hand_after_hit_value15 + 2
            if players_hand_after_hit15[-1] == 3:
                players_hand_after_hit_value15 = players_hand_after_hit_value15 + 3
            if players_hand_after_hit15[-1] == 4:
                players_hand_after_hit_value15 = players_hand_after_hit_value15 + 4
            if players_hand_after_hit15[-1] == 5:
                players_hand_after_hit_value15 = players_hand_after_hit_value15 + 5
            if players_hand_after_hit15[-1] == 6:
                players_hand_after_hit_value15 = players_hand_after_hit_value15 + 6
            if players_hand_after_hit15[-1] == 7:
                players_hand_after_hit_value15 = players_hand_after_hit_value15 + 7
            if players_hand_after_hit15[-1] == 8:
                players_hand_after_hit_value15 = players_hand_after_hit_value15 + 8
            if players_hand_after_hit15[-1] == 9:
                players_hand_after_hit_value15 = players_hand_after_hit_value15 + 9
            if players_hand_after_hit15[-1] == 10:
                players_hand_after_hit_value15 = players_hand_after_hit_value15 + 10
            if players_hand_after_hit15[-1] == 'Ace':
                players_hand_after_hit_value15 = players_hand_after_hit_value15 + 11
            if players_hand_after_hit15[-1] == 'J':
                players_hand_after_hit_value15 = players_hand_after_hit_value15 + 10
            if players_hand_after_hit15[-1] == 'Q':
                players_hand_after_hit_value15 = players_hand_after_hit_value15 + 10
            if players_hand_after_hit15[-1] == 'K':
                players_hand_after_hit_value15 = players_hand_after_hit_value15 + 10
            if players_hand_after_hit_value15 > 21 and 'Ace' in players_hand_after_hit15:
                players_hand_after_hit_value15 = players_hand_after_hit_value15 - 10
        else:
            continue


    dealers_hand_after_hit15 = dealers_hand15[:]
    dealers_hand_after_hit_value15 = 3

    for each in range(len(dealers_hand_after_hit15)):
        if dealers_hand_after_hit15[each] == 2:
            dealers_hand_after_hit_value15 = dealers_hand_after_hit_value15 + 2
        if dealers_hand_after_hit15[each] == 3:
            dealers_hand_after_hit_value15 = dealers_hand_after_hit_value15 + 3
        if dealers_hand_after_hit15[each] == 4:
            dealers_hand_after_hit_value15 = dealers_hand_after_hit_value15 + 4
        if dealers_hand_after_hit15[each] == 5:
            dealers_hand_after_hit_value15 = dealers_hand_after_hit_value15 + 5
        if dealers_hand_after_hit15[each] == 6:
            dealers_hand_after_hit_value15 = dealers_hand_after_hit_value15 + 6
        if dealers_hand_after_hit15[each] == 7:
            dealers_hand_after_hit_value15 = dealers_hand_after_hit_value15 + 7
        if dealers_hand_after_hit15[each] == 8:
            dealers_hand_after_hit_value15 = dealers_hand_after_hit_value15 + 8
        if dealers_hand_after_hit15[each] == 9:
            dealers_hand_after_hit_value15 = dealers_hand_after_hit_value15 + 9
        if dealers_hand_after_hit15[each] == 10:
            dealers_hand_after_hit_value15 = dealers_hand_after_hit_value15 + 10
        if dealers_hand_after_hit15[each] == 'Ace':
            dealers_hand_after_hit_value15 = dealers_hand_after_hit_value15 + 11
        if dealers_hand_after_hit15[each] == 'J':
            dealers_hand_after_hit_value15 = dealers_hand_after_hit_value15 + 10
        if dealers_hand_after_hit15[each] == 'Q':
            dealers_hand_after_hit_value15 = dealers_hand_after_hit_value15 + 10
        if dealers_hand_after_hit15[each] == 'K':
            dealers_hand_after_hit_value15 = dealers_hand_after_hit_value15 + 10

    if dealers_hand_after_hit_value15 == 22:
        dealers_hand_after_hit_value15 = 12

    dealers_hit15 = []

    for each in range(10):
        if players_hand_after_hit_value15 > dealers_hand_after_hit_value15 and players_hand_after_hit_value15 < 22 and dealers_hand_after_hit_value15 < 22:
            dealers_hit15 = random.sample(cards_in_deck15, 1)
            print("\nThis is dealers_hit:", dealers_hit15)
            print("\nThis is dealers_hit[-1]:", dealers_hit15[-1])
            cards_in_deck15.remove(dealers_hit15[-1])
            dealers_hand_after_hit15.append(dealers_hit15[-1])
            if dealers_hand_after_hit15[-1] == 2:
                dealers_hand_after_hit_value15 = dealers_hand_after_hit_value15 + 2
            if dealers_hand_after_hit15[-1] == 3:
                dealers_hand_after_hit_value15 = dealers_hand_after_hit_value15 + 3
            if dealers_hand_after_hit15[-1] == 4:
                dealers_hand_after_hit_value15 = dealers_hand_after_hit_value15 + 4
            if dealers_hand_after_hit15[-1] == 5:
                dealers_hand_after_hit_value15 = dealers_hand_after_hit_value15 + 5
            if dealers_hand_after_hit15[-1] == 6:
                dealers_hand_after_hit_value15 = dealers_hand_after_hit_value15 + 6
            if dealers_hand_after_hit15[-1] == 7:
                dealers_hand_after_hit_value15 = dealers_hand_after_hit_value15 + 7
            if dealers_hand_after_hit15[-1] == 8:
                dealers_hand_after_hit_value15 = dealers_hand_after_hit_value15 + 8
            if dealers_hand_after_hit15[-1] == 9:
                dealers_hand_after_hit_value15 = dealers_hand_after_hit_value15 + 9
            if dealers_hand_after_hit15[-1] == 10:
                dealers_hand_after_hit_value15 = dealers_hand_after_hit_value15 + 10
            if dealers_hand_after_hit15[-1] == 'Ace':
                dealers_hand_after_hit_value15 = dealers_hand_after_hit_value15 + 11
            if dealers_hand_after_hit15[-1] == 'J':
                dealers_hand_after_hit_value15 = dealers_hand_after_hit_value15 + 10
            if dealers_hand_after_hit15[-1] == 'Q':
                dealers_hand_after_hit_value15 = dealers_hand_after_hit_value15 + 10
            if dealers_hand_after_hit15[-1] == 'K':
                dealers_hand_after_hit_value15 = dealers_hand_after_hit_value15 + 10
            if dealers_hand_after_hit_value15 > 21 and 'Ace' in dealers_hand_after_hit15:
                dealers_hand_after_hit_value15 = dealers_hand_after_hit_value15 - 10
        else:
            continue

    if players_hand_value15 == 21:
        BlackjackTotal15 = BlackjackTotal15 + 1
    elif players_hand_after_hit_value15 > 21:
        LossTotal15 = LossTotal15 + 1
    elif (players_hand_after_hit_value15 < 22 and players_hand_after_hit_value15 > dealers_hand_after_hit_value15) or (
            dealers_hand_after_hit_value15 > 21):
        WinTotal15 = WinTotal15 + 1
    elif (dealers_hand_after_hit_value15 > players_hand_after_hit_value15 and dealers_hand_after_hit_value15 < 22) or (
            players_hand_after_hit_value15 > 21):
        LossTotal15 = LossTotal15 + 1
    elif (players_hand_after_hit_value15 == dealers_hand_after_hit_value15) and (dealers_hand_after_hit_value15 < 22) and (
            players_hand_after_hit_value15 < 22):
        PushTotal15 = PushTotal15 + 1

    d15 = {'Players Initital Hand:': players_hand_value15, 'Dealers Hand:': dealers_hand_value15, "Players Hit:": players_hit15, "Players Final Hand:": players_hand_after_hit_value15, "Dealers Final Hand:": dealers_hand_after_hit_value15,  "Blackjack Total:": BlackjackTotal15, "Win Total:": WinTotal15, "Loss Total:": LossTotal15, "Push Total:": PushTotal15}
    data15.append(d15)

hey15 = pd.DataFrame(data15)

hey15.to_excel("Dealer3HU15.xlsx")

# START OF 16 START OF 16 #START OF 16 START OF 16  START OF 16  START OF 16

for each in range(100000):
    cards_in_deck16 = ['Ace', 2, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                     'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                     'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                     'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                     'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                     'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                     'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                     'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

    players_hand_value16 = 0
    dealers_hand_value16 = 3

    print("\n\n\nThese are cards_in_deck before any dealing:", cards_in_deck16)

    players_hand16 = random.sample(cards_in_deck16, 2)

    print("\nThis is players_hand:", players_hand16)

    for each in players_hand16:
        cards_in_deck16.remove(each)

    print("\nThese are cards_in_deck after dealing to player:", cards_in_deck16)

    dealers_hand16 = random.sample(cards_in_deck16, 1)

    print("\nThis is dealers_hand:", dealers_hand16)

    for each in dealers_hand16:
        cards_in_deck16.remove(each)

    print("\nThese are cards_in_deck after dealing to dealer:", cards_in_deck16)

    # Need to figure out how to make the values from face cards / ace change

    for each in range(len(players_hand16)):
        if players_hand16[each] == 2:
            players_hand_value16 = players_hand_value16 + 2
        if players_hand16[each] == 3:
            players_hand_value16 = players_hand_value16 + 3
        if players_hand16[each] == 4:
            players_hand_value16 = players_hand_value16 + 4
        if players_hand16[each] == 5:
            players_hand_value16 = players_hand_value16 + 5
        if players_hand16[each] == 6:
            players_hand_value16 = players_hand_value16 + 6
        if players_hand16[each] == 7:
            players_hand_value16 = players_hand_value16 + 7
        if players_hand16[each] == 8:
            players_hand_value16 = players_hand_value16 + 8
        if players_hand16[each] == 9:
            players_hand_value16 = players_hand_value16 + 9
        if players_hand16[each] == 10:
            players_hand_value16 = players_hand_value16 + 10
        if players_hand16[each] == 'Ace':
            players_hand_value16 = players_hand_value16 + 11
        if players_hand16[each] == 'J':
            players_hand_value16 = players_hand_value16 + 10
        if players_hand16[each] == 'Q':
            players_hand_value16 = players_hand_value16 + 10
        if players_hand16[each] == 'K':
            players_hand_value16 = players_hand_value16 + 10

    if players_hand_value16 == 22:
        players_hand_value16 = 12

    print("\nThis is players_hand_value after dealing:", players_hand_value16)

    for each in range(len(dealers_hand16)):
        if dealers_hand16[each] == 2:
            dealers_hand_value16 = dealers_hand_value16 + 2
        if dealers_hand16[each] == 3:
            dealers_hand_value16 = dealers_hand_value16 + 3
        if dealers_hand16[each] == 4:
            dealers_hand_value16 = dealers_hand_value16 + 4
        if dealers_hand16[each] == 5:
            dealers_hand_value16 = dealers_hand_value16 + 5
        if dealers_hand16[each] == 6:
            dealers_hand_value16 = dealers_hand_value16 + 6
        if dealers_hand16[each] == 7:
            dealers_hand_value16 = dealers_hand_value16 + 7
        if dealers_hand16[each] == 8:
            dealers_hand_value16 = dealers_hand_value16 + 8
        if dealers_hand16[each] == 9:
            dealers_hand_value16 = dealers_hand_value16 + 9
        if dealers_hand16[each] == 10:
            dealers_hand_value16 = dealers_hand_value16 + 10
        if dealers_hand16[each] == 'Ace':
            dealers_hand_value16 = dealers_hand_value16 + 11
        if dealers_hand16[each] == 'J':
            dealers_hand_value16 = dealers_hand_value16 + 10
        if dealers_hand16[each] == 'Q':
            dealers_hand_value16 = dealers_hand_value16 + 10
        if dealers_hand16[each] == 'K':
            dealers_hand_value16 = dealers_hand_value16 + 10

    if dealers_hand_value16 == 22:
        dealers_hand_value16 = 12

    print("\nThis is dealers_hand_value after dealing:", dealers_hand_value16)

    players_hand_after_hit16 = players_hand16[:]
    players_hand_after_hit_value16 = 0

    for each in range(len(players_hand_after_hit16)):         #This is to set another variable to the initial hand, we actually add the hits next step!
        if players_hand_after_hit16[each] == 2:
            players_hand_after_hit_value16 = players_hand_after_hit_value16 + 2
        if players_hand_after_hit16[each] == 3:
            players_hand_after_hit_value16 = players_hand_after_hit_value16 + 3
        if players_hand_after_hit16[each] == 4:
            players_hand_after_hit_value16 = players_hand_after_hit_value16 + 4
        if players_hand_after_hit16[each] == 5:
            players_hand_after_hit_value16 = players_hand_after_hit_value16 + 5
        if players_hand_after_hit16[each] == 6:
            players_hand_after_hit_value16 = players_hand_after_hit_value16 + 6
        if players_hand_after_hit16[each] == 7:
            players_hand_after_hit_value16 = players_hand_after_hit_value16 + 7
        if players_hand_after_hit16[each] == 8:
            players_hand_after_hit_value16 = players_hand_after_hit_value16 + 8
        if players_hand_after_hit16[each] == 9:
            players_hand_after_hit_value16 = players_hand_after_hit_value16 + 9
        if players_hand_after_hit16[each] == 10:
            players_hand_after_hit_value16 = players_hand_after_hit_value16 + 10
        if players_hand_after_hit16[each] == 'Ace':
            players_hand_after_hit_value16 = players_hand_after_hit_value16 + 11
        if players_hand_after_hit16[each] == 'J':
            players_hand_after_hit_value16 = players_hand_after_hit_value16 + 10
        if players_hand_after_hit16[each] == 'Q':
            players_hand_after_hit_value16 = players_hand_after_hit_value16 + 10
        if players_hand_after_hit16[each] == 'K':
            players_hand_after_hit_value16 = players_hand_after_hit_value16 + 10

    if players_hand_after_hit_value16 == 22:
        players_hand_after_hit_value16 = 12

    players_hit16 = []

    for each in range(10):                                              #for 10 iterations
        if players_hand_after_hit_value16 < 16:                           #only if current hand value is <19
            players_hit16 = random.sample(cards_in_deck16, 1)               #players_hit is a random sampling of 1 card that remains in the deck
            print("\nThis is players_hit:", players_hit16)
            print("\nThis is players_hit[-1]:", players_hit16[-1])
            cards_in_deck16.remove(players_hit16[-1])                       #remove the last item (aka most recent) in players_hit
            players_hand_after_hit16.append(players_hit16[-1])              #add the latest item to our hand
            if players_hand_after_hit16[-1] == 2:
                players_hand_after_hit_value16 = players_hand_after_hit_value16 + 2
            if players_hand_after_hit16[-1] == 3:
                players_hand_after_hit_value16 = players_hand_after_hit_value16 + 3
            if players_hand_after_hit16[-1] == 4:
                players_hand_after_hit_value16 = players_hand_after_hit_value16 + 4
            if players_hand_after_hit16[-1] == 5:
                players_hand_after_hit_value16 = players_hand_after_hit_value16 + 5
            if players_hand_after_hit16[-1] == 6:
                players_hand_after_hit_value16 = players_hand_after_hit_value16 + 6
            if players_hand_after_hit16[-1] == 7:
                players_hand_after_hit_value16 = players_hand_after_hit_value16 + 7
            if players_hand_after_hit16[-1] == 8:
                players_hand_after_hit_value16 = players_hand_after_hit_value16 + 8
            if players_hand_after_hit16[-1] == 9:
                players_hand_after_hit_value16 = players_hand_after_hit_value16 + 9
            if players_hand_after_hit16[-1] == 10:
                players_hand_after_hit_value16 = players_hand_after_hit_value16 + 10
            if players_hand_after_hit16[-1] == 'Ace':
                players_hand_after_hit_value16 = players_hand_after_hit_value16 + 11
            if players_hand_after_hit16[-1] == 'J':
                players_hand_after_hit_value16 = players_hand_after_hit_value16 + 10
            if players_hand_after_hit16[-1] == 'Q':
                players_hand_after_hit_value16 = players_hand_after_hit_value16 + 10
            if players_hand_after_hit16[-1] == 'K':
                players_hand_after_hit_value16 = players_hand_after_hit_value16 + 10
            if players_hand_after_hit_value16 > 21 and 'Ace' in players_hand_after_hit16:
                players_hand_after_hit_value16 = players_hand_after_hit_value16 - 10
        else:
            continue


    dealers_hand_after_hit16 = dealers_hand16[:]
    dealers_hand_after_hit_value16 = 3

    for each in range(len(dealers_hand_after_hit16)):
        if dealers_hand_after_hit16[each] == 2:
            dealers_hand_after_hit_value16 = dealers_hand_after_hit_value16 + 2
        if dealers_hand_after_hit16[each] == 3:
            dealers_hand_after_hit_value16 = dealers_hand_after_hit_value16 + 3
        if dealers_hand_after_hit16[each] == 4:
            dealers_hand_after_hit_value16 = dealers_hand_after_hit_value16 + 4
        if dealers_hand_after_hit16[each] == 5:
            dealers_hand_after_hit_value16 = dealers_hand_after_hit_value16 + 5
        if dealers_hand_after_hit16[each] == 6:
            dealers_hand_after_hit_value16 = dealers_hand_after_hit_value16 + 6
        if dealers_hand_after_hit16[each] == 7:
            dealers_hand_after_hit_value16 = dealers_hand_after_hit_value16 + 7
        if dealers_hand_after_hit16[each] == 8:
            dealers_hand_after_hit_value16 = dealers_hand_after_hit_value16 + 8
        if dealers_hand_after_hit16[each] == 9:
            dealers_hand_after_hit_value16 = dealers_hand_after_hit_value16 + 9
        if dealers_hand_after_hit16[each] == 10:
            dealers_hand_after_hit_value16 = dealers_hand_after_hit_value16 + 10
        if dealers_hand_after_hit16[each] == 'Ace':
            dealers_hand_after_hit_value16 = dealers_hand_after_hit_value16 + 11
        if dealers_hand_after_hit16[each] == 'J':
            dealers_hand_after_hit_value16 = dealers_hand_after_hit_value16 + 10
        if dealers_hand_after_hit16[each] == 'Q':
            dealers_hand_after_hit_value16 = dealers_hand_after_hit_value16 + 10
        if dealers_hand_after_hit16[each] == 'K':
            dealers_hand_after_hit_value16 = dealers_hand_after_hit_value16 + 10

    if dealers_hand_after_hit_value16 == 22:
        dealers_hand_after_hit_value16 = 12

    dealers_hit16 = []

    for each in range(10):
        if players_hand_after_hit_value16 > dealers_hand_after_hit_value16 and players_hand_after_hit_value16 < 22 and dealers_hand_after_hit_value16 < 22:
            dealers_hit16 = random.sample(cards_in_deck16, 1)
            print("\nThis is dealers_hit:", dealers_hit16)
            print("\nThis is dealers_hit[-1]:", dealers_hit16[-1])
            cards_in_deck16.remove(dealers_hit16[-1])
            dealers_hand_after_hit16.append(dealers_hit16[-1])
            if dealers_hand_after_hit16[-1] == 2:
                dealers_hand_after_hit_value16 = dealers_hand_after_hit_value16 + 2
            if dealers_hand_after_hit16[-1] == 3:
                dealers_hand_after_hit_value16 = dealers_hand_after_hit_value16 + 3
            if dealers_hand_after_hit16[-1] == 4:
                dealers_hand_after_hit_value16 = dealers_hand_after_hit_value16 + 4
            if dealers_hand_after_hit16[-1] == 5:
                dealers_hand_after_hit_value16 = dealers_hand_after_hit_value16 + 5
            if dealers_hand_after_hit16[-1] == 6:
                dealers_hand_after_hit_value16 = dealers_hand_after_hit_value16 + 6
            if dealers_hand_after_hit16[-1] == 7:
                dealers_hand_after_hit_value16 = dealers_hand_after_hit_value16 + 7
            if dealers_hand_after_hit16[-1] == 8:
                dealers_hand_after_hit_value16 = dealers_hand_after_hit_value16 + 8
            if dealers_hand_after_hit16[-1] == 9:
                dealers_hand_after_hit_value16 = dealers_hand_after_hit_value16 + 9
            if dealers_hand_after_hit16[-1] == 10:
                dealers_hand_after_hit_value16 = dealers_hand_after_hit_value16 + 10
            if dealers_hand_after_hit16[-1] == 'Ace':
                dealers_hand_after_hit_value16 = dealers_hand_after_hit_value16 + 11
            if dealers_hand_after_hit16[-1] == 'J':
                dealers_hand_after_hit_value16 = dealers_hand_after_hit_value16 + 10
            if dealers_hand_after_hit16[-1] == 'Q':
                dealers_hand_after_hit_value16 = dealers_hand_after_hit_value16 + 10
            if dealers_hand_after_hit16[-1] == 'K':
                dealers_hand_after_hit_value16 = dealers_hand_after_hit_value16 + 10
            if dealers_hand_after_hit_value16 > 21 and 'Ace' in dealers_hand_after_hit16:
                dealers_hand_after_hit_value16 = dealers_hand_after_hit_value16 - 10
        else:
            continue

    if players_hand_value16 == 21:
        BlackjackTotal16 = BlackjackTotal16 + 1
    elif players_hand_after_hit_value16 > 21:
        LossTotal16 = LossTotal16 + 1
    elif (players_hand_after_hit_value16 < 22 and players_hand_after_hit_value16 > dealers_hand_after_hit_value16) or (
            dealers_hand_after_hit_value16 > 21):
        WinTotal16 = WinTotal16 + 1
    elif (dealers_hand_after_hit_value16 > players_hand_after_hit_value16 and dealers_hand_after_hit_value16 < 22) or (
            players_hand_after_hit_value16 > 21):
        LossTotal16 = LossTotal16 + 1
    elif (players_hand_after_hit_value16 == dealers_hand_after_hit_value16) and (dealers_hand_after_hit_value16 < 22) and (
            players_hand_after_hit_value16 < 22):
        PushTotal16 = PushTotal16 + 1


    d16 = {'Players Initital Hand:': players_hand_value16, 'Dealers Hand:': dealers_hand_value16, "Players Hit:": players_hit16, "Players Final Hand:": players_hand_after_hit_value16, "Dealers Final Hand:": dealers_hand_after_hit_value16,  "Blackjack Total:": BlackjackTotal16, "Win Total:": WinTotal16, "Loss Total:": LossTotal16, "Push Total:": PushTotal16}
    data16.append(d16)

hey16 = pd.DataFrame(data16)

hey16.to_excel("Dealer3HU16.xlsx")

# START OF 17START OF 17START OF 17START OF 17START OF 17START OF 17START OF 17START OF 17

for each in range(100000):
    cards_in_deck17 = ['Ace', 2, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                     'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                     'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                     'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                     'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                     'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                     'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                     'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

    players_hand_value17 = 0
    dealers_hand_value17 = 3

    print("\n\n\nThese are cards_in_deck before any dealing:", cards_in_deck17)

    players_hand17 = random.sample(cards_in_deck17, 2)

    print("\nThis is players_hand:", players_hand17)

    for each in players_hand17:
        cards_in_deck17.remove(each)

    print("\nThese are cards_in_deck after dealing to player:", cards_in_deck17)

    dealers_hand17 = random.sample(cards_in_deck17, 1)

    print("\nThis is dealers_hand:", dealers_hand17)

    for each in dealers_hand17:
        cards_in_deck17.remove(each)

    print("\nThese are cards_in_deck after dealing to dealer:", cards_in_deck17)

    # Need to figure out how to make the values from face cards / ace change

    for each in range(len(players_hand17)):
        if players_hand17[each] == 2:
            players_hand_value17 = players_hand_value17 + 2
        if players_hand17[each] == 3:
            players_hand_value17 = players_hand_value17 + 3
        if players_hand17[each] == 4:
            players_hand_value17 = players_hand_value17 + 4
        if players_hand17[each] == 5:
            players_hand_value17 = players_hand_value17 + 5
        if players_hand17[each] == 6:
            players_hand_value17 = players_hand_value17 + 6
        if players_hand17[each] == 7:
            players_hand_value17 = players_hand_value17 + 7
        if players_hand17[each] == 8:
            players_hand_value17 = players_hand_value17 + 8
        if players_hand17[each] == 9:
            players_hand_value17 = players_hand_value17 + 9
        if players_hand17[each] == 10:
            players_hand_value17 = players_hand_value17 + 10
        if players_hand17[each] == 'Ace':
            players_hand_value17 = players_hand_value17 + 11
        if players_hand17[each] == 'J':
            players_hand_value17 = players_hand_value17 + 10
        if players_hand17[each] == 'Q':
            players_hand_value17 = players_hand_value17 + 10
        if players_hand17[each] == 'K':
            players_hand_value17 = players_hand_value17 + 10

    if players_hand_value17 == 22:
        players_hand_value17 = 12

    print("\nThis is players_hand_value after dealing:", players_hand_value17)

    for each in range(len(dealers_hand17)):
        if dealers_hand17[each] == 2:
            dealers_hand_value17 = dealers_hand_value17 + 2
        if dealers_hand17[each] == 3:
            dealers_hand_value17 = dealers_hand_value17 + 3
        if dealers_hand17[each] == 4:
            dealers_hand_value17 = dealers_hand_value17 + 4
        if dealers_hand17[each] == 5:
            dealers_hand_value17 = dealers_hand_value17 + 5
        if dealers_hand17[each] == 6:
            dealers_hand_value17 = dealers_hand_value17 + 6
        if dealers_hand17[each] == 7:
            dealers_hand_value17 = dealers_hand_value17 + 7
        if dealers_hand17[each] == 8:
            dealers_hand_value17 = dealers_hand_value17 + 8
        if dealers_hand17[each] == 9:
            dealers_hand_value17 = dealers_hand_value17 + 9
        if dealers_hand17[each] == 10:
            dealers_hand_value17 = dealers_hand_value17 + 10
        if dealers_hand17[each] == 'Ace':
            dealers_hand_value17 = dealers_hand_value17 + 11
        if dealers_hand17[each] == 'J':
            dealers_hand_value17 = dealers_hand_value17 + 10
        if dealers_hand17[each] == 'Q':
            dealers_hand_value17 = dealers_hand_value17 + 10
        if dealers_hand17[each] == 'K':
            dealers_hand_value17 = dealers_hand_value17 + 10

    if dealers_hand_value17 == 22:
        dealers_hand_value17 = 12

    print("\nThis is dealers_hand_value after dealing:", dealers_hand_value17)

    players_hand_after_hit17 = players_hand17[:]
    players_hand_after_hit_value17 = 0

    for each in range(len(players_hand_after_hit17)):         #This is to set another variable to the initial hand, we actually add the hits next step!
        if players_hand_after_hit17[each] == 2:
            players_hand_after_hit_value17 = players_hand_after_hit_value17 + 2
        if players_hand_after_hit17[each] == 3:
            players_hand_after_hit_value17 = players_hand_after_hit_value17 + 3
        if players_hand_after_hit17[each] == 4:
            players_hand_after_hit_value17 = players_hand_after_hit_value17 + 4
        if players_hand_after_hit17[each] == 5:
            players_hand_after_hit_value17 = players_hand_after_hit_value17 + 5
        if players_hand_after_hit17[each] == 6:
            players_hand_after_hit_value17 = players_hand_after_hit_value17 + 6
        if players_hand_after_hit17[each] == 7:
            players_hand_after_hit_value17 = players_hand_after_hit_value17 + 7
        if players_hand_after_hit17[each] == 8:
            players_hand_after_hit_value17 = players_hand_after_hit_value17 + 8
        if players_hand_after_hit17[each] == 9:
            players_hand_after_hit_value17 = players_hand_after_hit_value17 + 9
        if players_hand_after_hit17[each] == 10:
            players_hand_after_hit_value17 = players_hand_after_hit_value17 + 10
        if players_hand_after_hit17[each] == 'Ace':
            players_hand_after_hit_value17 = players_hand_after_hit_value17 + 11
        if players_hand_after_hit17[each] == 'J':
            players_hand_after_hit_value17 = players_hand_after_hit_value17 + 10
        if players_hand_after_hit17[each] == 'Q':
            players_hand_after_hit_value17 = players_hand_after_hit_value17 + 10
        if players_hand_after_hit17[each] == 'K':
            players_hand_after_hit_value17 = players_hand_after_hit_value17 + 10

    if players_hand_after_hit_value17 == 22:
        players_hand_after_hit_value17 = 12

    players_hit17 = []

    for each in range(10):                                              #for 10 iterations
        if players_hand_after_hit_value17 < 17:                           #only if current hand value is <19
            players_hit17 = random.sample(cards_in_deck17, 1)               #players_hit is a random sampling of 1 card that remains in the deck
            print("\nThis is players_hit:", players_hit17)
            print("\nThis is players_hit[-1]:", players_hit17[-1])
            cards_in_deck17.remove(players_hit17[-1])                       #remove the last item (aka most recent) in players_hit
            players_hand_after_hit17.append(players_hit17[-1])              #add the latest item to our hand
            if players_hand_after_hit17[-1] == 2:
                players_hand_after_hit_value17 = players_hand_after_hit_value17 + 2
            if players_hand_after_hit17[-1] == 3:
                players_hand_after_hit_value17 = players_hand_after_hit_value17 + 3
            if players_hand_after_hit17[-1] == 4:
                players_hand_after_hit_value17 = players_hand_after_hit_value17 + 4
            if players_hand_after_hit17[-1] == 5:
                players_hand_after_hit_value17 = players_hand_after_hit_value17 + 5
            if players_hand_after_hit17[-1] == 6:
                players_hand_after_hit_value17 = players_hand_after_hit_value17 + 6
            if players_hand_after_hit17[-1] == 7:
                players_hand_after_hit_value17 = players_hand_after_hit_value17 + 7
            if players_hand_after_hit17[-1] == 8:
                players_hand_after_hit_value17 = players_hand_after_hit_value17 + 8
            if players_hand_after_hit17[-1] == 9:
                players_hand_after_hit_value17 = players_hand_after_hit_value17 + 9
            if players_hand_after_hit17[-1] == 10:
                players_hand_after_hit_value17 = players_hand_after_hit_value17 + 10
            if players_hand_after_hit17[-1] == 'Ace':
                players_hand_after_hit_value17 = players_hand_after_hit_value17 + 11
            if players_hand_after_hit17[-1] == 'J':
                players_hand_after_hit_value17 = players_hand_after_hit_value17 + 10
            if players_hand_after_hit17[-1] == 'Q':
                players_hand_after_hit_value17 = players_hand_after_hit_value17 + 10
            if players_hand_after_hit17[-1] == 'K':
                players_hand_after_hit_value17 = players_hand_after_hit_value17 + 10
            if players_hand_after_hit_value17 > 21 and 'Ace' in players_hand_after_hit17:
                players_hand_after_hit_value17 = players_hand_after_hit_value17 - 10
        else:
            continue


    dealers_hand_after_hit17 = dealers_hand17[:]
    dealers_hand_after_hit_value17 = 3

    for each in range(len(dealers_hand_after_hit17)):
        if dealers_hand_after_hit17[each] == 2:
            dealers_hand_after_hit_value17 = dealers_hand_after_hit_value17 + 2
        if dealers_hand_after_hit17[each] == 3:
            dealers_hand_after_hit_value17 = dealers_hand_after_hit_value17 + 3
        if dealers_hand_after_hit17[each] == 4:
            dealers_hand_after_hit_value17 = dealers_hand_after_hit_value17 + 4
        if dealers_hand_after_hit17[each] == 5:
            dealers_hand_after_hit_value17 = dealers_hand_after_hit_value17 + 5
        if dealers_hand_after_hit17[each] == 6:
            dealers_hand_after_hit_value17 = dealers_hand_after_hit_value17 + 6
        if dealers_hand_after_hit17[each] == 7:
            dealers_hand_after_hit_value17 = dealers_hand_after_hit_value17 + 7
        if dealers_hand_after_hit17[each] == 8:
            dealers_hand_after_hit_value17 = dealers_hand_after_hit_value17 + 8
        if dealers_hand_after_hit17[each] == 9:
            dealers_hand_after_hit_value17 = dealers_hand_after_hit_value17 + 9
        if dealers_hand_after_hit17[each] == 10:
            dealers_hand_after_hit_value17 = dealers_hand_after_hit_value17 + 10
        if dealers_hand_after_hit17[each] == 'Ace':
            dealers_hand_after_hit_value17 = dealers_hand_after_hit_value17 + 11
        if dealers_hand_after_hit17[each] == 'J':
            dealers_hand_after_hit_value17 = dealers_hand_after_hit_value17 + 10
        if dealers_hand_after_hit17[each] == 'Q':
            dealers_hand_after_hit_value17 = dealers_hand_after_hit_value17 + 10
        if dealers_hand_after_hit17[each] == 'K':
            dealers_hand_after_hit_value17 = dealers_hand_after_hit_value17 + 10

    if dealers_hand_after_hit_value17 == 22:
        dealers_hand_after_hit_value17 = 12

    dealers_hit17 = []

    for each in range(10):
        if players_hand_after_hit_value17 > dealers_hand_after_hit_value17 and players_hand_after_hit_value17 < 22 and dealers_hand_after_hit_value17 < 22:
            dealers_hit17 = random.sample(cards_in_deck17, 1)
            print("\nThis is dealers_hit:", dealers_hit17)
            print("\nThis is dealers_hit[-1]:", dealers_hit17[-1])
            cards_in_deck17.remove(dealers_hit17[-1])
            dealers_hand_after_hit17.append(dealers_hit17[-1])
            if dealers_hand_after_hit17[-1] == 2:
                dealers_hand_after_hit_value17 = dealers_hand_after_hit_value17 + 2
            if dealers_hand_after_hit17[-1] == 3:
                dealers_hand_after_hit_value17 = dealers_hand_after_hit_value17 + 3
            if dealers_hand_after_hit17[-1] == 4:
                dealers_hand_after_hit_value17 = dealers_hand_after_hit_value17 + 4
            if dealers_hand_after_hit17[-1] == 5:
                dealers_hand_after_hit_value17 = dealers_hand_after_hit_value17 + 5
            if dealers_hand_after_hit17[-1] == 6:
                dealers_hand_after_hit_value17 = dealers_hand_after_hit_value17 + 6
            if dealers_hand_after_hit17[-1] == 7:
                dealers_hand_after_hit_value17 = dealers_hand_after_hit_value17 + 7
            if dealers_hand_after_hit17[-1] == 8:
                dealers_hand_after_hit_value17 = dealers_hand_after_hit_value17 + 8
            if dealers_hand_after_hit17[-1] == 9:
                dealers_hand_after_hit_value17 = dealers_hand_after_hit_value17 + 9
            if dealers_hand_after_hit17[-1] == 10:
                dealers_hand_after_hit_value17 = dealers_hand_after_hit_value17 + 10
            if dealers_hand_after_hit17[-1] == 'Ace':
                dealers_hand_after_hit_value17 = dealers_hand_after_hit_value17 + 11
            if dealers_hand_after_hit17[-1] == 'J':
                dealers_hand_after_hit_value17 = dealers_hand_after_hit_value17 + 10
            if dealers_hand_after_hit17[-1] == 'Q':
                dealers_hand_after_hit_value17 = dealers_hand_after_hit_value17 + 10
            if dealers_hand_after_hit17[-1] == 'K':
                dealers_hand_after_hit_value17 = dealers_hand_after_hit_value17 + 10
            if dealers_hand_after_hit_value17 > 21 and 'Ace' in dealers_hand_after_hit17:
                dealers_hand_after_hit_value17 = dealers_hand_after_hit_value17 - 10
        else:
            continue


    if players_hand_value17 == 21:
        BlackjackTotal17 = BlackjackTotal17 + 1
    elif players_hand_after_hit_value17 > 21:
        LossTotal17 = LossTotal17 + 1
    elif (players_hand_after_hit_value17 < 22 and players_hand_after_hit_value17 > dealers_hand_after_hit_value17) or (
            dealers_hand_after_hit_value17 > 21):
        WinTotal17 = WinTotal17 + 1
    elif (dealers_hand_after_hit_value17 > players_hand_after_hit_value17 and dealers_hand_after_hit_value17 < 22) or (
            players_hand_after_hit_value17 > 21):
        LossTotal17 = LossTotal17 + 1
    elif (players_hand_after_hit_value17 == dealers_hand_after_hit_value17) and (dealers_hand_after_hit_value17 < 22) and (
            players_hand_after_hit_value17 < 22):
        PushTotal17 = PushTotal17 + 1

    d17 = {'Players Initital Hand:': players_hand_value17, 'Dealers Hand:': dealers_hand_value17, "Players Hit:": players_hit17, "Players Final Hand:": players_hand_after_hit_value17, "Dealers Final Hand:": dealers_hand_after_hit_value17,  "Blackjack Total:": BlackjackTotal17, "Win Total:": WinTotal17, "Loss Total:": LossTotal17, "Push Total:": PushTotal17}
    data17.append(d17)

hey17 = pd.DataFrame(data17)

hey17.to_excel("Dealer3HU17.xlsx")

