class Ticket(object):
    count = 0
    
    #code for the ticket number, incremental every time one is created
    def TicketNumber(self):
        self.ticketnumber = tn
        tn=2000
        tn+=1
        pass
    
 # Main code for the ticket
    def Tickets():
        self.name = input("Please enter your name: ")
        self.StaffID = input ("Please enter your StaffID: ")
        self.Email = input ("Please enter your Email: ")
        print('If you require a new password, type Password Change')
        Ticket.count += 1
        self.problem = input ("Please describe the problem: ")
        if self.problem == "Password Change" or "password change" or "Password change":
            password = self.StaffID[0:2]+self.name[0:3]
            print ("Your new password is: ", password)
        else:
            default = "Response: Not Yet Provided"
            print (default)

        self.question = input("Do you have another problem to submit: Y/N   ")
        if self.question == "Y" or "y" or "yes" or "Yes":
            Ticket()
        else:
            Menu()
   


        def __enter__(self):
            return self
        def __exit__(self):
            return  self

        def __str__(self):
            return str(self.Ticket) + ": " + str(self.__dict__)

       #Writing the input file to a txt file
        with open("t.txt", "w") as f:
            f.write("Ticket number: ", tn, "\n")
            f.write("Thank you:", self.name)
            f.write("Your Staff ID is ", self.StaffID)
            f.write("Your email address is", self.Email)
            f.write("Description of the problem", self.problem)
            f.write("Response", default)
            f.write("Ticket Status:", )


    def displayTicket (self):
        with open('t.txt', 'w') as f:
            f.write("t")
            f.write("Ticket number: ", Ticket.count)
            f.write("Thank you:", self.name)
            f.write("Your Staff ID is ", self.StaffID)
            f.write("Your email address is", self.Email)
            f.write("Description of the problem", self.problem)
            f.write("Response", default)
            f.write("Ticket Status:",  )

    def stats (self):
        self.r = Resolved
        self.o = Opened
        self.c = Closed


class Count:
    pass


def Stats ("TicketNumber", "Resolved", "Open", "Closed")
       if ticket is finish == "Closed"
           print("Ticket is closed")
        if ticket is closed == "Resolved"
            #print("Ticket is resolved")
        else:
            print ("Open")

        Count ( "Open", "Resolved", "Closed")
            #print (count)

