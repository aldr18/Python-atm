from decimal import Decimal, InvalidOperation

balance = Decimal("1000.00")

while True:
    print("\n--- Simple ATM Simulator ---")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choose an option (1-4): ").strip()

    if choice == "1":
        print(f"Your current balance: {balance:.2f} SAR")

    elif choice == "2" or choice == "3":
        try:
            amount = Decimal(input("Enter the amount (SAR): "))

            if not amount.is_finite() or amount <= 0:
                print("Invalid amount. Enter a number greater than zero.")
                continue

            if amount != amount.quantize(Decimal("0.01")):
                print("Please use no more than two decimal places.")
                continue

        except InvalidOperation:
            print("Invalid amount. Please enter a valid number.")
            continue

        if choice == "2":
            balance += amount
            print("Deposit successful.")

        elif amount > balance:
            print("Insufficient balance.")
            continue

        else:
            balance -= amount
            print("Withdrawal successful.")

        print(f"Your current balance: {balance:.2f} SAR")

    elif choice == "4":
        break

    else:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")

print("Thank you for using the ATM simulator.")