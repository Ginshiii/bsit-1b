total_sum = 0  

while True:
    # Ask the user for input
    number = int(input("Enter a number (or 0 to stop): "))
    
    if number == 0:
        break  
    
    total_sum += number  # Add the number to the total sum

# Output the total sum
print("The total sum is:", total_sum)