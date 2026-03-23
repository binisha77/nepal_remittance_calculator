for i in range(3):
    print("\n--- Transaction", i+1, "---")


    # Taking input from user
    receiver_name = input("Enter receiver's name: ")
    country = input("Enter receiver's country: ")
    amount = float(input("Enter amount to send: "))


# Displaying the information
print("\n--- Transaction Details ---")
print("Receiver Name:", receiver_name)
print("Country:", country)
print("Amount:", amount)


#Task 2: Use if-elif to assign the exchange rate based on the country 
if country == "USA":
        rate = 132
elif country == "Australia":
        rate = 88
elif country == "India":
        rate = 1.6
else:
        rate = 1  
