from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

webdriver_path="C:\development\chromedriver_win32\chromedriver.exe"
website_path="https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
driver=webdriver.Chrome(executable_path=webdriver_path)
driver.get(website_path)

sign_in_btn=driver.find_element_by_xpath('/html/body/div[1]/header/nav/div/a[2]')
sign_in_btn.click()

my_email="rawadkady@gmail.com"
my_password="rawad.18"

input_email=driver.find_element_by_id("username")
input_email.click()
input_email.send_keys(my_email)

input_password=driver.find_element_by_id("password")
input_password.click()
input_password.send_keys(my_password)

complete_sign_in=driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
complete_sign_in.click()


time.sleep(5)

all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)
# #press first job
# first_job=driver.find_element_by_xpath('//*[@id="ember203"]')
# first_job.click()

#press easy apply
    try:
        easy_apply_btn=driver.find_element_by_xpath('//*[@id="ember347"]/span')
        easy_apply_btn.click()
        time.sleep(5)

        phone =driver.find_element_by_class_name("fb-single-line-text__input")



    #click submit application
        submit_application_btn=driver.find_element_by_css_selector("footer button")
        if submit_application_btn.get_attribute("data-control-name")=="continue_unify":
            close_btn=driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_btn.click()
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_application_btn.click()
        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()
    except NoSuchElementException:
        print("No application button, skipped.")
        continue