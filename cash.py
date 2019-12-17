# Prints the minimum possible ammount of coins needed to give in change
def main():
    # Prompts the user for change
    try:
        change = float(input("Change owed:"))
        while change <= 0:
            change = float(input("Change owed:"))
    except ValueError as err1:
        print(err1)
        print("Insert only float numbers!")
        main()
    # Performs the 'greedy' program
    coins = 0
    # Turns the change into cents
    cents = change * 100
    cents = int(round(cents))
    # Checks if the change is major or equal than 25 cents
    if cents >= 25:
        coins = coins + int(cents / 25)
        cents = cents % 25
        # Checks if the change is major or equal than 10 cents
    if cents >= 10:
        coins = coins + int(cents / 10)
        cents = cents % 10
    # Checks if the change is major or equal than 5 cents
    if cents >= 5:
        coins = coins + int(cents / 5)
        cents = cents % 5
    # Checks if the change is major or equal than 5 cents
    if cents >= 1:
        coins = coins + int(cents / 1)
        cents = cents % 1

    return print(coins)


if __name__ == "__main__":
    main()