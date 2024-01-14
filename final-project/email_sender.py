import yagmail

class EmailSender():
    _password = ""

    def __init__(self):
        with open("/home/pi/.local/share/.email_password", "r") as f:
            self._password = f.read()
            self.yag = yagmail.SMTP("kevin.raspi.quing@gmail.com", self._password)
    
    def send_email(self, to, subject, contents, attachments):
        self.yag.send(to=to,
                 subject=subject,
                 contents=contents,
                 attachments=attachments)
        print("Email sent")