new_deck = Deck()
new_deck.cards_shuffle()

player1 = Player('A')
player2 = Player('B')

for i in range(26):
    player1.add_cards(new_deck.pop_one())
    player2.add_cards(new_deck.pop_one())

print('Player {} has cards now: {}'.format(player1.name, len(player1.all_cards)))
print('Player {} has cards now:def Play_War_Card_Game():
    game_on = True
    
    round_number = 0
    
    while game_on:

        player_one_cards_rem = len(player1.all_cards)
        player_two_cards_rem = len(player2.all_cards)

        if player_one_cards_rem == 0 and player_two_cards_rem != 0:
            print('{} wins the game. Congratulations!'.format(player2.name))
            game_on = False
            break
        elif player_one_cards_rem != 0 and player_two_cards_rem == 0:
            print('{} wins the game. Congratulations!'.format(player1.name))
            game_on = False
            break
        elif player_one_cards_rem == 0 and player_two_cards_rem == 0:
            print('Match draw! Play again')
            game_on = False
            break

        round_number += 1
        print('Round Number: {}'.format(round_number))

        if game_on:

            player_one_card = []
            player_two_card = []
            
            player_one_card.append(player1.pop_one())
            player_two_card.append(player2.pop_one())

            war = False
            if player_one_card[0].value == player_two_card[0].value:
                war = True

            if war:

                while war:

                    print(' --- War begins --- ')

                    if len(player1.all_cards) == 0 or len(player1.all_cards) < 5:
                        print('{} wins the game. Congratulations!'.format(player2.name))
                        game_on = False
                        war = False
                        break
                    if len(player2.all_cards) == 0 or len(player2.all_cards) < 5:
                        print('{} wins the game. Congratulations!'.format(player1.name))
                        game_on = False
                        war = False
                        break
                    if len(player1.all_cards) == 0 and len(player2.all_cards) == 0:
                        print('Match draw! Play again')
                        game_on = False
                        war = False
                        break

                    for i in range(5):
                        player_one_card.append(player1.pop_one())
                        player_two_card.append(player2.pop_one())

                    if player_one_card[-1].value < player_two_card[-1].value:
                        player2.add_cards(player_one_card)
                        player2.add_cards(player_two_card)
                        war = False
                    elif player_one_card[-1].value > player_two_card[-1].value:
                        player1.add_cards(player_two_card)
                        player1.add_cards(player_one_card)
                        war = False
                    elif player_one_card[-1].value == player_two_card[-1].value:
                        pass

                    print(' ----- War ends ----- ')

            else:
                if player_one_card[0].value < player_two_card[0].value:
                    player2.add_cards(player_one_card)
                    player2.add_cards(player_two_card)
                else:
                    player1.add_cards(player_one_card)
                    player1.add_cards(player_two_card)

            print('{}'.format(player1, len(player1.all_cards)))
            print('{}'.format(player2, len(player2.all_cards)))
        else:
            pass {}'.format(player2.name, len(player2.all_cards)))

