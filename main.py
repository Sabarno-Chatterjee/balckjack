import random
import art


def calculations(player_total, dealer_total):
    if player_total > 21 and dealer_total > 21:
        return "That's a double bust, regame time!"
    elif player_total == 21 and dealer_total < 21:
        return "You win."
    elif player_total < 21 and dealer_total == 21:
        return "Computer wins!"
    elif player_total == dealer_total:
        return "It's a draw."
    elif player_total > 21 and dealer_total < 21:
        return "That's a bust, computer wins!"
    elif dealer_total > 21 and player_total < 21:
        return "The comp busted, you win!"
    elif dealer_total < 21 and player_total < 21:
        if dealer_total > player_total:
            return "The comp wins."
        else:
            return "You win!"

# if (input("Do you want to play a game of blackjack. Type 'y' or 'n'.\n").lower()) == "y":
new_game = True

while new_game:
    if (input("Do you want to play a game of blackjack. Type 'y' or 'n'.\n").lower()) == "y":
        print(art.logo)

        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        player = []
        dealer = []
        player_total = 0
        dealer_total = 0

        is_continue = True

        for card in range(0, 2):
            player.append(random.choice(cards))
            dealer.append(random.choice(cards))
            player_total += player[card]
            dealer_total += dealer[card]

        print(f"Your cards: {player}, current score: {player_total}")
        print(f"Computer's first card: {dealer[0]}")

        cue = 1
        while is_continue:
            if (input("Type 'y' to get another card, type 'n' to pass:\n")) == "y":
                print()
                cue += 1
                player.append(random.choice(cards))
                player_total += player[cue]
                dealer.append(random.choice(cards))
                dealer_total += dealer[cue]
                print(f"Your cards: {player}, current score: {player_total}")
                print(f"Computer's first card: {dealer[0]}")
                print()
            else:
                is_continue = False

        print()
        print(f"Your final hand: {player}, final score: {player_total}")
        print(f"Computer's final hand: {dealer}, final score: {dealer_total}")

        result = calculations(player_total, dealer_total)
        print(result)
    else:
        new_game = False

print("Goodbye bitch! See you in hell.")