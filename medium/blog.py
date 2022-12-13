import tkinter as tk
import tkinter.ttk as ttk
from selenium import webdriver
import time
import threading
driver = webdriver.Chrome( executable_path="C:\\Users\\Administrator\\Desktop\\bogbot\\medium\\chromedriver.exe")
# driver = webdriver.Chrome(executable_path="D:\\projects\\blog bot\\YoutubeBot\\edge\\chromedriver.exe")
driver.get(
        'https://medium.com/@programmerspark21/how-to-choose-insurance-why-it-is-so-important-651900089cee')
original_tab = driver.current_window_handle
time.sleep(300)
def run():
 try:
 
   dur = 20
   
   i = 0

   while i < 1000000:
      driver.get(
        'https://medium.com/@programmerspark21/how-to-choose-insurance-why-it-is-so-important-651900089cee')
      original_tab = driver.current_window_handle
      time.sleep(4)
      link = driver.find_element_by_xpath("/html/body/div/div/div[3]/div[2]/div/main/div/div[2]/div[1]/div/article/div/div[2]/section/div/div[2]/p[8]/a")

      driver.execute_script(
        "arguments[0].setAttribute('target', '_self')", link)
      link.click()
      
      blogheading = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/main/div/div[1]/div/div/article/div/div/h3/a")
      blogheading.click()
      driver.switch_to.window(original_tab)
      
      driver.execute_script(
        "window.scrollTo(0,document.body.scrollHeight/2.5)")
      ads1 = driver.find_element_by_id('ads1')
      ads1.click()
      time.sleep(15)
      ads2 = driver.find_element_by_id('ads2')
      ads2.click()
      time.sleep(15)
      ads3 = driver.find_element_by_id('ads3')
      ads3.click()
     

      time.sleep(10)
      
      backBtn = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/header/div/div[1]/a")
      backBtn.click()
      driver.switch_to.window(original_tab)
      driver.execute_script(
        "window.scrollTo(0,document.body.scrollHeight/2.5)")
        
      time.sleep(4)
      latestblog = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/main/div/div[2]/div[1]/div[1]/div/div/h3/a")
      latestblog.click()
      driver.execute_script(
        "window.scrollTo(0,document.body.scrollHeight/2.5)")
      time.sleep(6)
      ads1 = driver.find_element_by_id('ads1')
      ads1.click()
      time.sleep(15)
      ads2 = driver.find_element_by_id('ads2')
      ads2.click()
      time.sleep(15)
      ads3 = driver.find_element_by_id('ads3')
      ads3.click()
      time.sleep(15)

    #  print("its working ")
      time.sleep(dur)
      driver.refresh()

      i += 1
 except:
    print("an error occord")
    run()
run()    