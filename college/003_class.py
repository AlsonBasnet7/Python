#write a program that creates a new list containing all the elements placed on even positions of the original list.
#[43,23,21,44,56,76]->[23,44,75]
a=[43,23,21,44,56,76]
b=[]
for i in range(len(a)):
    if i%2!=0:
        b.append(a[i])
        