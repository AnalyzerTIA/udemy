# #If the bill was $150.00, split between 5 people, with 12% tip. 

# #Each person should pay (150.00 / 5) * 1.12 = 33.6
# #Format the result to 2 decimal places = 33.60

# #Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# #Write your code below this line 👇

#print("Welcome to the tip calculator")

# total_bill = input()
# print(f"What is your total bill? \n{total_bill}")

# percentage_tip = input()

# print(f"What percentage tip would you like to give? \n{percentage_tip}")

# people = input()

# print(f"How many peaple to split the bill \n{people}")

# print(f"Each people should pay \n ({total_bill}/{people}) * {percentage_tip}/100 $")

print("Welcome to the tip calculator!")

bill = float(input("What is the total bill? $"))

tip = int(input("What percentage tip would you like to give 10 or 15 or 20?"))

people = int(input("How many people to split the bill?"))

tip_as_perc = tip / 100
total_tip_ammount = bill * tip_as_perc
total_bill = bill + total_tip_ammount
total_tip_pers = total_bill / people
final_amount = round(total_tip_pers, 2)

# FAQ: How to round to 2 decimal places?

# Find the answer in the Q&A here: https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048

#If you want the final_amount to always have 2 decimal places.
#e.g. $12 becomes $12.00
#You can use this link to figure out how to do this:
#https://www.kite.com/python/answers/how-to-print-a-float-with-two-decimal-places-in-python
#This is how you can implement it:
final_amount = "{:.2f}".format(total_tip_ammount)

print(f"Each person should pay: ${final_amount}")
