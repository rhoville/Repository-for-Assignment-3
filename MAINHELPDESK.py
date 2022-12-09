print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~ IT5016D - Help Desk: How May I Help You? ~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Please select from the following choices:")
from Ticket import *
from Menu import *

open(Menu())
option = int(input("Please select from 0-5:    "))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
while option!=0 :
        if option == 1:
            open(Tickets())

        if option == 2:
            print(displayTicket)

        if option == 3:
            open(Ticket.count)== input("Enter the ticket number to respond")
            response = input("Respond to ticket", Ticket.count)

        if option == 4:
            open(Ticket.count = input("Enter the ticket number to Open?")
            print("Do you want to open ticket? Y/N", input())
            if answer == "Y" or "y":
                status = "Opened"
            else:
                open(Menu())

        if option == 5:
            print (displayStatus)

        else:
            print ("Wrong input")

print("Thank you for using our Help Desk!")




