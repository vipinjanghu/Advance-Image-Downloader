 # Advance-Image-Downloader

## Introduction
The Image Downloader is a Python script that can be used to download thousands of images from the internet for given requirements (e.g. Cat, Dog). It makes use of web scraping techniques to extract the images and store them in our machine.

## Requirements
* Python >=3.7
* Requests library
* Selenium library
* Flask library
* Apsscheduler library
* Smtplib
## How to run the script
Clone or download the repository to your local machine
Install the required libraries using pip
Enter the required details in the script (Name, schedule time, and email Id)
Run the script using the command python app.py
## Functionality
The Image Downloader script performs the following functions:

* Extracts images for the given requirements (e.g. Cat, Dog)
* Schedules the job to perform the scraping
* Sends an email to the requester with a URL to download the extracted images after the job completion(As of Now we are not using any cloud services so it will give us the path of the folder where it stores the images.)
## Scheduling the job
To schedule the job, you need to provide the following details:

* Name: The name of the job (e.g. Cat, Dog)
* Timing: The schedule time for the job in the format "YYYY-MM-DD HH:MM" (e.g. "2021-07-20 04:00")
* Email Id: The email Id of the requester
## Email Notification
After the job completion, the requester will receive an email from the Image Downloader with a URL(path of folder) to download the extracted images. The email will be sent from the same email Id that was provided while scheduling the job.

## Note:
Before running the script please provide the eamil id and password of that it in the constant.py .Also If you are downloading thousands of images it will take some time to extract them form the internat.

## Contributing:
Suggestion are open .
If you would like to contribute to the project, please create a pull request with your changes
