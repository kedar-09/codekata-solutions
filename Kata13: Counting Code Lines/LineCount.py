#Checks the number of lines of code in a python file (excludes empty lines and comments)

#file=open("C:/Users/ADMIN/Desktop/passwordchecker.py")
file=open("C:/Users/ADMIN/Desktop/wo.txt")
count=0
for line in file:
    if line.strip() and not line.lstrip().startswith('#') and not line.startswith("'''") and not line.startswith('"""'):
        count=count+1
print("Number of lines are:",count)
