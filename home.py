
# Program to take receiver details

# Taking input from user
receiver_name = input("Enter receiver's name: ")
country = input("Enter receiver's country: ")
amount = float(input("Enter amount to send: "))

# Displaying the information
print("\n--- Transaction Details ---")
print("Receiver Name:", receiver_name)
print("Country:", country)
print("Amount:", amount)


# Task 3: Calculate NPR amount and service charge

if country.lower() == "usa":
    rate = 132
elif country.lower() == "india":
    rate = 1.6
elif country.lower() == "australia":
    rate = 88
else:
    rate = 100  # default rate

npr_amount = amount * rate
service_charge = npr_amount * 0.02

print("Converted NPR:", npr_amount)
print("Service Charge:", service_charge)