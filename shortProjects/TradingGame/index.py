import random

marbles = [
    'green',
    'green', 
    'green',
    'green', 
    'green',
    'black', 
    'red',
    'red', 
    'red',
    'white'
]

def play():
    init_money = 1000
    win_money = 0
    money = init_money + win_money
    try:
        rounds = int(input("How much rounds do you want to play? "))
    except UnboundLocalError:
        print("Not a valid number. You can try again after restarting")
        return 0
    except ValueError:
        print("Not a valid number. You can try again after restarting")
        return 0
    
    index = 0
    while index < rounds:
        index += 1
        try:
            wager = int(input(f"How much money do you want to wager? You have {money} gold pieces. You lose at {init_money / 2} gold pieces. You played {index - 1} / {rounds} times. "))
        except UnboundLocalError:
            index -= 1
            continue
        except ValueError:
            index -= 1
            continue

        marble_color = marbles[random.randrange(0, 10)]
        print(f"You got a {marble_color} marble.")

        if marble_color == 'green':
            win_money += wager
        elif marble_color == 'red':
            win_money -= wager
        elif marble_color == 'black':
            win_money += 10*wager
        elif marble_color == 'white':
            win_money -= 5*wager

        money = init_money + win_money

        if money <= init_money / 2:
            print(f"Sorry you lose. You only have {money} goldpieces left.")
            break

    print(f"You played {index} / {rounds} times.")
    if win_money < 0:
        print(f"Thank you for playing. You lost {win_money * -1} gold pieces. You have {money} gold pieces now.")
    else:
        print(f"Thank you for playing. You won {win_money} gold pieces. You have {money} gold pieces now.")

play()    