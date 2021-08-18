# FOR NORMAL USERS:
#The length of the password must be at least 7 characters in length
#The password must contain at least 1 letter
#The password must contain at least 1 digit

#FOR ADMINS:
#Admin passwords must be at least 10 characters in length
#Admin passwords must contain at least 1 special character

#NOTE:
#We need to provide feedback to the user about the strength of their password
#Provide the user with a list of reasons why their password is 'weak'
while True:
    print()
    password=str(input("Enter Password: "))
    #print(password)
    if password=="exit":
        break;
    print("Length:",len(password))
    lowercase=0
    uppercase=0
    lengthcheck=0
    numcheck=0
    special=0
    choice=str(input("Who are you?: "))
    if choice=="user":
        print("Welcome, User")
        for character in password:
            if character in "abcdefghijklmnopqrstuvwxyz":
                lowercase=True
            if character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                uppercase=True
            if len(password)>=7:
                lengthcheck=True
            if character in "0123456789":
                numcheck=True

        if lowercase==False:
            print("Password should have atleast one lowercase letter.")
        if uppercase==False:
            print("Password should have atleast one uppercase letter.")
        if lengthcheck==False:
            print("Password should have a minimum length of 7 characters.")
        if numcheck==False:
            print("Password should have atleast one digit in it.")
        if lowercase and uppercase and lengthcheck and numcheck==True:
            print("Valid Password.")
        else:
            print("Invalid Password.")

    elif choice=="admin":
        print("Welcome, Admin")
        for character in password:
            if character in "abcdefghijklmnopqrstuvwxyz":
                lowercase=True
            if character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                uppercase=True
            if len(password)>=10:
                lengthcheck=True
            if character in "0123456789":
                numcheck=True
            if character in "!@#$%":
                special=True

        if lowercase==False:
            print("Password should have atleast one lowercase letter.")
        if uppercase==False:
            print("Password should have atleast one uppercase letter.")
        if lengthcheck==False:
            print("Password should have a minimum length of 10 characters.")
        if numcheck==False:
            print("Password should have atleast one digit in it.")
        if special==False:
            print("Password should have atleast one special character.")
        if lowercase and uppercase and lengthcheck and numcheck and special==True:
            print("Valid Password.")
        else:
            print("Invalid Password.")

    else:
        print("Enter a valid choice.")
