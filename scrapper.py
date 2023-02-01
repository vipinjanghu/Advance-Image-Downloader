import time
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from app_logger import log


def scrape_images(name,num_images=10):
    try:
        driver_path = r'chromedriver.exe'
        # # Create a webdriver object and set the path to the chromedriver executable
        driver = webdriver.Chrome(executable_path=driver_path)

        # Navigate to Google Images
        driver.get("https://www.google.com/imghp")

        # Find the search box element and enter your search query
        search_box = driver.find_element_by_name("q")
        search_box.send_keys(name)
        search_box.send_keys(Keys.ENTER)
        time.sleep(1)

        # Wait for the images to load
        driver.implicitly_wait(10)

        # Find all of the image elements on the page
        images = driver.find_elements_by_css_selector("img.rg_i")
        last_height = driver.execute_script(
            "return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );")
        count = 0
        img=[]
        # Iterate through the images and download them
        while count < num_images:
            for image in images:
                if count >= num_images:
                    break
                # Get the image source
                if image.get_attribute('src') and 'http' in image.get_attribute('src'):
                    img_src = image.get_attribute("src")

                    img.append(img_src)
                count =len(img)

            # Scroll down to the bottom of the page
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                load_more_button = driver.find_element_by_css_selector(".mye4qd")
                load_more_button.click()
            except:
                continue

            # Wait for the page to load
            time.sleep(1)

            new_height = driver.execute_script(
                "return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );")

            # If the new height is the same as the last height, then we have reached the end of the page
            if new_height == last_height:
                break

            # Find all of the image elements on the page
            images = driver.find_elements_by_css_selector("img.rg_i")

        # Close the webdriver
        driver.close()
        log().info("Successfully Get the Source links of images")
        #return img
    except Exception as e:
        log().exception(e)
    try:
        counter=1
        #img=scrape_images(name)
        for i in img:
            response = requests.get(i)
            if not os.path.exists(f"images/{name}"):
                os.makedirs(f"images/{name}")
            open(f"images/{name}/image{counter}.jpg", "wb").write(response.content)
            counter+=1
        log().info(f"Successfully Download the images:{name}")
        return os.getcwd()
    except Exception as e:
        log().exception(e)
#
# def scrape_download(name):
#     try:
#         counter=1
#         img=scrape_images(name)
#         for i in img:
#             response = requests.get(i)
#             if not os.path.exists(f"images/{name}"):
#                 os.makedirs(f"images/{name}")
#             open(f"images/{name}/image{counter}.jpg", "wb").write(response.content)
#             counter+=1
#         log().info(f"Successfully Download the images:{name}")
#         return os.getcwd()
#     except Exception as e:
#         log().exception(e)
#
#
#
