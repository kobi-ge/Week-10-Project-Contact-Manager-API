class Contact:
    def __init__(self, contact_info):
        self.id = contact_info[0]
        self.first_name = contact_info[1]
        self.last_name = contact_info[2]
        self.phone_number = contact_info[3]

    def convert_to_dict(self):
        return {"id": self.id, 
                "first_name": self.first_name, 
                "last_name": self.last_name, 
                "phone_number": self.phone_number}
    
    