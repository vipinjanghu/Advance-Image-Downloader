import csv
from datetime import datetime
from app_logger import  log

def save_to_csv(name, time, email_id):
    # Convert the input time to a datetime object
    try:
        schedule_time = datetime.strptime(time, "%Y-%m-%d %H:%M")

        # Open a CSV file in write mode
        with open("scheduled_jobs.csv", "a",newline='') as csvfile:
            # Create a CSV writer object
            csv_writer = csv.writer(csvfile)

            # Write the name, schedule time, and email_id to the CSV file
            #csv_writer.writerow(["Name", "schedule_time", "email_id"])
            csv_writer.writerow([name, schedule_time, email_id])
            log().info(f"Successfully scheduled {name } at {schedule_time} by {email_id}")
    except Exception as e:
        log().exception(e)
