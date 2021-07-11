# Displaying grades in Python
# 06-26-2021
# CTI-110 P3HW1
# Tristan Falcon
# 

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 50
    # TO DO: define the rest of the scores

    
    score = int (input('Enter grade: '))

    if score >= A_score:
        print ('Your grade is: A Great job')
    
    elif score > B_score and score < A_score:
            print ('Your Grade is: B Great job')
    
    elif score > C_score and score < B_score:
         print ('Your Grade is: C Needs work')
    
    elif score > D_score and score < C_score:
        print ('Your grade is: D Needs a lot of work')

    elif score > F_score and score < D_score:
        print ('Your grade is: F See teacher')
    else:
        print ('Your grade is: F See teacher')
    
# TO DO: finish this

# program start
main()