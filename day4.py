grade= float(input("Enter your grade: "))

if(grade >= 3.6 and grade <= 4.0):
    print("A+")
elif(grade >= 3.2 and grade < 3.6):
    print("A")
elif(grade >= 2.8 and grade < 3.2):
    print("B+")
elif(grade >= 2.4 and grade < 2.8):
    print("B")      
elif(grade >= 2.0 and grade < 2.4):
    print("C+")
elif(grade >= 1.6 and grade < 2.0):
    print("C")
elif(grade >= 1.2 and grade < 1.6):
    print("D+")
elif(grade >= 1.0 and grade < 1.2):
    print("D")
elif(grade <= 1.0 and grade >= 0.0):
    print("E+")
else:
    if grade   >4.1:
        print("wrong input")  
    elif grade<0.0:
        print("grade should be in positive")
    else:
        print(f"{grade} is an error GPA")


gender = "M"

if gender == "M":
    print("Male")
else:
    print("Female")

    data = "Male" if gender == "M" else "Female"
    print(data)



number=2
data=f"{number} is even" if number%2==0 else f"{number} is odd"
print(data)



unit = 2
if (unit <=100 and unit >=0):
    total_bill = unit*5
    print(f"Total bill: {total_bill}")
elif(unit >100 and unit <=200):
    total_bill = (100*5) + (unit-100)*7
    print(f"Total bill: {total_bill}") 
elif(unit >200 and unit <=300):
    total_bill = (100*5) + (100*7) + (unit-200)*10
    print(f"Total bill: {total_bill}")
elif(unit >300):
    total_bill = (100*5) + (100*7) + (100*10) + (unit-300)*15
    print(f"Total bill: {total_bill}")
else:
    if unit < 0:
        print("unit should be in positive")    
    else:
        print(f"{unit} is an error unit")     





username = input("Enter your username: ")
password = input("Enter your password: ")

if(username == "prakriti"):
    if(password == "lama"):
        print("login successful")
    elif(password != "lama"):
        print("password is incorrect")
    else:
        print("username is incorrect")
else:
    print("invalid username and password")




a = [1, 2, 3, 4, 5]
print(a)
print(type(a))


a=["Hello" , 1,1.4,True]
print(a[-2] )


print(len(a))

      