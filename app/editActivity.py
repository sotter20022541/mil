from getDatabase import *

class editActivity :

    def add(self,ID,dicAct):

        nameAct = dicAct['nameAc']
        typeAct = dicAct['type']
        dateAct = dicAct['date']
        photoAct = dicAct['photo']
        advisorAct = dicAct['advisor']
        desAct = dicAct['des']
        fileAct = dicAct['File']

        add = Add_Method(ID)
        re = return_Method(ID)

        nameAct = nameAct.replace(" ","")
        if nameAct != "":
            ID = add.Act_name(nameAct)
            if typeAct != "":
                add.Act_type(ID,typeAct,nameAct)
            if dateAct != "":
                add.Act_date(ID,dateAct,nameAct)
            if photoAct != "":
                add.Act_photo(ID,photoAct,nameAct)
            elif photoAct == "":
                photoAct = "en1.png"
                add.Act_photo(ID,photoAct,nameAct)
            if advisorAct != "":
                add.Act_advisor(ID,advisorAct,nameAct)
            if desAct != "":
                add.Act_des(ID,desAct,nameAct)
            if fileAct != "":
                add.Act_file(ID,fileAct,nameAct)

    def edit(self,ID,nameAct,dicAct,idAct):

        typeAct = dicAct['type']
        dateAct = dicAct['date']
        #photoAct = dicAct['photo']
        advisorAct = dicAct['advisor']
        desAct = dicAct['des']
        #fileAct = dicAct['File']

        add = Add_Method(ID)
        re = return_Method(ID)

        if typeAct != "":
            add.Act_type(idAct,typeAct,nameAct)
        if dateAct != "":
            add.Act_date(idAct,dateAct,nameAct)
        #if photoAct != "":
            #add.Act_photo(idAct,photoAct,nameAct)
        if advisorAct != "":
            add.Act_advisor(idAct,advisorAct,nameAct)
        if desAct != "":
            add.Act_des(idAct,desAct,nameAct)
        #if fileAct != "":
            #add.Act_file(idAct,fileAct,nameAct)
