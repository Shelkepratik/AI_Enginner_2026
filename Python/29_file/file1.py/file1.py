file1=open("text.txt","r")
result=file1.read()
print(result)

#wrting
file2=open("text.txt","w")
result=file2.write("hello!!!")
print(result)


file3=open("text.txt","r")
result=file3.read(7)
print(result)

#append

file4=open("text.txt","a")
result=file4.write("\nhello")
print(result)