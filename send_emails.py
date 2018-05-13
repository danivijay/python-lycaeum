import smtplib
import csv
import smtplib
from email.mime.text import MIMEText

# http://thelycaeum.in/example.csv

def construct_email(name, course):
    template = """Hello {},

You signed up for the '{}' course. This is a confirmation email.

Thanks!"""
    return template.format(name, course)

    

def get_password():
    f = open("gmailpw.txt")
    pw = f.read()
    f.close()
    return pw



def send_email(frm, to_name, to_addr, subject, body):
    msg = MIMEText(body)
    msg['To'] = "{} <{}>".format(to_name, to_addr)
    msg['From'] = "Noufal Ibrahim<{}>".format(frm)
    msg['Subject'] = subject

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("noufal@gmail.com", get_password())
    s.sendmail('noufal@gmail.com',
               [to_addr],
               msg.as_string())
    


def parse_file(fname, course):
    f = open(fname)
    reader = csv.reader(f)

    for i in reader:
        email = i[1]
        name = i[2]
        courses = i[3]
        if course in courses:
            print ("Sending email to {}".format(name))
            content = construct_email(name, course)
            send_email("noufal@gmail.com", name, email, "Registration for {} course".format(course), content)

    f.close()

parse_file("example.csv", "Introduction to Python")
        
