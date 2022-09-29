def calc(player_total, dealer_total):
    if player_total > 21 and dealer_total > 21:
        return "That's a double bust, regame time!"
    elif player_total == 21 and dealer_total < 21:
        return "You win."
    elif player_total < 21 and dealer_total == 21:
        return "Computer wins!"
    elif player_total == dealer_total:
        return "It's a draw."
    elif player_total > 21 and dealer_total <= 21:
        return "That's a bust, computer wins!"
    elif dealer_total > 21 and player_total <= 21:
        return "The comp busted, you win!"
    elif dealer_total < 21 and player_total < 21:
        if dealer_total > player_total:
            return "The comp wins."
        else:
            return "You win!"
