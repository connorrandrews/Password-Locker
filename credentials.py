#This Script was created by Connor Andrews, Please DO NOT COPY
class Credentials:

    credentials_list = []

    def __init__(self,credentials_name,usr_name,password,email):
        self.credentials_name = credentials_name
        self.usr_name = usr_name
        self.password = password
        self.email = email    

    def save_credentials(self):



        Credentials.credentials_list.append(self)    


    def delete_credentials(self):



        Credentials.credentials_list.remove(self)   


    @classmethod
    def find_by_name(cls,name):
        for credentials in cls.credentials_list:
            if credentials.credentials_name == name:
                return credentials  


    @classmethod
    def credentials_exist(cls,name):

        for credentials in cls.credentials_list:
            if credentials.password == name:
                    return credentials

        return False      


    @classmethod
    def display_credentials(cls):  #check this line later

        return cls.credentials_list            
                      