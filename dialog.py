from tkinter import *
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import messagebox

pencere = Tk()
pencere.title("Otomatik Bot Yazılımı")
pencere.geometry("500x350+450+150")
pencere.resizable(FALSE,FALSE)
pencere.state("normal")
pencere['bg'] = '#49A'
lbl0 = Label(text="Hangi platform :",fg = "white" , bg = "green" , font = ("Open Sans" , "18" , "normal"))
lbl0.pack()
secim = Listbox(width=15, height=2,font = ("Open Sans" , "14" , "normal"))
secim.insert(END , "İnstagram")
secim.insert(END ,"Twitter")
secim.pack()
tercih = Listbox(width=15, height=2 , font = ("Open Sans" , "14" , "normal"))
tercih.insert(1, "Takip et")
tercih.insert(2, "Takip bırak")
tercih.pack()
lblx1 = Label(text="", bg = '#49A' )
lblx1.pack()
lbl1 = Label(text="Kullanıcı adınızı giriniz:",fg = "white" , bg = "blue" , font = ("Open Sans" , "18" , "normal"))
lbl1.pack()
textbox1 = Entry(width=30)
textbox1.pack()
lblx2 = Label(text="", bg = '#49A' )
lblx2.pack()
lbl2 = Label(text="Şifrenizi Giriniz:",fg = "white" , bg = "red" , font = ("Open Sans" , "18" , "normal"))
lbl2.pack()
textbox2 = Entry(width=30,show = "*")
textbox2.pack()

def twgiris():
    kl = textbox1.get()
    sfr = textbox2.get()
    browser = webdriver.Chrome()
    browser.get("https://twitter.com/login")
    time.sleep(2)
    kulInp = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input")
    sfrInp = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input")
    kulInp.send_keys(kl)
    sfrInp.send_keys(sfr)
    sfrInp.send_keys(Keys.ENTER)
    browser.get("https://twitter.com/i/connect_people")
    time.sleep(4)
    a=2
    while a<15:
        try:
            browser.find_element_by_xpath(f"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/section/div/div/div[{a}]/div/div/div/div[2]/div[1]/div[2]/div/div/span/span").click()
        except:
            browser.refresh()
            a =2
        a += 1
        time.sleep(2)
        if a%10 == 0:
            browser.refresh()
            time.sleep(3)
            a=2
def insgiris():
    kull = textbox1.get()
    sfr = textbox2.get()
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(2)
    yazi = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input")
    sifre = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input")
    yazi.send_keys(kull)
    sifre.send_keys(sfr)
    sifre.send_keys(Keys.ENTER)
    time.sleep(2)
    driver.get("https://www.instagram.com/explore/people/suggested/")
    time.sleep(3)
    a = 1
    while a<500:
        btn1 = driver.find_element_by_xpath(f"//*[@id='react-root']/section/main/div/div[2]/div/div/div[{a}]/div[3]/button")
        btn1.click()
        a +=1
        time.sleep(2)
        if a%15 == 0:
            driver.refresh()
            time.sleep(2)
            a=1
def insbirak():
    kull = textbox1.get()
    sfr = textbox2.get()
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(2)
    yazi = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input")
    sifre = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input")
    yazi.send_keys(kull)
    sifre.send_keys(sfr)
    sifre.send_keys(Keys.ENTER)
    time.sleep(2)
    driver.get(f"https://www.instagram.com/{kull}/")
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a/span").click()
    time.sleep(2)
    b = 1
    while b<500:
        driver.find_element_by_xpath(f"/html/body/div[4]/div/div/div[2]/ul/div/li[{b}]/div/div[2]/button").click()
        time.sleep(.5)
        driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[1]").click()
        b +=1
        time.sleep(.5)
def twbirak():
    kl = textbox1.get()
    sfr = textbox2.get()
    browser = webdriver.Chrome()
    browser.get("https://twitter.com/login")
    time.sleep(2)
    kulInp = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input")
    sfrInp = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input")
    kulInp.send_keys(kl)
    sfrInp.send_keys(sfr)
    sfrInp.send_keys(Keys.ENTER)
    browser.get(f"https://twitter.com/{kl}/following")
    time.sleep(3)
    a=1
    while a<500:
        browser.find_element_by_xpath(f"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/section/div/div/div[{a}]/div/div/div/div[2]/div[1]/div[2]/div/div/span/span").click()
        time.sleep(.5)
        browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div[3]/div[2]/div").click()
        time.sleep(.5)
        a += 1
        if a%15 == 0:
            browser.refresh()
            time.sleep(2)
            a=1


def secici():
    
    if secim.get(ACTIVE) == "İnstagram" :
        if tercih.get(ACTIVE) == "Takip et" :
            insgiris()
        if tercih.get(ACTIVE) == "Takip bırak":
            insbirak()
    elif secim.get(ACTIVE) == "Twitter" :
        if tercih.get(ACTIVE) == "Takip et" :
            twgiris()
        if tercih.get(ACTIVE) == "Takip bırak" :
            twbirak()
    else :
        messagebox.showerror("Hata", "Seçim yapınız...")
buton = Button(pencere, text = "Başla", command = secici)
buton.pack()
mainloop()