import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import os

@pytest.fixture(scope="function")
def driver(request):
    options = Options()
    options.add_argument("--headless")  # הפעלת מצב Headless
    options.add_argument("--disable-gpu")  # שיפור מהירות
    options.add_argument("--window-size=1920,1080")  # גודל חלון וירטואלי
    
    driver = webdriver.Chrome(options=options)  # פתיחת דפדפן Chrome

    yield driver
    driver.quit()

def test_browswer_open(driver):
    driver.get("https://www.google.com")  # כניסה לאתר Google
    assert "Google" in driver.title, "הדף שנפתח אינו גוגל!"  # בדיקה שהכותרת מכילה 'Google'


# def test_open_google(driver):
#     # driver = webdriver.Chrome()  # פתיחת דפדפן Chrome
#     driver.get("https://www.google.com")  # כניסה לאתר Google

#     assert "Google" in driver.title, "הדף שנפתח אינו גוגל!"  # בדיקה שהכותרת מכילה 'Google'

#     # driver.quit()  # סגירת הדפדפן
#     print("✅ הבדיקה עברה בהצלחה!")


# def test_google_lucky_button(driver):
#     # driver = webdriver.Chrome()  # פתיחת דפדפן Chrome
#     driver.get("https://www.google.com")  # כניסה לאתר Google

#     serch_box = driver.find_element(By.NAME, "q")  # מציאת תיבת החיפוש
#     serch_box.send_keys("Selenium")  # הקלדת המילים "Selenium"
#     time.sleep(1)  # המתנה של 2 שניות

#     lucky_button = driver.find_element(By.NAME, "btnI")  # מציאת כפתור "I'm Feeling Lucky"
#     lucky_button.click()  # לחיצה על הכפתור

#     time.sleep(3)  # המתנה של 2 שניות

#     assert "selenium.dev" in driver.current_url, "האתר שנפתח אינו האתר של Selenium!"  # בדיקה שהאתר שנפתח הוא האתר של Selenium

#     # driver.quit()  # סגירת הדפדפן

#     print("✅ הבדיקה עברה בהצלחה!")

# def test_google_text(driver):
#     # driver = webdriver.Chrome()  # פתיחת דפדפן Chrome
#     driver.get("https://www.google.com")  # כניסה לאתר Google

#     search_box = driver.find_element(By.NAME, "q")  # מציאת תיבת החיפוש
#     # search_box.send_keys("Selenium" + Keys.RETURN)  # הקלדת המילים "Selenium"

#     wait = WebDriverWait(driver, 5)  # המתנה של 10 שניות 
#     search_button = wait.until(EC.presence_of_element_located((By.NAME, "q")))  # מציאת תיבת החיפוש

#     # search_button = driver.find_element(By.NAME, "btnK")  # מציאת כפתור החיפוש

#     assert search_button.is_displayed(), "no search button"  # בדיקה שהכפתור מוצג

#     # driver.quit()  # סגירת הדפדפן
    
#     print("✅ הבדיקה עברה בהצלחה!")

# def test_login_error(driver):
#     # driver = webdriver.Chrome()  # פתיחת דפדפן Chrome
#     driver.get("https://practicetestautomation.com/practice-test-login/")  # כניסה לאתר

#     userName_box = driver.find_element(By.ID, "username")  # מציאת תיבת המשתמש
#     password_box = driver.find_element(By.ID, "password")  # מציאת תיבת הסיסמה
#     login_button = driver.find_element(By.ID, "submit")  # מציאת כפתור ההתחברות

#     time.sleep(2)  # המתנה של 2 שניות
#     userName_box.send_keys("wrong")  # הקלדת שם משתמש
#     time.sleep(2)  # המתנה של 2 שניות
#     password_box.send_keys("wrong")  # הקלדת סיסמה
#     time.sleep(2)  # המתנה של 2 שניות
#     login_button.click()  # לחיצה על הכפתור

#     time.sleep(2)  # המתנה של 2 שניות

#     error_message = driver.find_element(By.ID, "error")  # מציאת הודעת השגיאה
#     assert error_message.is_displayed(), "הודעת השגיאה לא מוצגת!"  # בדיקה שהודעת השגיאה מוצגת
#     assert "Your username is invalid!" in error_message.text, "הודעת השגיאה אינה תואמת את הצפוי!"  # בדיקה שהודעת השגיאה תואמת את הצפוי

#     # driver.quit()  # סגירת הדפדפן   

#     print("✅ הבדיקה עברה בהצלחה!")

