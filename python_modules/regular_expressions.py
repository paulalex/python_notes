import re

# Replace the first and last character
str_to_replace = "Hello my name is Paul and I am from Weymouth"

print(re.sub("^.|.$", "*", str_to_replace))

print(str_to_replace[1:-1])

print(str_to_replace.replace("Paul", "Sid"))

print(str_to_replace[::-1])
