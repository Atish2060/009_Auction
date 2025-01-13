print("Welcome to the auction everyone !! ")
persons_bid = {}
eof = "y"

while eof == "y":
    name = input("Please Enter Your Name: ")
    bid = int(input("Please Enter your bid please: "))
    persons_bid[name] = bid
    eof = input("Is there any other bidder (Y for yes and N for no): ").lower()
    print("\n" * 100)

highest_name = ""
highest_bid = 0
for name in persons_bid:
    if persons_bid[name] > highest_bid:
        highest_name = name
        highest_bid = persons_bid[name]
print(f"The person with the highest bid is {highest_name} with the bid of ${highest_bid}.")

