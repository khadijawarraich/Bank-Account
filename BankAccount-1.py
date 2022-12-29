# BankAccount.py
# Author: Khadija Warraich
# Date: 12/12/22

#import Transaction class
from Transaction import *

def main():
    """Display main menu and class functions based on the selected action"""

    print ('Welcome to Bank Account Application')
    print ()

    done = False

    # Create an empty list of transactions
    list_of_transactions = []

    #Loop as long as done is False
    while (not done):
        #Display menu
        print ('===================================')
        print ('A - Read data from the file')
        print ('B - Display list of transactions')
        print ('C - Add a new transaction')
        print ('D - Calculate current balance')
        print ('E - Save data to a file')
        print ('Q - Quit')
        print ('===================================')
        print ('Please select an action by typing A, B, C, D, E, or Q')
        action = input ('? ')

        if (action == 'A' or action == 'a'):
            read_data (list_of_transactions)
        elif (action == 'B' or action == 'b'):
            display_list (list_of_transactions)
        elif (action == 'C' or action == 'c'):
            add_transaction (list_of_transactions)
        elif (action == 'D' or action == 'd'):
            calculate_balance (list_of_transactions)
        elif (action == 'E' or action == 'e'):
            save_data (list_of_transactions)
        elif (action == 'Q' or action == 'q'):
            done = True
        else:
            print ('Incorrect action type. Please try again')

        print ()

    print ('Thank you for using Bank Account Application')

def read_data (list_of_transactions):
    """Read data from the input file, create transaction object and add it to
       the list of transactions"""
    print ('Read Data Function')
       # Ask user for name of the input file, read each line of the data,
    try:
        filename = input("What is the file name?")
        infile = open(filename, "r")
        for line in infile:
       # split line using colon (:) is delimiter, create transaction object
            date, transtype, amount = line.split(":")
            transaction = Transaction(date, transtype, amount)
       # and add it to the list of transaction. Display error message if the
            list_of_transactions.append(transaction)
        infile.close()
       # input file is not found.
    except FileNotFoundError as err:
        print("File not found. Input valid file.")

def display_list (list_of_transactions):
   """ Displays list of transactions """
   # Sort the list of transactions by date and display list of transactions
   # in form of a table
   print ('Display List Function')
   list_of_transactions.sort(key=Transaction.get_date)
   for data in list_of_transactions:
       print(data.get_date()," ",data.get_transaction_type()," ",data.get_amount())
   
def add_transaction (list_of_transactions):
    """Adds a new transaction to list of Transactions"""
    print ('Add Transaction Function')
    # Ask user for date, type, and amount of transaction, create a transaction
    # object and append it to the list of transactions.
    userdate = input("Enter the date:")
    usertranstype = input("Enter transaction type:")
    useramount = float(input("Enter amount:"))
    # Display an error message if the transaction type is not valid or amount
    # is negative. Valid transaction types are deposit, withdraw, bank charge
    # and interest
    if usertranstype != "deposit" and usertranstype != "withdraw" and usertranstype != "bank charge" and usertranstype != "interest":
        print("Transaction type not a valid type")
    elif useramount < 0:
        print("Amount is negative. Error")
    else:
        usertransaction = Transaction(userdate, usertranstype, useramount)
        list_of_transactions.append(usertransaction)

def calculate_balance (list_of_transactions):
    """Calculates the current balance"""
    print ('Calculate Balance Function')
    # Start with initializing balance to zero
    balance = 0.0
    # For each transaction in the list of transactions you will
    for i in list_of_transactions:
    # add the amount to balance if the transaction type is deposit or interest
        if i.get_transaction_type() == "deposit" or i.get_transaction_type() == "interest":
            balance += float(i.get_amount())
    # subtract the amount if transaction type is withdraw or bank charge
        elif i.get_transaction_type() == "withdraw" or i.get_transaction_type() == "bank charge":
            balance -= float(i.get_amount())
        
    # Print the balance on the screen
    print("Your balance is: ", balance)
    
def save_data (list_of_transactions):
    """ Saves list of transaction to a file"""
    print ('Save Data Function')
    # Ask user for name of the output file, sort the list of transactions by date
    outfilename = input("Enter the name of the output file")
    outfile = open(outfilename, "w")
    # and save the data using the following format:
    # date:transaction_type:amount
    list_of_transactions.sort(key=Transaction.get_date)
    for form in list_of_transactions:
        print("{0}:{1}:{2:.3f}".format(form.get_date(),form.get_transaction_type(),float(form.get_amount())), file = outfile)
    # Display a message that data was saved to the output file.
    print("Data saved to", outfilename,".")
    
            
