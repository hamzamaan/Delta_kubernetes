# # from selenium import webdriver
# # from selenium.webdriver.chrome.options import Options
# import pytest
# import time

# # def test_set_up():
# #     global driver
# #     options = Options()
# #     options.headless = True
# #     driver = webdriver.Chrome("options=options") #/usr/lib/chromium-browser/chromedriver
# #     driver.implicitly_wait(10)
# #     driver.maximize_window()

# # def test_log_In():    
    
# #     driver.get("http://ac5ad16daadd14de191f60545f6ce6df-576534898.us-west-1.elb.amazonaws.com:5000/account/login")
# #     driver.find_element_by_id("username").send_keys("admin")
# #     driver.find_element_by_id("password").send_keys("admin")
# #     driver.find_element_by_xpath("//button[contains(., 'Log in')]").click()
# #     driver.close()
# #     driver.quit()
# #     print ("Test completed")
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

# def test_case():
#   options = Options()
#   options.headless = True
#   driver = webdriver.Chrome(ChromeDriverManager().install())
#   # driver = webdriver.Chrome(options=options)
#   driver.get("http://a1228a13199ac4aa795a9f15215d58e3-1768551268.us-west-1.elb.amazonaws.com:5000/account/login")
#   driver.find_element_by_id("username").send_keys("admin")
#   driver.find_element_by_id("password").send_keys("admin")
#   driver.find_element_by_xpath("//button[contains(., 'Log in')]").click()
#   driver.close()
#   driver.quit()
#   print ("Test completed")
