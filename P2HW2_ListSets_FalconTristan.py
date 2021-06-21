# CTI-110
# P2HW2 - List and Sets
# Tristan Falcon
# 06-20-2021
#

# Make empty list
num_list = []
# Ask user to input numbers
print ('Enter ten number')
# Have the user enter each number
num1 = int (input('Enter 1st number: '))
num2 = int (input('Enter 2nd number: '))
num3 = int (input('Enter 3rd number: '))
num4 = int (input('Enter 4th number: '))
num5 = int (input('Enter 5th number: '))
num6 = int (input('Enter 6th number: '))
num7 = int (input('Enter 7th number: '))
num8 = int (input('Enter 8th number: '))
num9 = int (input('Enter 9th number: '))
num10 = int (input('Enter 10th number: '))
# Add inputed numbers to the empty list
num_list.append (num1)
num_list.append (num2)
num_list.append (num3)
num_list.append (num4)
num_list.append (num5)
num_list.append (num6)
num_list.append (num7)
num_list.append (num8)
num_list.append (num9)
num_list.append (num10)
# Output the numbers entered
print ('The lowest value is: ', min(num_list))
print ('The highest value is: ', max(num_list))
print ('The total of the numbers is: ', sum(num_list))
print ('The average of these numbers is: ', sum(num_list) / len(num_list))
# Convert the list into a set
set_list = set(num_list)
# Display the newly converted set of numbers
print ('This list of numbers in a set would be: ', set_list)


# Create empty list named num_list
# Declare integer num1
# Declare integer num2
# Declare integer num3
# Declare integer num4
# Declare integer num5
# Declare integer num6
# Declare integer num7
# Declare integer num8
# Declare integer num9
# Declare integer num10

# Display "Enter ten number"
# Display "Enter 1st number: "
# Input num1
# Display "Enter 2nd number: "
# Input num2
# Display "Enter 3rd number: "
# Input num3
# Display "Enter 4th number: "
# Input num4
# Display "Enter 5th number: "
# Input num5
# Display "Enter 6th number: "
# Input num6
# Display "Enter 7th number: "
# Input num7
# Display "Enter 8th number: "
# Input num8
# Display "Enter 9th number: "
# Input num9
# Display "Enter 10th number: "
# Input num10

# Display "The lowest value is: ", min num_list
# Display "The highest value is: ", max num_list
# Display "The total of the number is: ", sum num_list
# Display "The average of these numbers is: ", sum num_list / len num_list
# Convert the list into a set
# set_list = set num_list
# Display "This list of numbers in a set would be: ", set_list