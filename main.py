#Adding Numbers
#int1 = 1
#int2 = 3
#var_text = "The answer is:"
#print(var_text)
#print(int1 + int2)

#Group Project: Lesson 2


#Lesson 2

#Booleans
#To declare a varlibe...
#Night = True
#Day = False

#Lists

location = ["At the school ", "At the park", "At the Apple Farm"]
lists = ['Bar', 'Chips Ahoy', 'Sugur']
l = len(lists)
print(lists)

#  .remove removes values from lists and   .extend adds to lists.

# If/else
condition = (5 == 3)
if condition:#If "Condition" is true
  print('ur in a diffrent universe')
else:#If "Condition is false"
  print('YOure in the same universe')

i = 0
while i < 223:
  i = i + 2
  print(i)

#use while True:
while True:#infine loop; Repeats the ufnction infinity times unless break function is used.
  print('Na Na Na Boo Boo')
  break

i = 2
while i < 39:
  print(i)
  i += 7

#For loops
words = "These are my words!"
for c in words:
  print(c)

#For loops with range()
for i in range(1, 11):
  print('I am currently on a loop number ' + str(i))
  import time
  time.sleep(0.1)
  #ex. I am currently on loop number 1
  #I am currently on loop number 2
  #I am currently on loop number 3 ect. ect.

#Tuples, Cannot change values
myTuple = ("This", "Is", "A", "Tuple")
print(myTuple)

#Dictionary:
myDict = {"eggs":2, "milk":3, "cookies":4}
print(myDict["cookies"])

#Functions
def greeting():
  print('Hello!')
greeting()

#Functions with Parameters
numone = 10
numtwo = 23
def add(numone, numtwo):
  result = numone + numtwo
  return result

#adding numbers without varibles
sum = add(2, 3)
print(sum)

#Return Statements

def my_example(fname):
  return fname + " is the name"

Name1 = my_example('Chrissy')
Name2 = my_example('Chris')
print(Name1 + ". " + Name2)