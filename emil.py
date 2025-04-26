import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import yaml


def send_email(subject: str, body: str):
    with open("./config.yaml", "r", encoding="utf-8") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    server = smtplib.SMTP(config["smtp"]["host"], config["smtp"]["port"])
    server.starttls()
    server.login(config["from_email"], config["from_email_password"])
    msg = MIMEMultipart()
    msg["From"] = config["from_email"]
    msg["To"] = config["to_email"]
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))
    text = msg.as_string()
    server.sendmail(config["from_email"], config["to_email"], text)
    server.quit()


if __name__ == "__main__":
    send_email("测试邮件", "测试邮件体")
