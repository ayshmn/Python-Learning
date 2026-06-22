try :
    marks = int(input("Enter your marks :"))
except ValueError :
    print("Please enter numbers only.")
except TypeError:
    print("Invalid type")
else:
    print("Marks entered successfully.")
finally: 
    print("Program ended")