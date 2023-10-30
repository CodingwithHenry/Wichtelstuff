
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage



def wichtelmail(Wichtel , Wichtelemail , empfaenger):
    senderEmail = "defnitivnichtderweihnachtsmann@gmail.com"


    empfangsEmail = Wichtelemail
    msg = MIMEMultipart()
    msg['From'] = senderEmail
    msg['To'] = empfangsEmail
    msg['Subject'] = "Auftrag vom Nordpol"
    html_message='''<!DOCTYPE html>
<html>
<head>
    <style>
        /* Style for the red banners */
        .red-banner {{
            background-color: rgb(29, 27, 139);
            color: white;
            text-align: center;
            padding: 100px;
            width: 100%;
            font-size: 24px;
        }}

        /* Style for the main content area with the background image */
        .content {{
            
            background-size: 100% ;
            background-repeat: no-repeat;
            background-position: center;
            text-align: center;
            padding: 950px;
           
            align-items: center; /* Center-align text horizontally */
             /* Increase content area width */
        }}
        .content h1, .content p {{
            font-size: 24px;
            color: rgb(76, 12, 224);
            text-align: center; /* Center-align text horizontally within content */
        }}
    </style>
</head>
<body>
    <div class="red-banner">
        <!-- Top red banner content goes here -->
        Hallo {schenker}
        Es ist mal wieder soweit und Weinachten steht vor der Tür.
            Allerdings habe ich überhaupt keinen Bock und brauche daher mal wieder deine Hilfe.
            Bitte kümmere dich darum das du {beschenkter} eine Freude* machst und Ihm oder Ihr eine Geschenk besorgst.
            Leg das Geld** erstmal für mich aus. Ich überweise dir das dann (vielleicht) irgendwann wieder.
            Danke fürs Erledigen.   <br>         
            Der Weihnachtsmann
    </div>


    <div class="red-banner">
        <!-- Bottom red banner content goes here -->
        *Die Weihnachtsmann&CO KG. übernimmt keine Verantwortung für die Freude über das Geschenk **25€ 
    </div>
</body>
</html>
'''.format(schenker=Wichtel,beschenkter=empfaenger)
    emailText = "Hallo "+Wichtel  +" nach einigen technischen Schwierigkeiten ist dies nun dein endgültiger Auftrag für Weihnachten. Denn wie du sicherlich weißt, wurde auf dem Nordpol 2g Regelungen am Arbeitsplatz eingeführt. Da viele meiner Mitarbeiter noch nicht geimpft sind können diese nun nicht Arbeiten kommen. Homeoffice ist auch schwierig in meiner Branche. Daher würde ich dich bitten, für" + empfaenger+" eine Kleinigkeit für das Weihnachtsfest im Hause Beiker/Ernst mitzubringen. Vielen dank im vorraus. Dein Weihnachtsmann ps. Wenn es jetzt auch nicht funktioniert hat wird das ganze halt Analog gemacht ich bin sowieso nicht überzeugt von diesem ganzen Technick schnick schnack"
    msg=MIMEMultipart()
    msg.attach(MIMEText(html_message,'html'))
    msg['Subject']="Top Secret - Nur Öffnen wenn alleine"

    image = open("bild.png", "rb").read()
    image_part = MIMEImage(image, name="bild.png")
    image_part.add_header("Content-ID", "<image>")
    msg.attach(image_part)

    server = smtplib.SMTP('smtp.gmail.com', 587)  # Die Server Daten
    server.starttls()
    server.login(senderEmail, "xqqo uafz xclz dbks")  # Das Passwort
    #text = msg.as_string()
    server.sendmail(senderEmail, empfangsEmail,msg.as_string())
    server.quit()
    print("Email sent")



def partnerCheck(partner_1:str,partner_2:str):
    
    partner = [("Ellen", "Simon"), ("Katja", "Thomas"),
               ("Henry", "Alina"), ("Janina", "Micha")]
    paar_1=(partner_1,partner_2)
    paar_2=(partner_2,partner_1)
    
    
    if paar_1 in partner:
        
        return False
    if  paar_2 in partner:
        
        return False
    
    return True


def checkPairings(Wichtelpartnerliste:list()):
    
    for pair in Wichtelpartnerliste:
        
        if pair[0][0]==pair[1][0] or not partnerCheck(pair[0][0],pair[1][0]):
            
            return False
    
    return True

        
def createPairing():
    Wichtelliste=[("Henry","HenryBeiker@aol.com"),("Ellen","ellen.beiker@aol.com"),
("Katja","KatjaBeiker@aol.com"),("Thomas","thomsen69@arcor.de"),
    ("Janina", "janinaernst@yahoo.de"), ("Micha", "michael.massow@outlook.com"), ("Simon", "simon@simon-steigner.de"), ("Alina", "alinaschmitthenner@aol.com")]
    empfanger= Wichtelliste

    wichtelpartner=list()
    x=0
    while (x< 8):
        Wichtel = random.sample(Wichtelliste,1)
        
        empfaenger= random.sample(empfanger,1)
        wichtelpartner.append((Wichtel[0],empfaenger[0]))
        Wichtelliste= [elem for elem in Wichtelliste if elem not in Wichtel]
        empfanger=[elem for elem in empfanger if elem not in empfaenger]
        x=x+1
    return wichtelpartner

def everyoneGetsSomething(wichtelpairing):
    empfeanger=set()
    sender=set()
    for pair in wichtelpairing:
        sender.add(pair[0][0])
        empfeanger.add(pair[1][0])
    
    if (len(empfeanger),len(sender)) ==(8,8):
        
        return False
    else :
        return True

wichtelpartner = createPairing()

everyoneGets=True

while(not checkPairings(wichtelpartner) or everyoneGets ):
    wichtelpartner=createPairing()
    everyoneGets=everyoneGetsSomething(wichtelpartner)

for pair in wichtelpartner:
    
    schenker= pair[0][0]
    schenkermail=pair[0][1]
    beschenkter=pair[1][0]
    
    
    wichtelmail(schenker,schenkermail,beschenkter) #auskommentieren zum abschicken der mails
    
    

     
        #print(x,Wichtel,empfaenger)
print("Alles abgeschickt")

