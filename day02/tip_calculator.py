#Welcome statement
print("Welcome to the Tip Calculator")

#Ask input for amount of total bill
total_bill = float(input("What was the total bill? $"))

#Ask input for percentage tip
percent_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

#Ask input for number of people to split the bill
split = int(input("How many people to split the bill? "))

#Add tip amount to the bill
total_bill_with_tip = (percent_tip / 100) * total_bill + total_bill

#Divide total bill with tip with number of people
each_person_pays = round(total_bill_with_tip / split, 2)

#Print the amount each person pays
print(f"Each person pays ${each_person_pays}")
