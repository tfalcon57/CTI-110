i = int (input())
num = int (input())
if i > num:
    print("Second integer can't be less than the first.")
else:
    while i <= num:
        print( i, end =" ")
        i += 5
    print()
# I think this is the right assignment for P4LAB2 but you had named it OutOfRange in Black Board