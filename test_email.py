import smtplib
import json
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

class MailSender:
    def __init__(self, subject, message, file_attachment_path):
        with open("credentials.json", "r") as f:
            creds = json.load(f)
        self.sender_email = creds["mail_sender"]
        self.sender_password = creds["passkey"]
        self.recipient_emails = creds["reciever"]
        self.subject = subject
        self.body = message
        self.path_to_file = file_attachment_path
        self.smtp_server = 'smtp.gmail.com'
        self.smtp_port = 587

    def sendmail(self):
        message = MIMEMultipart()
        message['Subject'] = self.subject
        message['From'] = self.sender_email
        message['To'] = ", ".join(self.recipient_emails)
        body_part = MIMEText(self.body)
        message.attach(body_part)

        if self.path_to_file:
            filename = os.path.basename(self.path_to_file)
            with open(self.path_to_file, 'rb') as file:
                message.attach(MIMEApplication(file.read(), Name=filename))

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, self.recipient_emails, message.as_string())

        print(f"Email sent to {', '.join(self.recipient_emails)}")

if __name__ == "__main__":
    subject = "Test 6: Testing Python with File Attachment"
    message = "TEST 6: get base filename of any file attached"
    filepath = r"C:\Users\qgee1\Downloads\Default_adventure_esekai_anime_world_for_adventurer_where_hero_1_c39d0968-c9b4-432c-8dc1-cb8fac044262_1.jpg"
    ms = MailSender(subject, message, filepath)
    ms.sendmail()
