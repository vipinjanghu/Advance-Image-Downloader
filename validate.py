import requests
from app_logger import log

def validator(email):
    """
    It will validate a email id exist or not .
    :param email: Email address of the person
    :return: email exist or not
    """
    try:
        res = requests.get("https://isitarealemail.com/api/email/validate", params={'email': email})
        status = res.json()['status']
        if status == "valid":
            log().info(f"Email verified and exist: {email}")
        else:
            log().info(f"Something wrong with email id: {email}")
        return status
    except Exception as e:
        log().exception(e)