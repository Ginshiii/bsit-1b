# Initialize the sum to 0
total_sum = 0

# Ask the user to input 10 random numbers
print("Please input 10 random numbers:")

# Loop to get 10 numbers from the user
for i in range(10):
    # Get each number from the user
    number = float(input(f"Enter number {i + 1}: "))
    # Add the number to the total sum
    total_sum += number

# Display the total sum
print("The sum of all the numbers is:", total_sum)