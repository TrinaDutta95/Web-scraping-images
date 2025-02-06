import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib

def image_scraping(url):
    # Initialize driver
    driver = webdriver.Chrome()  
    driver.get(url)  

    # Scroll multiple times to load more images
    num_scrolls = 10  # Adjust this number to load more images
    for _ in range(num_scrolls):
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)  # Scroll to bottom
        time.sleep(5)  # Allow time for images to load

    # Now collect image elements
    img_results = driver.find_elements(By.XPATH, "//img[contains(@class, 'YQ4gaf')]")

    print(f"Total images found: {len(img_results)}")

    image_urls = set()

    for img in img_results:
        src = img.get_attribute("src")  # Fix: Use parentheses
        if src and "http" in src:  # Ensure valid URLs
            image_urls.add(src)

    # Convert set to list
    image_urls = list(image_urls)[:300]  # Limit to 300 images

    folderPath = "path/to/your/folder/to/save/images"

    # Download images
    for i, img_url in enumerate(image_urls):  
        try:
            file_path = os.path.join(folderPath, f"file_name_{i}.jpg")
            urllib.request.urlretrieve(img_url, file_path)
            print(f"Downloaded: {file_path}")
        except Exception as e:
            print(f"Failed to download {img_url}: {e}")

    # Close driver


    driver.quit()
    

if __name__=="__main__":
    url = "url to google search"
    image_scraping(url)