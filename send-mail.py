# coding: utf-8

# read the ReadMe note before using the code

import smtplib
from email.message import EmailMessage

MyEmail='xxxxx@gmail.com' # your mail
MyPassword='*******'      # your password


mailer= smtplib.SMTP('smtp.gmail.com', port=587)
mailer.starttls()
mailer.login(MyEmail,MyPassword )




file_1 = 'path to the first attached file'
with open(file_1, 'rb') as f1:
	my_cv=f1.read()
	my_cv_name='xxx.pdf'


file_2 = 'path to the second attached file'
with open(file_2, 'rb') as f2:
	my_LM=f2.read()
	my_LM_name='yyy.pdf'


liste='path to your contatc list/mailingList.csv'
with open(liste, 'r') as l:
	liste_mail= l.readlines()

Messages_envoyés=0
Messages_erreur =0
liste_mail_envoyé = open("path to and empty file in ordre to save sent emails /mail_envoye.txt","w+")
liste_mail_erreur = open("path to and empty file in ordre to save non-sent emails/mail_erreur.txt","w+")
for i in range(len(liste_mail)):
	try:
		msg = EmailMessage()
		receiver = ''.join(liste_mail[i].strip())
		msg['To'] = receiver
		msg['Subject'] = 'Choos a subject'
		msg['From'] = 'your name'
		msg.add_alternative("""\
		<!DOCTYPE html>
		<html>
		    <body>
		    <div id="i4c-draggable-container" style="position: fixed; z-index: 1499; width: 0px; height: 0px;">&nbsp;</div>
				<p><span>Bonjour</span></p>
        ..
        ..
        ..
				<p><span>Cordialement</span></p>

				<div id="i4c-dialogs-container">&nbsp;</div>
		    </body>
		</html>
		""", subtype='html')

		msg.add_attachment(my_cv, maintype='application', subtype=('octet-stream'), filename=my_cv_name)
		msg.add_attachment(my_LM, maintype='application', subtype=('octet-stream'), filename=my_LM_name)
		mailer.send_message(msg)
		Messages_envoyés+=1
		print('SUCCES ',Messages_envoyés,' : ',receiver)
		liste_mail_envoyé.write(receiver+ '\n')
	except:
		Messages_erreur+=1
		print('FAILD ',Messages_erreur,' : ',receiver)
		liste_mail_erreur.write(receiver + '\n')
		continue

print('envoye = ', Messages_envoyés)
print('echec = ', Messages_erreur)
mailer.quit()
