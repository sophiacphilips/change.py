# Author: Sophia Philips
# GitHub Username: sophiacphilips
#Date: 10/05/2022
#This program will take a whole number between 0-99 and output how many of each type coin would represent that amount using the fewest coins.


print("Please enter an amount in cents less than a dollar.")
num_1=float(input())
quarters=25
dimes=10
nickels=5
pennies=1
num_quarters=(num_1//quarters)
cents_remq=(num_1%quarters)
num_dimes=(cents_remq//dimes)
cents_remd=(cents_remq%dimes)
num_nickels=(cents_remd//nickels)
cents_remn=(cents_remd%nickels)
num_pennies=(cents_remn//pennies)
print("Your change will be:")
print("Q:", num_quarters)
print("D:", num_dimes)
print("N:", num_nickels)
print("P:", num_pennies)
