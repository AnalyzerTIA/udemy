print("Welcome to the rollercoaster!")
height = int(input("What is your heigh in cm? "))

if height >= 120:
  print("You can ride the rollercoster!")
  age = int(input("What is your age? "))
  if age < 12:
    print("Please pay $5.")
  elif age <= 18:
    print("Please pay $7.")
  else:
    print("Please pay $12.")
else: 
    print("Sorry, you are not tall enough to ride the rollercoster!")
  