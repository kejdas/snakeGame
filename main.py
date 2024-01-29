import random

MIN_LINES = 1
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def chech_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symobols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symobols)
            current_symobols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()

def deposit():
    while True:
        amount = input("How much $ would u like to depsit? ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Ammount must be grater than 0!")
        else:
            print("You can only pass positive numbers!")
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"How much lines would u like to display? ({MIN_LINES} - {MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if MIN_LINES <= lines <= MAX_LINES:
                break
            else:
                print(f"Lines must be in range ({MIN_LINES} - {MAX_LINES}): ")
        else:
            print("Please enter number")
    return lines

def get_bet():
    while True:
        bet = input(f"How much money would u like to bet on each line? ({MIN_BET}$ - {MAX_BET}$): ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Lines must be in range ({MIN_BET}$ - {MAX_BET}$): ")
        else:
            print("Please enter number")
    return bet

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You can not afford for that move! Your current balance is: {balance}$")
        else:
            break

    print(f"You are betting {bet}$ on {lines} lines. Total bet is: {total_bet}$")

    slots = get_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winning, winning_lines = chech_winnings(slots, lines, bet, symbol_value)
    print(f"You won {winning}$!")
    print(f"You won on lines: ", *winning_lines)

    return  winning - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Your current balance is {balance}$")
        if balance == 0:
            print("You lost everything, good job F00l!")
            break
        answer = input("Press enter to play (q to quit)")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with {balance}")

if __name__ == '__main__':
    main()