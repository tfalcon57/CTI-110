# I tried making it look better by adding ('Enter three numbers') and ('Enter first number') etc
# But Zybook kept failing it...

user_num1 = int (input ())
user_num2 = int (input ())
user_num3 = int (input ())

if user_num1 < user_num2 and user_num1 < user_num3:
    print (user_num1)
elif user_num3 < user_num1 and user_num2 < user_num3:
    print (user_num2)
else:
    print(user_num3)
    