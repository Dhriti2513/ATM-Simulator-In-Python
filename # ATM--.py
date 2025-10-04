 # ATM Simulation
name = "Dhriti"
ac_no = 131625
pin_code = "9505"
bal = 16000
locked = False
transaction_history = []

print("Welcome", name)

max_attempts = 3
attempts = 0

while attempts < max_attempts:
    entered_pin = input("Enter Your Pin: ")

    if entered_pin == pin_code:
        print("\n✅ Login Successful!")
        print("Available Options:")
        print("B - Check Balance")
        print("W - Withdraw")
        print("D - Deposit")
        print("C - Change Pin")
        print("N - Update Name")
        print("V - View Profile")
        print("T - Transaction History")
        print("L - Lock Account")
        print("U - Unlock Account")
        print("E - Exit")

        while True:
            option = input("\nEnter your next choice (or E to exit): ").upper()

            if locked and option in ["W", "D", "C"]:
                print("🔒 Account is locked. Unlock to proceed.")
                continue

            if option == "B":
                print("Current Balance:", bal)

            elif option == "W":
                amount = int(input("Enter Withdrawal Amount: "))
                if amount <= bal:
                    bal -= amount
                    transaction_history.append(f"Withdrawn ₹{amount}")
                    if len(transaction_history) > 5:
                        transaction_history.pop(0)
                    print("Withdraw Success")
                    print("Updated Balance:", bal)
                    if bal < 500:
                        print("⚠️ Warning: Your balance is below ₹500.")
                else:
                    print("Insufficient Balance")

            elif option == "D":
                amount = int(input("Enter Deposit Amount: "))
                bal += amount
                transaction_history.append(f"Deposited ₹{amount}")
                if len(transaction_history) > 5:
                    transaction_history.pop(0)
                print("Deposit Success")
                print("Updated Balance:", bal)

            elif option == "C":
                current_pin = input("Enter Your Current Pin: ")
                if current_pin == pin_code:
                    new_pin = input("Enter New Pin: ")
                    pin_code = new_pin
                    print("Pin Changed Successfully")
                else:
                    print("Invalid Current Pin")

            elif option == "N":
                new_name = input("Enter New Name: ")
                name = new_name
                print("Name Updated Successfully")

            elif option == "V":
                print(f"\nWelcome {name}")
                print(f"Your Account No: {ac_no}")
                print(f"Your Current Balance: ₹{bal}")
                print("Thanks for using ATM")

            elif option == "T":
                print("\nLast 5 Transactions:")
                if transaction_history:
                    for txn in transaction_history:
                        print("-", txn)
                else:
                    print("No transactions yet.")

            elif option == "L":
                locked = True
                print("🔒 Account Locked. Transactions disabled.")

            elif option == "U":
                locked = False
                print("🔓 Account Unlocked. You may proceed.")

            elif option == "E":
                print("Thanks for using ATM")
                break

            else:
                print("Enter a Valid Option")

        break  # Exit PIN loop after successful session

    else:
        attempts += 1
        print("Invalid Pin")

else:
    print("Three attempts done, Your ATM is Blocked")
    print("Bye, Contact Your Branch")