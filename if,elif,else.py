# if statement

age = print(int(input("enter your age:")))

if age >= 18:
    print("Eligible to vote.")


# if and elif

age = (int(input("enter your age :")))

if age >=18:
    print("Eligible to vote.")
elif age < 18:
    print("Not Eligible.")


# if, elif and else

age = (int(input("enter your age :")))

if age > 18:
    print("Eligible to vote.")
elif age == 18:
    print("Just eligible to vote.")
else:
    print("Not eligible to vote.")