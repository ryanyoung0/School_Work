# Ryan Young
# CSE 4701
# Project #2
# Dong SHIN
import pymysql.cursors
import time


def Format_Output():
    print("Main Menu")
    print("1 - Create Account")
    print("2 - Check Balance")
    print("3 - Deposit")
    print("4 - Withdraw")
    print("5 - Transfer")
    print("0 - Quit")


def Create_Connection():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='MikeLuu=69',
                                 db='cse4701s20_project2',
                                 charset='latin1',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection


def Create_Account(connection):
    User_Name = input("Name on account: ")
    Balance = int(input("Enter Initial Balance: "))
    # Do some mysql stuff
    with connection.cursor() as cursor:
        # Create a new Account
        sql = "insert into account (name_on_account, balance) VALUES('%s', %d);" \
              % (User_Name, Balance)
        cursor.execute(sql)
    connection.commit()
    with connection.cursor() as cursor:
        sql = "select * from account where account.name_on_account = '%s';" \
              % (User_Name)
        cursor.execute(sql)
        result = cursor.fetchone()
        if result is None:
            print("--------------------------")
            print("Invalid Account Name")
            print("--------------------------")
        else:
            print("Account Number:", result['account_no'])
            print("Account Name:", result['name_on_account'])
            print("Account Balance:", result['balance'])
            print("Account Opening Date:", result['account_open_date'])
    connection.commit()


def Check_Balance(connection):
    account_no = int(input("Please Enter an account number: "))
    with connection.cursor() as cursor:
        sql = "select * from account where account_no = '%d';" \
              % (account_no)
        cursor.execute(sql)
        result = cursor.fetchone()
        if result is None:
            print("--------------------------")
            print("Invalid Account Number")
            print("--------------------------")
        else:
            print("-----Checking Your Balance-----")
            print("Account Number:", result['account_no'])
            print("Account Name:", result['name_on_account'])
            print("Account Balance:", result['balance'])
            print("Account Opening Date:", result['account_open_date'])
            print("--------------------------")
        connection.commit()


def Deposit(connection):
    account_no = int(input("Please enter an account number: "))
    # need to now pull account information
    # lock the account with the for update part
    # from the table and print it
    with connection.cursor() as cursor:
        sql = "select * from account where account.account_no = %s for update;" \
              % (account_no)
        cursor.execute(sql)
        result = cursor.fetchone()
        if result is None:
            print("--------------------------")
            print("Invalid Account Number")
            print("--------------------------")
            connection.commit()
        else:
            print("-----Existing Account Balance-----")
            print("Account Number:", result['account_no'])
            print("Account Name:", result['name_on_account'])
            print("Account Balance:", result['balance'])
            print("Account Opening Date:", result['account_open_date'])
            # asking teller how much to deposit and doing it
            deposit_amount = int(input("Please enter deposit amount: "))
            new_balance = deposit_amount + result['balance']
            sql = "update account set balance = %d where account_no = %s;" \
                  % (new_balance, account_no)
            cursor.execute(sql)
            sql = "select * from account where account.account_no = %s;" \
                  % (account_no)
            cursor.execute(sql)
            result = cursor.fetchone()
            print("-----New Account Balance-----")
            print("Account Number:", result['account_no'])
            print("Account Name:", result['name_on_account'])
            print("Account Balance:", result['balance'])
            print("Account Opening Date:",
                  result['account_open_date'])
            print("--------------------------")
            connection.commit()


def Withdraw(connection):
    account_no = int(input("Please enter an account number: "))
    # need to now pull account information
    # lock the account with the for update part
    # from the table and print it
    with connection.cursor() as cursor:
        sql = "select * from account where account.account_no = %s for update;" \
              % (account_no)
        cursor.execute(sql)
        result = cursor.fetchone()
        if result is None:
            print("--------------------------")
            print("Invalid Account Number")
            print("--------------------------")
            connection.commit()
        else:
            print("-----Existing Account Balance-----")
            print("Account Number:", result['account_no'])
            print("Account Name:", result['name_on_account'])
            print("Account Balance:", result['balance'])
            print("Account Opening Date:", result['account_open_date'])
            print("--------------------------")
            # asking teller how much to withdraw and doing it
            withdraw_amount = int(input("Please enter withdraw amount: "))
            new_balance = result['balance'] - withdraw_amount
            if withdraw_amount > result['balance']:
                print("Insufficient Funds")
                connection.commit()
            else:
                sql = "update account set balance = %d where account_no = %s;" \
                      % (new_balance, account_no)
                cursor.execute(sql)
                sql = "select * from account where account.account_no = %s;" \
                      % (account_no)
                cursor.execute(sql)
                result = cursor.fetchone()
                print("-----New Account Balance-----")
                print("Account Number:", result['account_no'])
                print("Account Name:", result['name_on_account'])
                print("Account Balance:", result['balance'])
                print("Account Opening Date:",
                      result['account_open_date'])
                print("--------------------------")
                connection.commit()


