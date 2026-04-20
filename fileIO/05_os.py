import os
#list of files present in the dir.
a= os.listdir("fileIO")
print(a)

#getting the current working dir
current_dir = os.getcwd()
print("THe current path I am working: ",current_dir)

#creating a new dir using os modules.

new_dir = os.mkdir("sub")
new_dir=os.getcwd()
print(new_dir)

