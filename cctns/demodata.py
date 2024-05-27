from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import os
os.chdir("C:\\Users\\Dell\\Desktop\\selenium")
opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:9515")
driver = webdriver.Chrome(options=opt)
print("connected ")
print(driver.title)

class FistQw:
    def fist(self):
        driver.find_element(By.NAME, "grdquestions$ctl02$110").click()
    def secound(self):
        driver.find_element(By.NAME, "grdquestions$ctl02$110").click()
    def third(self):
        driver.find_element(By.NAME, "grdquestions$ctl02$110").click()
    def fourth(self):
        driver.find_element(By.NAME, "grdquestions$ctl02$110").click()

class Answer:
    def qw1(self):
        driver.execute_script(
            "document.getElementsByClassName('correctAnswer bg-warning  font-weight-bold p-2')[0].style.display = 'block';") #currect answr display
        # qw = driver.find_elements(By.XPATH, "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[2]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr") #answer all
        qwa = driver.find_element(By.XPATH, "//span[@id='grdquestions_lbAnswer_0']").text #correct answer
        aa = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[2]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/label")
        b = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[2]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/label")

        c = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[2]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td/label")
        d = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[2]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[4]/td/label")

        if qwa == 'A':
            return aa.text
        elif qwa == 'B':
            return b.text
        elif qwa == 'C':
            return c.text
        elif qwa == 'D':
            return d.text


    def qw2(self):
        driver.execute_script(
            "document.getElementsByClassName('correctAnswer bg-warning  font-weight-bold p-2')[1].style.display = 'block';")  # currect answr display
        # qw = driver.find_elements(By.XPATH, "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[3]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr")  # answer all
        qwa = driver.find_element(By.XPATH, "//span[@id='grdquestions_lbAnswer_1']").text  # correct answer

        aa = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[3]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/label")
        b = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[3]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/label")
        c = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[3]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td/label")
        d = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[3]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[4]/td/label")
        if qwa == 'A':
            return aa.text
        elif qwa == 'B':
            return b.text
        elif qwa == 'C':
            return c.text
        elif qwa == 'D':
            return d.text

    def qw3(self):
        driver.execute_script(
            "document.getElementsByClassName('correctAnswer bg-warning  font-weight-bold p-2')[2].style.display = 'block';")  # currect answr display
        # qw = driver.find_elements(By.XPATH, "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[4]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr")  # answer all
        qwa = driver.find_element(By.XPATH, "//span[@id='grdquestions_lbAnswer_2']").text  # correct answer

        aa = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[4]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/label")
        b = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[4]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/label")
        c = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[4]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td/label")
        d = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[4]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[4]/td/label")

        if qwa == 'A':
            return aa.text
        elif qwa == 'B':
            return b.text
        elif qwa == 'C':
            return c.text
        elif qwa == 'D':
            return d.text



    def qw4(self):
        driver.execute_script(
            "document.getElementsByClassName('correctAnswer bg-warning  font-weight-bold p-2')[3].style.display = 'block';")  # currect answr display
        # qw = driver.find_elements(By.XPATH, "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[5]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr")  # answer all
        qwa = driver.find_element(By.XPATH, "//span[@id='grdquestions_lbAnswer_3']").text  # correct answer

        aa = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[5]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/label")
        b = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[5]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/label")
        c = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[5]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td/label")
        d = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[5]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[4]/td/label")

        if qwa == 'A':
            return aa.text
        elif qwa == 'B':
            return b.text
        elif qwa == 'C':
            return c.text
        elif qwa == 'D':
            return d.text

    def qw5(self):
        driver.execute_script(
            "document.getElementsByClassName('correctAnswer bg-warning  font-weight-bold p-2')[4].style.display = 'block';")  # currect answr display
        # qw = driver.find_elements(By.XPATH, "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[6]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr")  # answer all
        qwa = driver.find_element(By.XPATH, "//span[@id='grdquestions_lbAnswer_4']").text  # correct answer

        aa = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[6]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/label")
        b = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[6]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/label")
        c = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[6]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td/label")
        d = driver.find_element(By.XPATH,
                                "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[6]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[4]/td/label")

        if qwa == 'A':
            return aa.text
        elif qwa == 'B':
            return b.text
        elif qwa == 'C':
            return c.text
        elif qwa == 'D':
            return d.text


class WinH:
    def __init__(self):
        handles = driver.window_handles
        size = len(handles)
        parent_handle = driver.current_window_handle
        for x in range(size):
            if handles[x] != parent_handle:
                driver.switch_to.window(handles[x])
                print(driver.title)
                aa = driver.find_element(By.XPATH, "/html/body/form/div[3]/div/div/div[1]/h4")
                print(aa.text)


class Totalans:
    def total_ans(self):
        ans_object = Answer()
        a = ans_object.qw1()
        b = ans_object.qw2()
        c = ans_object.qw3()
        d = ans_object.qw4()
        e = ans_object.qw5()
        return [a, b, c, d, e]


class TotalQw(Totalans):
    def tatal_qw(self):
        aqw = driver.find_elements(By.XPATH, "//th[@class ='text-gray-800 p-1']")
        allqw = []
        for i in aqw:
            allqw.append(i.text)
        return allqw

class MakeDict:
    def make_dict(self):
        obj = TotalQw()
        a = obj.tatal_qw()
        b = obj.total_ans()
        return dict(zip(a, b))




WinH()
# x=driver.find_element(By.XPATH, "/html/body/form/div[3]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[2]/td/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td")
# print(x.text)

qw=TotalQw().tatal_qw()
aa=MakeDict().make_dict()
d = [[1,2],[3,4]]
df=pd.DataFrame(d)
df2=pd.read_excel("C:\\Users\\Dell\\Desktop\\selenium\\Book1.xlsx")
# df.to_excel(df2, ignore_index=True)
# print(aa.get(qw[2]))
# pd.read_excel("C:\\Users\\Dell\\Desktop\\selenium\\Book1.xlsx")
# data =pd.DataFrame(aa)
# data.to_excel("paperdata.xlsx")