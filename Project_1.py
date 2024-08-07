# Objective:
# Create a program to calculate and display a detailed bill for a customer, including a 10% tip and 20% GST. The program should also handle the customer's payment and calculate the change to return.
# Instructions:

# 1. Customer Details:
#     Ask the customer for their name.
#     Ask the customer for the total bill amount.

# 2. Calculations:
#     Calculate 10% tip on the total bill.
#     Calculate 20% GST on the total bill.
#     Calculate the grand total (total bill + tip + GST).

# 3. Payment
#     Ask the customer how much they paid.
#     Calculate the change to return to the customer.

# 4. Display the Bill:
#     Show the customer's name.
#     Show the total bill amount.
#     Show the tip amount.
#     Show the GST amount.
#     Show the grand total.
#     Show the amount paid by the customer.
#     Show the change to return.
#     Include a "Thank you for your visit!" message.

# Requirements:
#  Use variables to store and calculate values.
#  Use arithmetic operators for calculations.
#  Ensure proper input and output from the user.

                              # 1. Customer Details:

Customer_name=input("Enter your name :")
Total_bill_amount=int(input("Enter your total bill amount :"))

                                # 2. Calculations:

#  Calculate 10% tip on the total bill.

Tip=int(0.1*Total_bill_amount)
print(Tip)

# Calculate 20% GST on the total bill.
Gst=int(0.2*Total_bill_amount)
print(Gst)

# Calculate the grand total (total bill + tip + GST).
Grand_Total=Total_bill_amount+Gst+Tip
print(Grand_Total)

                                # 3. Payment
#   Ask the customer how much they paid.
payment=int(input("Enter your paid amount :"))

if  payment == Grand_Total:
     print("Sorry!!,There is no change you paid full payment.Thank you ")
elif payment < Grand_Total:
    print("Please pay full amount ")
else:
    change=payment-Grand_Total
    print(change)

                                 #  4. Display the Bill:

Bill="Displaying Bill"
print(Bill)

print("Customer Name is :", Customer_name)
print("Customer total bill amount is :", Total_bill_amount )
print("10 percent tip is :", Tip)
print("20 percent GST tax is :", Gst)
print("Grand Total is :", Grand_Total)
print("Total amount paid by customer is :", payment)
print("Chnage return to the customer is :", change)

print("Thank you for your visit!")