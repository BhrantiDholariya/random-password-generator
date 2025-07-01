import random
import string
length=int(input("enter desired paasword length : "))
characters=string.digits+string.ascii_letters+string.punctuation
password=""
for i in range(length):
    password+=random.choice(characters)
if length<4:
    print("password should have atleast length of 4 characters")
else:
    print(f"Generated Password is : {password}")
