import string
import random

if __name__ == "__main__":

    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    
    plen = int(input("Enter Password Length\n"))

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    # print(s)
    random.shuffle(s)
    # print(s)
    
    print("Your Password is : ")
    print("".join(s[0:plen]))

    # This is a Password Generator Project , it is a useful tool that generates strong and random passwords for user
    