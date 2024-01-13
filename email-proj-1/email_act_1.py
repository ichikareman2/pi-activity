import yagmail

password = ""

with open("/home/pi/.local/share/.email_password", "r") as f:
    password = f.read()

yag = yagmail.SMTP("kevin.raspi.quing@gmail.com", password)
yag.send(to="kevin.raspi.quing@gmail.com",
         subject="Hello from raspi",
         contents="Hello from raspi (content)",
         attachments="/home/pi/Documents/code/email-proj-1/test_file.txt")
print("Email sent")
