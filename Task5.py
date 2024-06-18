2
contacts={"Swetha":{"Phone":"1234567890","Email":"swe1234@gmail.com","Address":"123 nehru St"},
                "Siddhu":{"Phone":"0987654321","Email":"sid1234@gmail.com","Address":"123 nehru St"}}
def add_contact():
    Name=input("Enter name: ")
    Phone=input("Enter phone number: ")
    Email=input("Enter email: ")
    Address=input("Enter address: ")
    contacts[Name]={"Phone":Phone,"Email":Email,"Address":Address}
def view_contacts():
    for Name,contact in contacts.items():
        print(Name,contact["Phone"])
def search_contacts():
    term=input("Enter search term: ")
    results=[]
    for Name,contact in contacts.items():
        if term in Name or term in contact["Phone"]:
            results.append((Name,contact["Phone"]))
    for Name,Phone in results:
        print(Name,Phone)
def update_contact():
    Name=input("Enter name of contact to update: ")
    if Name in contacts:
        Phone=input("Enter new phone number: ")
        Email=input("Enter new email id: ")
        Address=input("Enter new address: ")
        contact=contacts[Name]
        if Phone:
            contact["Phone"]=Phone
        if Email:
            contact["Email"]=Email
        if Address:
            contact["Address"]=Address
        else:
            print("contact not found")
def delete_contact():
    Name=input("Enter name of contact to delete: ")
    if Name in contacts:
        del contacts[Name]
    else:
        print("contact not found")
while True:
    print("1.Add contact")
    print("2.View contact")
    print("3.Search contact")
    print("4.Update contact")
    print("5.Delete contact")
    print("6.Quit")
    choice=input("Enter your choice(1/2/3/4/5): ")
    if choice=='1':
        add_contact()
    elif choice=='2':
        view_contacts()
    elif choice=='3':
        search_contacts()
    elif choice=='4':
        update_contact()
    elif choice=='5':
        delete_contact()
    elif choice=='6':
        break
    else:
        print("Invalid choice")
        


           
