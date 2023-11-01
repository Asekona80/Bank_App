# File names for data storage
bank_data_file = "Bank_Data.txt"
transaction_log_file = "Transaction_log.txt"

# Function to display the current balance
def display_balance():
    print(f"Current Balance: R{balance:.2f}")

# Function to make a deposit
def make_deposit(amount):
    global balance
    balance += amount
    with open(transaction_log_file, "a") as transaction_file:
        transaction_file.write(f"Deposit: +R{amount:.2f}\n")
    display_balance()

# Function to make a withdrawal
def make_withdrawal(amount):
    global balance
    if amount <= balance:
        balance -= amount
        with open(transaction_log_file, "a") as transaction_file:
            transaction_file.write(f"Withdrawal: -R{amount:.2f}\n")
        display_balance()
    else:
        print("Insufficient funds. Withdrawal canceled.")

# Initialize account balance in Rands
balance = 0.0

# Main application loop
while True:
    print("Would you like to make a transaction? (Yes or No)")
    choice = input().strip().lower()

    if choice == "no":
        break
    elif choice == "yes":
        print("Would you like to make a deposit or withdrawal? (Deposit or Withdrawal)")
        transaction_type = input().strip().lower()

        if transaction_type == "deposit":
            display_balance()
            print("How much would you like to deposit in Rands?")
            try:
                amount = float(input())
                if amount > 0:
                    make_deposit(amount)
                else:
                    print("Invalid deposit amount.")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        elif transaction_type == "withdrawal":
            display_balance()
            print("How much would you like to withdraw in Rands?")
            try:
                amount = float(input())
                if amount > 0:
                    make_withdrawal(amount)
                else:
                    print("Invalid withdrawal amount.")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        else:
            print("Invalid transaction type.")
    else:
        print("Invalid choice. Please enter 'Yes' or 'No.")

# Display transaction history from the text file
print("Transaction_log.txt:")
with open(transaction_log_file, "r") as transaction_file:
    transaction_history = transaction_file.read()
    print(transaction_history)
# Display the final balance
display_balance()
