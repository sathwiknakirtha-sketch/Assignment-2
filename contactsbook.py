contacts = {}
while True:
 print("\n--contact book--")
 print("1.add contact")
 print("2.search contact")
 print("3.update contact")
 print("4.delete contact")
 print("5.display contacts")
 print("6.exit")
 choice = input("enter your choice:")
 if choice =="1":
        name=input("enter name:")
        phone=input("enter phone number:")
        contacts[name]=phone
        print("contact added successfully!")
 elif choice=="2":
     name=input("enter name to search:")
     if name in contacts:
         print("phone number:",contacts[name])
     else:
         print("contact not found!")
 elif choice=="3":
     name =input("enter name to update:")
     if name in contacts:
         contacts[name]=input("enter new phone number:")
         print("contact update successfully!")
     else:
         print("contact not found")
 elif choice =="4":
     name =input("enter name to delete:")
     if name in contacts:
         del contacts[name]
         print("contact deleted successsfully!")
     else:
         print("contact not found!")
 elif choice=="5":
     for name,phone in contacts.items():
         print (name,":",phone)
 elif choice=="6":
     break
 else:
     print("invalid choice!")