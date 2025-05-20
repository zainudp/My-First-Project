#****************************************************************
#Name:Zainab Udaipurwala
#Student Number: A00255427
#
#ANA1001 Lab 1
#****************************************************************

#############								   	                  
#Question #1	
#############
#Describe four programs you would like to create using full sentences	
print (" Question 1 ".center(60,"*"))  #Acts like a header
print("I want to make a program that gives me the meaning of Names") #1st Program
print("I want to make a program that would plan my day for me") #2nd Program
print("I want to make a program that gives me virtual tours of places") #3rd Program
print("I want to make a program that tells me the weather for today") #4th Program
print("\n") #Next line

############
#Question #2
############
#First store the name of a city (the value) in a variable, and then print the name. Repeat this process with two other city names but use the same variable name. Format the output using .title() and .upper()
print (" Question 2 ".center(60,"*"))
place= "Frankfurt"
print(place)
place = "delhi"
print (place.title()) #Displays result with Title case(first letter in uppercase)
place = "rome"
print(place.upper()) #Displays resut with all letters in uppercase
print("\n")

############
#Question #3
############
#Store your name in a variable and print out your name within a sentence using an f string. Do this three times, modifying your name to print out in uppercase, lowercase and title case.
print (" Question 3 ".center(60,"*"))
name = "zainab"
print(f"{name.lower()} enjoys canvas painting") #Using Lower Case in sentence
print(f"{name.upper()} enjoys canvas painting") #Using Upper Case in sentence
print(f"{name.title()} enjoys canvas painting") #Using Title Case in sentence
print("\n")

############
#Question #4
############
#Variable with a Canadian food using commands "\t", "\n", lstrip(), rstrip(), and strip().
print (" Question 4 ".center(60,"*"))
food = "    Butter Tarts    " #Adding whitespaces to left & right of Value
print("\t\t",food,"\n")  #using the Tab and nextline command
print(food.lstrip()) #Removing White spaces from Left
print(food.rstrip()) #Removing White spaces from Right
print(food.strip()) #Removing White spaces from Left and right
print("\n")

############
#Question #5
############
#Using 4 operations addition, subtraction, multiplication, and division to equal 2022 and then print in message explaining the result
print (" Question 5 ".center(60,"*"))
add = 1011+1011
subtract = 3500-1478
multiply = 337*6
divide = 4044/2
print(f"Adding 1011 twice equals {add}")  #displaying the add results in words using f string
print(f"Subtracting 1478 from 3500 equals {subtract}") #displaying the subtract results in words using f string
print("Multiplying 337 six times equals", multiply) #multiplication results in words using join (,)
print("Dividing 4044 by 2 equals " + str(divide))  #Division results in words using join (+)
print("\n")

############
#Question #6
############
#A dog runs from one side of a park to the other. The park is 80.0 meters across. The dog takes 16.0 seconds to cross the park. What is the speed of the dog?
print (" Question 6 ".center(60,"*"))
distance = 80 #meters
time = 16 #seconds
speed = distance/time #calculating the speed
print (f"The speed of the dog is {distance} meters/ {time} seconds which equals to {speed} m/s") #displays the result in words using variables and string