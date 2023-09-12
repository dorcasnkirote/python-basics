#!/bin/python3

#Comments are shown with the hash when using python 3
#STRINGS
print ("This is a string!")
print('This is also a string!')
print("""This string runs
multiple lines!""") #triple quote for multiple lines
print("This string is "+"awesome") #we can also concatenate
print('\n')
print('Test the newline out')


print('\n')
#MATH
print(50 + 50) #add
print(50 - 50) #subtract
print(50 * 50) #multiply
print(50 / 50) #divide
print(50 + 50 -50 * 50 /50) #PEMDAS
print(50 ** 2) #exponents
print(50 % 6) #modulo - takes whta is left over
print(50 // 6) #no remainder


print('\n')
#VARIABLES AND METHODS

quote = "All is fair in love and war."
print(quote)

print(quote.upper()) #uppercase
print(quote.lower()) #lower
print(quote.title()) #title case
print(len(quote)) #count characters

name = "Dorcas" #string
age = 18 #int
gpa = 3.7 #float - has a decimal

print(int(age))

print("My name is " + name + ". I am " + str(age) + " years old")

age += 1
print(age)

birthday = 1
age += birthday
print(age)


print('\n')
#FUNCTIONS

def who_am_i(): #this is a function without parameters
	name = "Dorcas" #local variable - do not apply outside the function
	age = 30
	print("My name is " + name + ". I am " + str(age) + " years old")

who_am_i()

def add_one_hundred(num):
	print(num + 100)
	
add_one_hundred(100)

def add(x,y):
	print(x + y)
	
add(7,7)

def multiply(x,y):
	return x * y #the result will be stored rather than being printed out
	
multiply(7,7)
print(multiply(7,7))

def square_root(x):
	print(x ** .5)
	
square_root(64)

def nl():
	print("\n")

nl()
#BOOLEAN EXPRESSIONS (TRUE OR FALSE)

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)
print(type(bool1))

bool5 = "True"

bool5 = "True"
print(type(bool5))

nl()
#RELATIONAL AND BOOLEAN OPERATIONS
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

test_and = (7 > 5) and (5 < 7) #True
test_and2 = (7 > 5) and (5 > 7) #False
test_or = (7 > 5) or (5 > 7) #True
test_or2 = (7 > 5) or (5 < 7) #True

test_not = not True #False 


nl()
#CONDITIONAL STATEMENTS - if/else

def drink(money):
	if money >= 2:
		return "You've got yourself a drink!"
	else:
		return "No drink for you!!"
		
print(drink(3))
print(drink(1))

def alchohol(age,money):
	if (age >= 21) and (money >= 5):
		return "We're getting a drink!"
	elif (age >= 21) and (money < 5):
		return "Come with enough money!"
	elif (age < 21) and (money >= 5):
		return "Nice try kid"
	else:
		return "You are too young and too poor"
		
print(alchohol(15,270))
print(alchohol(25,270))
print(alchohol(25,2))
print(alchohol(15,2))

nl()
#LISTS - Have brackets []
movies = ["War Room", "Overcomer", "God's not Dead", "Do you Believe?"]

print(movies[1])
print(movies[0]) #returns the first item in the list 
print(movies[1:3]) #returns the first index nember given right until the last number, but not including the last number 
print(movies[1:])
print(movies[:1])
print(movies[-1]) #returns the last item in list

print(len(movies)) #count items in the list
movies.append("An Encounter with God")
print(movies) #appends to the end of the list
 
movies.insert(2, "Grace unplugged")
print(movies)

movies.pop() #removes the last item
print(movies)

movies.pop(0) #removes the first item
print(movies)

sarah_movies = ['sistas', 'Dicknison']
our_favorite_movies = movies + sarah_movies #combining lists
print(our_favorite_movies)

#2d lists
grades = [["Doro", 82], ["Claire", 90], ["Jeff", 73]]
doros_grade = grades[0][1]
print(doros_grade)
grades[0][1] = 83
print(grades)

nl()
#TUPLES - Do not change(immutable), ()
grades = ("a", "b", "c", "d", "e", "f")

print(grades[1])


nl()
#LOOPING

#For loops - start to finish of an iterate
vegetables = ["cucumber", "spinach", "cabbage"]
for x in vegetables:
	print(x)
	
	
#while loops - execute as long as True
i =1

while i < 10:
	print(i)
	i += 1
	
nl()
#ADVANCED STRINGS

my_name = "Dorcas" #note strings are also immutable like tuples
print(my_name[0]) #first letter
print(my_name[-1]) #last letter

sentence = "This is a sentence."
print(sentence[:4])
print(sentence.split()) #delimeter - default is a space

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

quote = "He said, 'give me all your money'"
print(quote)
quote = "He said, \"give me all your money\""
print(quote)

too_much_space = "                  hello       "
print(too_much_space.strip()) # takes the delimeter of space as default

print("A" in "Apple") #True
print("a" in "Apple") #False

letter = "A" 
word = "Apple"
print(letter.lower() in word.lower()) #improved

#string formatting
movie = "War Room"
print("My favorite movie is {}.".format(movie))
print("My favorite movie is %s." % movie)
print(f"My favorite movie is {movie}.") #using a string literal f


nl()
#DICTIONARIES - key/value pairs {}

drinks = {"Virgin Tequilla": 200, "Blue Lagoon": 350, "Lemon Drop": 250} #drink is the key, price is the value
print(drinks)

employees = {"Finance": ["Carol", "Mergery", "Linda"], "IT": ["Gene", "Louise", "Teddy"], "HR": ["Jimmy Jr.", "Mort"]}
print(employees)
employees['Legal'] = ["Mr. Frond"] #adds new key:value pair
print(employees)

employees.update ({"Sales": ["Andie", "Ollie"]}) #adds new key:value pair as well
print(employees)

drinks['Virgin Tequilla']= 250
print(drinks)

print(drinks.get("Virgin Tequilla"))







