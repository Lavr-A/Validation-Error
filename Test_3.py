from selenium import webdriver
import time
driver = webdriver.Chrome ("D:\Лекции IT Academy\Chrome\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://accounts.google.com")
create_account_button = driver.find_element_by_xpath("//*[text()='Создать аккаунт']")
create_account_button.click()
time.sleep(2)
for_myself_button = driver.find_element_by_xpath("//*[text()='Для себя']")
for_myself_button.click()

#variables
validation_error = "Имя пользователя может включать латинские буквы (a-z), цифры (0-9) и точку (.)."
first_name_field = driver.find_element_by_id("firstName")
last_name_field = driver.find_element_by_id("lastName")
password_field = driver.find_element_by_name("Passwd")
confirm_password_field = driver.find_element_by_name("ConfirmPasswd")
username_field = driver.find_element_by_id("username")
next_button = driver.find_element_by_id("accountDetailsNext")

email_list = {'@b.a','@ba','@в.а','@а@b.a','@а@b.'}
user_dictionary = {'fn':'Andrei','ln':'Laurynovich','password':'Lavr123456'}

first_name_field.send_keys(user_dictionary['fn'])
last_name_field.send_keys(user_dictionary['ln'])
time.sleep(2)
password_field.send_keys(user_dictionary['password'])
confirm_password_field.send_keys(user_dictionary['password'])


def validate_username_field(email):
    username_field.clear()
    username_field.send_keys(email)
    next_button.click()
    time.sleep(2)
    assert validation_error in driver.page_source

for email in email_list:
    validate_username_field(email)

driver.quit()

