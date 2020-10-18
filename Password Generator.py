import random
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"

def generator(length, n_of_iterations):
    counter = 0
    while counter < n_of_iterations:
        sec1 = ""
        for s1 in range(length):
            sec1 += random.choice(chars)
        sec2 = ""
        for s2 in range(length):
            sec2 += random.choice(chars)
        sec3 = ""
        for s3 in range(length):
            sec3 += random.choice(chars)
        counter += 1
        password = sec1 + "-" + sec2 + "-" + sec3
        print(password)

def final_password(sec1, sec2, sec3):
    password = sec1 + "-" + sec2 + "-" + sec3
    print(password)

noi = input("Enter the number of passwords to be generated: ")
try:
    noi = int(noi)
except:
    print("You can only enter integer values")
    quit()
clength = input("How many characters should each section have? ")
try:
    clength = int(clength)
    generator(length = clength, n_of_iterations = noi)
except:
    print("You can only enter integer values")
    quit()
