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


def Edit_in_database(s, ar):
    '''
    This Function checks if the contact to edit exists. If it does, it asks the user what he wants to edit,
    and it execute a query accordingly.

    Parameters:
    -----------
    s: String
    The name of the database.

    ar: String
    The name of the contact to be edited.

    '''
    con = sqlite3.connect(s)
    cur = con.cursor()
    cur.execute(
        '''
        SELECT Name
        FROM contacts
        '''
    )
    names = cur.fetchall()
    con.commit()
    exist = False
    for n in names:
        if ar == n[0]:
            exist = True
    
    if exist == True:
        while True:
            continue_edit = input("do you want to continue editing ?")
            if continue_edit.lower() == 'yes':
                what_to_edit = input("what to edit?")
                if what_to_edit.lower() == "name":
                    edited_name = input("The new name is: ")
                    cur.execute(
                        '''
                        UPDATE contacts
                        SET Name = (:edited_name)
                        WHERE Name = (:name)
                        ''' , {
                            "edited_name":edited_name,
                            "name":ar
                        }
                    )
                elif what_to_edit.lower() == "address":
                    edited_address = input("The new address is: ")
                    cur.execute(
                        '''
                        UPDATE contacts
                        SET Address = (:edited_address)
                        WHERE Name = (:name)
                        ''' , {
                            "edited_name":edited_address,
                            "name":ar
                        }
                    )
                elif what_to_edit.lower() == "number":
                    edited_number = input("The new number is: ")
                    cur.execute(
                        '''
                        UPDATE contacts
                        SET Phone_Number = (:edited_number)
                        WHERE Name = (:name)
                        ''' , {
                            "edited_number":edited_number,
                            "name":ar
                        }
                    )
                elif what_to_edit.lower() == "email":
                    edited_email = input("The new email is: ")
                    cur.execute(
                        '''
                        UPDATE contacts
                        SET Email = (:edited_email)
                        WHERE Name = (:name)
                        ''' , {
                            "edited_email":edited_email,
                            "name":ar
                        }
                    )
                else:
                    print("I don't understand!")
            else:
                break
            con.commit()
        con.close()
    else :
        print("This name does not exist!")


def Delete_from_Database(s, ar):
    '''
    This function chooses a line from the table contacts where the name is equal to ar, and deletes it.

    Parameters:
    -----------
    s: String
    The name of the database

    ar: String
    The name of the contact to be deleted.

    '''
    con = sqlite3.connect(s)
    cur = con.cursor()
    ar_dict = {"name":ar}
    cur.execute(
        '''
        DELETE FROM contacts
        WHERE Name = (:name)
        ''',ar_dict
    )
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
            elif sys.argv[1] == 'display':
                if len(sys.argv) < 3:
                    Display_database(s)
                    break
                if len(sys.argv) >= 3:
                    ar = sys.argv[2]
                    Display_database(s, ar)
                    break
            elif sys.argv[1] == 'edit':
                if len(sys.argv) >= 3:
                    ar = sys.argv[2]
                    Edit_in_database(s, ar)
                    break
                if len(sys.argv) < 3:
                    print("Please Specify the name of the contact you want to edit next time!")
                    break
            elif sys.argv[1] == 'delete':
                if len(sys.argv) >= 3:
                    ar = sys.argv[2]
                    Delete_from_Database(s, ar)
                    break
                else:
                    print("You should specify which contact to be deleted by entering its name!")
                
        else:
            print(
            '''
            Add argument add in the command line to add a contact.\n
            Add argument display in the command line to display all your contacts.\n
            Add argument display x in the command line to display the information of the contact with the name: x.\n
            Add argument Edit x to edit a contact with x its name.
            Add argument Delete x to delete a contact with x its name.
            Thank you!
            ''')
            break

if __name__ == '__main__':
    main()








        
