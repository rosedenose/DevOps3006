from selenium import webdriver
my_driver = webdriver.Chrome("chromedriver.exe")
#my_driver.get("https://github.com")

my_driver.get("file:///c:/course/tip_calc/tip_calc/index.html")
my_driver.find_element(by="id", value="billamt").send_keys("100")
my_driver.find_element(by="xpath", value="/html/body/div/div[1]/form/p[4]/select/option[4]").click()
my_driver.find_element(by="id", value="peopleamt").send_keys("5")
my_driver.find_element(by="xpath", value="/html/body/div/div[1]/form/p[6]/select/option[4]").click()
my_driver.find_element(by="id", value="calculate").click()
#billamt.send_keys("100")

expected = "6.00"
actual = my_driver.find_element(by="id", value="tip")

if expected == actual:
    print("all good")
else:
    print("there is an issue")