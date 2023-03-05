# import functions
import random
from replit import clear
from art import logo
# define for starting and end of game True or False

# Blackjack Cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def dealer_card(card):
    return random.choice(cards)


def user_score(user_card):
    return sum(user_card)


def comp_score(comp_card):
    return sum(comp_card)


def first_card(user_card, comp_card):
    # Your cards: [10, 5], current score: 15
    # Computer's first card: 2
    print(f"Your cards: {user_card}, current score: {user_score(user_card)}")
    print(f"Computer's first card: {comp_card[0]}")


def final_card(user_card, comp_card):
    # Your final hand: [2, 10, 10], final score: 22
    # Computer's final hand: [9, 5, 1, 10], final score: 25
    print(
        f"Your final hand: {user_card}, final score: {user_score(user_card)}")
    print(
        f"Computer's final hand: {comp_card}, final score: {comp_score(comp_card)}"
    )


def Blackjack(user_card, comp_card):
    if (10 in user_card and 11 in user_card) and (10 in comp_card
                                                  and 11 in comp_card):
        final_card(user_card, comp_card)
        print("User and computer got a Blackjack, It's a draw 🙃")
    elif (10 in user_card and 11 in user_card):
        final_card(user_card, comp_card)
        print("It's a Blackjack, you win😄")
    elif (10 in comp_card and 11 in comp_card):
        final_card(user_card, comp_card)
        print("Computer chose Blackjack, you lose😭")


def Ace(card):
    pos = card.index(11)
    card[pos] = 1
    return card



def should_continue():
    Game_over = False
    while not Game_over:
        user_card = []
        comp_card = []
        draw_card = True
        start = input(
            "Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if start == "y":
            clear()
            print(f"{logo}\n")
            for i in range(2):
                user_card.append(dealer_card(user_card))
                comp_card.append(dealer_card(comp_card))
            print(comp_card)
            first_card(user_card, comp_card)
            if (10 in user_card and 11 in user_card) or (10 in comp_card
                                                         and 11 in comp_card):
                Blackjack(user_card, comp_card)
                Game_over = False
            else:
                while draw_card:
                    take_card = input(
                        "Type 'y' to get another card, type 'n' to pass: ")
                    if take_card == 'y':
                        user_card.append(dealer_card(user_card))
                        first_card(user_card, comp_card)
                        while comp_score(comp_card) < 17:
                            comp_card.append(dealer_card(comp_card))
                        if user_score(user_card) > 21:
                            if 11 in user_card:
                                Ace(user_card)
                            else:
                                final_card(user_card, comp_card)
                                print("You went over. You lose 😤")
                                draw_card = False
                                Game_over = False
                                # should_continue()
                        elif comp_score(comp_card) > 21:
                            if 11 in comp_card:
                                Ace(comp_card)
                            else:
                                final_card(user_card, comp_card)
                                print("Opponent went over. You win😄")
                                draw_card = False
                                Game_over = False
                                # should_continue()
                        else:
                            if (user_score(user_card)
                                    or comp_score(comp_card)) > 21:
                                final_card(user_card, comp_card)
                                if comp_score(comp_card) > 21:
                                    print("Opponent went over. You win😄")
                                    draw_card = False
                                    Game_over = False
                                elif user_score(user_card) > 21:
                                    print("You went over, you lose😭")
                                    draw_card = False
                                    Game_over = False
                                elif user_score(user_card) == comp_score(
                                        comp_card):
                                    print("It's a Draw 🙃")
                                    draw_card = False
                                    Game_over = False
                            else:
                                draw_card = True
                    else:
                        while comp_score(comp_card) < 17:
                            comp_card.append(dealer_card(comp_card))
                        if comp_score(comp_card) > 21:
                            if 11 in comp_card:
                                Ace(comp_card)
                            else:
                                final_card(user_card, comp_card)
                                print("Opponent went over. You win😄")
                                draw_card = False
                                Game_over = False
                        else:
                            final_card(user_card, comp_card)
                            if user_score(user_card) > comp_score(comp_card):
                                print("Opponent went over. You win😄")
                                draw_card = False
                                Game_over = False
                            elif comp_score(comp_card) > user_score(user_card):
                                print("You went over, you lose😭")
                                draw_card = False
                                Game_over = False
                            elif (user_score(user_card) == comp_score(
                                    comp_card)):
                                print("It's a Draw 🙃")
                                draw_card = False
                                Game_over = False
        else:
            Game_over = True
should_continue()

