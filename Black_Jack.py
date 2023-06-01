import random
from math import *


# le variabili che passano tramite valuta e non referenza anche se cambiano nella funzione non
# cambiano al di fuori a meno che non ci sia un retrun, oppure posso rendere il valore della
# valuta globale senza inserirla nei paramentri della funzione
# per esempio my_cards e bot_cards passano tramite referenza quindi cambiano dentro e fuori
# questo accade principalmente in python
def initial_draw(deck, my_cards, bot_cards):
    global card_drawn

    print("you and your opponent get 2 cards each\n")

    my_cards.append(deck.pop(ceil(random.random() * (12 - card_drawn))))
    card_drawn += 1
    bot_cards.append(deck.pop(ceil(random.random() * (12 - card_drawn))))
    card_drawn += 1
    my_cards.append(deck.pop(ceil(random.random() * (12 - card_drawn))))
    card_drawn += 1
    bot_cards.append(deck.pop(ceil(random.random() * (12 - card_drawn))))
    card_drawn += 1


def my_turn(deck):
    global card_drawn
    global my_stay
    print("\nit s your turn, do you hit or stay?")
    hit_or_stay = ""
    while hit_or_stay.lower() != "hit" and hit_or_stay.lower() != "stay":
        hit_or_stay = input()
        if hit_or_stay.lower() == "hit":
            my_cards.append(deck.pop(ceil(random.random() * (12 - card_drawn))))
            card_drawn += 1
        elif hit_or_stay.lower() == "stay":
            my_stay = False
        else:
            print("wrong command, please write hit or stay")


def bot_turn(bot_cards):
    global bot_stay
    global card_drawn

    if (
        sum_cards(bot_cards) < 14
    ):  # se la probabilita di pescare una carta che resta sotto 21 e del 50% o >
        print("\n\nYour opponent draw")
        bot_cards.append(deck.pop(ceil(random.random() * (12 - card_drawn))))
        card_drawn += 1
    else:
        print("\n\nYour opponent stay")
        bot_stay = False


def sum_cards(card_array):
    x = 0
    for card in card_array:  # to fix the Q, K, J problem
        if str(card) in "KQJ":
            x += 10
        else:
            x += card
    return x


def on_table(bot_cards, my_cards):
    print(
        "[x] "
        + f"{bot_cards[1:]}   = ? + "
        + str(
            sum_cards(bot_cards) - bot_cards[0]  # interesting code
            if str(bot_cards[0]) not in "KJQ"
            else sum_cards(bot_cards) - 10
        )
        + "\n\n"
        + "[x] "
        + f"{my_cards[1:]}    = "
        + str(sum_cards(my_cards))
        + f"\n({my_cards[0]})"
    )


deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Q", "K", "J"]
my_cards = []
bot_cards = []
my_score = 0  # how many time the player won the black jack
bot_score = 0  # how many time the bot won the black jack
card_drawn = 0  # the number of the card removed in the array
bot_stay = True
my_stay = True
play_again = ""

"""
print(
    "Welcome to Black Jack, this is slightly different versioin of it, do you want to read the rule?"
)

rule = input()

if rule == "yes":
    print(
        "\n- The deck will be made by 13 cards 1-10 with their value and Q, K and J with value 10\n- When a card is on the desk it can't exist another card with the same number/letter\n- Cards will be given A, B, A, B\n- The First card will be covered and only you will know the value of it, same for the bot, from the second on all of them will be uncovered\n- At the beginning of each turn the bot or the player will be able to confirm their cards or draw a single one, once one of this action happen the turn will pass to the other player\n- If both the players confirm who get closer to 21 win, or tie in case both score are equal\n- If both the bot and the player get over 21 win the one with the number closer to 21 else tie\n"
    )

# aggiungo qui il while play_again == "yes":
# + AGGIUNGO TUTTI I VALORI QUI

print("Press entrer to start playing, have fun!!")
input()
print("\n\n\n\n")
"""

initial_draw(deck, my_cards, bot_cards)
on_table(bot_cards, my_cards)

while bot_stay or my_stay:  # why?
    my_turn(deck)
    bot_turn(bot_cards)
    on_table(bot_cards, my_cards)

print("******************")

if sum_cards(my_cards) == sum_cards(bot_cards):
    print(
        f"Tie! your card value is {sum_cards(my_cards)} and the opponent's one is {sum_cards(bot_cards)}"
    )
elif abs(sum_cards(my_cards) - 21) < abs(sum_cards(bot_cards) - 21):
    print(
        f"Good job!! You won!! your card value is {sum_cards(my_cards)} and the opponent's one is {sum_cards(bot_cards)}"
    )
    my_score += 1
else:
    print(
        f"Your opponent won! your card value is {sum_cards(my_cards)} and the opponent's one is {sum_cards(bot_cards)}"
    )
    bot_score += 1

print(f"Your score: {my_score}\nOpponent's score: {bot_score}")
play_again = input("\ndo you wanna play again?")

# if play == 'yes':
#
# else:
