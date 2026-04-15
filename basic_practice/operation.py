# with open("text.txt","w") as f:
#     data=f.write("ID001,Harry,85\nID002,Alson,95\nID003,Suidp,90")

# def read(path):
#     l=[]
#     with open(path) as f:
#         data=f.readlines()
#         print(data)
#         for i in data:
#             part=i.strip().split(",")
#             part[2]=int(part[2])
#             l.append(part)
#             print(part)
#             ## if i just print i not storing the values here
#     return 1



# student=read("text.txt")
# print(student)
# def add(data,sid,name,mark):
#     data.append([sid,name,mark])
def update(data):
    id=input('enter a id')
    found=False
    for i in data:
        if id==i[0]:
            found=True
            try:
                mark=int(input('Enter a mark'))
                i[2]=mark
                print("Update Successfully")
            except:
                print('enter a numberic value!')
    if not found:
        print("id not found!!")

def write(filename,data):
    with open(filename,"w") as file:
        for i in data:
            line=f"{i[0]},{i[1]},{i[2]}\n"
            file.write(line)

   

            







# # l=[1,2,3,4]
# # print(l)
# # for i in l:
# #     print(i)

# Step 1: Create / overwrite file
with open("text.txt", "w") as f:
    f.write("ID001,Harry,85\nID002,Alson,95\nID003,Suidp,90")


# Step 2: Read function
def read(path):
    l = []
    with open(path) as f:
        data = f.readlines()
        print("Raw data:", data)

        for i in data:
            part = i.strip().split(",")
            part[2] = int(part[2])  # convert marks to int
            l.append(part)
            print("Processed:", part)

    return l


# Step 3: Add function
def add(data, sid, name, mark):
    data.append([sid, name, mark])
    return data


# Step 4: Use functions
student = read("text.txt")
print("Before add:", student)

student = add(student, "ID004", "Rushan", 69)
print("After add:", student)