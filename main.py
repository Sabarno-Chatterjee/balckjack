
import random
import art
from replit import clear

def play_game():

  print(art.logo)
  
  def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
  
  def calculate_score(cards):
    """Calculates the total score"""
    if sum(cards) == 21 and len(cards) == 2:
      return 0
    
    if 11 in cards and sum(cards) > 21:
      cards.remove(11)
      cards.append(1)
    return sum(cards)
  #Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
  
  def compare(user_score, computer_score):
    """Takes user_score & computer_score as argument and returns the result."""
    if user_score == computer_score:
      return "Draw."
    elif computer_score == 0:
      return "You lost! Opponent has a Blackjack."
    elif user_score == 0:
      return "Win with a Blackjack."
    elif user_score > 21:
      return "You went over! You lose."
    elif computer_score > 21:
      return "Opponent went over. You win!"
    elif user_score > computer_score:
      return "You win."
    else:
      return "You lose."
      
      
  user_cards = []
  computer_cards = []
  is_game_over = False
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not is_game_over:
    
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards are: {user_cards}, Current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      new_card = input("Type 'y' for new card or 'n' to pass.\n").lower()
      if new_card == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  
  print(f"Your final hand was: {user_cards} and final score: {user_score}.")
  print(f"Computer's final hand was : {computer_cards} and final_score: {computer_score}.")
  print(compare(user_score, computer_score))

  
while input("Do you want to play another game of Blackjack? Press 'y' for yes or 'n for 'no'.\n") == "y":
  clear()
  play_game()