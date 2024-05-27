import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import subprocess
import os
from selenium.webdriver.common.by import By
from demo import PaperSM
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Conn:
    def __init__(self):
        print(">>>>>>working conn")
        try:
            Conn.win_all_opeen(self)
            print("try section me entry huea hai ")
            if Conn.driver(self).name == 'chrome':
                print("find chrome")
        except:
            print("chrome not open, so opening chrome brower")
            Conn.win_star_open(self)
        finally:
            print("chrome opened")

    def driver(self):
        opt = Options()
        opt.add_experimental_option("debuggerAddress", "localhost:9515")
        driver = webdriver.Chrome(options=opt)
        return driver
        # print("connected ")

    def win_star_open(self):
        os.chdir("C:\Program Files\Google\Chrome\Application")  # chrome app avlabel path
        subprocess.Popen("chrome.exe --remote-debugging-port=9515 --user-data-dir=E:\chrome")
        os.chdir("C:\\Users\\HP\\Desktop\\selenium")
        # conn_object.driver().get("https://hackathon.uppolice.gov.in/CCTNS-Training/index.aspx")
    def win_all_opeen(self):
        return os.chdir("C:\\Users\\Dell\\Desktop\\selenium")

    def prnt(self):
        print("test print")


class AllWin():
    def __init__(self):
        print(">>>>>>working All win")
        win = []

        dr = conn_object.driver()
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
        dr = conn_object.driver()
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
            conn_object.driver().switch_to.window(self.swin)
        except Exception as e:
            print(e)
        try:
            conn_object.driver().switch_to.window(self.fwin)
        except Exception as e:
            print(e)

class Penting:
    def __init__(self):
        print(">>>>>>working Pencting class")
        #pending check
        try:
            totall_pending = conn_object.driver().find_element(By.ID, "ContentPlaceHolder1_ContentPlaceHolder1_hhome")
            print(totall_pending.text)


        except:
            pass

    def click_pending(self):
        totall_pending = conn_object.driver().find_element(By.ID, "ContentPlaceHolder1_ContentPlaceHolder1_hhome").text
        if totall_pending != 0:
            pendig_click=conn_object.driver().find_element(By.XPATH,"/html/body/div/div[2]/div/div/form/div[3]/div[1]/div[3]/div/div[2]/a")
            pendig_click.click()
            print("click pending list")
        else:
            print("Not pending any thing")

class Subject:
    def __init__(self):
        print(">>>>>>>working subject class")
    def sub_click(self):
        try:
            conn_object.driver().find_element(By.XPATH, "/html/body/div/div[2]/div/div/form/div[3]/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[5]/a").click()
            element = WebDriverWait(conn_object.driver(), 61).until(
                EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div/div[2]/div/div/form/div[3]/div[2]/div/div/div/div/div[1]/div/a")))
            conn_object.driver().find_element(By.XPATH,
                                              "/html/body/div/div[2]/div/div/form/div[3]/div[2]/div/div/div/div/div[1]/div/a").click()

        except:
            pass
    def qw(self):
        conn_object.driver().find_element(By.XPATH,"/html/body/div/div[2]/div/div/form/div[3]/div[2]/div/div/div/div/div[1]/div/a").click()

    def home_page(self):
        try:
            conn_object.driver().find_element(By.XPATH,"/html/body/div/div[1]/a/div[1]/i").click() #traingi module pr click
            # conn_object.driver().find_element(By.XPATH,"/html/body/form/div[3]/div/div/div[1]/nav/button/span").click()
            # conn_object.driver().find_element(By.XPATH,"/html/body/form/div[3]/div/div/div[1]/nav/div/ul/li[1]/a").click()
        except:
            conn_object.driver().find_element(By.XPATH,"/html/body/nav/button/span").click()
            conn_object.driver().find_element(By.XPATH,"/html/body/nav/div/ul/li[1]/a").click()
class PrSolver:
    def conti_all(self):
        conn_object.driver().find_element(By.XPATH,"/html/body/div/div[2]/div/div/form/div[3]/div[1]/div[3]/div/div[2]/a").click()
        conn_object.driver().find_element(By.XPATH,"/html/body/div/div[2]/div/div/form/div[3]/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[5]/a").click()
        conn_object.driver().find_element(By.XPATH,"/html/body/div/div[2]/div/div/form/div[3]/div[2]/div/div/div/div/div[1]/div/a").click()



conn_object = Conn()
pending_object=Penting()
win_object=AllWin()
sub_object=Subject()
pr_obj=PrSolver()
while True:
    print("enter while loop")
    try:
        if conn_object.driver().find_element(By.XPATH,"/html/body/div/div[2]/div/div/form/div[3]/div/div/div[1]/h2").text == 'लम्बित (अभ्यास)Excercise की सूची':
            sub_object.sub_click()
            # sub_object.qw()
            print("open paper for solve")
            PaperSM()
            print("demo work")
            sub_object.home_page()
            if conn_object.driver().find_element(By.XPATH,
                                                 "/html/body/div/div[2]/div/div/form/div[3]/div[1]/div[3]/div/div[2]/a").text == '0':
                print("NO PENDING QUESTIONS")
                break
            i=0
            for x in range(54):
                print("entering for loop while paper solved")
                i=i+1
                pr_obj.conti_all()
                PaperSM()
                sub_object.home_page()
                if conn_object.driver().find_element(By.XPATH,"/html/body/div/div[2]/div/div/form/div[3]/div[1]/div[3]/div/div[2]/a").text=='0':
                    break
            continue

    except:
        pass
    try:
        if conn_object.driver().find_element(By.XPATH,"/html/body/div/div[2]/div/div/form/div[3]/h4").text =='DASHBOARD':
            print("dashboard me intery hua hai")
            pending_object.click_pending()
            continue
    except:
        sub_object.qw()
        print("open paper for solve")
        print("demo work")
        sub_object.home_page()
