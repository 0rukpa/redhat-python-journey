print("Exercise 1")
string =input("What fruit are you thinking off the top of your head?:" )
print(string, len(string)) 

" "


print("Exercise 2")
first_name =input("What is your First Name:" )
last_name  =input("What is your Last Name:"  )

print("The User's name is :" , first_name,last_name)


print("Exercise 3")
text = input("Write me any text you can think of:" ) 
print("Does the text end with a period",text.endswith("."))
print("Is the text all alphabetical", text.isalpha())
print("Does the text contain an 'X':",text.find("x"))
new_text=text.replace("e", "E")
print(new_text)

print("Exercise 4")
sentence = input("How are you feeling today?:" )
print(sentence[0], sentence[0].count(sentence))
print(sentence[-1], sentence[-1].count(sentence))

print("Exercise 5")
radius = int(input("What is the radius of the circle that you have measured?:"))
print("The area of your circle is: ", 3.14159 * radius * radius  )

print("Exercise 6")
seperator = "========================"

print(seperator)
print("Mathematics Game")
print(seperator)
value1= int(input("Type in your first number:" ))
value2 = int(input("Type in your second number:" ))
answer = value1 * value2
print(seperator)
print(answer)
print(seperator)



print("Exercise 7")
string =input("Input a word:" )
number =int(input("Input a number:" ))
 
print(string * number)


print("Exercise 8")
number1=int(input("Put your base value:" ))
number2=int(input("Put your exponent value:" ))
print(pow(number1,number2))
