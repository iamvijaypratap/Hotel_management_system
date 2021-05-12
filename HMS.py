class Hotel:
      def __init__(self ,room ,reserved):
        self.room = room
        self.reserved = reserved
      def Options (self):
        print(" * BOOKING  \n * ENQUIRY ")
      def Booking (self):
        while True:
              print(" *(1) for No Of Rooms Available : \n * (2)for No Of Rooms Reserved : \n * (3) for Book Your Room Now : \n * (4) for Main Menu :")
              choice = int(input("Enter Yor Choice : \n"))
              if choice == 1:
                 print(f" No Of Rooms Available : {self.room}")
              elif choice == 2:
                 print(f"No Of Rooms Reserved : {self.reserved}")
              elif choice == 3:
                 Name = input("Your Name : \n")
                 Number =  input("Your Contact Number : \n")
                 Rooms =  int(input("How Many Rooms To Book ?: \n"))
                 duration =  input("Stay Duration In Hours: \n")
                 print(f"Your Room is booked \n Your Name : {Name}, \n Your Number : {Number}, \n Rooms : {Rooms}, \n Stay Duration : {duration} , Have a Nice Day .... ")
                 self.room = self.room - Rooms
                 self.reserved = self.reserved + Rooms
                 with open('log.txt','a') as f:
                   f.write(f" Name = {Name},\n Contact-Number = {Number},\n Rooms = {Rooms},\n Stay-Duration = {duration} \n") 
              elif choice == 4:
                  return None
              else:
                  print("invalid choice")
      def Enquiry (self):
          search = input("Search By Name : \n")
          with open('log.txt') as f:
            query = f.read()
          if search in query.lower():
            print("Here are Details :")
            print(query)
          else:
            print("Not Found")

Hotel_Management = Hotel(100 , 0)
while True:
       welcome_msg = '''====== HOTEL MANAGEMENT SYSTEM ====== '''
       print(welcome_msg)
       Hotel_Management.Options()
       user_choice = input("Type Your Input : \n ")
       try:
           if user_choice == "booking":
              Hotel_Management.Booking()
           elif user_choice == "enquiry":
               Hotel_Management.Enquiry()
           else:
              print("Please Choose From Options")
       except Exception as e:
            print("Invalid Choice! Please Choose From Given Options")