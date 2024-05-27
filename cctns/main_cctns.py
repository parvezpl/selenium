import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# import subprocess
import os
from selenium.webdriver.common.by import By
from demo import PaperSM
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
os.chdir("F:\\program\\selenium")
opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:9515")
driver = webdriver.Chrome(options=opt)

class AllWin():
    def __init__(self):
        print(">>>>>>working All win")
        win = []
        dr = driver
        for i in dr.window_handles:
            win.append(i)
            continue
        if len(win) != 1:
            self.fwin = win[0]
            self.swin = win[1]
        else:
            self.fwin = win[0]

    def len_win(self):
        win = []
        dr = driver
        for i in dr.window_handles:
            win.append(i)
            continue
        return len(win)

    def fwin(self):
        return self.fwin

    def swin(self):
        return self.swin

    def switch_wind(self):
        a=AllWin.swin(self)
        b=AllWin.fwin(self)
        print("a", a)
        print("b",b)
        try:
            driver.switch_to.window(self.swin)
        except Exception as e:
            print(e)
        try:
            driver.switch_to.window(self.fwin)
        except Exception as e:
            print(e)

class Penting:
    def __init__(self):
        print(">>>>>>working Pencting class")
        #pending check
        try:
            totall_pending = driver.find_element(By.ID, "ContentPlaceHolder1_ContentPlaceHolder1_hhome")
            print(totall_pending.text)
        except:
            pass

    def click_pending(self):
        totall_pending = driver.find_element(By.ID, "ContentPlaceHolder1_ContentPlaceHolder1_hhome").text

        if totall_pending != 0:
            pendig_click=driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div/form/div[3]/div[1]/div[3]/div/div[2]/a")
            pendig_click.click()
            print("click pending list")
        else:
            print("Not pending any thing")

class Subject:
    def __init__(self):
        print(">>>>>>>working subject class")
    def sub_click(self):
        try:
            print("inter try")
            driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/form/div[3]/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[5]/a").click()
            element = WebDriverWait(driver, 61).until(
                EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div/div[2]/div/div/form/div[3]/div[2]/div/div/div/div/div[1]/div/a")))
            driver.find_element(By.XPATH,
                                              "/html/body/div/div[2]/div/div/form/div[3]/div[2]/div/div/div/div/div[1]/div/a").click()

        except:
            print ("subject exepction ")
            pass
    def qw(self):
        driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div/form/div[3]/div[2]/div/div/div/div/div[1]/div/a").click()

    def home_page(self):
        try:
            driver.find_element(By.XPATH,"/html/body/div/div[1]/a/div[1]/i").click() #traingi module pr click
            print("direct click traing pr")
            # conn_object.driver().find_element(By.XPATH,"/html/body/form/div[3]/div/div/div[1]/nav/button/span").click()
            # conn_object.driver().find_element(By.XPATH,"/html/body/form/div[3]/div/div/div[1]/nav/div/ul/li[1]/a").click()
        except:
            print("home page ex")
            driver.find_element(By.XPATH,"/html/body/nav/button/span").click()
            driver.find_element(By.XPATH,"/html/body/nav/div/ul/li[1]/a").click()
class PrSolver:
    def conti_all(self):
        try:

            driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div/form/div[3]/div[1]/div[3]/div/div[2]/a").click()
            driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div/form/div[3]/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[5]/a").click()
            driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div/form/div[3]/div[2]/div/div/div/div/div[1]/div/a").click()
            
        except :
            print("except")


pending_object=Penting()
win_object=AllWin()
sub_object=Subject()
pr_obj=PrSolver()

class Start:
    def start(self):
        try:
            if driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/form/div[3]/div[1]/div[3]/div/div[2]/a").text != '0':

                i = 0
                for x in range(100):
                    i = i + 1
                    pr_obj.conti_all()
                    PaperSM()
                    sub_object.home_page()
                    pnd = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/form/div[3]/div[1]/div[3]/div/div[2]/a").text
                    print(pnd)
                    if driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/form/div[3]/div[1]/div[3]/div/div[2]/a").text == '0':
                        print("NO PENDING QUESTIONS")
                        break
            else:
                print("NO PENDING QUESTIONS")
        except:
            print("chrome always top")
            time.sleep(5)
            Start().start()
Start().start()
