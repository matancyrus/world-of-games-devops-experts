from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
def test_scores_service(application_url):
    driver = None
    try:
        driver = webdriver.Chrome()
        driver.get(application_url)
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "score"))
        )        
        score = int(element.text)
        print(score)
        if 1 <= score <= 1000:
            return True
        else: 
            return False
    except Exception:
        return False
    finally:
        if driver is not None:
            driver.quit()

def main():
    result = test_scores_service("http://localhost:8777")
    if result:
        sys.exit(0)
    else:
        sys.exit(-1)

if __name__ == "__main__":
    main()