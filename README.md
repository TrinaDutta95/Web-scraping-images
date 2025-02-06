# Web-scraping-images
This repository contains a step-by-step tutorial on how to scrape images from a web search. This can be useful for data preparation or dataset construction for ML or Data Science projects or any other project that needs loads of images.

## Pre-requisites to run this project
* Python 3.10>
* Google Chrome and Chrome driver
* Selenium
* pillow (optional for post processing images)

## Google Chrome Driver

Assuming you already have Google Chrome installed in your machine, the next step would be to install Google Chrome Driver. This will help us getting the images from google search.
1. First check the version of your Google Chrome- this will be necessary to download the specific driver
2. Select the version from [ChromeDriver](https://developer.chrome.com/docs/chromedriver/downloads) page, if you have the latest version of Chrome, you can directly go to the [ChromeforTesting dashboard](https://googlechromelabs.github.io/chrome-for-testing/) and download the correct driver based on your OS requirement.
3. Unzip the downloaded folder


## Install Selenium/PIL
This can be done using the pip command
```
pip install Selenium pillow
```

## Get the images in bulk
Once you have installed everything, you are almost done! All you have to do is run the python file to download the images you want in bulk.
* Make sure to change the folder path in the code
* Go to Google search and type the subject you want images of, for example: "dog". Go to the image option and you will see images pop up. Copy the url from the top of the page and put that in the code.
* Check the image tag "<img ...>". You can do this by right clicking on the search page and select "Inspect". Find the class of the images, this can change from time to time but at this moment the class value is "YQ4gaf".

```
python3 image_scraping.py
```
If everything goes well, you can bulk download images of your subject!
