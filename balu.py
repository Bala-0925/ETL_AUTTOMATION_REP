weight_float=75.8
#print("The value of weight variable is: ",weight_float," and data type of weight variable is:",type(weight_float))

weight_int=int(weight_float)
#print("The value of weight variable is: ",weight_int," and data type of weight variable is:",type(weight_int))

age=10
age_flt=float(age)
#print(age_flt,"and type is ",type(age_flt))

num1="123455"
num2="123123"
#print(type(num1)," and ",type(num2)," and addition of 2 numbers is ",num1+num2)

num3=int(num1)
num4=int(num2)
#print(type(num3)," and ",type(num4)," and addition of 2 numbers is ",num3+num4)

#Camel case:
myFirstName = "Balu"

#Pascal case:
MyFirstName = "Balu"

#Snake case
my_first_name = "Balu"

#Data Types in Python
#str, int, float, boolean - primitive/basic datatype

#Sequence Types (List, Tuple, Set)

#Mapping type (dict)

#EXAMPLE OF LIST

# to store a single value we can use primitive data types
# e.g age,name of a person

age=20
name="Balu"
#print("My name is ", name ,"and my age is ", age)

#if we want to store multiple similar values in a single variable then type should be non primitive

name_list=["Ajay","Akshay","Balu","Ankitha","Bhupendar","Karthik","Ajay"]
name_list.append("Azhar")
#print("List of students ",name_list," and type is ",type(name_list))
#print("Hello ",name_list[0]," Welcome to python class")
#print(f"Hello {name_list[0]}! Welcome to Python class")

#EXAMPLE OF TUPLE
#if we want to store multiple similar values in a single variable then type should be non primitive

name_tuple=("Ajay","Akshay","Balu","Ankitha","Bhupendar","Karthik","Ajay")
name_tuple=name_tuple +("Azhar",)
#print("list of students ",name_tuple," and type is ",type(name_tuple))
#print(f"hello {name_tuple[2]}! Welcome to python class")

#EXAMPLE OF SET
#if we want to store multiple similar values in a single variable then type should be non primitive

name_set= {"Ajay", "Akshay", "Balu", "Ankitha", "Bhupendar", "Karthik", "Ajay"}
#print("List of students ", name_set," and type is ",type(name_set))
#print(f"{name_set}! Welcome to python class")

address = "Bangalore"
int_size = len(address)
#print(address[0])
#print(address[int_size-1])

name_raj = "Surya"
#print(name_raj.upper())
#print(name_raj.lower())

channel_name = "ETL QA Labs"
n = len(channel_name)
#print(n)

#print(channel_name[n-1])

'''
for idx in range(startindex,endindex+,1)
    print(channel_name[idx],end=",")
    pass


for idx in range(0,6,1):
    print(channel_name[idx],end = "|")
    pass


for ele in channel_name:
    print(ele,end="")
    pass

print(channel_name[0:6:1])


for idx in range(0,11,3):
    print(channel_name[idx],end="")
    pass


for idx in range(0,11,3):
    print(channel_name[idx],end="")
    pass
'''
#string slicing
channel_name = "ETL QA Labs"
#print (type(channel_name))
first_word = channel_name[0:3:1]
#print(first_word)
#print("first word is ",first_word , " and type is :",type(first_word))
full_string = channel_name[0:n:1]
#print(full_string)
#print("Forward direction :",full_string)
alternate_char = channel_name[0:n:2]
#print(alternate_char)
forward_string = channel_name[::1]
#print(forward_string)
reversed_string = channel_name[::-1]
#print(reversed_string)
reverse_ch_name = channel_name[n::-1]
#print(reverse_ch_name)
l = ["prathap reddy","prabhu reddy","aadi thammudu",
     "central minister","aadu evadaina gaani"]
for i in l:
    print("Na thokkalo ",i,end=",")