def Transfer(connection):
    # GETTING SOURCE ACCOUNT
    source_account_no = int(input("Please enter source account number: "))
    with connection.cursor() as cursor:
        # Locking the account
        sql = "select * from account where account.account_no = %s for update;" \
              % (source_account_no)
        cursor.execute(sql)
        result = cursor.fetchone()
        if result is None:
            print("--------------------------")
            print("Invalid Account Number")
            print("--------------------------")
            connection.commit()
        else:
            print("-----Existing Account Balance-----")
            print("Account Number:", result['account_no'])
            print("Account Name:", result['name_on_account'])
            print("Account Balance:", result['balance'])
            print("Account Opening Date:", result['account_open_date'])
            source_balance = result['balance']
            connection.commit()
    # GETTING TARGET ACCOUNT
    target_account_no = int(input("Please enter target account number: "))
    with connection.cursor() as cursor:
        # Locking the account
        sql = "select * from account where account.account_no = %s for update;" \
              % (target_account_no)
        cursor.execute(sql)
        result = cursor.fetchone()
        if result is None:
            print("--------------------------")
            print("Invalid Account Number")
            print("--------------------------")
            connection.commit()
        else:
            print("-----Existing Account Balance-----")
            print("Account Number:", result['account_no'])
            print("Account Name:", result['name_on_account'])
            print("Account Balance:", result['balance'])
            print("Account Opening Date:", result['account_open_date'])
            target_balance = result['balance']
            connection.commit()
        # Withdrawing from source account
        transfer_amount = int(input("Please enter transfer amount amount: "))
        if transfer_amount > source_balance:
            print("Insufficnet Funds!")
            connection.commit()
        else:
            Withdraw_balance = source_balance - transfer_amount
            with connection.cursor() as cursor:
                sql = "update account set balance = %d where account_no = %s;" \
                      % (Withdraw_balance, source_account_no)
                cursor.execute(sql)
                sql = "select * from account where account.account_no = %s;" \
                      % (source_account_no)
                cursor.execute(sql)
                result = cursor.fetchone()
                print("-----New Account Balance-----")
                print("Account Number:", result['account_no'])
                print("Account Name:", result['name_on_account'])
                print("Account Balance:", result['balance'])
                print("Account Opening Date:",
                      result['account_open_date'])
                print("--------------------------")
                #time.sleep(100)
            # Depositing into target account
                Deposit_balance = transfer_amount + target_balance
                sql = "update account set balance = %d where account_no = %s;" \
                      % (Deposit_balance, target_account_no)
                cursor.execute(sql)
                sql = "select * from account where account.account_no = %s;" \
                      % (target_account_no)
                cursor.execute(sql)
                result = cursor.fetchone()
                print("-----New Account Balance-----")
                print("Account Number:", result['account_no'])
                print("Account Name:", result['name_on_account'])
                print("Account Balance:", result['balance'])
                print("Account Opening Date:",
                      result['account_open_date'])
                print("--------------------------")
            connection.commit()



def main():
    # initial Setup and getting choice from user
    while True:
        Format_Output()
        User_Choice = int(input("Enter Your Choice: "))
        # Connection to DB
        connection = Create_Connection()
        # Exit Option
        if User_Choice == 0:
            print("Good Bye")
            break
        # Create Account Option
        elif User_Choice == 1:
            Create_Account(connection)
        # Check Balance Option
        elif User_Choice == 2:
            Check_Balance(connection)
        # Deposit Option
        elif User_Choice == 3:
            Deposit(connection)
        # Withdraw Option
        elif User_Choice == 4:
            Withdraw(connection)
        # Transfer Option
        elif User_Choice == 5:
            Transfer(connection)


main()
