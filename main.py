import os
import datetime
import time
import unittest
from selenium import webdriver


def main():

    options = webdriver.ChromeOptions()
    # options.add_argument('window-size=1200x600')
    # options.add_argument('disable-gpu')
    # options.add_argument("remote-debugging-port=9223")
    options.add_argument("disable-dev-shm-usage")

    # options.add_argument("start-maximized")


    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        # desired_capabilities={
        #     'browserName': 'chrome',
        #     # 'javascriptEnabled': True
        # },
        options=options
    )

    driver.get('http://softwaretester.info/')

# def test_something(self):
#     dt_format = '%Y%m%d_%H%M%S'
#     cdt = datetime.datetime.fromtimestamp(time.time()).strftime(dt_format)
#     current_location = os.getcwd()
#     img_folder = current_location + '/images/'
#
#     if not os.path.exists(img_folder):
#         os.mkdir(img_folder)
#
#     picture = img_folder + cdt + '.png'
#     self.driver.save_screenshot(picture)
#
# def tearDown(self):
    driver.quit()


if __name__ == "__main__":
    main()