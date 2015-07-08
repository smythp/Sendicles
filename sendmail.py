import smtplib
import csv

# Credentials
username = 'example@gmail.com'
password = '#######'
sender_first = 'Your First Name'
sender_last = 'Your Last Name'

fromaddr = username

from jinja2 import Environment, PackageLoader,Template
env = Environment(loader=PackageLoader('emails', 'templates'))
template = env.get_template('email1.html')

with open('list.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        email_number = row['Number']
        toaddr  = row['Email']
        last = row['Last']
        valediction = row['Valediction']
        company = row['Company']
        first = row['First']
        subject = row['Subject']
        position = row['Position']
        email_out = template.render(email_number=email_number,
                                    toaddr=toaddr,
                                    fromaddr=fromaddr,
                                    first=first,
                                    company=company,
                                    position=position,
                                    valediction=valediction,
                                    sender_first=sender_first,
                                    sender_last=sender_last,
                                    last=last,
                                    subject=subject)
        #print(email_out)
        print("Sending message %s..." % (email_number))
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, toaddr, email_out)
        print('''Message sent
        ''')
server.quit()
print('Done')
