import tkinter as tk
import time
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By

def get_user_id():
    user_id = user_id_entry.get()
    if not user_id:
        messagebox.showerror("Error", "Please enter your User ID")
        return
    run_attendance_bot(user_id)
    app.after(0, user_id_entry.destroy)



def run_attendance_bot(user_id):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://attendance.autmdu.in/")
    time.sleep(2)

    student_login = driver.find_element(By.XPATH, value="/html/body/div[2]/a[2]")
    student_login.click()
    time.sleep(1)

    user_id_field = driver.find_element(By.XPATH, value="/html/body/div[1]/form/input[1]")
    user_id_field.send_keys(user_id)

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

app = tk.Tk()
app.title("Attendance Bot")

user_id_label = tk.Label(app, text="User ID:")
user_id_label.grid(row=0, column=0)

user_id_entry = tk.Entry(app, font=("Helvetica", 16), width=10)
user_id_entry.grid(row=0, column=1, padx=10, pady=10)

submit_button = tk.Button(app, text="Submit", command=get_user_id)
submit_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

app.bind('<Return>', lambda event: get_user_id())

app.mainloop()