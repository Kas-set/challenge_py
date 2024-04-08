import smtplib

email = input("Adrese de l'expéditeur: ")
receiver_email = input("Adresse du destinataire: ")

subject = input("Subject: ")
message = input("Message: ")

text = f"Subject: {subject}\n\n {message}"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(email, "")
server.sendmail(email, receiver_email, text)

print("Email has been sent to: ", receiver_email)
 
