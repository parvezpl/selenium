from selenium.webdriver.common.by import By
from chrom_driver import driver
driver=driver()
class FinalSurtificat():
    # def __init__(self):
    #     driver.find_element(By.XPATH,"//a[@class='nav-link collapsed']").click()
    #     driver.find_element(By.XPATH,"/html/body/div/div[1]/ul/li/div/div/a[1]/span").click()
    #     driver.find_element(By.XPATH,"//input[@id='ContentPlaceHolder1_ContentPlaceHolder1_grid_bid_0']").click()
    def final_paper_solver(self):

        ans=driver.execute_script('''co4=[];
        test.forEach((element, index) => {
            co4.push(element.ans);
            });
        return co4;''')

        qwtext=driver.find_element(By.XPATH,"//label[@id='ques']").text  #question ka test
        q=qwtext.split(":")[0].split(" ")
        qwN = int(q[1])         #full value
        # qwN=int(qwtext[8:11])     #int me convert kr ke
        curAns=ans[qwN-1]         #ans prapt
        ops=driver.find_elements(By.XPATH,"//div[@class='card-body m-3']/p/label")

        l=['A','B','C','D']
        for i in l:
            if curAns=='A':
                ops[0].click()
                print("question no:",qwN, ops[0].text)
                break
            elif curAns=='B':
                ops[1].click()
                print("question no:",qwN,ops[1].text)
                break
            elif curAns=='C':
                ops[2].click()
                print("question no:",qwN,ops[2].text)
                break
            else:
                ops[3].click()
                print("question no:",qwN,ops[3].text)
                break

        driver.find_element(By.XPATH,"/html/body/div/form/div[3]/div/div/div/div[3]/div[1]/div[3]/div/button[2]/span[1]").click() #next click
        if (qwN)!=100:
            FinalSurtificat().final_paper_solver()
        else:
            driver.execute_script('''alert('All 100 question currect.Click to Finish')''')
            print("Click to Finish")

FinalSurtificat().final_paper_solver()