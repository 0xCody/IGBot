# -*- coding: utf-8 -*-
from tkinter import *
import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import base64
import os
import time
import datetime as dt
import random


def LoginPage():
    global nameEL
    global pwordEL
    global root
    global icon
	
    root = Tk()  
	
    root.configure(bg='gray')
    root.geometry("725x400")
    root.resizable(width=False, height=False)
    root.title('IGBOT 2K19')
    top_color = Frame(width=900, height=60, bg='#4c7f4e')
    top_color.place(x=0, y=0)

    label = Label(root, fg='white', font='Calibri', bg='#4c7f4e', text='\n#1 Instagram Growth Bot')
    label.place(x=267, y=-5)

    nameL = Label(root, bg="gray", fg='white', font='Calibri', text='Username: ')
    pwordL = Label(root, bg="gray", fg='white', font='Calibri', text='Password: ')
    nameL.place(x=220, y=75)
    pwordL.place(x=220, y=125)

    nameEL = Entry(root, width=50)
    pwordEL = Entry(root, width=50, show='●')
    nameEL.place(x=220, y=105)
    pwordEL.place(x=220, y=155)

    options = ["Comment Bot", "Like Bot", "Follow Bot"]
    global var
    var = StringVar()
    var.set("Pick A Bot")
    menu = OptionMenu(root, var, options[0], options[1], options[2], command=bot_entry)
    menu.place(x=325, y=195)

    loginB = Button(root, text='Login', bg="#4c7f4e", fg='white', width=5, font='Calibri', command=bot_and_login_picked)
    loginB.config(width=20)
    loginB.place(x=270, y=310)

    cr = Label(root, bg="gray", fg='white', font=('Calibri', 10), text='© 2019 Cody Carter. All Rights Reserved')
    cr.place(x=495, y=375)

    root.mainloop()


def bot_entry(entry):
    global commententry
    global likeentry
    global followentry

    try:
        commentblank.destroy()
    except:
        pass
    try:
        likeblank.destroy()
    except:
        pass
    try:
        followblank.destroy()
    except:
        pass

    if var.get() == 'Comment Bot':
        global commentlabel
        global commententry
        commentlabel = Label(root, bg="gray", fg='white', font='Calibri', text='Comment Bot Hashtag: ')
        commentlabel.place(x=220, y=227)
        commententry = Entry(root, width=50)
        commententry.place(x=220, y=257)

    else:
        try:
            commentlabel = Label(root, bg="gray", fg='gray', font='Calibri', text='Comment Bot Hashtag: ')
            commentlabel.place(x=220, y=227)
            commententry.destroy()
        except:
            pass

    if var.get() == 'Like Bot':
        global likelabel
        global likeentry
        likelabel = Label(root, bg="gray", fg='white', font='Calibri', text='Like Bot Hashtag: ')
        likelabel.place(x=220, y=227)
        likeentry = Entry(root, width=50)
        likeentry.place(x=220, y=257)

    else:
        try:
            likeentry.destroy()
            likelabel.destroy()
        except:
            pass

    if var.get() == 'Follow Bot':
        global followlabel
        global followentry
        followlabel = Label(root, bg="gray", fg='white', font='Calibri', text='Follow Bot @: ')
        followlabel.place(x=220, y=227)
        followentry = Entry(root, width=50)
        followentry.place(x=220, y=257)

    else:
        try:
            followentry.destroy()
            followlabel.destroy()
        except:
            pass


