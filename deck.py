from random import randint

def card_name(card_rank):
  if card_rank > 1 and card_rank <= 10:
    card = str(card_rank)
  elif card_rank == 1:
      card = "Ace"
  elif card_rank == 11:
      card = "Jack"
  elif card_rank == 12:
      card = "Queen"
  elif card_rank == 13:
      card = "King"
  return card

def card_value(card_rank):
  if card_rank > 1 and card_rank <= 10:
      value = card_rank
  elif card_rank == 1:
      value = 11
  elif card_rank == 11:
      value = 10
  elif card_rank == 12:
      value = 10
  elif card_rank == 13:
      value = 10
  return value

def end_turn_status(hand):
    if hand > 21:
        status = "BUST."
    elif hand == 21:
        status = "BLACKJACK!"
    elif hand < 21:
        status = ""
    return status

def end_game_status(user_hand,dealer_hand):
    if user_hand == 21 and dealer_hand == 21:
          end = "Tie."
    elif (user_hand > 21 and dealer_hand > 21):
        end = "Tie."
    elif user_hand == dealer_hand:
        end = "Tie."
    elif user_hand > dealer_hand and dealer_hand != 21 and user_hand < 21:
        end = "You win!"
    elif (user_hand == 21 and dealer_hand < user_hand) or dealer_hand > 21:
        end = "You win!"
    elif dealer_hand > user_hand and user_hand != 21 and dealer_hand < 21:
        end = "Dealer wins!"
    elif (dealer_hand == 21 and user_hand < dealer_hand) or user_hand > 21:
        end = "Dealer wins!"
    return end


