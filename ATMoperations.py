accounts = {10101:[2408,5000],20202:[6824,25000],40404:[None,1000]}
def withdraw():
    accno = int(input("Enter your Accoutn Number: "))
    if accno in accounts:
        pin = int(input("Enter Your Pin: "))
        if accounts[accno][0] == pin:
            amt = int(input("Enter Amount to widthdraw: "))
            if accounts[accno][1] >= amt:
                accounts[accno][1] -= amt
                print("withdraw Sucessfull")
            else:
                print("Insufficient Balance !")
        else:
            print("Incorrect Pin !")
    else:
        print("Account Number does not Exists !")
def deposit():
    accno = int(input("Enter your Account Number: "))
    if accno in accounts:
        pin = int(input("Enter Pin: "))
        if accounts[accno][0] == pin:
            amt = int(input("Enter amount to be deposit: "))
            accounts[accno][1] += amt
            print("Deposit Sucessfull")
            print(f"Updated Balance: Rs.{accounts[accno][1]}")
        else:
            print("Invalid pin !")
    else:
        print("Account does not Exists !")
def display():
    accno = int(input("Enter account number: "))
    if accno in accounts:
        pin = int(input("Enter your Pin: "))
        if accounts[accno][0] == pin:
            print(f"Balance: {accounts[accno][1]}")
        else:
            print("Incorrect Pin !")
    else:
        print("Account does not Exists !")
def pingenerate():
    accno = int(input("Enter Account Number: "))
    if accno in accounts:
        if accounts[accno][0] is None:
            pin1 = input("Enter 4 digit Pin: ")
            if len(pin1) == 4:
                pin2 = input("Enter pin once again: ")
                if pin1 == pin2:
                    accounts[accno][0] = int(pin1)
                    print("Pin generation sucessfull !")
                else:
                    print("Confirmation Unsucessfull !")
            else:
                print("Enter Only 4 digit Pin !")
        else:
            print("Pin already Generated !")
    else:
        print("Account Does not Exists !")
while True:
    print("Choose Required Option")
    print("1. withdraw ")
    print("2. Deposit ")
    print("3. Check Balanace ")
    print("4. Pin Generation ")
    print("5. Exit")
    try:
        x = int(input("Enter Option Number: "))
    except:
        print("Choose the Correct option !")
    else:
        if x == 1:
            print("=========withdraw=========")
            withdraw()
        elif x == 2:
            print("=========Deposit=========")
            deposit()
        elif x == 3:
            print("=========Check balanace=========")
            display()
        elif x == 4:
            print("=========Pin Generation=========")
            pingenerate()
        elif x == 5:
            break
        else:
            print("Choose the Correct Option")