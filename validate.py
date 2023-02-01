import requests
from app_logger import log

def validator(email):
    try:
        res=requests.get("https://isitarealemail.com/api/email/validate", params={'email':email})
        status = res.json()['status']
        if status=="valid":
            log().info(f"Email verified and exist :{email}")
        else:
            log().info(f"Something Wrong with email id  :{email}")
        return status
    except Exception as e:
      log().exception(e)