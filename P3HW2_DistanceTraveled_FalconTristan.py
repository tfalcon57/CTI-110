# This progarm will show the distance traveled in a car and will
# show and error if the value entered is less then 0
# 06-27-2021
# CTI-110 P3HW2 - Distance Traveled
# Tristan Falcon
#

# Create input numbers
car_speed = int (input ('Enter the cars speed '))
time_traveled = int (input ('Enter hours traveled '))
# Create an if statement that the time traveled must be greater than 0
if time_traveled <=0:
# If the statement is true print the error
    print ("Error ! time entered should be > 0")
    time_traveled = 1
    total_distance = car_speed * time_traveled
    print()
# Display the values entered by the user 
    print ('Speed entered: ', car_speed)
    print ('Time entered: ', time_traveled)
    print()
# Display the total distance traveled 
    print ('Distance traveled', total_distance,'miles. ')
# If the statement is false run the else statement
else:  
    total_distance = car_speed * time_traveled
    print()
# Display the values entered by the user 
    print ('Speed entered: ', car_speed)
    print ('Time entered: ', time_traveled)
    print()
# Display the total distance traveled 
    print ('Distance traveled', total_distance,'miles. ')




# Declare Integer carSpeed
# Declare Integer timeTraveled
# Declare Integer totalDistance

# Display "Enter the cars speed "
# Input carSpeed
# Display "Enter hours traveled "
# Input timeTraveled

# If timeTraveled is <= 0 then
#   Display "Error ! time entered should be >0"
# Else
#   Set totalDistance = carSpeed * timeTraveled
#   Display "Speed entered: "
#   Display "Time entered: "

#   Display "Distance traveled", totalDistance, "miles."
# End If