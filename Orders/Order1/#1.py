import string # for the alphabets
import time # for the time mesurements
from hashlib import sha256 #for the hashuse
import csv # to read the csv file
import os # not really necessary
from itertools import product # to make the characters!

hashes = []

# Def for better controle of the Printing

def Debug(msg, state):
    if state: #check if state is True
        print(f"[DEBUG] %s" % msg) # if True it prints the msg %s gets replaced with the message in this example


debug = input("[Debug] Show debug msg? (y/n): ") # ask for the Debug
if debug == "y" or debug == "Y":
    state = True # set state to true so it prints the debug messages
elif debug == "n" or debug == "N":
    state = False # set state to False so it dosnt print the debug messages
else:
    print("[Debug] Wrong input!")
    state = True

# Ask which characters to use!

print("[Info] What character do you want to use?") # ask the user with input what type of alphabet he wants to use
mode1 = input("[Info] Ascii_lowercase? ['abc'] (y/n): ") # 'abcdefghijklmnopqrstuvwxyz'
mode2 = input("[Info] Ascii_uppercase? ['ABC'] (y/n): ") # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
mode3 = input("[Info] digits? ['123'] (y/n): ") # '0123456789'
mode4 = input("[Info] punctuation ['#$%'] (y/n): ") # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
alphabet = ""
# appending the characters to the alphabet var
if mode1 == "y" or mode1 == "Y": alphabet = string.ascii_lowercase # used to append the characters to the alphabet
if mode2 == "y" or mode2 == "Y": alphabet += string.ascii_uppercase
if mode3 == "y" or mode3 == "Y": alphabet += string.digits
if mode4 == "y" or mode4 == "Y": alphabet += string.punctuation

ask = input("[Info] File or Text: [F/T] :") # ask to use a File or a String
if ask == "F" or ask == "f":
    path = input("[Info] Please enter the path (.csv):") # ask for the filepath to the csv file!
    if os.path.exists(path):
        csvreader = csv.reader(open(path, "r")) # open the File
        for line in csvreader: # read the file
            hashes.append(line) # append the file content to the hash var
    else:
        print("[ERROR] File not found :",path) # if file cant get find


elif ask == "T" or ask == "t": # ask if text / string
    ask1 = input("[Info] Input one or more hashes [...;...] :") # ... <-- the first hash ; <-- The separator ... <-- the second hash ; ... you can do it as long as you want!
    hashes = ask1.split(";") # split text by the ';' so you get a list of hashes all separated by the ';' ("aa;ab" gets to (("aa"),("ab")) )

else:
    print("[Info] ERROR wrong input")

max_len = 5
a = 0

print("[Info] String the bruteforce now!")
w = 100

def bruteforce(password, max_length, w): #Bruteforce def
    begin = time.time() # the time in seconds!
    finish = [] # Varible of the decrypted passwords
    a = 0
    for i in range(max_length): # ´that the password is only 1 - 5 chars long
        for attempt in product(alphabet, repeat=i): # produces a charmap
            a += 1
            if a == w: # check for the print every w * 10
                w *= 10
                # ''.join(attempt) <-- to print "aaa" instead of ("a","a","a")
                print(f"[Bruteforce] Checked [{''.join(attempt)}] : {a} hashes!") # printing an interim result
            Debug(f"Current attempt : {''.join(attempt)} | {sha256(''.join(attempt).encode()).hexdigest()} | {a} | {password}", state) # using the debug def to print!
            for i in password: #check for the passwords | with i is the list of passwords in password meant
                #sha256() used to generate the hash of the password | i[0] to get the 0. also first entry of the list!
                if sha256(''.join(attempt).encode()).hexdigest() == i: # check if hashed password is the same to one of the hashes
                    finish.append((''.join(attempt),i)) # appends the attempt and the hash so you can see the hash in plain text
                    if len(finish) == len(hashes): # check if the decrypted hashes are as many as the given one!
                        print("[Info] finished")
                        return finish,begin #returns the time in seconds when it begone and the results

result, begin = bruteforce(hashes, max_len, w) #start the function
end = time.time() # get the time the def ended
time1 = end - begin # get the needed time
print(f"The time to decrypt the Password : {round(time1, 3)}\n results:",result) # printing the results