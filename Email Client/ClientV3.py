import smtplib
from email.mime.multipart import MIMEMultipart
import mimetypes
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

# -----------------------------
# SETTING UP ATTACHMENT TO SEND
# -----------------------------

# name of file to send 
fileToSend = "TestCSV.csv"

# to and from emails
strFrom = "testece4436lab3@gmail.com"
strTo = "testece4436lab3@gmail.com"

# finds out file type of "fileToSend"
ctype, encoding = mimetypes.guess_type(fileToSend)
if ctype is None or encoding is not None:
    ctype = "application/octet-stream"
maintype, subtype = ctype.split("/", 1)
print("Type of file to send: ",ctype)

# create the root message
msgRoot = MIMEMultipart('related')
msgAlternative = MIMEMultipart('alternative')
msgAlternative.attach(MIMEText("\r\n I love computer networks!"))
msgRoot.attach(msgAlternative)

# open file, add to "attachment" variable and encode
fp = open(fileToSend, "rb")
attachment = MIMEBase(maintype, subtype)
attachment.set_payload(fp.read())
fp.close()
encoders.encode_base64(attachment)

# add header to the attachment, add attachment to the message
attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
msgRoot.attach(attachment)

# --------------------------
# SETTING UP SMTP CONNECTION 
# --------------------------

print("STARTING SMTP CONNECTION\n")
smtp = smtplib.SMTP()
mailserver = smtplib.SMTP('smtp.gmail.com',587)

print("SENDING EHLO COMMAND\n")
mailserver.ehlo()

print("ESTABLISHING SECURE TLS CONNECTION\n")
mailserver.starttls()

print("RE-SENDING EHLO COMMAND\n")
mailserver.ehlo()

print("SENDING LOGIN CREDENTIALS\n")
mailserver.login('testece4436lab3@gmail.com', 'ece4436lab3')

print("PROCESSING AND SENDING YOUR EMAIL\n")
mailserver.sendmail(strFrom, strTo, msgRoot.as_string())

mailserver.quit()
print ('MESSAGE HAS BEEN SENT!')

