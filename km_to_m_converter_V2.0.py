print ("~~~Mini Converter~~")

num1 = float(input("Enter first number here : "))

print ("press 1 for Kilometer \npress 2 for Meter ")

choice = int(input("Enter your choice from 1 - 2: "))

if choice == 1:
  print ("The conversion of", num1, "to Meter", "is: ", num1 * 1000)

elif choice == 2:
  print ("The conversion of", num1, "to Kilometer", "is: ", num1 / 1000)

else:
  print ("Invalid Input")