
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

x=0
def wichtelmail(Wichtel , Wichtelemail , empfaenger):
    senderEmail = "defnitivnichtderweihnachtsmann@gmail.com"


    empfangsEmail = Wichtelemail
    msg = MIMEMultipart()
    msg['From'] = senderEmail
    msg['To'] = empfangsEmail
    msg['Subject'] = "Finaler Auftrag vom Nordpol"

    emailText = "Hallo "+Wichtel  +" nach einigen technischen Schwierigkeiten ist dies nun dein endgültiger Auftrag für Weihnachten. Denn wie du sicherlich weißt, wurde auf dem Nordpol 2g Regelungen am Arbeitsplatz eingeführt. Da viele meiner Mitarbeiter noch nicht geimpft sind können diese nun nicht Arbeiten kommen. Homeoffice ist auch schwierig in meiner Branche. Daher würde ich dich bitten, für" + empfaenger+" eine Kleinigkeit für das Weihnachtsfest im Hause Beiker/Ernst mitzubringen. Vielen dank im vorraus. Dein Weihnachtsmann ps. Wenn es jetzt auch nicht funktioniert hat wird das ganze halt Analog gemacht ich bin sowieso nicht überzeugt von diesem ganzen Technick schnick schnack"
    msg.attach(MIMEText(emailText, 'html'))

    server = smtplib.SMTP('smtp.gmail.com', 587)  # Die Server Daten
    server.starttls()
    server.login(senderEmail, "Willi5366")  # Das Passwort
    text = msg.as_string()
    server.sendmail(senderEmail, empfangsEmail, text)
    server.quit()
    print("Email sent")

Wichtelliste=[("Henry","HenryBeiker@aol.com"),("Ellen","ellen.beiker@aol.com"),
("Katja","KatjaBeiker@aol.com"),("Thomas","thomsen69@arcor.de"),
    ("Janina", "janinaernst@yahoo.de"), ("Micha", "michael.massow@outlook.com"), ("Simon", "simon@simon-steigner.de"), ("Alina", "alinaschmitthenner@aol.com")]
empfanger= Wichtelliste

partner=[("Ellen","Simon"),("Katja","Thomas"),("Henry","Alina"),("Janina","Micha")]

def partnerCheck(partner_1:str,partner_2:str):
    partner = [("Ellen", "Simon"), ("Katja", "Thomas"),
               ("Henry", "Alina"), ("Janina", "Micha")]
    if (partner_1,partner_2) in partner:
        return False
    if (partner_2,partner_1) in partner:
        return False
    return True
wichtelpartner=list(tuple())

def checkPairings(Wichtelpartnerliste:list(),partner):
    for pair in Wichtelpartnerliste:
        if pair[0]==partner[1] or not partnerCheck(pair[0],pair[1]) :
            return False
    return True

        

while (x< 8):
    Wichtel = random.sample(Wichtelliste,1)
    empfaenger= random.sample(empfanger,1)
    wichtelpartner.append((Wichtel,empfaenger))
    x=x+1

while(not checkPairings(wichtelpartner,partner)):
    wichtelpartner.clear()
    while (x < 8):
        Wichtel = random.sample(Wichtelliste, 1)
        empfaenger = random.sample(empfanger, 1)
        wichtelpartner.append((Wichtel, empfaenger))
        x = x+1

for pair in wichtelpartner:
    print(pair)
    '''
    if (Wichtel[0][0]!=empfaenger[0][0] and partnerCheck(Wichtel[0][0],empfaenger[0][0])):
        #wichtelmail(Wichtel[0][0],Wichtel[0][1],empfaenger[0][0]) #auskommentieren zum abschicken der mails
        print("Wichtel", Wichtel[0][0], "mit Mail", Wichtel[0][1], "schenkt", empfaenger[0][0])
        Wichtelliste= [elem for elem in Wichtelliste if elem not in Wichtel]
        empfanger=[elem for elem in empfanger if elem not in empfaenger]
        '''
        #print(x,Wichtel,empfaenger)
print("Alles abgeschickt")

