
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
    msg['Subject'] = "Auftrag vom Nordpol (Jetzt der Richtige)"

    emailText = "Hallo "+Wichtel  +", ich brauche deine Hilfe! \n Die Gesundheitsbehörde auf dem Nordpol hat die 2G Regelung am Arbeitsplatz eingeführt. \n da sehr viele meiner Mitarbeiter noch nicht geimpft sind, sind wir somit mit der Geschenkelieferung im Zeitdruck. Daher würde ich dich bitten, für  "+ empfaenger +" beim gemeinsamen Weihnachtsfest ein kleines Wichtel Geschenk zu organisieren. \r Liebe Grüße und HOHOHOHOHO dein Weihnachtsmann "
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
    ("Janina", "janinaernst@yahoo.de"), ("Micha", "Michael.Maßow@outlook.com".encode()), ("Simon", "simon@simon-steigner.de"), ("Alina", "alinaschmitthenner@aol.com")]
empfanger= Wichtelliste

while (x< 8):
    Wichtel = random.sample(Wichtelliste,1)
    empfaenger= random.sample(empfanger,1)
    if(Wichtel[0][0]=="Micha"):
        x=x+1
        print(empfaenger[0][0])
        Wichtelliste = [elem for elem in Wichtelliste if elem not in Wichtel]
        empfanger = [elem for elem in empfanger if elem not in empfaenger]
        
    elif(Wichtel[0][0]!=empfaenger[0][0]):
        #wichtelmail(Wichtel[0][0],Wichtel[0][1],empfaenger[0][0])
        #print("Wichtel", Wichtel[0][0], "mit Mail", Wichtel[0][1], "schenkt", empfaenger[0][0])
        Wichtelliste= [elem for elem in Wichtelliste if elem not in Wichtel]
        empfanger=[elem for elem in empfanger if elem not in empfaenger]
        x=x+1
        #print(x,Wichtel,empfaenger)


