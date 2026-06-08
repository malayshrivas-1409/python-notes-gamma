#Python program to swap two variables
'''a= int(input("Enter the first number = "))
b= int(input("Enter the second number = "))
a=a+b
b=a-b
a=a-b
print(f"""First number = {a} and the Second number = {b}""")'''


'''#Python program to take input as age and name and print it in formatted way
name = str(input("Enter name = "))
age = int(input("Enter the age = "))
print(f"""My name is {name} and my age is {age}""")'''


'''#Program to Check the number is even or odd using modulo operator only
num = int(input("Enter the number"))
if num%2==0:
    print("Even")
else:
    print("Odd")'''


'''#By using a function 
def isprime(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"

n = int(input("Enter the number you wanna check = "))
result = isprime(n)
print(f"""The number was {n} and it is an {result} number""")'''

'''#celsius to fahrenheit
unit = str(input("In which unit you have Temperature C or F ")).lower()
if (unit ==  "c"):
     c = float(input("Enter the temperature = "))
     f = (c*1.8)+32
     print("The temp in fahrenheit is = ", f)

elif (unit == "f"):
    f = float(input("Enter the temperature = "))
    c = (f-32)/1.8
    print("The temp in Celsius is = ", c)
    print(f"""The temperature {f} is {c} in celsius""")
else:
    print("Wrong input")'''


'''#Check if the string is palindrome or not:
s= str(input("Enter a string  :")).lower()
print(len(s))
left =0
right = len(s)-1
print(right)
is_palindrome = True
while(left<right):
    if s[left]!=s[right]:
        is_palindrome = False
        break
    left +=1
    right -=1

if is_palindrome:
    print("Palindrome")
else:
    print("Not a palindrome number")'''
 

'''#prg to print frequency of each character in string
s= str(input("Enter the String : "))
freq = {}
for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print(freq)'''

'''#string formatiing methods:
s = "Malay"
print("The String belongs to {Malay}".format(Malay="Shubham"))
print("My name is %s" %s)
print(f"""Hello {s}""")'''

'''#prg to print whether a year is a leap year or not
year = int(input("Enter the Year : "))
if year%4==0:
    print(f"""{year} is a leap year""")
else:
    print(f"""{year} is not a leap year""")'''


'''#prg to print whether two strings are anagrams 
s1 = str(input("Enter the First string : ")).lower()
s2 = str(input("Enter the Seocnd string : ")).lower()
if len(s1) != len(s2):
    print("Not an anagram")
else:
    freq1={}
    freq2={}

for ch in s1:
    freq1[ch] = freq1.get(ch,0)+1

for ch in s2:
    freq2[ch] = freq2.get(ch,0)+1

if freq1==freq2:
    print("Anagram")
else:
    print("not")'''


'''while True:

    print("\n---- CLI Calculator ----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Choose operation (1-5): ")

    if choice == "5":
        print("Calculator Closed.")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice! Please select 1-5.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    except ValueError:
        print("Invalid input! Enter numbers only.")
        continue

    if choice == "1":
        print(f"Result = {num1 + num2}")

    elif choice == "2":
        print(f"Result = {num1 - num2}")

    elif choice == "3":
        print(f"Result = {num1 * num2}")

    elif choice == "4":

        if num2 == 0:
            print("Division by zero not allowed.")

        else:
            print(f"Result = {num1 / num2}")'''



'''#Dynamic typing [Means the type is specified by python itself no need to pre decide / neither the type is fixed ]
age = 18 
print(type(age))
age = "Sixteen"
print(type(age)) #Can change the string without even specifying before 
age = 18.889
print(type(age))
print(size(int))'''

'''age = 20
print("hello" +str(age)) #type conversion'''

'''age = None
print(age, type(age))''' # None means no value as if now , somnetimes no values are known so we later change them:



'''#arithmetic operators
a = 10
b = 3

print("Addition:", a+b)
print("Subtraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)
print("Floor Division:", a//b)
print("Modulus:", a%b)
print("Power:", a**b)'''


'''s="malay"
print(s[1:4])
print(s[::-1])
print(s.capitalize())'''

