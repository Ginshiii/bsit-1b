#code challenge7 ni tamad
def calculate_change():
    # Input values
    name = input("Enter your name: ")
    grocery_purchase = input("Did you purchase a grocery today (Y/N): ").strip().upper()
    
    if grocery_purchase == 'Y':
        item_name = input("What did you purchase: ")
        item_price = float(input("Item Price: "))
        age = int(input("Age: "))
        payment = float(input("Payment: "))
        
        # Constants
        tax_rate = 0.123  # 12.3%
        discount_rate = 0.038  # 3.8%
        discount_threshold = 4000  # threshold for discount
        senior_age_threshold = 60  # age for senior discount

        # Calculate taxed price
        taxed_price = item_price + (item_price * tax_rate)

        # Check for discount eligibility
        if item_price > discount_threshold:
            discount = item_price * discount_rate
            final_price = taxed_price - discount
        else:
            final_price = taxed_price

        # Check for senior discount
        if age > senior_age_threshold:
            senior_discount = final_price * tax_rate  # 12.3% of taxed price
            final_price -= senior_discount

        # Calculate change
        change = payment - final_price

        # Output results
        print(f"\nReceipt for {name}:")
        print(f"Item: {item_name}")
        print(f"Item Price (untaxed): {item_price:.2f}")
        print(f"Taxed Price: {taxed_price:.2f}")
        print(f"Final Price after discounts: {final_price:.2f}")
        print(f"Change due: {change:.2f}")

    else:
        print("No grocery purchased.")
