import os.path
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm

class saveText():

    def create(self,ID,Profile,Activity = None):

        name = 'Portfolio_'+ str(ID) + '.pdf'
        Protfolio = canvas.Canvas(name)
        Protfolio.drawString(40, 800 , 'Protfolio')
        Protfolio.drawString(40, 780 , 'Profile')

        for profile in Profile:
            Protfolio.drawString(40, 765 , 'Name : ' + str(profile['name']) + "  " + str(profile['sur']))
            Protfolio.drawString(40, 750 , 'Date of birth : ' + str(profile['dateofbirth']) )
            Protfolio.drawString(40, 735 , 'Nationality : ' + str(profile['nation']))
            size = 720
            if profile['contact'] != None :
                Protfolio.drawString(40, size , 'Contact')
                size -= 15
                Protfolio.drawString(40, size , str(profile['phone']))
                size -= 15
                Protfolio.drawString(40, size , str(profile['email']))
                size -= 15
                Protfolio.drawString(40, size , str(profile['address']))
                size -= 15
            if profile['dis'] != None:
                Protfolio.drawString(40, size , str(profile['dis']))
                size -= 15
            if profile['birthplace'] != None:
                Protfolio.drawString(40, size , str(profile['birthplace']))
                size -= 15
            if profile['gpax'] != None:
                Protfolio.drawString(40, size , str(profile['gpax']))




        if Activity != [] :
            num = 0
            for Act in Activity:
                size -= 20
                num += 1
                Protfolio.drawString(40, size , '-- Activity ' + str(num) + " --")
                size -= 15
                Protfolio.drawString(40, size ,'Name Activity : ' + str(Act['Name_Activity']))
                size -= 15
                Protfolio.drawString(40, size , 'Type Activity : ' + str(Act['Type']))
                size -= 15
                Protfolio.drawString(40, size , 'Date Activity : ' + str(Act['Date_Activity']))


        Protfolio.save()
