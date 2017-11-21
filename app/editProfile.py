from getDatabase import *

class editProfile():
    def edit(self,ID,dicProfile):
        print(ID)
        print(dicProfile)
        name = dicProfile["name"]
        surname = dicProfile["surname"]
        nation = dicProfile["nation"]
        birth = dicProfile["bd"]
        birthplace = dicProfile["bp"]
        disease = dicProfile["dis"]
        emerphone = dicProfile["emerphone"]
        reletive = dicProfile["reletive"]
        phone = dicProfile["phone"]
        email = dicProfile["email"]
        address = dicProfile["address"]
        print (name,surname,nation,birth,birthplace,disease,emerphone,reletive,phone,address,email)

        add = Add_Method(ID)
        re = return_Method(ID)
        if name != "":
            add.name(name)
        if surname != "":
            add.surname(surname)
        if nation != "":
            add.nation(nation)
        if birth != "":
            add.date(birth)
        if birthplace != "":
            add.birth(birthplace)
        if disease != "":
            add.edit_disease(re.disease(),disease)
        if emerphone != "":
            add.phoneEmer(emerphone)
        if reletive != "":
            add.relative(reletive)
        if phone != "":
            add.phonestu(phone)
        if email != "":
            print(email)
            add.email(email)
        if address != "":
            add.address(address)
