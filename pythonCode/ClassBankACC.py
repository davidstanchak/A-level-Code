class Bank:
    __bankAccounts = {"Samantha Hey":"000001"}
    def __init__(self, accountName, accountNumber):
        self.__bankAccounts = dict(self.__bankAccounts, accountName=accountNumber)
    
    def getAccount(self, bankAccounts):
        return bankAccounts.get("Bob Shni")



myName = input("Enter Name")
myAccNum = input("Enter acc number")
newAccount = Bank(myName, myAccNum)
print(Bank.getAccount())

