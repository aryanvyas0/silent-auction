from replit import clear
#clear() clears the console in replit

auction_over = False
print("Welcome to the auction🫂")
def find_max_val(bid_dictionary):
    max_val = 0
    max_person = ""
    for bidder in bid_dictionary:
        bid_amount = bid_dictionary[bidder]
        if bid_amount > max_val:
            max_val = bid_amount
            max_person = bidder
    print(f"The winner is {max_person} and the winning bid is ${max_val}!\nCongratulations🎉 ")     

while not auction_over:
    namee = input("What is your name? ")
    pricee = int(input("What is your bid? $"))
    my_bid_dictionary = {}
    my_bid_dictionary[namee] = pricee
    for_continue = input("Does anyone else want to bid? Type 'yes' or 'no' \n")
    if for_continue == 'no':
        find_max_val(my_bid_dictionary)
        break
    elif for_continue == 'yes':
        clear()
    



