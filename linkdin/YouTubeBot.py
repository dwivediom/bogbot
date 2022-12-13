import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
import time
import pyautogui
import threading

height = pyautogui.size()[1]
width = pyautogui.size()[0]
print("resolution = " + str(width) + ", " + str(height))
window  = tk.Tk()
window.title("YouTube Bot")
window.resizable(0,0)
window.configure(background="white")
window.rowconfigure([0], minsize=round(width/96), weight=0)
window.columnconfigure([0,2], minsize=round(width/24), weight=0)
window.columnconfigure(1, minsize=round(width/2.13), weight=0)

def fetch(x):
    import requests as r
    res = r.get(f"https://img.youtube.com/vi/{x}/maxresdefault.jpg")
    with open("./images/image1.jpg", "wb") as f:
        f.write(res.content)

def filter():
    x = url_input.get().strip().split("=")[1].strip().split("&")[0]
    if x == "":
        print("Can't find image")
        return
    else:
        try:
            fetch(x)
            global img0
            img0 = Image.open("./images/image1.jpg")
            img0 = img0.resize((round(img0.size[0]*0.7*width/1920), round(img0.size[1]*0.7*width/1920)))
            print("thumbnail size -> " + str(img0.size[0]) + ", " + str(img0.size[1]))
            img0 = ImageTk.PhotoImage(img0)
            thumbnail_frm.configure(image=img0)
        except:
            print("Permission error: writing to a file")
            return

def duration_split(duration):
    hour = 0
    min = 0
    sec = 0
    list = duration.split(":")
    hour = int(list[0])
    min = int(list[1])
    sec = int(list[2])
    return hour*3600 + min*60 + sec


def start():
    dur = dur_entry.get()
    loop = loop_entry.get()

    if len(dur.split(":")) == 3:
        dur = duration_split(dur)
    else:
        return
    if loop == "":
        return
    else:
        if loop.lower() == "inf":
            loop = 999999999
        else:
            try:
                loop = int(loop)
            except:
                return

    # while loop:
        # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(executable_path="D:\\projects\\blog bot\\YoutubeBot\\edge\\chromedriver.exe")
        # driver.get(url_input.get().strip())
        # plybtn = driver.find_element_by_class_name("ytp-play-button")
        # time.sleep(3)
        # ---> If the video doesnt start playing within three seconds of opening, then disable this  <--- #
        # plybtn.click() 
        # driver.get('https://twitter.com/TeamAumm/status/1602562838265995265')
        # w=1 
        # while w<2:
        #   time.sleep(60)  
        #   popup = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div")
        #   if(popup): 
        #     popup.click()
        #   w +=1
        i=0
        
        while i<6 :
         driver.get('https://www.linkedin.com/posts/programmers-park-52129225a_check-out-my-new-blog-about-insurance-activity-7008390675704500224-Lhca?utm_source=share&utm_medium=member_desktop')
         
         
         time.sleep(4)  
         link = driver.find_element_by_xpath("/html/body/main/section[1]/div/section/div/p/a")
        
         driver.execute_script("arguments[0].setAttribute('target', '_self')",link)
         link.click()

         blogheading = driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div[1]/div/div/article/div/div/h3/a")
         blogheading.click()
          
         driver.execute_script("window.scrollTo(0,document.body.scrollHeight/2.5)")  
         time.sleep(dur)    
         
         backBtn= driver.find_element_by_xpath("/html/body/div[1]/div/div/header/div/div[1]/a")
         backBtn.click()
         driver.execute_script("window.scrollTo(0,document.body.scrollHeight/2.5)")  
         time.sleep(4)  
         latestblog=driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div[2]/div[1]/div[1]/div/div/h3/a")
         latestblog.click()  
         driver.execute_script("window.scrollTo(0,document.body.scrollHeight/2.5)")              
        
         
        #  print("its working ")  
         time.sleep(dur)
         driver.refresh()

          
         i+=1
        
       
        
        # driver.close()
        # loop -= 1
    
# ---> IMAGES <--- #
img0 = Image.open("./images/image.jpg")
img0 = img0.resize((round(img0.size[0]*0.7*width/1920), round(img0.size[1]*0.7*width/1920)))
print("img0 size -> " + str(img0.size[0]) + ", " + str(img0.size[1]))
img0 = ImageTk.PhotoImage(img0)
img1 = Image.open("./images/youtubebot.png")
img1 = img1.resize((round(img1.size[0]*0.5*width/1920), round(img1.size[1]*0.5*width/1920)))
print("img1 size -> " + str(img1.size[0]) + ", " + str(img1.size[1]))
img1 = ImageTk.PhotoImage(img1)

# ---> TITLE OF THE GUI <--- #
title = tk.Label(master=window, image=img1, font=("", 40), bg="white")
title.grid(row=0, column=0, sticky="nsew", pady=5, columnspan=3)

# ---> DESCRIPTION <--- #
desc = tk.Label(master=window, text = "Increase the number of views on any YouTube video.", font=("aNYTHING", 25), bg="white")
desc.grid(row=1, column=0, pady=(5,30), columnspan=3)

# ---> URL INPUT <--- #
url_label = tk.Label(master=window, text="URL of the Youtube Video ", font=("", 15), bg="white")
url_label.grid(row=2, column=0, padx=(15, 5), pady=(0, 5))
url_input = ttk.Entry(master=window, font=("", 15))
url_input.grid(row=2, column=1, sticky="ew", pady=(0, 5))
# ---> SUBMIT BUTTON <--- #
style = ttk.Style()
style.configure("TButton", font=("", 15))
url_btn = ttk.Button(style='TButton', master=window, text="Submit", command = filter)
url_btn.grid(row=2, column=2, padx=(3, 15), pady=(0, 5))

# ---> YOUTUBE THUMBNAIL FRAME <--- #
thumbnail_frm = tk.Label(master=window, image=img0, bg="red")
thumbnail_frm.grid(row=3, column=0, columnspan=3)

# ---> BOTTOM FRAME <--- #
dur_loop_frm = tk.Frame(master=window, bg="white")
dur_loop_frm.grid(row=4, column=0, columnspan=3, sticky="nsew")
# dur_loop_frm.columnconfigure([0], minsize=430, weight=1)
# dur_loop_frm.columnconfigure([1], minsize=425, weight=1)
# dur_loop_frm.columnconfigure(2, minsize=40, weight=1)
# ---> DURATION <--- #
dur_lbl = tk.Label(master=dur_loop_frm, text="Duration (hour:min:sec) ", font=("", 15), bg="white")
dur_lbl.pack(side="left", pady=10, padx=(15,3))
dur_entry = ttk.Entry(master=dur_loop_frm, font=("", 15))
dur_entry.pack(side="left")
# ---> LOOP <--- #
loop_lbl = tk.Label(master=dur_loop_frm, text="Loops (inf for infinity) ", font=("", 15), bg="white")
loop_lbl.pack(side="left", pady=10, padx=(15,3))
loop_entry = ttk.Entry(master=dur_loop_frm, font=("", 15))
loop_entry.pack(side="left")
# ---> START BUTTON <--- #
dur_loop_btn = ttk.Button(style = "TButton", master=dur_loop_frm, text="Start", command=start)
dur_loop_btn.pack(side="right", padx=15)

window.mainloop()