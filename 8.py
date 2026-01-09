
def find_highest_bidder(bidding_dictionary):
     winner =""
     highest_bid =0
     max(bidding_dictionary)
     for bidder in bidding_dictionary:
        bid_amout = bidding_dictionary[bidder]
        if bid_amout > highest_bid:
            highest_bid = bid_amout
            winner = bidder
        print(f"The winner is {winner} with a bid of ${highest_bid}")

name=input("what is  your name:")
price=int(input("what is your bid?: $"))

should_continue=input("are there any other bidders? type 'yes' or 'no'.\n")
bids={}

continue_bidding = True
while continue_bidding :
     name=input("what is  your name:")
     price=int(input("what is your bid?: $"))
     bids[name]=price
     should_continue=input("are there any other bidders? type 'yes' or 'no'.\n").lower()

     if should_continue == "no":
         continue_bidding = False
         find_highest_bidder(bids)
     elif should_continue == "yes":
         continue_bidding = True

'''
# output:
PS C:\Users\DELL\CSS> python -u "c:\Users\DELL\CSS\8.py"
what is  your name:fasi
what is your bid?: $100
are there any other bidders? type 'yes' or 'no'.
yes
what is  your name:md
what is your bid?: $900
are there any other bidders? type 'yes' or 'no'.
yes
what is  your name:uddin 234
what is your bid?: $786
are there any other bidders? type 'yes' or 'no'.
no
The winner is md with a bid of $900
The winner is md with a bid of $900
PS C:\Users\DELL\CSS> 

'''