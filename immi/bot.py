from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.common.by import By
import keyboard
import time
import requests
import threading

def send_Alert(text):
    bot_token = "6760777598:AAFsWV5UDvdcXbdpq0sQ2Z9oVr3LMWeITuU"
    chatId = "-1002094784281"
    print(text)
    text = '<b>' + text +'</b>'
    req = 'https://api.telegram.org/bot'+ bot_token + '/sendMessage?chat_id='+chatId+'&parse_mode=HTML&text=' + text
    res = requests.get(req)
    print(res.content)

svc = webdriver.ChromeService(executable_path=binary_path)
driver = webdriver.Chrome(service=svc)

driver.get("https://online.immi.gov.au/ola/app")
# if require login
username = driver.find_element(By.ID,"username")
username.send_keys("austinx1311@gmail.com")

password = driver.find_element(By.ID,"password")
password.send_keys("Nguyenngoctoan123")

login = driver.find_element(By.XPATH, '//button[@name="login"]')
login.click()
time.sleep(2)

cont = driver.find_element(By.XPATH, '//button[@name="continue"]')
cont.click()
time.sleep(5)

edit = driver.find_element(By.XPATH, '//button[@name="defaultActionPanel_0_1"]')
edit.click()
time.sleep(5)

flag = True

# check 'q' enter
def check_exit_key():
    global flag
    while True:
        if keyboard.is_pressed('q'):
            flag= False
            send_Alert("Bot is turning off. Thank you for using the service")
            driver.quit() 
            exit()

# new thread
exit_thread = threading.Thread(target=check_exit_key)
exit_thread.daemon = True
exit_thread.start()

send_Alert("The bot is in the process of turning on. I will inform you when the gate is open")
while flag:
    try:
        pages = driver.find_element(By.XPATH, '//span[@class="wc-label"]').text.strip().split("/")
        page = int(pages[0])
        time.sleep(5)

        nextPage = driver.find_element(By.XPATH, '//button[@title="Go to next page"]')
        nextPage.click()
        print(page)
        if page > 5:
            for i in range(1,5):
                send_Alert("EMERGENCY SUCCESS: Dear boss, the gate is open, please proceed with registration")
                time.sleep(10)
            for i in range(1,5):
                send_Alert("EMERGENCY SUCCESS: Dear boss, the gate is open, please proceed with registration")
                time.sleep(600)
                break
    except Exception as e:
        send_Alert("ERROR: Bot is turning off. Thank you for using the service")
        driver.quit() 
        break

