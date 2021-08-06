import string
import random
s = string.ascii_letters+string.digits+string.punctuation
password_length = int(input("Enter the length of password:"))
password = "".join(random.sample(s,password_length))
print(password)
