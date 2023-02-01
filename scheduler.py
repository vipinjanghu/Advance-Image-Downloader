import pandas as pd
from datetime import datetime
from scrapper import scrape_images
from mailer import send_email
from app_logger import log

def job():
    """
    It will run all the task at a specific time
    """
    try:
        df = pd.read_csv("scheduled_jobs.csv")

        # Iterate over each row in the dataframe
        for i in range(len(df)):
            # Check if the schedule time has passed
            if datetime.strptime(df["schedule_time"][i], "%Y-%m-%d %H:%M:%S") <= datetime.now():
                # Call the scrape_images function and pass the name
                url = scrape_images(df['Name'][i])
                # Call the send_email function and pass the email ID and message
                send_email(f"{df['email_id'][i]}", "Link to download images",
                           f"Here is the link {url}\images\{df['Name'][i]}")
                # Drop the row from the dataframe and save the updated dataframe to the CSV file
                df.drop(i, inplace=True)
                df.to_csv('scheduled_jobs.csv', index=False)
    except Exception as e:
        # Log the exception message
        log().exception(e)