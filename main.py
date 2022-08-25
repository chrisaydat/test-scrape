from socket import timeout
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome(ChromeDriverManager(cache_valid_range=0).install())
link = "https://appstoreconnect.apple.com/analytics/app/d30/1608146534/overview?iaemeasure=totalDownloads"
driver.get(link)
def apple_login():
 driver.get("https://appstoreconnect.apple.com/analytics/app/d30/1608146534/overview?iaemeasure=totalDownloads")
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"aid-auth-widget-iFrame")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "account_name_text_field"))).send_keys("chris@myladder.africa")
driver.find_element_by_id().click()
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"aid-auth-widget-iFrame")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "password_text_field"))).send_keys("enter password")
#driver.find_element_by_id ("password_text_field").send_keys(""")

driver.find_element_by_id ("sign_in_button").click()
time.sleep(5)
try:
    element_present = EC.presence_of_element_located((By.ID, 'container'))
    WebDriverWait(driver, timeout).until(element_present)

    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    Impressions =soup.find().text
    Productpageviews = soup.find().text
    Conversionrate = soup.find().text
    Totaldownloads = soup.find().text
    Sessionperactiveusers = soup.find().text
    Crashes = soup.find().text
    TotaldownloadsbyTerritory = soup.find().text
    Totaldownloadsbysource = soup.find().text
    Totaldownloadsbydevice = soup.find().text
    Averageretention = soup.find().text
    result = {
        "Impressions" : Impressions,
        "Product_page_views" : Productpageviews,
        "conversion_rate" : Conversionrate,
        "Totaldownloads" : Totaldownloads,
        "Session_per_active_users" : Sessionperactiveusers,
        "Crashes" : Crashes,
        "Totaldownloads_by_Territory" : TotaldownloadsbyTerritory,
        "Totaldownloads_by_source" : Totaldownloadsbysource,
        "Totaldownloads_by_device" : Totaldownloadsbydevice,
        "Average_retention" : Averageretention
    }
    print(result)
except TimeoutException:
    print("Loading took too much time")
    driver.quit()
    exit()