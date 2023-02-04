import smtplib
from constant import email_id,password
from  app_logger import log

def send_email(to,subject, body):
    """
    It will send email along with the path where we stored the images
    :param to: person email_id who schedule the job
    :param subject: Subject of mail templete
    :param body: what we want to write inside the mail.
    """
    try:
        # Connecting to the email server
        server = smtplib.SMTP('smtp.gmail.com', 587)

        # Starting a secure connection to the email server
        server.starttls()

        # Logging into the email account
        server.login(email_id,password)

        # Creating the message to be sent
        message = f"Subject: {subject}\n\n{body}"

        # Sending the email
        server.sendmail(email_id, to, message)

        # Closing the connection to the email server
        server.quit()

        # Logging a success message
        log().info(f"Successfully sent the link of images to :{to}")
    except Exception as e:
        # Logging the error message in case of an exception
        log().exception(e)
