card_name_to_id = {}
next_card_id = 0

deck_to_cards = {}

player_to_decks = {}

try:
    lines = []
    while True:
        line = input()
        if not line.strip():
            break
        lines.append(line)
except EOFError:
    pass

for line in lines:
    parts = line.split(' / ')
    if parts[0][0].isdigit():
        deck_number = int(parts[0])
        card_name = parts[1]
        if card_name not in card_name_to_id:
            card_name_to_id[card_name] = next_card_id
            next_card_id += 1
        card_id = card_name_to_id[card_name]
        if deck_number not in deck_to_cards:
            deck_to_cards[deck_number] = []
        deck_to_cards[deck_number].append(card_id)
    else:
        player_name = parts[0]
        deck_number = int(parts[1])
        if player_name not in player_to_decks:
            player_to_decks[player_name] = []
        player_to_decks[player_name].append(deck_number)

for deck_number in deck_to_cards:
    deck_to_cards[deck_number].sort()

def count_unique_sorted(sorted_list):
    if not sorted_list:
        return 0
    count = 1
    prev = sorted_list[0]
    for num in sorted_list[1:]:
        if num != prev:
            count += 1
            prev = num
    return count

max_pack_size = -1
largest_pack_players = []

for player, decks in player_to_decks.items():
    all_cards = []
    append = all_cards.append
    for deck in decks:
        if deck in deck_to_cards:
            cards = deck_to_cards[deck]
            for card in cards:
                append(card)
    if not all_cards:
        unique_count = 0
    else:
        all_cards.sort()
        unique_count = count_unique_sorted(all_cards)
    if unique_count > max_pack_size:
        max_pack_size = unique_count
        largest_pack_players = [player]
    elif unique_count == max_pack_size:
        largest_pack_players.append(player)

largest_pack_players.sort()

for player in largest_pack_players:
    print(player)
