def display_filipino_denomination(amount):
    denominations = {
        1000: "₱1000",
        500: "₱500",
        200: "₱200",
        100: "₱100",
        50: "₱50",
        20: "₱20",
        10: "₱10",
        5: "₱5",
        1: "₱1"
    }
    
    print("\nFilipino Denominations for amount ₱", amount, ":")
    
    for denom in sorted(denominations.keys(), reverse=True):
        count = amount // denom
        amount %= denom
        if count > 0:
            print(f"{denominations[denom]} x {count}")

def main():
    print("Welcome to the Bank Simulation Program!")
    
    balance = 0.0
    account_created = False

    while True:
        if not account_created:
            print("\nStep 1: Create Account")
            account_name = input("Enter your name to create an account: ")
            print(f"Account created successfully for {account_name}!")
            account_created = True

            # Initial deposit
            try:
                deposit_amount = float(input("\nPlease enter your initial deposit: ₱"))
                if deposit_amount <= 0:
                    print("Deposit amount must be greater than zero.")
                    continue

                display_filipino_denomination(deposit_amount)
                balance += deposit_amount
                print(f"₱{deposit_amount} deposited successfully. Current Balance: ₱{balance:.2f}")

            except ValueError:
                print("Invalid input! Please enter a valid number for the deposit.")
                continue

        print("\n--- Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        try:
            choice = int(input("Choose an option (1-4): "))
        except ValueError:
            print("Invalid input! Please select a valid option.")
            continue

        if choice == 1:
            try:
                deposit_amount = float(input("Enter the amount you want to deposit: ₱"))
                if deposit_amount <= 0:
                    print("Deposit amount must be greater than zero.")
                    continue

                display_filipino_denomination(deposit_amount)
                balance += deposit_amount
                print(f"₱{deposit_amount} deposited successfully. Current Balance: ₱{balance:.2f}")
            except ValueError:
                print("Invalid input! Please enter a valid number for the deposit.")

        elif choice == 2:
            try:
                withdraw_amount = float(input("Enter the amount you want to withdraw: ₱"))
                if withdraw_amount > balance:
                    print("Insufficient balance! Please enter an amount less than or equal to your current balance.")
                    continue
                elif withdraw_amount <= 0:
                    print("Withdrawal amount must be greater than zero.")
                    continue
                
                balance -= withdraw_amount
                print(f"₱{withdraw_amount} withdrawn successfully. Current Balance: ₱{balance:.2f}")
            except ValueError:
                print("Invalid input! Please enter a valid number for the withdrawal.")

        elif choice == 3:
            print(f"Current Balance: ₱{balance:.2f}")
        
        elif choice == 4:
            print("Thank you for using the Bank Simulation Program!")
            break

        else:
            print("Invalid option! Please choose a number between 1 and 4.")

if __name__ == "_main_":
    main()