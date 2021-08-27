# File


#1. Write a program to read text file

f = open("simplefile.txt", "r")
print(f.read())


# # 2. Write a program to write text to .txt file using InputStream

f=open("newfile.txt", "w")
f.write("how are you")
f.close()

 
# 3. Write a program to read a file stream

f=open("newfile.txt", "r")
print(f.readline())



# 4. Write a program to read a file stream supports random access\

import random
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
print(random_line('simplefile.txt'))


#5. Write a program to read a file a just to a particular index using seek()

f = open("simplefile.txt", "r")
f.seek(2)
print(f.read())


#6. Write a program to check whether a file is having read access and write access permissions

new=open("simplefile.txt", "a")
new.write("I am a fresher")
new.close()