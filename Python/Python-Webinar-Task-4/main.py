import random

words = ["london","paris","madrid","rome","berlin"]
numbers = range(10)
punctuation = ["!","@","£","$","%","^","&","*","(",")"]

# Method 1
for word in words:
  for number in numbers:
    for punc in punctuation:
      print(word + str(number) + punc)


# Method 2
passwords = [word + str(number) + punc for word in words for number in numbers for punc in punctuation]

print("\n".join(passwords))

# Extension

userInput = ""
while userInput != 'n' :
  print("password: " + passwords[random.randint(0,len(passwords))])
  userInput = input("would you like another password (y/n)\n")

