reservation = {}
topSecretOperation = "CHECK"
close = "QUIT"

def ask_reservation ():
    global reservation
    while True:
        try:
            nric = input("Enter NRIC for booking: ").upper()
            name = input("Enter Name: ").title()
            pax = int(input("Enter amount of pax: "))
            print("\n")
            print("NRIC:", nric)
            print("Name:", name)
            print("No. of pax:", pax)
            confirmation = input("Please confirm details(Y/N): ").upper()
            print("\n")
            if confirmation == "Y":
                reservation[nric] = []
                break
            else:
                print("Please try again")
        except ValueError or UnboundLocalError:
            print("Invalid input, try agian")
    return pax, nric, name
    
def add_reservation(throw,nric,name,pax):
    global reservation
    reservation[throw].append(nric)
    reservation[throw].append(name)
    reservation[throw].append(pax)

def check_reservation():
    while True:
        check_nric = input("Enter NRIC to check booking list: ").upper()
        if check_nric == topSecretOperation:
            break
        elif check_nric in reservation:
            inside_check_reservation = reservation[check_nric]
            print("\nReservation found")
            print("NRIC:", inside_check_reservation[0])
            print("Name:", inside_check_reservation[1])
            print("No. of pax:", inside_check_reservation[2], "\n")
            break
        else:
            print("\nReservation not found for", check_nric)

def reservation_process():
    booking = 1
    while booking == 1:
        print("type \'quit\' to exit this program")
        ask = input("Make Reservation (Y/N): ").upper()
        if ask == "Y":
            ask_pax, ask_nric, ask_name = ask_reservation()
            if ask_pax > 8:
                print("Due to covid-19 measures we can't make this booking, please limit pax to 5. Thank you.\n")
                booking = 1
            elif ask_pax < 1:
                print("Sorry..you are inviting?\n")
                booking = 1
            else:
                # print(reservation)
                add_reservation(ask_nric, ask_nric, ask_name, ask_pax)
                # print(reservation)
                inside_reservation = reservation[ask_nric]
                print("Thank you", inside_reservation[1])
                print("Booking for table of", inside_reservation[2],"has been made!")
                print("Please provide your NRIC", inside_reservation[0], "upon arrival.\n")
                booking = 1
                print("type \'check\' to proceed to check booking list via NRIC")
        elif ((ask == topSecretOperation) or (ask == close)):
            booking = 0
        else:
            print("Next please")
            booking = 1
    return ask

while(True):
    ask_quit = reservation_process()
    if ask_quit == topSecretOperation:
        check_reservation()
    if ask_quit == close:
        break