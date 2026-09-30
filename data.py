""" x = 6
y= float(x)

print(x,y) """
""" 
values = [1,2,5,7,2,42,25]
print(values)
for i in values:
    print(i) """

""" values = [1,2,5,7,2,42,25]
print(values)
print(values[0])
print(values[6])
 """


""" #integer
x = 7
#string
name = "kevin"
#boolean 
isValid = True
#float
bill = 12.22
#list
students = ["aiden", "kevin", "william", "nathaniel"]
students.append("david")

for student in students:
    if student == "aiden":
        print(f'we found {student}')

#string 
y = input("money?")
z = y + 5 """

""" x = "Hello, my name is Chatgpt."
y= x.split( )
z = y[0]
print(y)
print(z) """

""" sentence = input("give me a sentence NOW")
y = len(sentence.split( ))
print(y) """

""" day_of_week = input("what day is it?")
if day_of_week == " Thursday":
    print("correct!!")
elif day_of_week == "Thursday":
    print("correct!!")
elif day_of_week == "thursday":
    print("correct!!")
elif day_of_week == " thursday":
    print("correct!!")
else:
    print("womp womp, INCORRECT!") """

""" x = "chatgpt"
print(f"hello {x}") """

""" temp = 68
if temp > 68:
    print("it is currently above 68 degrees.")
elif temp == 68:
    print("it is currently exactly 68 degrees.")
else:
    print("it is currently below 68 degrees") """

""" number=int(input("give me a number - aiden lee"))
if number %2 ==0:
    print("even")
else: 
    print ("odd") """

""" bill = float(input("how much was the bill?"))
service = input("how was the service?")
if service == "good":
    print(float(bill) * 1.15)
elif service == "never coming back":
    print(float(bill) * 1.0)
elif service == "great":
    print(float(bill) * 1.20)
elif service == "Amazing":
    print(float(bill)* 1.25)
  """ 

def spaces(N,Y,T):
    X = 0
    for i in range(N):
            if Y[i] == "c" and T[i] == "c":
                X=X+1
    print(str(X))

