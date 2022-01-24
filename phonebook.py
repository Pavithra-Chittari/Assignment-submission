import sys
def create_contact(n):
    for i in range(n):
        temp_list=[]

        name=input("Enter contact name*: ")
        if name in phonebook:
            print("Contact with name "+name+" already exists...")
            print("\nstart again...")
            continue
        elif name.isdigit():
            print("invalid name...")
            print("\nstart again...")
            continue
        else:
            temp_list.append(name)

        mobile=int(input("Enter mobile number*:"))
        if len(str(mobile))==10 or len(str(mobile))==3:
            temp_list.append(mobile)
        else:
            print("invalid mobile number...")
            print("\nstart again...")
            continue

        e_mail=input("Enter e_mail address: ")
        if '@' in e_mail or len(e_mail)==0:
            temp_list.append(e_mail)
        else:
            print("invalid e-mail address...")
            print("\nstart again...")
            continue

        category=input("Enter category(Work/Family/Friend/Others): ")
        if category=="Work" or category=="Family" or category=="Friend" or category=="Others" or len(category)==0:
            temp_list.append(category)
        else:
            print("invalid category...")
            print("\nstart again...")
            continue

        address=input("Enter address: ")
        temp_list.append(address)

        phonebook[name]=temp_list
        print()

        print("contact(s) entered successfully...")
    print()

def delete_contact():
    name=input("Enter contact name to delete: ")
    if name in phonebook:
        del phonebook[name]
        print("Contact deleted successfully...")
        print()
    else:
        print("Contact is unavailable in phonebook...")
        print()

def delete_all_contacts():
    if len(phonebook)==0:
        print("Phonebook is already empty...")
    else:
        phonebook.clear()
        print("Your phonebook is empty now...")
    print()

def search_contact():
    criteria=int(input("Search criteria :\n1.Name\n2.Mobile number\n3.E-mail\n4.Category\nEnter your choice: "))
    if criteria==1:
        name=input("Enter name: ")
        if name not in phonebook:
            print("contact is unavailable in Phonebook...")
        else:
            print(phonebook[name])
    elif criteria==2:
        mobile=int(input("Enter mobile number: "))
        for i in phonebook.keys():
            if phonebook[i][1]==mobile:
                print(phonebook[i])
                break
        else:
            print("Mobile number unavailable in Phonebook...")
    elif criteria==3:
        e_mail=input("Enter E_mail: ")
        for i in phonebook.keys():
            if phonebook[i][2]==e_mail:
                print(phonebook[i])
                break
        else:
            print("E-mail address unavailable in Phonebook...")

    elif criteria==4:
        category=input("Enter category: ")
        for i in phonebook.keys():
            if phonebook[i][3]==category:
                print(phonebook[i])
                break
        else:
            print("No contact available in Phonebook with "+category+" category...")
    else:
        print("invalid criteria...")
    print()

def display_all_contacts():
    if len(phonebook)>0:
        for i in phonebook.keys():
            print(phonebook[i])
    else:
        print("phonebook is empty...")
    print()

def menu():
    while(True):
        print("1.Create contact\n2.Delete contact\n3.Delete all contacts\n4.Search contact\n5.Display all contacts\n6.Exit Phonebook")
        choice=int(input("Please enter your choice: "))
        if choice<1 or choice>6:
            print("invalid choice!!\nPlease enter choice between 1 and 6")
        elif choice==1:
            n=int(input("Enter number of contacts you wish to create: "))
            create_contact(n)
        elif choice== 2:
            delete_contact()
        elif choice==3:
            delete_all_contacts()
        elif choice==4:
            search_contact()
        elif choice==5:
            display_all_contacts()
        elif choice== 6:
            print("******************Thank You for using our Phonebook service******************\n*********************************Visit Again*********************************")
            sys.exit()
        else:
            print("invalid choice...")
        print()

phonebook={}
print("**********************************************\n Dear user, Welcome to the Phonebook directory!\n**********************************************\n")
n=int(input("Enter number of contacts you wish to create: "))
print("Enter contact details in the following order only..\nNOTE: * indicates mandatory field..")
create_contact(n)
print("*****You may now utilize the following services*****")
menu()
