print(2 == "2")
print(22 != 2)

print("Hari" == "hari")
print(5 > 2)
print(10 < 2)

print(10 >= 10)
print(4 <= 6)

print(True and True)
print(True or False)
print(not (True))


print(2 == 2 and True)

print(5 > 2 and 10 > 0)






'''
a=2
if (a == 4):
print ("this is testing")

'''


if(2 ==1):
    print("True condition")
    print ("code block of if condition")
else:
    print("this is else block")





    a=int(input("Enter a number: "))
    if(a%2==0):
        print(f"{a} is an even number")
    else:
        print(f"{a} is an odd number")



if (1 == 1 and 2== 2):
   print("this is true condition")
elif(2 == 3):
     print("this is elif condition")
elif(3 == 1):
        print("this is another elif condition")
else:
    print("this is else condition")






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
    print("Invalid grade")



