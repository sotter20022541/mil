class keepID():

    def __init__(self, ID=None, Password=None, Name = None):
        self.ID = ID
        self.Password = Password
        self.Name = Name

    def Print_ID(self):
        print(self.ID)
        print(self.Password)
        ptint(self.Name)

    def reset_keepID(self):
        self.ID = None
        self.Password = None
        self.Name = None
