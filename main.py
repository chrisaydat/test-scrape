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
    driver.get(
        "https://appstoreconnect.apple.com/analytics/app/d30/1608146534/overview?iaemeasure=totalDownloads")


WebDriverWait(driver, 10).until(
    EC.frame_to_be_available_and_switch_to_it((By.ID, "aid-auth-widget-iFrame")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.ID, "account_name_text_field"))).send_keys("chris@myladder.africa")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.ID, "aid-auth-widget-iFrame"))).click()
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "sign-in"))).click()
WebDriverWait(driver, 10).until(
    EC.frame_to_be_available_and_switch_to_it((By.ID, "aid-auth-widget-iFrame")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.ID, "password_text_field"))).send_keys("sadat1SADAT@")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.ID, "aid-auth-widget-iFrame"))).click()
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "sign-in"))).click()
time.sleep(5)
try:
    element_present = EC.presence_of_element_located((By.ID, 'container'))
    WebDriverWait(driver, timeout).until(element_present)

    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    Impressions = soup.find('title', attrs={
                            'class': 'Box-sc-18eybku-0 Text__BaseText-sc-4nqr4q-0 Text-sc-4nqr4q-1 dquphU'}).text
    Productpageviews = soup.find('title', attrs={
                                 'class': '_Box-sc-18eybku-0 Text__BaseText-sc-4nqr4q-0 Text-sc-4nqr4q-1 dquphU'}).text
    Conversionrate = soup.find('title', attrs={
                               'class': 'Box-sc-18eybku-0 Text__BaseText-sc-4nqr4q-0 Text-sc-4nqr4q-1 dquphU'}).text
    Totaldownloads = soup.find('title', attrs={
                               'class': 'Box-sc-18eybku-0 Text__BaseText-sc-4nqr4q-0 Text-sc-4nqr4q-1 dquphU'}).text
    Sessionperactiveusers = soup.find('title', attrs={
                                      'class': 'Box-sc-18eybku-0 Text__BaseText-sc-4nqr4q-0 Text-sc-4nqr4q-1 dquphU'}).text
    Crashes = soup.find('title', attrs={
                        'class': 'Box-sc-18eybku-0 Text__BaseText-sc-4nqr4q-0 Text-sc-4nqr4q-1 dquphU'}).text
    TotaldownloadsbyTerritory = soup.find(
        'title', attrs={'class': '_3qQ9m1'}).text
    Totaldownloadsbysource = soup.find(
        'title', attrs={'class': '_3qQ9m1'}).text
    Totaldownloadsbydevice = soup.find(
        'title', attrs={'class': '_3qQ9m1'}).text
    Averageretention = soup.find('title', attrs={'class': '_3qQ9m1'}).text
    result = {
        "Impressions": Impressions,
        "Product_page_views": Productpageviews,
        "conversion_rate": Conversionrate,
        "Totaldownloads": Totaldownloads,
        "Session_per_active_users": Sessionperactiveusers,
        "Crashes": Crashes,
        "Totaldownloads_by_Territory": TotaldownloadsbyTerritory,
        "Totaldownloads_by_source": Totaldownloadsbysource,
        "Totaldownloads_by_device": Totaldownloadsbydevice,
        "Average_retention": Averageretention
    }
    print(result)
except TimeoutException:
    print("Loading took too much time")
    driver.quit()
    exit()
