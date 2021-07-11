# CTI-110 
# P4HW2 - Distance Traveled
# Tristan Falcon
# 07-06-2021
# 

# Create input numbers
def main():
    car_speed = 0
    time_traveled = 0
    total_distance = 0
    restart = 'y'

    # Create a while loop
    while restart == 'y':
        car_speed = float (input ('Enter the cars speed: '))
        time_traveled = int (input ('Enter hours traveled: '))
        print()

    # Create an if statement that the time traveled must be greater than 0
        if time_traveled <=0:
        # If the statement is true print the error
            print ("Error ! time entered should be > 0")
            print ('Please try again')
            print()
        # If the statment is false run else
        else:
            print ('Time\tDistance')
            print ('-----------------')
            for t in range (time_traveled):          
                total_distance = car_speed * (t + 1)    
                print (t + 1 , '\t', total_distance)
            # Ask the user if they would like to restart the program
            restart = input('Would you like to restart? y for yes or n for no: ')
    # When the user is done this will show them the program is over
    print ('End')

# This will start the program
main()


    # Function main()
    # Declare Integer carSpeed
    # Declare Integer timeTraveled
    # Declare Integer totalDistance
    # Declare String restart

    # While restart = 'y'
        # Display "Enter the cars speed: "
        # Input carSpeed
        # Display "Enter hours traveled: "
        # Input timeTraveled

            # If timeTraveled <= 0 Then
            # Display "Error ! time entered should be > 0"
            # Display "Please try again"

            # Else
                # Display "Time\tDistance"
                # Display "------------------"
                # For t in Range timeTraveled
                # Set totalDistance = carSpeed * t + 1
                # Display t + 1, "\t", totalDistance
                # Display "Would you like to restart? y for yes or n for no: "
                # End For
            # End If
    # End While 

    # Display "End"

# EndFunction main()
