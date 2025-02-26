import random

password = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789qwertyuioplkjhgfdsazxcvbnm.`,/';][\+-*]~!@#$%^&()=_<>:{?}")
length_pass = int(input("Enter the length of the password: "))
var = "".join(random.sample(password, length_pass))

print(f"Your random password is: {var}")