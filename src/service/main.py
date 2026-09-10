from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

from dataclasses import dataclass

@dataclass
class element:
    TAG: str
    TEXT: str
    ID: str
    CLASS: str

driver = webdriver.Chrome()

driver.get("https://talkabit-z3eg.onrender.com/app/login")

title = driver.title

driver.implicitly_wait(0.5)

elementos = driver.find_elements(By.XPATH, "//*")

print(f"Total de elementos: {len(elementos)}")

elementsData = []

for elemento in elementos:

    elementsData.append({
        "TAG:", elemento.tag_name,
        "| TEXT:", repr(elemento.text),
        "| ID:", elemento.get_attribute("id"),
        "| CLASS:", elemento.get_attribute("class")
    })

tokenCamp = driver.find_element(By.ID, "teamToken")
tokenCamp.send_keys("FRIENDS-TCRJ7")
password_camp = driver.find_element(By.ID, "password")
password_camp.send_keys("talkabit")

botao = driver.find_element(
    By.XPATH,
    "//button[normalize-space()='Acessar']"
)

botao.click()
time.sleep(3)

elementos = driver.find_elements(By.XPATH, "//*")
print(" ")
print("elementos pg 2")
print("///////////////////////////////////////")
print(f"Total de elementos: {len(elementos)}")

for elemento in elementos:
    print(
        "TAG:", elemento.tag_name,
        "| TEXT:", repr(elemento.text),
        "| ID:", elemento.get_attribute("id"),
        "| CLASS:", elemento.get_attribute("class")
    )

    dic[elemento.get_attribute("id")] = elemento.get_attribute("class")


driver.quit()
