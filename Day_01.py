print("Hello World!")

# From Real Python: Variable examples
message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course world!"
print(message)


#In Python, data types don't need to be declared.

#1. INTEGERS

type(42)
#The above shows what class the value belongs to, which is class 'int'

#(a.)INTEGER LITERALS

0b10
#'0b'before a number means that number is in base 2.

0o10
#'0o' before a number means that number is in base 8.

10
#without any preceed in the back, it's assumed to be base 10.

0x10
#that's base 16

type(10)

#(b.)INTEGER METHODS


(10).as_integer_ratio() #outputs the number as a fraction, the int as numerator and 1 as denominator.
(10).bit_count()

(100).bit_count()# returns/outputs the number of ones in the binary representation of the given integer.

int(42.0)#the 'int' function converts other data types into integers as long as they are numerical values.

#2. FLOATING -POINT NUMBERS -Numbers with a decimal place.

type(1.0)
type(42.0)

#a. Floating-point Literals
4.2

#b. Floating-point Methods
(4.2).as_integer_ratio() #returns a pair of integers whose ratio is equivalent to original float.
(4.2).is_integer()  #is a method that allows you to check whether a given float value is an integer.

float(42)#the 'float() function converts other data types into floats provided they are valid numerical values.

#3. COMPLEX NUMBERS - consists of real and imaginary parts. Have a form: a+bj
type(2+3j)

3j


number = 2+9j
number.conjugate()

2+4j+1


#4. Strings and characters
type("Hello,World!")


#*Escape sequeences in strings
"Hello\
    World"
#the backlash makes python to ignore the new line and interpret the whole construct as a  single line.

print("a\tb")# the '\t' introduces a horizontal tab space.
print("a\nb")# the '\n' shifts the characters that follow to the next line- intro vertical space.
print("\141")# to represent string in the olden octal escape sequence.

#*String methods

("brandon").capitalize() #converts first character to uppercase and the rest to lower case.
text="Brandon mUrithi"
text.title()
text.upper()
text.lower()

text.find("r")#uses indexing - 0,1,2,3,4,5,6
text.count("r")
text.isalpha()


name="Brandon"
age="20"
f"{name} is {age} years old!"#f-strings- string formatting
"{} is {} years old!".format(name, age) #achieved same above output but by using '.format()' method

#****COMMON SEQUENCE OPERATIONS ON STRINGS
len("Brandon")# The'Brandon' is the argument as it appears within the parentheses, while 'len() is a built in function.
"Brandon"[0] # this is indexing used to retrieve a single character from an existing string.
"Brandon"[2:4]
str(3)


#**PERSONALISED MESSAGE PROGRAM
name="Brandon".upper()
age="20"
hobby="drawing"
message="{} is {} years old".format(name,age)
print(message)

message= f"{name} is {age} years old"
print(message)

#5. BYTES AND BYTE ARRAYS
type(b"This is a byte literal")
type(bytearray(b"This is a bytearray literal"))

bytes("Hello, World!", encoding='utf-8') #You use the 'bytes()' fuction plus  appropriate character encoding in order to change data type into bytes

bytes([65,66,67,46,47,48])

#6. BOOLEANS

type(False)
bool(0)
bool("")
bool(0j)
bool(3j)
bool("hello")
bool(3.2)
