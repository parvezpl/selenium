from impmodul import By
from chrom_driver import driver
import pandas as pd
from thefuzz import fuzz, process

driver=driver()

# storeDataList.append(storeData)
def final_paper_solver():
    findAns = 0
    # storeDataList=[]
    data = pd.read_excel('cctns\paperdata3.xlsx')
    data2 = pd.read_excel('cctns\dataRemain.xlsx')
    storeData1 = data2.values.tolist()
    data1 = pd.DataFrame(data)
    storeData = data1.values.tolist()
    print("st1...", storeData1)
    qwtext = driver.find_element(By.XPATH, "//label[@id='ques']").text  # question ka test
    qq = qwtext.split(":")[0].split(" ")
    qwN = int(qq[1])  # question number
    # print(question)
    notAnsList=[]
    for i in range(100):
        if qwN < 101:
            qwtext = driver.find_element(By.XPATH, "//label[@id='ques']").text  # question ka test
            question = qwtext.split(":")[1].strip()
            ops = driver.find_elements(By.XPATH, "//div[@class='card-body m-3']/p/label")
            if question in [x[0] for x in storeData ]:
                for opns in ops:  # ans or not ans and shift to next qw
                        res=list(filter(lambda y: y[0]==question, storeData))
                        if res[0][1] == (opns.text).strip():
                            opns.click()
                            findAns +=1
            else:
                options=[(x.text).strip() for x in ops]
                options.insert(0,question)
                notAnsList.append(options)

            driver.find_element(By.XPATH, "/html/body/div/form/div[3]/div/div/div/div[3]/div[1]/div[3]/div/button[2]/span[1]").click()  # next click
            qwN+=1
    # print(findAns)
    print(notAnsList)
    # aa=pd.DataFrame(notAnsList)
    # aa.to_excel("cctns\qwNotAns.xlsx", index=False)
    dataDump(storeData1,notAnsList)

def validetion(storedata1, currentData): # return a list opject
    notAvlebleqwList=list(filter(lambda x: x if x[0] not in storedata1 else None , currentData))
    return notAvlebleqwList

def dataDump(storedata1, currentData):
    print("store", storedata1)
    notAvlebleqwList=validetion(storedata1, currentData)
    print(".....", notAvlebleqwList)
    addWebData=pd.DataFrame(notAvlebleqwList)
    stData=pd.DataFrame(storedata1)
    aa = pd.concat([stData, addWebData], ignore_index=True)
    aa.to_excel("cctns\dataRemain.xlsx", index=False)

final_paper_solver()
