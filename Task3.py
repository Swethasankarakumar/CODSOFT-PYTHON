5import random
import string
def generate_password(length):
    characters=string.ascii_letters+string.digits+string.punctuation
    password=' '.join(random.choice(characters)for i in range (length))
    return password
length=int(input("Enter the desired password length: "))
password=generate_password(length)
print("Generated password is:",password)
