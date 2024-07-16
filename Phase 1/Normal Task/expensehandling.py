from colorama import Fore, Back, Style
# print(Back.BLACK + Style.NORMAL)
# print("\033[1;31;40m Bright Green \n")
print(Fore.LIGHTRED_EX + "WELCOME TO EXPENSE MANAGEMENT PROGRAM!".center(175))

class expense_app:
    def __init__(self):
        self.users = []
        self.expenses = []


    def add_user(self, name):
        if name not in self.users:
            self.users.append(name)
            print(f'User {name} has been added')
        else:
            print(f'User {name} exists')

    def add_expense(self, payer, sum, members):
        if payer not in self.users:
            print(f'User {payer} does not exist')
            return


        for member in members:
            if member not in self.users:
                print(f'user {member} does not exist')
                return

        expense = { 'payer': payer,
                    'sum' : sum,
                    'members' : members}
        self.expenses.append(expense)
        print(f"Expense added: {payer} paid {sum} for {', '.join(members)}.")

    def bill_splitting(self):
        balances = {user: 0 for user in self.users}

        for expense in self.expenses:
            payer = expense['payer']
            sum = expense['sum']
            members = expense['members']
            sum_split = sum/len(members)

            for member in members:
                if member != payer:
                    balances[member] -= sum_split
                    balances[payer] += sum_split

        return balances

    def disp_balance(self):
        balances = self.bill_splitting()
        print(("\n Current Balance:\t"))
        for user, balance in balances.items():
            print(f'{user}: {balance:.2f} rupees')
        print("")

def main():
    exp_app = expense_app()

    while True:
        # print("\nWelcome to Expense Management App\n")
        print(Fore.LIGHTYELLOW_EX + '1. Add User'.center(175))
        print('2. Add Expense'.center(177))
        print('3. Display remaining Balance'.center(191))
        print('4. Exit'.center(171))

        a = int(input("\n\nWhat would you like to do?(use numbers only): "))
        if a == 1:
            name = input("What is your name?: ")
            exp_app.add_user(name)

        elif a == 2:
            payer = input('Who is paying?:\t ')
            sum = float(input(f"Amount of money {payer} is paying?:\t"))
            members = input(f'Who is {payer} paying for?(use commas):\t ').split(',')
            members = [m.strip() for m in members]
            exp_app.add_expense(payer, sum, members)
        elif a == 3:
            exp_app.disp_balance()
        elif a == 4:
            print("Exiting the program...")
            break
        else:
            print("ERROR : Invalid option selected")


if __name__ == "__main__":
    main()
