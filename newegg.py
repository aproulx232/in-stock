from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    # path to chromedriver.exe
    path = "C:\chromedriver_win32\chromedriver86_win32\chromedriver.exe"
    # create nstance of webdriver
    driver = webdriver.Chrome(path)
    evga_3070_backplate = (
        "https://www.newegg.com/evga-geforce-rtx-3070-08g-p5-3751-kr/p/N82E16814487528#"
    )
    test_url = "https://www.newegg.com/p/N82E16813157923?Item=N82E16813157923"
    driver.get(test_url)
    close_pop_up(driver)
    if not is_sold_out(driver):
        notify()
    driver.quit()


def is_sold_out(driver):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@class='btn btn-message btn-wide']")
            )
        )
        print(element.get_attribute("innerHTML"))
        return True
    except Exception as e:
        print("In Stock!!:", e)
        return False


def close_pop_up(driver):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "popup-close"))
        )
        element.click()
    except Exception as e:
        print("No Pop Up", e)


def notify():
    pass


if __name__ == "__main__":
    main()