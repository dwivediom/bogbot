import tkinter as tk
import tkinter.ttk as ttk
from selenium import webdriver
import time
import threading
dur =30 
driver = webdriver.Chrome(executable_path="D:\\projects\\blog bot\\YoutubeBot\\edge\\chromedriver.exe")
i = 0
  
while i < 6:
    driver.get('https://www.linkedin.com/posts/programmers-park-52129225a_check-out-my-new-blog-about-insurance-activity-7008390675704500224-Lhca?utm_source=share&utm_medium=member_desktop')

    time.sleep(4)
    link = driver.find_element_by_xpath(
        "/html/body/main/section[1]/div/section/div/p/a")

    driver.execute_script(
        "arguments[0].setAttribute('target', '_self')", link)
    link.click()

    blogheading = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/main/div/div[1]/div/div/article/div/div/h3/a")
    blogheading.click()

    driver.execute_script(
        "window.scrollTo(0,document.body.scrollHeight/2.5)")
    time.sleep(dur)

    backBtn = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/header/div/div[1]/a")
    backBtn.click()
    driver.execute_script(
        "window.scrollTo(0,document.body.scrollHeight/2.5)")
    time.sleep(4)
    latestblog = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/main/div/div[2]/div[1]/div[1]/div/div/h3/a")
    latestblog.click()
    driver.execute_script(
        "window.scrollTo(0,document.body.scrollHeight/2.5)")

    #  print("its working ")
    time.sleep(dur)
    driver.refresh()

    i += 1
