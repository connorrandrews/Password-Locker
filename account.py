#This Script was created by Connor Andrews, Please DO NOT COPY
class Account:

    account_list = []

    def __init__(self,account_name,user_name,password,email):
        self.account_name = account_name
        self.user_name = user_name
        self.password = password
        self.email = email
    

    def save_account(self):



        Account.account_list.append(self)


    def delete_account(self):



        Account.account_list.remove(self)    
    @classmethod
    def find_by_name(cls,name):
        for account in cls.account_list:
            if account.account_name == name:
                return account    
    

    @classmethod
    def account_exist(cls,name):

        for account in cls.account_list:
            if account.password == name:
                    return account

        return False
    @classmethod
    def display_accounts(cls):

        return cls.account_list    