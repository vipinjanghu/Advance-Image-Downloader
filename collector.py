import csv
from datetime import datetime
from app_logger import  log

def save_to_csv(name, time, email_id):
    """
    It will collect data from the person who wangt to scrape images and store then in a csv file for schedule at
    specific time
    :param name: Name of the object which we want to scrape
    :param time: At what time we want to scrape that specific object images along with date
    :param email_id: Email address of the person to notify him that his task is done.
    """
    # Convert the input time to a datetime object
    try:
        # Convert the input time to a datetime object
        schedule_time = datetime.strptime(time, "%Y-%m-%d %H:%M")

        # Open a CSV file in append mode
        with open("scheduled_jobs.csv", "a", newline="") as csvfile:
            # Create a CSV writer object
            csv_writer = csv.writer(csvfile)

            # Write the name, schedule time, and email_id to the CSV file
            csv_writer.writerow([name, schedule_time, email_id])

        log().info(f"Successfully scheduled {name} at {schedule_time} by {email_id}")
    except Exception as e:
        log().exception(e)
