import time
from selenium import webdriver
from selenium.webdriver.common.by import By

USERID = input("Enter Your User ID: ")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://attendance.autmdu.in/")
time.sleep(2)

student_login = driver.find_element(By.XPATH, value="/html/body/div[2]/a[2]")
student_login.click()
time.sleep(1)

user_id = driver.find_element(By.XPATH, value="/html/body/div[1]/form/input[1]")
user_id.send_keys(USERID)

academic_yr = driver.find_element(By.XPATH, value="/html/body/div[1]/form/select[1]")
academic_yr.click()

academic_yr_dropdown = driver.find_element(By.XPATH, value="/html/body/div[1]/form/select[1]/option[3]")
academic_yr_dropdown.click()

semester = driver.find_element(By.XPATH, value="/html/body/div[1]/form/select[2]")
semester.click()

semester_dropdown = driver.find_element(By.XPATH, value="/html/body/div[1]/form/select[2]/option[7]")
semester_dropdown.click()

click_submit = driver.find_element(By.XPATH, value="/html/body/div[1]/form/input[2]").click()
time.sleep(2)

driver.close()
