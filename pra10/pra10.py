#Write File
f=open("C:\\Users\\hp\\OneDrive\\Desktop\\python programs\\file 1.txt","w")
f.write("Practical No 10")
f.close()


#Read File
f=open("C:\\Users\\hp\\OneDrive\\Desktop\\python programs\\file 1.txt","r")
content=f.read()
print(content)
f.close()

#Append File
f=open("C:\\Users\\hp\OneDrive\\Desktop\\python programs\\file 1.txt","a")
f.write("\n This is file handling practical")
f.close()

