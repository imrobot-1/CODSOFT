import random 
import string

length = int(input("Enter password length: "))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
number= string.digits
symbol= string.punctuation

all_chars = lower + upper + number + symbol 

sample = random.sample(all_chars,length)
password = "".join(sample)
print("Here is your generated password:", password)