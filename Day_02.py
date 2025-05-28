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
