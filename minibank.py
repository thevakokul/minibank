def customer_menu():
    while True:
        print("\n================ Welcome to the Mini Bank Customer Menu =================")
        print("1. Deposit Money.")
        print("2. Withdraw Money.")
        print("3. Check Balance.")
        print("4. Transaction History.")
        print("5. Exit.")

        choice = input("Select your option:")  
        if choice == "1":
            deposit()  
        elif choice == "2":
            withdraw()
        elif choice == "3":
            check_balance()
        elif choice == "4":
            transaction()
        elif choice == "5":
            break  
        else:
            print("Invalid option. Please try again.")



def admin_menu():
    while True:
        print("\n==========Welcome to the mini bank Admin Menu==========")
        print("===========select your option===========")

        print("1. Create Account.")
        print("2. Deposit Money.")
        print("3. Withdraw Money.")
        print("4. Check Balance.")
        print("5. Transaction History.")
        print("6. Exit.")

        choice = input("Select your option: ")  

        if choice == "1":
            Create_Account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            transaction()
        elif choice == "6":
            break  
            print("Thankyou very much","Have a nice day")
        else:
            print("Invalid option. Please try again.")




users={"kokul":["abc",500],
"kevin":["def",1000],
"kobi":["xyz",1500]}

def get_customer_info():
    username = input("Enter your username: ")
    user_password = input("Enter your password: ")
    other_name = input("Enter your surname: ")
    address = input("Enter your address: ")
    gender = input("Enter your gender: ")
    phone_number = input("Enter a valid phone number: ")  

    customers=[username, address, user_password, phone_number, gender, other_name]  
    


    with open("users.txt", "a") as file:
        file.write(f"{customers[0]},{customers[1]}\n")  

    with open("customers.txt", "a") as file:
        file.write(f"{customers[2]},{customers[3]},{customers[4]},{customers[5]}\n")  


def register():
    print("\n=====Register=====")
    user_name = input("enter a user name:")
    if user_name in users:
        print("Sorry,user name already exists.")
    else:
        password = input("creat a password:")
        users[user_name]=[password,0.0]

def admin_info():
    admin_u_name = "admin123"  
    admin_p_word = "12345"  

    return [admin_u_name, admin_p_word]


admin_details = admin_info()


with open("admin_p_code.txt", "a") as file:
    file.write(f"{admin_details[0]},{admin_details[1]}\n")  


def login():
    while True:
        global user_account
        print('1.Admin Login'.center(100))
        print('2.customer login'.center(100))
        print('3.Exit'.center(100))
        choice=input('choose login type:').strip()
        if choice=='1':
            admin_username=input('\nEnter Admin username:').strip()
            admin_password=input('enter Admin password:').strip()
       
            if admin_username == "admin123" and admin_password == "12345":
                print('\n==========Admin login successfully===========')
                admin_menu()
            else:
                print('Sorry,Incorrect username or password')
                print('===========invalid admin user============')
              
        elif choice == '2':
            try:
                user__account=int(input('\nenter your account number:'))
                password=input('enter your password:').strip()
                if user__account in accounts[user_account]and['password'] == password:
                    print('=============customer login successful===============')
                    return user_account,customer_menu()
                else:
                    print('============invalid referance============')
            except ValueError:
                print('\n=============invalid input===========')
        elif choice=='3':
            break
        else:
            print('\n==================invalid choice===============')

def Create_Account():
    print("\n=====Create_Account=====\n")
    get_customer_info()

    Account_Holder_Name = input(f"\n{'Enter Account Holder Name' :<25} :")
    User_Name = input(f"{'Enter User Name' :<50} :")
    User_Password = input(f"{'Enter User Password' :<50} :")
    balance = float(input(f"{'Enter Initial Balance' :<50} :"))
    Phone_number = input(f"{'Enter phone number' :<50} :")
    Address=input(f"{'Enter the Address' :<50} :")

    try:
        with open("Acc_No.txt", 'r') as file:
            last = file.read().strip()
            new = int(last[3:]) + 1
    except FileNotFoundError:
        new = 1

    Account_Number = "ACC" + str(new).zfill(3)
    user_ID = "U_ID" + str(new).zfill(4)


    with open("Acc_No.txt", 'w') as file:
        file.write(Account_Number)


    with open("account_Details.txt", "a") as file:
        file.write(f"{Account_Number},{User_Password},{User_Name},{balance}\n")


    with open("User_Details.txt", "a") as file:
        file.write(f"{user_ID},{User_Name},{User_Password},\n")



    print("\nAccount Created Successfully")
    print(f"\nAccount_number : {Account_Number}")
    print(f"user_ID : {user_ID}")
    print(f"Account_Holder_Name : {Account_Holder_Name}")
    print(f"User_Name : {User_Name}")
    print(f"User_Password : {User_Password}")
    print(f"Balance : {balance}")
    print(f"Phone_number : {Phone_number}")
    print(f"Address : {Address}")

    from datetime import datetime
    date_time_now = datetime.now()

    with open("Transaction_Details.txt", "a") as file:
        file.write(f"{date_time_now},{Account_Number} ,withdraw,{balance},{balance},\n")

# Create_Account()







from datetime import datetime
date_time_ = datetime.now()
print(date_time_)


def deposit():
    global balance
    global accounts
    account_number=print("enter your account number:")
    if account_number in accounts:
        print("Your account number is:",[account_number])
        deposite_amount= int(input("enter your deposite amount"))
    if deposite_amount <= 0:
        print("ERROR","Amount must be in positive number")
    else:
        print("amount sucuessfully deposited")
        new_balance = balance + deposite_amount
        print(new_balance)
       
 




def withdraw():
    global balance
    global accounts
    acc_num = input("Enter your account number: ")
    if acc_num in accounts:
        print("Your account number is:", acc_num)
    else:
        print("Sorry, account number not found")
        return  
    
    try:
        withdraw_amount = int(input("Enter your withdraw amount: ")) 
    except ValueError:
        print("ERROR: Please enter a valid number")
        return

    if withdraw_amount <= 0:
        print("ERROR: Amount must be a positive number")
        return
    elif withdraw_amount > balance:  
        print("Sorry, insufficient balance")
        return
    else:
        balance -= withdraw_amount
        print("Amount successfully withdrawn")
        print("Your Remaining balance is:", balance)




def check_balance():
    global balance
    global accounts
    
    print("\n======== Check Balance =========")
    account_number = input("Enter your account number: ")

    if account_number in accounts:
        print("Your balance is:",balance, accounts[account_number])  
        print("======Thankyou====")
    else:
        print("Account number not identified")






def transaction_history():
    global accounts
    print("\n==========Transaction History==========")
    account_number = input("enter your account number")
    if account_number in accounts :
        print("=========Your Account is found=========")
        print("your account number is:",account_number)
    else:
        print("Sorry,Account number not found")


login()