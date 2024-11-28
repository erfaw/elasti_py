from clear_sc import clear_screen
from art import logo

clear_screen()
input(f"{logo} \n\t\tWELCOME TO OUR BLIND AUCTION\npress Enter to continue...")

def main():
    is_anymore = 'y'
    bid_info = {}

    while is_anymore == 'y':
        clear_screen()
        bidder_name = input("whats your name? :\n\t")
        bid_amount = input("how many you want to bid? :\n\t$ ")
        bid_info[bidder_name] = int(bid_amount)
        is_anymore = input("there is anymore?(y/n): ").lower()
    
    highest_bidder = ''
    for person in bid_info:
        if highest_bidder == '':
            highest_bidder = person
        elif bid_info[person] > bid_info[highest_bidder] :
            highest_bidder = person 

    clear_screen()
    input(f"{logo} \nwinner is {highest_bidder} with {bid_info[highest_bidder]}$ bid amount")



while True:
    clear_screen()
    main()
    if input('try again? (y/n)').lower() != 'y':
        break