def bot_and_login_picked():
    global invalid
    global commentblank
    global likeblank
    global followblank

    if var.get() == 'Comment Bot' and commententry.get() != '':
        try:
            commentblank.destroy()
        except:
            pass

    elif var.get() == 'Like Bot' and likeentry.get() != '':
        try:
            likeblank.destroy()
        except:
            pass

    elif var.get() == 'Follow Bot' and followentry.get() != '':
        try:
            followblank.destroy()
        except:
            pass

    if var.get() == 'Pick A Bot':
        global pickbot
        pickbot = Label(root, bg='gray', text='Please choose a bot type before starting')
        pickbot.place(x=267, y=280)
        pickbot['fg'] = 'white'
        root.mainloop()

    else:
        pickbot = Label(root, bg='gray')
        pickbot.place(x=267, y=280)
        pickbot['fg'] = 'gray'
        pickbot['text'] = 'Please choose a bot type before starting'

    if nameEL.get() == '' or pwordEL.get() == '':

        invalid = Label(root, bg='gray')
        invalid.place(x=220, y=280)
        invalid['fg'] = 'white'
        invalid['text'] = 'You must enter a username and password.'
        pwordEL.delete(0, END)
        root.mainloop()

    else:
        invalid = Label(root, bg='gray')
        invalid.place(x=220, y=280)
        invalid['fg'] = 'gray'
        invalid['text'] = 'You must enter a username and password.'

    if var.get() == 'Comment Bot' and commententry.get() == '':

        commentblank = Label(root, bg='gray', text='Please choose a hashtag (#) for the comment bot')
        commentblank.place(x=220, y=280)
        commentblank['fg'] = 'white'
        root.mainloop()

    try:
        commentblank.destroy()
    except:
        pass

    if var.get() == 'Like Bot' and likeentry.get() == '':

        likeblank = Label(root, bg='gray', text='Please choose a hashtag (#) for the like bot')
        likeblank.place(x=220, y=280)
        likeblank['fg'] = 'white'
        root.mainloop()

    try:
        likeblank.destroy()
    except:
        pass

    if var.get() == 'Follow Bot' and followentry.get() == '':

        followblank = Label(root, bg='gray', text='Please choose a user (@) whose followers you will follow')
        followblank.place(x=220, y=280)
        followblank['fg'] = 'white'
        root.mainloop()

    try:
        followblank.destroy()
    except:
        pass

    igbot = InstagramBot(nameEL.get(), pwordEL.get())
    global popup


    popup = Tk()

    popup.title('Bot Process')
    popup.configure(bg='gray')
    popup.geometry("235x125")
    popup.resizable(width=False, height=False)
    lbl = Label(popup, text='Bot in process...', bg='gray', fg='white', font='Calibri')
    lbl.place(x=50, y=20)
    shutdown = Button(popup, text='Shut Down Bot', bg="#4c7f4e", fg='white', width=5, font='Calibri', command=igbot.quitbot)
    shutdown.config(width=17)
    shutdown.place(x=27, y=65)

    bot_begin = threading.Thread(target=igbot.login)
    bot_begin.start()

    popup.mainloop()


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        # options = webdriver.FirefoxOptions()
        # options.add_argument('-headless')
        self.driver = webdriver.Firefox()

    def login(self):
        global id_invalid
        driver = self.driver
        driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(5)
        driver.find_element_by_name('username').send_keys(self.username)
        driver.find_element_by_name('password').send_keys(self.password)
        driver.find_element_by_name('password').send_keys(Keys.RETURN)

        try:
            time.sleep(5)
            driver.find_element_by_id('slfErrorAlert')
            id_invalid = Label(root, bg='gray')
            id_invalid.place(x=220, y=280)
            id_invalid['text'] = 'Username or Password Incorrect. Try Again!'
            id_invalid['fg'] = 'white'
            pwordEL.delete(0, END)
            driver.quit()
            root.mainloop()

        except:
            id_invalid = Label(root, bg='gray')
            id_invalid.place(x=220, y=280)
            id_invalid['text'] = 'Username or Password Incorrect. Try Again!'
            id_invalid['fg'] = 'gray'
            time.sleep(4)
            InstagramBot.run_bot(self)

    def like_bot(self):
        try:
            global like_error
            like_error.destroy()
        except:
            pass

        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + str(likeentry.get()).rstrip() + "/")

        try:
            time.sleep(3)
            driver.find_element_by_class_name('error-container.-cx-PRIVATE-ErrorPage__errorContainer.-cx-PRIVATE-ErrorPage__errorContainer__')
            InstagramBot.quitbot(self)
            like_error = Label(root, bg='gray', text='Please enter a valid hashtag (#)')
            like_error.place(x=220, y=280)
            like_error['fg'] = 'white'
            root.mainloop()
        except:
            pass

        pic_hrefs = []
        for i in range(1, 7):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(3)
                # get tags
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                # finding relevant hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]
                # building list of unique photos
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]

            except Exception:
                continue

        for pic_href in pic_hrefs:
            if 8 <= dt.datetime.now().hour <= 23:
                driver.get(pic_href)
                try:
                    time.sleep(random.randint(95, 115))
                    like_button = lambda: driver.find_element_by_xpath('//span[@aria-label="Like"]').click()
                    like_button().click()

                except Exception:
                    time.sleep(2)
            else:
                time.sleep(60)

    def follow_bot(self):
        try:
            global follow_error
            follow_error.destroy()
        except:
            pass

        driver = self.driver
        driver.get('https://www.instagram.com/' + str(followentry.get()).rstrip() + '/')
        time.sleep(3)

        try:
            driver.find_element_by_class_name('error-container.-cx-PRIVATE-ErrorPage__errorContainer.-cx-PRIVATE-ErrorPage__errorContainer__')
            InstagramBot.quitbot(self)
            follow_error = Label(root, bg='gray', text='Please enter a valid username (@)')
            follow_error.place(x=220, y=280)
            follow_error['fg'] = 'white'
            root.mainloop()
        except:
            pass

        driver.find_element_by_xpath("//a[@href='/" + followentry.get().rstrip() + "/followers/']").click()
        time.sleep(5)

        for i in range(1, 20):
            popups = driver.find_element_by_xpath("//div[@class='isgrP']")
            popups.send_keys(Keys.END)
            time.sleep(3)

        who_to_follow = driver.find_elements_by_class_name('wo9IH')
        i = 0
        while i < len(who_to_follow):
            if 8 <= dt.datetime.now().hour <= 23:
                try:
                    driver.find_element_by_xpath('//button[@class="_0mzm- sqdOP  L3NKy       "][contains(text(), "Follow")]').click()
                    time.sleep(random.randint(360, 400))

                except:
                    time.sleep(2)

                i += 1
            else:
                time.sleep(60)

    def comment_bot(self):
        try:
            global comment_error
            comment_error.destroy()
        except:
            pass

        driver = self.driver
        comments = ["Love!❤", "Great pic!😍", "You have an awesome feed!🙌"]
        driver.get('https://www.instagram.com/explore/tags/' + str(commententry.get()).rstrip() + '/')
        time.sleep(3)

        try:
            driver.find_element_by_class_name('error-container.-cx-PRIVATE-ErrorPage__errorContainer.-cx-PRIVATE-ErrorPage__errorContainer__')
            InstagramBot.quitbot(self)
            comment_error = Label(root, bg='gray', text='Please enter a valid hashtag (#)')
            comment_error.place(x=220, y=280)
            comment_error['fg'] = 'white'
            root.mainloop()
        except:
            pass

        time.sleep(3)
        hrefs = driver.find_elements_by_tag_name('a')
        hrefs = [ele.get_attribute("href") for ele in hrefs if ".com/p/" in ele.get_attribute("href")]

        fp = open("visited_images.txt")
        data = [line.rstrip() for line in fp]
        fp.close()

        fp = open("visited_images.txt", "a")
        for image in hrefs:
            if image not in data and 8 <= dt.datetime.now().hour <= 23:
                driver.get(image)
                time.sleep(4)
                fp.write(str(image) + '\n')
                data.append(image.strip())
                driver.find_element_by_class_name('Ypffh').click()
                driver.find_element_by_class_name('Ypffh').send_keys(random.choice(comments))
                driver.find_element_by_class_name('Ypffh').send_keys(Keys.RETURN)
                time.sleep(random.randint(775, 860))

        fp.close()

    def quitbot(self):
        popup.destroy()
        self.driver.quit()

    def run_bot(self):
        while True:
            try:
                if var.get() == 'Comment Bot':
                    InstagramBot.comment_bot(self)

                elif var.get() == 'Follow Bot':
                    InstagramBot.follow_bot(self)

                else:
                    InstagramBot.like_bot(self)

            except:
                InstagramBot.quitbot(self)
                time.sleep(60)
                root.mainloop()


LoginPage()
