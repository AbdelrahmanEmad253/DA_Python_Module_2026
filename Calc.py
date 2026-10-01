# **Core Execution & Flow**

# * The program must run continuously in an infinite loop, resetting to the main menu after every completed calculation or 
# user error.
# * The program must terminate only when the user types the word `quit` (case-insensitive) as the operation choice, 
# printing an exit message before closing.

# **User Inputs & Validation**

# * Display a menu header and prompt the user to input an operation choice: `+`, `-`, `*`, `/`, or `quit`.
# * If the user enters an unrecognized symbol or word, display an "invalid operation" error message and restart the loop.
# * Once a valid math operator is chosen, prompt the user to sequentially enter a "first number" and a "second number".
# * The system must parse these numbers as floating-point decimals to support both whole numbers and fractions.
# * Implement `try/except` error handling on the number inputs: if a user types letters or symbols instead of digits, 
# catch the error to prevent a crash, display a specific invalid input warning, and return to the start of the loop.

# **Calculations & Output**

# * Execute the mathematical operation corresponding to the selected symbol.
# * Format the output to display the entire equation, not just the answer (e.g., `Result: 5.0 + 3.0 = 8.0`).
# * Include specific logic for division: verify the second number is not `0` before calculating. If it is `0`, 
# bypass the calculation and print a "Cannot divide by zero" error message.



while True:
    print("\n--- Basic Python Calculator ---")
    print("Options: +, -, *, /  (or type 'quit' to exit)")
    
    # 1. Get the operation choice
    choice = input("Choose an operation: ")

    # 2. Check if the user wants to quit
    if choice.lower() == 'quit':
        print("Exiting calculator...")
        break

    # 3. Verify the choice is a valid math operator
    if choice in ('+', '-', '*', '/'):
        
        # 4. Safely capture the numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numerical digits.")
            continue

        # 5. Perform the calculation based on the choice
        if choice == '+':
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif choice == '-':
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif choice == '*':
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif choice == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
    else:
        print("Invalid operation. Please select +, -, *, or /.")