# def test_navigation(driver):
#     # driver = webdriver.Chrome()  # פתיחת דפדפן Chrome
#     driver.get("https://practicetestautomation.com/")  # כניסה לאתר

#     nav_button = driver.find_element(By.LINK_TEXT, "PRACTICE")  # מציאת כפתור הניווט
#     nav_button.click()  # לחיצה על הכפתור

#     time.sleep(2)  # המתנה של 2 שניות

#     assert "practice" in driver.current_url, "האתר שנפתח אינו האתר של Practice!"  # בדיקה שהאתר שנפתח הוא האתר של Practice

#     # driver.quit()  # סגירת הדפדפן   

#     print("✅ הבדיקה עברה בהצלחה!")

# def test_alert(driver):
#     # driver = webdriver.Chrome()  # פתיחת דפדפן Chrome
#     driver.get("https://the-internet.herokuapp.com/javascript_alerts")  # כניסה לאתר

#     alert_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']")  # מציאת כפתור האזהרה 
#     alert_button.click()  # לחיצה על הכפתור

#     time.sleep(2)  # המתנה של 2 שניות

#     alert = Alert(driver)  # יצירת אובייקט של האזהרה
#     alert.send_keys("Hello, Selenium")  # הקלדת הטקסט "Hello, Selenium"
#     time.sleep(2)  # המתנה של 2 שניות
#     alert.accept()  # אישור האזהרה

#     time.sleep(2)  # המתנה של 2 שניות

#     # driver.quit()  # סגירת הדפדפן

#     print("✅ הבדיקה עברה בהצלחה!")

# def test_dropDown(driver):
#     driver.get("https://the-internet.herokuapp.com/dropdown")  # כניסה לאתר
#     dropDown_box = Select(driver.find_element(By.ID, "dropdown"))
#     time.sleep(2)  # המתנה של 2 שניות
#     dropDown_box.select_by_visible_text("Option 1")
#     time.sleep(2)
#     selected_option = dropDown_box.first_selected_option.text
#     assert selected_option == "Option 1", "The selected option is not Option 1"

# def test_radio_button(driver):
#     driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_form_radio")  # כניסה לאתר
#     time.sleep(2)  # המתנה של 2 שניות
#     driver.switch_to.frame(driver.find_element(By.ID, "iframeResult"))
    
#     html_radio_button = driver.find_element(By.XPATH, "//input[@type='radio' and @value='HTML']")
#     html_radio_button.click()
#     time.sleep(2)

#     assert html_radio_button.is_selected(), "The radio button is not selected"

# def test_file_upload(driver):
#     driver.get("https://the-internet.herokuapp.com/upload")  # כניסה לאתר

#     file_path = os.path.abspath("/Users/guybenmoshe/Documents/General/GuyBenMoshe_CV.pdf")

#     file_upload = driver.find_element(By.ID, "file-upload")
#     file_upload.send_keys(file_path)

#     time.sleep(2)

#     upload_button = driver.find_element(By.ID, "file-submit")
#     upload_button.click()

#     time.sleep(2)

#     aploaded_file_name = driver.find_element(By.ID, "uploaded-files").text
#     assert "GuyBenMoshe_CV.pdf" in aploaded_file_name, "The file was not uploaded"

# def test_file_download(driver):
#     driver.get("https://the-internet.herokuapp.com/download")  # כניסה לאתר

#     download_link = driver.find_element(By.LINK_TEXT, "GuyBenMoshe_CV.pdf")

#     time.sleep(2)

#     download_link.click()

#     time.sleep(2)

#     assert os.path.exists("/Users/guybenmoshe/Downloads/GuyBenMoshe_CV.pdf"), "The file was not downloaded"

# def test_google_search_optimize(driver):
#     driver.get("https://www.google.com")  # כניסה לאתר Google

#     searh_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))  # מציאת תיבת החיפוש

#     searh_box.send_keys("Selenium" + Keys.RETURN)  # הקלדת המילים "Selenium" ולחיצה על Enter

#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search")))  # המתנה של 10 שניות

#     assert "selenium" in driver.page_source, "המילה 'selenium' לא נמצאה בדף!"  # בדיקה שהמילה 'selenium' נמצאת בדף

# def test_page_load_time(driver):
#     startTime = time.time()  # זמן התחלתי
#     driver.get("https://www.google.com")  # כניסה לאתר Google
#     loadTime = time.time() - startTime  # זמן טעינה 

#     assert loadTime < 3, "זמן הטעינה ארוך מדי!"  # בדיקה שזמן הטעינה קצר מ-5 שניות