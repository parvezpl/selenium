from impmodul import  os, Options, webdriver

def driver():
    os.chdir("C:\\Users\\HP\\Desktop\\selenium")
    opt = Options()
    opt.add_experimental_option("debuggerAddress", "localhost:9515")
    driver = webdriver.Chrome(options=opt)
    return driver