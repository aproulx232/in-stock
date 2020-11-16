from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from twilio.rest import Client
from random import randint
from time import sleep
import config


def main():
    path = "C:\chromedriver_win32\chromedriver86_win32\chromedriver.exe"
    driver = webdriver.Chrome(path)
    evga_3070_backplate = (
        "https://www.newegg.com/evga-geforce-rtx-3070-08g-p5-3751-kr/p/N82E16814487528#"
    )
    test_in_stock_url = "https://www.newegg.com/p/N82E16813157923?Item=N82E16813157923"
    while True:
        driver.get(evga_3070_backplate)
        close_pop_up(driver)
        if not is_sold_out(driver):
            notify(evga_3070_backplate)
            break
        sleep(randint(10, 100))
    driver.quit()


def is_sold_out(driver):
    sold_out_element = "//*[@class='btn btn-message btn-wide']"
    page_load_wait = 10
    try:
        element = WebDriverWait(driver, page_load_wait).until(
            EC.presence_of_element_located((By.XPATH, sold_out_element))
        )
        print(element.get_attribute("innerHTML"))
        return True
    except Exception as e:
        print("In Stock!!")
        return False


def close_pop_up(driver):
    page_load_wait = 10
    try:
        element = WebDriverWait(driver, page_load_wait).until(
            EC.presence_of_element_located((By.ID, "popup-close"))
        )
        sleep(randint(1, 7))
        element.click()
    except Exception as e:
        print("No Pop Up")


def notify(url):
    account_sid = config.account_sid
    auth_token = config.auth_token
    client = Client(account_sid, auth_token)

    to_number = config.to_number
    from_number = config.from_number
    body = "Item in stock here: " + url
    message = client.messages.create(from_=from_number, body=body, to=to_number)


if __name__ == "__main__":
    main()