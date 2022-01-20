class bank:

    def __init__(self,accno,name,acctype,bal):
        self.ano = accno
        self.name = name
        self.acct = acctype
        self.balance = bal

    def deposit(self):
        depo = float(input("Enter amount to deposit"))
        self.balance += depo
        print("RS {} is CREDITED to your account\nAVL BALANCE IS:{}\n".format(depo,self.balance))

    def withdraw(self):
        draw = float(input("Enter amount to withdraw"))
        self.balance -= draw
        print("RS {} is withdrawed from your account\nAVL BALANCE IS:{}\n".format(draw,self.balance))

    def show(self):
        print("Accoubt number:",self.ano)
        print("User name:",self.name)
        print("Account type:",self.acct)
        print("Balance:",self.balance)
        print(" ")

print("******Initialize your bank account******\n")
accno = int(input("Enter your account number:"))
username = input("Enter account holder name:").title()
acct = input("Enter your account type:").upper()
balance = float(input("Enter your total balance:\n"))

ob = bank(accno,username,acct,balance)

while(1):
    
    print("\n_________________MENU_________________\n")
    print("Enter a option from following:")    
    ch = int(input("1.DEPOSITE\n2.WITHDRAW\n3.VIEW ACCOUNT DETAILS\n4.EXIT"))
    if ch == 1:
        ob.deposit()
    elif ch == 2:
        ob.withdraw()
    elif ch == 3:
        ob.show()
    elif ch == 4:
        print("EXITING...")
        exit()
    else:
        print("Enter a valid option") 

