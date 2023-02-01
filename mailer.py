import smtplib
from  app_logger import log

def send_email(to,subject, body):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("vipinjanghu40@gmail.com", "muzxanmxabiyvxft")
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail("vipinjanghu40@gmail.com",to, message)
        server.quit()
        log().info(f"Successfully sent the link of images to :{to}")
    except Exception as e:
        log().exception(e)

