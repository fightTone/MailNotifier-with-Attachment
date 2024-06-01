# MailNotifier-with-Attachment

python script for notifying running status with file attachment


Pre-requisite

1. Go toyour Google Account
2. Manage Google Account
3. Go to security, look for App Passwords (or you can search directly  for "App Passwords")
   Note: make sure you enable your 2 factor before doing this
4. Enter the App name then copy the password provided
5. put your password in the credentials.json and replace the "passkey" : "you-own-passkey", along with the other details

   ```
   {
   	"mail_sender" : "youSir@gmail.com",
   	"passkey" : "you-own-passkey",
   	"reciever" : [
           "workmate1@sample.com",
           "workmate2@mail.com",
           "manager@gmail.com",
           "someone@yahoo.com"
       ]
   }

   ```

you can now import MailSender in your own usage, and pass your parameters

```
from test_email import MailSender

ms = MailSender(subject, message, file_attachment_path)
ms.sendmail()
```
