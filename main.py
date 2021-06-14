import sqlite3
import sys
import contacts as ct #type: ignore

def create_database(data_base_name = ''):
    """
    A function that will create a data base formed with one Table called contacts.
    This Table contains the name, address, phone number and email of the contact.

    Parameters:
    -----------
    data_base_name: String
    The name of the database.

    Raises:
    -------
    Exception: If the database is already created, it will raises an exception to avoid any errors.

    """
    con = sqlite3.connect(data_base_name)
    cur = con.cursor()
    try :
        cur.execute(
        '''
        CREATE TABLE contacts (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT,
            Address TEXT,
            Phone_Number TEXT,
            Email Text
        )

        '''
        )
    except Exception:
        print("DataBase is created!")
    
    con.commit()
    con.close()

def add_to_database(contact, s):
    """
    A function that will add the contact information into the database.

    Parameters:
    -----------
    contact: object
    An object from the class Contacts, containing the information that will be registered.
    s: String
    The name of the database.
    """
    contact_dict = {
        "name":contact.name,
        "addr":contact.address,
        "num":contact.phone_number,
        "mail":contact.email
    }
    con = sqlite3.connect(s)
    cur = con.cursor()
    cur.execute(
        '''
        INSERT INTO contacts (Name, Address, Phone_Number, Email)
        Values (:name, :addr, :num, :mail)
        ''', contact_dict
    )
    con.commit()
    con.close()

def Display_database(s, ar = 'all'):
    """
    A function that will display information present in the database.

    Parameters:
    -----------
    ar : Optional String
    It represents the name of the contact, and it will be used in the Where clause, for the sql querrey.
    s : String
    It is the name of the function.
    
    """
    ar_dict = {
        "name":ar
    }
    con = sqlite3.connect(s)
    cur = con.cursor()
    if ar.lower() == 'all':
        cur.execute("SELECT * FROM contacts")
        for i in cur.fetchall():
            print(i, "\n")
    else :
        cur.execute("SELECT * FROM contacts WHERE name  = (:name)", ar_dict)
        print(cur.fetchall())
    
    con.commit()
    con.close()

def main():
    
    s = 'Phone_Book.db'
    create_database(s)
    
    while True:

        if len(sys.argv) > 1:
            if sys.argv[1] == 'add':
                name = input("The name of your contact: ")
                address = input("The address of your contact: ")
                while True:
                    num = input("The number of your contact: ")
                    if num.isdigit():
                        break
                mail = input("The email of your contact: ")
                contact = ct.Contacts(name, address, num, mail)
                add_to_database(contact,s)
                break
            if sys.argv[1] == 'display':
                if len(sys.argv) < 3:
                    Display_database(s)
                    break
                if len(sys.argv) >= 3:
                    ar = sys.argv[2]
                    Display_database(s, ar)
                    break
        else:
            print(
            '''
            Add argument add in the command line to add a contact.\n
            Add argument display in the command line to display all your contacts.\n
            Add argument display x in the command line to display the information of the contact with the name: x.\n
            Thank you!
            ''')
            break

if __name__ == '__main__':
    main()








        
