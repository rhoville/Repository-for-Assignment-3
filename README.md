# Repository-for-Assignment-3
Loved Codes
Repository found in:
https://github.com/rhoville/Repository-for-Assignment-3.git

This is one of the codes I used in my software project in making a ticket in a Help Desk.

    def Ticket():
        self.name = input("Please enter your name: ")
        self.StaffID = input ("Please enter your StaffID: ")
        self.EmailEmail = input ("Please enter your Email: ")
        print('If you require a new password, type Password Change')
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

The code works just that I need to save the input data to an empty dictionary...


This is an example of how to use a dict(), however, I have no idea how to include this to my project

x = dict(name = "John", age = 36, country = "Norway")

I then found a way to write code in an empty .txt file
It saves the input data, however, the challenge is displaying the input data to another file

Code looks like this:

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

It work on the first line, noted that writing "\n" is the command that says continue writing the rest of the inputs.
