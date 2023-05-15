class Atm:
    # constructor(special function don't need to call constructor)
    def __init__(self):
        self.pin = ' '
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""Hi,How can i help you
        1. Press 1 to create PIN
        2. PRess 2 to change PIN
        3. Press 3 to check Balance
        4. Press 4 to Withdraw
        5. Anything ealse to exit
        """)
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.chack_balance()
        elif user_input == '4':
            self.withdraw()
        else:
            exit()

    def create_pin(self):
        user_pin = input('Enter your pin ')
        self.pin = user_pin

        user_balance = int(input('Enter balance '))
        self.balance = user_balance
        print('pin created succesfully')
        self.menu()

    def change_pin(self):
        old_pin = input('Enter old pin ')
        if old_pin == self.pin:
            # let him change
            new_pin = input('Enter new pin ')
            self.pin = new_pin
            print('Pin change succesfully')
            self.menu()
        else:
            print("Pin cann't change")
            self.menu()

    def chack_balance(self):
        user_pin = input('Enter your pin ')
        if user_pin == self.pin:
            print('your balance is', self.balance)
        else:
            print('Please! create account first')
            self.menu()

    def withdraw(self):
        user_pin = input('Enter your pin ')
        if user_pin == self.pin:
            # allow to withdraw
            amount = int(input('Enter the amount'))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print('withdraw successful. Balance is ', self.balance)
            else:
                print('No money')
        else:
            print('Wasted')
        self.menu


obj = Atm()
