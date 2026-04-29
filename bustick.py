print("=================================================================")
print("               -| JOJ Bus Ticketing System |-    ")
print("=================================================================")

start_booking = "yes"

while start_booking == "yes":
    print("")
    name = input("Enter passenger name: ")

    print("")
    travel_date = input("Enter travel date (YYYY-MM-DD): ")

    print("")
    print("Available Routes:")
    print("-----------------------------------------------------------------")
    print("1. Kathmandu to Pokhara - Rs. 1000")
    print("2. Kathmandu to Chitwan - Rs. 1500")
    print("3. Kathmandu to Lumbini - Rs. 2000")
    print("4. Kathmandu to Biratnagar - Rs. 2500")
    print("5. Kathmandu to Janakpur - Rs. 3000")
    print("-----------------------------------------------------------------")
    
    choice = 0
    valid_choice = False
    while valid_choice == False:
        print("")
        choice = int(input("Select route(1-5): "))
        if choice >= 1 and choice <= 5:
            valid_choice = True
        else:
            print("Invalid route! Please select 1-5.")
            
    route_name = ""
    price = 0
    
    if choice == 1:
        route_name = "Kathmandu to Pokhara"
        price = 1000
    elif choice == 2:
        route_name = "Kathmandu to Chitwan"
        price = 1500
    elif choice == 3:
        route_name = "Kathmandu to Lumbini"
        price = 2000
    elif choice == 4:
        route_name = "Kathmandu to Biratnagar"
        price = 2500
    elif choice == 5:
        route_name = "Kathmandu to Janakpur"
        price = 3000

    passengers = 0
    valid_passengers = False
    while valid_passengers == False:
        passengers = int(input("Number of passengers: "))
        if passengers > 0 and passengers <= 10:
            valid_passengers = True
        else:
            print("Invalid number of passengers! Please enter 1-10.")

    print("")
    print("Seat Preference:")
    print("1. Window")
    print("2. Aisle")

    seat_type = ""
    valid_seat = False
    while valid_seat == False:
        seat_choice = int(input("Select seat type (1-2): "))
        if seat_choice == 1:
            seat_type = "Window"
            valid_seat = True
        elif seat_choice == 2:
            seat_type = "Aisle"
            valid_seat = True
        else:
            print("Invalid! Choose 1 or 2.")

    print("")
    print("--------------------------------------------------------------------")
    print("-| Passenger Type |- :")
    print(" | 1. Regular |")
    print(" | 2. Student (20% discount) |")
    print(" | 3. Senior Citizen (30% discount) |")
    print(" | 4. PWD (30% discount) |")
    print("--------------------------------------------------------------------")

    ptype = 0
    valid_ptype = False
    while valid_ptype == False:
        ptype = int(input("Select passenger type (1-4): "))
        if ptype >= 1 and ptype <= 4:
            valid_ptype = True
        else:
            print("Invalid! Please select 1-4.")

    discount = 0
    ptype_name = ""

    if ptype == 1:
        discount = 0
        ptype_name = "Regular"
    elif ptype == 2:
        discount = 20
        ptype_name = "Student"
    elif ptype == 3:
        discount = 30
        ptype_name = "Senior Citizen"
    elif ptype == 4:
        discount = 30
        ptype_name = "PWD"
    
    subtotal = price * passengers
    discount_amount = subtotal * discount / 100
    total = subtotal - discount_amount
    
    print("")
    print("=======================================================================")
    print("                     -|   TICKET SUMMARY |-                            ")
    print("=======================================================================")
    print("Name: " + name)
    print("Travel Date: " + travel_date)
    print("Route: " + route_name)
    print("Seat Type: " + seat_type)
    print("Passenger Type: " + ptype_name)
    print("Number of Passengers: " + str(passengers))
    print("Base Price per Ticket: P" + str(price))
    
    if discount > 0:
        print("Discount: " + str(discount) + "%")
        print("Discount Amount: P" + str(discount_amount))
   
    print("Subtotal: P" + str(int(subtotal)))
    print("TOTAL: P" + str(int(total)))
    print("====================================================================")
    
    print("")
    print("--------------------------------------------------------------------")
    print("| Payment Options | : ")
    print("_______________________")
    print("")
    print("| 1. Cash |")
    print("| 2. Credit Card |")
    print("| 3. GCash |")
    print("--------------------------------------------------------------------")
    
    payment = 0
    valid_payment = False
    while valid_payment == False:
        payment = int(input("Select Payment Method (1 - 3) : "))
        if payment == 1 or payment == 2 or payment == 3:
            valid_payment = True
        else:
            print("Invalid! Please select a valid option (1 - 3) : ")
        
    if payment == 1:
        print("")
        print("Payment : Cash")
        amount = 0
        enough = False
        while enough == False:
            amount = float(input("Enter Cash Amount : P"))
            if amount >= total:
                enough = True
                change = amount - total
                print("Change : P" + str(int(change)))
            else:
                more = total - amount
                print("Insufficient amount! You need P" + str(int(more)) + " more.")
                
    elif payment == 2:
        print("")
        print("Payment : Credit Card")
        print("Processing...")
        print("Payment successful!")
        
    elif payment == 3:
        print("")
        print("Payment : GCash")
        print("Sending request...")
        print("Payment successful!")

    print("")
    print("=============================================================================")
    print("                            -| BUS Tickets |-                                ")
    print("=============================================================================")
    
    ticket_price = int(total / passengers)
    
    seat_number = 1
    for i in range(1, passengers + 1):
        print("")
        print("----- Ticket #" + str(i) + " -----")
        print("Name  : " + name)
        print("Route : " + route_name)
        print("Date  : " + travel_date)
        print("Seat  : " + seat_type + " #" + str(seat_number))
        print("Type  : " + ptype_name)
        print("Price : P" + str(ticket_price))
        seat_number = seat_number + 1
        
    print("")
    print("===================================================================================")
    print("                    -| Thank You For Using Our Ride! |-                            ")
    print("===================================================================================")
    
    again_valid = False
    while again_valid == False:
        print("")
        again = input("Book another ticket? (yes/no) : ")
        if again == "yes" or again == "y" or again == "Yes" or again == "Y" or again == "YES":
            again_valid = True
            start_booking = "yes"
        elif again == "no" or again == "n" or again == "No" or again == "N" or again == "NO":
            again_valid = True
            start_booking = "no"
        else:
            print("Invalid! Please enter 'yes' or 'no'.")
            
    print("")
    print("Goodbye! Have a safe trip!")