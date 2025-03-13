def addition(fnum, snum):
    return fnum + snum

def subtraction(fnum, snum):
    return fnum - snum

def multiplication(fnum, snum):
    return fnum * snum

def division(fnum, snum):
    if snum == 0:
        return "Error! Division by zero is not allowed."
    return fnum / snum

print("Welcome To \"Basic Calculator\" ")
while True:
    print("""
  The Operations in calculator are: 
  =========================================
  1. Addition
  2. Subtraction
  3. Multiplication
  4. Division
  5. Exit""")

    User_Choice = input("Select The Operation You Want To Perform (1/2/3/4/5): ")

    # Check if User_Choice is a valid digit
    if not User_Choice.isdigit():
        print("Invalid Input, please select the operation again correctly.")
        continue

    User_Choice = int(User_Choice)

    # If user chooses to exit
    if User_Choice == 5:
        print("Exiting, Goodbye!")
        break

    if User_Choice not in [1, 2, 3, 4]:
        print("Invalid Choice, please try again.")
        continue

    # Get user input for numbers
    Num1 = input("Enter First Number: ")
    Num2 = input("Enter Second Number: ")

    # Validate numeric input (allowing floats)
    if not Num1.replace('.', '', 1).isdigit() or not Num2.replace('.', '', 1).isdigit():
        print("Invalid Input, please enter two numeric values correctly.")
        continue

    # Convert to float after validation
    Num1 = float(Num1)
    Num2 = float(Num2)

    # Perform the selected operation
    if User_Choice == 1:
        print(f"{Num1} + {Num2} = {addition(Num1, Num2)}")
    elif User_Choice == 2:
        print(f"{Num1} - {Num2} = {subtraction(Num1, Num2)}")
    elif User_Choice == 3:
        print(f"{Num1} * {Num2} = {multiplication(Num1, Num2)}")
    elif User_Choice == 4:
        print(f"{Num1} / {Num2} = {division(Num1, Num2)}")

    # Ask if the user wants to perform another calculation
    another = input("Do you want to perform another calculation? (y/n): ").strip().lower()
    if another == 'y':
      print("==================================================")
      continue
    else:
        print("Thank you for using the calculator. Goodbye!")
        break