'''s1= "Mal ay Shrivas"
print(s1.strip())'''


'''#Ternary operator (single line if-else )
age = int(input("Enter the AGE : "))
result = "Adult" if age>=18 else "Minor"
print(result)'''

'''#iterating over a list:
fruits = ["apple", "banana", "cherry"]
for items in fruits:
    if items=='apple':
        print(items)
        break #breaks the loop and stops the next iteration
    print(items)'''

'''for x in "banana":
    if x=='a':
        print(x)
        continue
    print(x)'''

'''for x in range(1,6): #in range() function lets us iterate over a specified value 
    print(x)'''

#Creating and accessing list in python:

ls= [1,2,"apple",3.14]
'''print(ls) #print whole list
print(ls[0]) #accesing list index-based starts from zero 
print(ls[2])
print(ls[-1])#Negative indexing (access last element of list from -1)'''

'''
#adding elements in the list:
ls.append(10) #Adds element to the last if the index is not specified 
print(ls)
ls.insert(2, 'banana') #Adds element at specific position
print(ls)
ls.extend([1,2,3,4]) #Adds multiple elements to the end of the list
print(ls)'''

#Updating elements in the list:
#just assign new values to their index the values will be updated 
'''ls[1]=0
print(ls)'''

#Removing an element from list 
#ls.remove(1)#Remove the first occurence of the element

'''
ls.pop() #specified index is removed if index is not specified last element is removed 
print(ls)'''
'''
del ls[0] # deletes from specific index 
print(ls)
del ls[1]
print(ls)'''


'''#Iterating over a list:
list1=['apple','banana','cherry']
for i in list1:
    if i in list1:
        print(i)
'''
'''#3 ways to reverse a list 
print(ls)
ls.reverse() #changes in existing list 
print(ls)'''

'''revers=reversed(ls)#Does not changes the existing list , it creates a new list 
print(list(revers))'''

'''#string slicing
revers= ls[::-1] #most pythonic way
print(revers)'''




#----------------TUPLES-----------------------------------------------#

#TUPLE IS AN IMMUTABLE ORDERED COLLECTION OF ELEMENTS
'''tup=(10,2,3,4,5,6,7,8,9,'apple',3.14)
t= (1,2,3)

print(tup)
print(tup[0])
print(tup[9])'''

#A single element cannot be deleted from the tuple as tuple is immutable however it is possible ton delete the 
#whole tuple by using del statements 
#print(type(tup))

#TUPLE UNPACKING (GETTING EACH ELEMENT OF TUPLE AND ASSIGNING IT A VARIABLE)
#------------------------------EXAMPLES-----------------------------------------------------------------|
'''a,b,c = t
print(a)
print(b)
print(c)
print(type(a))'''
#-------------------------------------------------------------------------------------------------------|
#a,*b,c = tup #unpacking using asterisk *b means all in between from starting to end 
#print(a,b,c)
#-------------------------------------------------------------------------------------------------------|
#Python dic is a data structure in python used to store data in key value pairs , each key maps to directly to a specific value
#creating a dic 
'''
dic = {"name":"Malay","age":21 , "work":"Software Developer"}
print(type(dic))
print(dic["name"])
dic["name"]="akash"
dic["work"]="AI engineer"
print(dic)
del dic["name"]
print(dic)
dic.pop("age")
print(dic)
dic.popitem()
print(dic)
dic['name']="RAhul"
print(dic)
dic['age']=50
dic['address']="Bhanwarkua"
print(dic)


#----------------------------------------------------------------------
#iterating through Dictonary:
for key in dic:
    print(key)
for value in dic.values():
    print(value)
for key , value in dic.items():
    print(key,value)
'''
#-------------------------------------NESTED LIST-----------------------------------------------
'''
d= {
    "student":{
        "age":21,
        "name":"Abeer"
    }
}

print(d["student"]["name"])'''

#==================================================  SETS IN PYTHON    ===================================================================
#creating a set 
se={1,1,1,1,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,} #duplicates will be automatically removed set is ordered collection//set are mutable 
print(type(se))
print(se)
se.add(10)
print(se)