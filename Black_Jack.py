import random
from math import *


# here card drawn is increasing in the function but it stay 0 out of it
def initial_draw(deck, my_cards, bot_cards, card_drawn):
    my_cards.append(deck.pop(ceil(random.random() * (12 - card_drawn))))
    card_drawn += 1
    bot_cards.append(deck.pop(ceil(random.random() * (12 - card_drawn))))
    card_drawn += 1
    my_cards.append(deck.pop(ceil(random.random() * (12 - card_drawn))))
    card_drawn += 1
    bot_cards.append(deck.pop(ceil(random.random() * (12 - card_drawn))))
    card_drawn += 1


def draw_or_stay(deck, card_drawn):
    print("\nit s your turn, do you hit or stay?")
    hit_or_stay = ""
    while hit_or_stay != "hit" and hit_or_stay != "stay":
        hit_or_stay = input()
        if hit_or_stay == "hit":
            my_cards.append(deck.pop(ceil(random.random() * (12 - card_drawn))))
            card_drawn += 1
        elif hit_or_stay == "stay":
            my_confirm = False
        else:
            print("wrong command, please write hit or stay")


def on_table(my_cards, bot_cards, card_drawn, bot_confirm, bot_score):
    for card in bot_cards:  # to fix the Q, K, J problem
        if card in "JQK":
            bot_score += 10
        else:
            bot_score += card

    if (
        bot_score < 15
    ):  # se la probabilita di pescare una carta che resta sotto 21 e del 50% o >
        print("\n\nYour opponent draw")
        bot_cards.append(deck.pop(ceil(random.random() * (12 - card_drawn))))
        card_drawn += 1
    else:
        print("\n\nYour opponent stay")
        bot_confirm = False
    print(
        "[x] "
        + f"{bot_cards[1:]}    ? + "
        + str(bot_score + bot_cards[0])
        + "\n\n"
        + "[x] "
        + f"{my_cards[1:]}        "
        + str(my_score)
        + f"\n({my_cards[0]})"
    )


deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Q", "K", "J"]
Score = 0
my_cards = []
bot_cards = []
bot_score = 0
my_score = 0
card_drawn = 0
bot_confirm = True
my_confirm = True

print(
    "Welcome to Black Jack, this is slightly different versioin of it, do you want to read the rule?"
)

rule = input()

if rule == "yes":
    print(
        "\n- The deck will be made by 13 cards 1-10 with their value and Q, K and J with value 10\n- When a card is on the desk it can't exist another card with the same number/letter\n- Cards will be given A, B, A, B\n- The First card will be covered and only you will know the value of it, same for the bot, from the second on all of them will be uncovered\n- At the beginning of each turn the bot or the player will be able to confirm their cards or draw a single one, once one of this action happen the turn will pass to the other player\n- If both the players confirm who get closer to 21 win, or tie in case both score are equal\n- If both the bot and the player get over 21 win the one with the number closer to 21 else tie\n"
    )
print("Press entrer to start playing, have fun!!\n\n\n\n")
input()
print("you and opponent get 2 cards each\n")

initial_draw(deck, my_cards, bot_cards, card_drawn)

my_score = sum(my_cards)

print(
    "[x] "
    + f"{bot_cards[1:]}    ? + "
    + str(sum(bot_cards[1:]))
    + "\n\n"
    + "[x] "
    + f"{my_cards[1:]}        "
    + str(my_score)
    + f"\n({my_cards[0]})"
)

while bot_confirm and my_confirm:
    draw_or_stay(deck, card_drawn)
    on_table(my_cards, bot_cards, card_drawn, bot_confirm, bot_score)
    # optimize, check if I can add the value ^^^ to the funcion itself if not needed outside
