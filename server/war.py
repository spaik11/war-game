import random


def war(player1, player2):
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
             'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
              'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

    class Card:
        def __init__(self, suit, rank):
            self.suit = suit
            self.rank = rank
            self.value = values[rank]

        def __str__(self):
            return f"{self.rank} of {self.suit}"

    class Deck:
        def __init__(self):
            self.all_cards = []

            for suit in suits:
                for rank in ranks:
                    created_card = Card(suit, rank)

                    self.all_cards.append(created_card)

        def shuffle(self):
            random.shuffle(self.all_cards)

        def deal_one(self):
            return self.all_cards.pop()

    class Player:
        def __init__(self, id, username):
            self.id = id
            self.username = username
            self.all_cards = []

        def remove_one(self):
            return self.all_cards.pop(0)

        def add_cards(self, new_cards):
            if type(new_cards) == type([]):
                self.all_cards.extend(new_cards)
            else:
                self.all_cards.append(new_cards)

        def __str__(self):
            return f'Player {self.username} has {len(self.all_cards)} cards.'

    player_one = Player(player1.id, player1.username)
    player_two = Player(player2.id, player2.username)

    new_deck = Deck()
    new_deck.shuffle()

    for x in range(26):
        player_one.add_cards(new_deck.deal_one())
        player_two.add_cards(new_deck.deal_one())

    game_on = True
    round_num = 0

    while game_on:
        round_num += 1
        print(f'Round {round_num}')

        if len(player_one.all_cards) == 0:
            print(f'{player_one.username}, out of cards! {player_two.username} Wins!')
            return (player_two, round_num, player_one)

        if len(player_two.all_cards) == 0:
            print(
                f'{player_two.username} , out of cards! {player_one.username} Wins!')
            return (player_one, round_num, player_two)

        # START A NEW ROUND
        player_one_cards = []
        player_one_cards.append(player_one.remove_one())

        player_two_cards = []
        player_two_cards.append(player_two.remove_one())

        # WHILE AT WAR
        at_war = True

        while at_war:
            if player_one_cards[-1].value > player_two_cards[-1].value:
                player_one.add_cards(player_one_cards)
                player_one.add_cards(player_two_cards)

                at_war = False
            elif player_one_cards[-1].value < player_two_cards[-1].value:
                player_two.add_cards(player_one_cards)
                player_two.add_cards(player_two_cards)

                at_war = False
            else:
                print('WAR!')

                if len(player_one.all_cards) < 5:
                    print(f'{player_one.username} unable to declare war')
                    print(f'{player_two.username.upper()} WINS!')
                    return (player_two, round_num, player_one)

                elif len(player_two.all_cards) < 5:
                    print(f'{player_two.username} unable to declare war')
                    print(f'{player_one.username.upper()} WINS!')
                    return (player_one, round_num, player_two)

                else:
                    for num in range(5):
                        player_one_cards.append(player_one.remove_one())
                        player_two_cards.append(player_two.remove_one())
