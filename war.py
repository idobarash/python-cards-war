from deck import Deck
from player import Player

class War:

    def __init__(self):
        deck = Deck()
        deck.shuffel()

        self.player1 = Player("Jose", deck.deal_half())
        self.player2 = Player("Chen", deck.cards)

        print("Initiated game")
        print(f'{str(self.player1)} GOT {len(self.player1.deck)} cards')
        print(f'{str(self.player2)} GOT {len(self.player2.deck)} cards')
        print("Can start game")

    def play_turn(self):

        player1_cards = []
        player2_cards = []

        finished = False
        while not finished:

            current_player1_card = self.player1.hit()
            current_player2_card = self.player2.hit()

            player1_cards.append(current_player1_card)
            player2_cards.append(current_player2_card)

            if not len(self.player1.deck) == 0 or len(self.player2.deck):
                if current_player1_card.value > current_player2_card.value:
                    self.player1.collect(player1_cards)
                    self.player1.collect(player2_cards)
                    finished = True
                    print(f'{str(self.player1)} WON THIS ROUND !!   pulled  {str(current_player1_card)}  VS {str(current_player2_card)}')
                elif current_player2_card.value > current_player1_card.value:
                    self.player2.collect(player1_cards)
                    self.player2.collect(player2_cards)
                    finished = True
                    print(f'{str(self.player2)} WON THIS ROUND !!   pulled  {str(current_player2_card)}  VS {str(current_player1_card)}')
                else:
                    print("WAR WAR WAR VAMMMOOSSS!!!");
                    player1_cards.extend(self.player1.pull3())
                    player2_cards.extend(self.player2.pull3())
            else:
                finished = True
            

    def get_winner(self):
        if len(self.player1.collected_cards) > len(self.player2.collected_cards):
            return self.player1
        elif len(self.player1.collected_cards) < len(self.player2.collected_cards):
            return self.player2
        else:
            return None

    def is_finished(self):
        return len(self.player1.deck) == 0 or len(self.player2.deck) == 0

    def play(self):
        finished = False
        while not finished:
            self.play_turn()
            finished = self.is_finished()
            
        winner = self.get_winner()
        print(f'Game Finished:  winner is {str(winner)} who collected {len(winner.collected_cards)} cards')
    
    