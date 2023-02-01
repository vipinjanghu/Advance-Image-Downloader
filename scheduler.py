import pandas as pd
from datetime import datetime
from scrapper import scrape_images #scrape_download
from mailer import send_email
from app_logger import log

def job():
    try:
        df = pd.read_csv("scheduled_jobs.csv")

        for i in range(len(df)):
            if datetime.strptime(df["schedule_time"][i], "%Y-%m-%d %H:%M:%S") <= datetime.now():
                url=scrape_images(df['Name'][i])
                send_email(f"{df['email_id'][i]}", "Link to download images", f"Here is the link {url}\images\{df['Name'][i]}")
                df.drop(i,inplace=True)
                df.to_csv('scheduled_jobs.csv',index=False)
    except Exception as e:
        log().exception(e)

job()