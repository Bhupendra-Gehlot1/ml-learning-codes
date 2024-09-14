# Data types
# IMMUTABLE
# INT
# float
# str
# bool
# complex
# tuple
# MUTABLE
# List
# Set
# Dictionary
a = 8
b= 8.3
CONSTANTS="hello"
print(type(a))
print(type(b))
print(type(CONSTANTS))
a=0
b=2
CONSTANTS="help"
print(a)
print(CONSTANTS)
c=False
type(c)
d=3+5j
type(d)

# Input Function
# number_1 = int(input("no. 1: "));
# number_2 = int(input());
# sum =number_1+ number_2;
# print(sum)

#Change DataType
number_1=8
print(float(number_1))


# list is array and can carry multiple data types

list_1  = [1,2,3,4,5,6,1];
type(list_1);
print(list_1);
list_1.append(7);
del list_1[2];
tuple_1 = tuple(list_1);
print(tuple_1);
print(len(tuple_1))

set_1 = {1,2,3,4,5,6,1};
print(type(set_1));
# Dictionary_1 = dict(set_1);
Dictionary_1 = {"name":"Modi", "Pura Name": "Narendra Modi", "Swach Bharat Swach Abhiyan": "Yaad rakhega Hindustan"};
print(Dictionary_1);
print(Dictionary_1["Pura Name"])
print(len(Dictionary_1))

a = 19;
b = 21;
c = 20;

if(b<a>c):
    print("a is king")
elif(a<b>c):
    print("b is queen")
else:
    print("c is villen")


for i in range(5):
    print(i);

list_2 = [1,23,456,7890]
for i in list_2:
    print(i)

i=0;
while (i<10):
    print(i)
    i+=1

def factoral_val(num):
    fact = 1;
    if (num==0):
         return fact;
    else:
        for i in range(1,num+1):
            fact*=i;
        print(fact);

print(factoral_val(0))