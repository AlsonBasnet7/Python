try:
    file =open("file.txt","r") #open in read mode
    content = file.read() 
    print(content)
    file.close() #closes the files
except FileNotFoundError:
    print("File not found")
#Reading line by line

try:
    file=open("file.txt","r")
    for line in file:
        print(line.strip())
    file.close()
except FileNotFoundError:
    print("File not Found")

