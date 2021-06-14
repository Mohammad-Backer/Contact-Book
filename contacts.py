class Contacts:
    """
    A class that defines the attributes of the contacts.

    Attributes:
    -----------
    name: String
    The name of the contact.

    address: String
    The address of the contact.

    phone_number: String
    The phone number of the contact.
    
    email: Sting
    The email of the contact.

    """


    def __init__(self, nom = ' ', adre = ' ', num = ' ', mail = ' '):
        self.name = nom
        self.address = adre
        self.phone_number = num
        self.email = mail
