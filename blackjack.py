from random import randint
from deck import card_name, card_value, end_turn_status, end_game_status

def main():

    print("-----------\n" "YOUR TURN\n" "-----------")

    random1 = randint(1, 13)
    random2 = randint(1, 13)
    print("Drew a {}".format(card_name(random1)))
    print("Drew a {}".format(card_name(random2)))
    user_total = card_value(random1) + card_value(random2)

    if user_total == 21:
        print("Final hand: {}.".format(user_total))
        print("BLACKJACK!")

    elif user_total != 21:
        question = input("You have {}. Hit (y/n)? ".format(user_total))
        if question == "n" and user_total < 21:
            print("Final hand: {}.".format(user_total))

        elif question == "y":
            while question == 'y' and user_total < 21:
                if question == "y" and user_total < 21:
                    random3 = randint(1, 13)
                    print("Drew a {}".format(card_name(random3)))
                    random3 = card_value(random3)
                    user_total = user_total + random3
                if user_total < 21:
                    question = input("You have {}. Hit (y/n)? ".format(user_total))
            else:
                print("Final hand: {}.".format(user_total))
                print(end_turn_status(user_total))

    print("-----------\n" "DEALER TURN\n" "-----------")

    random1 = randint(1, 13)
    random2 = randint(1, 13)
    print("Drew a {}".format(card_name(random1)))
    print("Drew a {}".format(card_name(random2)))
    dealer_total = card_value(random1) + card_value(random2)
    if dealer_total > 17 or dealer_total == 21:
        print("Final hand: {}.".format(dealer_total))
    if dealer_total <= 17:
        print("Dealer has {}.".format(dealer_total))

    while dealer_total <= 17:
        random3 = randint(1, 13)
        print("Drew a {}".format(card_name(random3)))
        random3 = card_value(random3)
        dealer_total = dealer_total + random3

        if dealer_total <= 17:
            print("Dealer has {}.".format(dealer_total))
        if dealer_total == 21 or dealer_total > 21 or dealer_total > 17:
            print("Final hand: {}.".format(dealer_total))

    print(end_turn_status(dealer_total))
    print("-----------\n" "GAME RESULT\n" "-----------")
    print(end_game_status(user_total, dealer_total))
if __name__ == "__main__":
    main()