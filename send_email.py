import smtplib
from email.mime.text import MIMEText
import schedule
import time

class Email(object):
    def __init__(self):
        pass

    def send_email(self, sender_addr, sender_password, receiver_addr, subject, body):
        ret = {"ret_val":True, "data":"", "info":"normal operation"}
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender_addr
        msg['To'] = receiver_addr

        try:
            with smtplib.SMTP_SSL("smtp.qq.com", 465) as smtp:
                smtp.login(sender_addr, sender_password)
                smtp.send_message(msg)
                print("Sent email !!!")
        except:
            ret["ret_val"] = False
            ret["info"] = "Sent failed"

        return ret

    def job(self):
        sender = "3396497133@qq.com"
        passwords = "pfvcshzdlycqdbfg"
        receiver = "411379501@qq.com"
        subject = "test"
        body = "test python code"
        
        self.send_email(sender, passwords, receiver, subject, body)

if __name__ == '__main__':
    email = Email()
    schedule.every().day.at("10:53").do(email.job)

    while True:
        schedule.run_pending()
        time.sleep(0.5)
        print("Waiting for")