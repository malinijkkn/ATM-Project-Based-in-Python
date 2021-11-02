###S.MALINI
###27.11.2021
###Modified ATM Code in Python

print('-------------------------------Welcome to SBI Bank ATM------------------------------------')
admin=input('Enter Admin Name:')
if admin== 'S.MALINI':
    restart=('Y')
    chances = 3
    Amount = int(input('Please Fill The Amount in ATM:'))
    balance=10000
    print('Thank You Admin')
else:
    print("You are Not a Admin.")  
    exit()  
    
while chances >= 0:
    user=input('you are user?(y):')
    if user in ('n','NO','no','N'):
                    print('-----Thank You-----')
                    exit()
                    break
    print("Please Inssert a Card!")
    acc_no=int(input('Please Enter the Acc No:'))
    pin = int(input('Please Enter You 4 Digit Pin: '))
    if pin == (1234):
        #restart = input('Would You you like to go back?(y/n) ')
        print('You entered you pin Correctly\n')
        while restart not in ('n','NO','no','N'):
            print('Please Press 1 For Your Balance Checking\n')
            print('Please Press 2 To Make a Withdrawl\n')
            print('Please Press 3 To Deposit in\n')
            print('Please Press 4 To Return Card\n')
            print('Please Press 5 to Exit\n')
            option = int(input('What Would you like to choose?'))
            if option == 1:
                print('Your Balance is Rs',balance,'\n')
                restart = input('Would You you like to go back?(y/n) ')
                if restart in ('n','NO','no','N'):
                    print('-----Thank You-----')
                    break
            elif option == 2:
                option2 = ('y')
                withdrawl = float(input('How Much Would you like to withdraw? : '))
                if withdrawl in range(1,10000000000):
                    balance = balance - withdrawl
                    print ('\nYour Balance is now Rs',balance)
                    restart = input('Would You you like to go back?(y/n) ')
                    if restart in ('n','NO','no','N'):
                        print('-------Thank You---------')
                        break
                elif withdrawl != range(1,100000000):
                    print('Invalid Amount, Please Re-try\n')
                    restart = ('y')
                elif withdrawl == 1:
                    withdrawl = float(input('Please Enter Desired amount:'))    

            elif option == 3:
                Deposit_in = float(input('How Much Would You Like To Deposit In?'))
                balance = balance + Deposit_in
                print ('\nYour Balance is now Rs',balance)
                restart = input('Would You you like to go back? (y/n)')
                if restart in ('n','NO','no','N'):
                    print('-----Thank You----------')
                    break
            elif option == 4:
                print('Please wait whilst your card is Returned...\n')
                print('***********************Thank you for you service*****************************')
                break
            elif option == 5:
                exit()
            else:
                print('Please Enter a correct number. \n')
                restart = ('y')
    elif pin != ('1234'):
        print('Incorrect Password')
        chances = chances - 1
        if chances == 0:
            print('\nNo more tries')
            break





def verify_pin(pin):
    if pin == '1234':
        return True
    else:
        return False

def log_in():
    tries = 0
    while tries < 4:
        pin = input('Please Enter Your 4 Digit Pin: ')
        if verify_pin(pin):
            print("Pin accepted!")
            return True
        else:
            print("Invalid pin")
            tries += 1
    print("To many incorrect tries. Could not log in")
    return False

def start_menu():
    print("Welcome to the atm!")
    if log_in():
        # you will need to make this one yourself!
        #main_menu()
        print("Exiting Program")

start_menu()