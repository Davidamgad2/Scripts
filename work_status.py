from ast import While
from time import sleep
from tkinter import MOVETO
from turtle import delay
import pyautogui as pg
import pygetwindow as gw

print("♦All rights reserved to David Amgad♦")
teams=gw.getWindowsWithTitle('EG TS | Microsoft Teams')[0]
browser=gw.getWindowsWithTitle('View: Your unsolved tickets – Cybertron International, Inc. – Zendesk - Opera')[0]


def get_teams():
    """Handling getting the teams window"""
    sleep(1)
    teams.minimize()
    sleep(3)
    teams.maximize()
    sleep(3)
    teams.activate()
    sleep(3)
    pg.click(694,22)
    sleep(3)

def be_available():
    """handling set the status of teams to available"""
    pg.write('/available',0.2)
    pg.press('enter')
    sleep(3)

def write_in_chat():
    """Handling writing in the chat"""
    pg.click(630,678)
    pg.click(630,678)
    sleep(1)
    
def switch_chat():
    """Handling switch chat for the first time"""
    sleep(3)
    pg.click(255,277)
    sleep(3)
    pg.click(630,678)
    sleep(3)

def switch_back():
    """Handling switch back to the main chat"""
    sleep(3)
    pg.click(172,219)

def get_browser():
    """Handling getting the browser"""
    browser.minimize()
    sleep(3)
    browser.maximize()
    sleep(3)
    browser.activate()
    sleep(3)

def get_online():
    """handling getting online"""
    pg.moveTo(1162,120,2)
    pg.click(1162,120)
    sleep(2)
    pg.moveTo(1174,151,2)
    pg.click(1174,151)
    sleep(2)

def get_agent_available():
    """Handling getting available in the agent section"""
    pg.moveTo(1257,123)
    pg.click(1257,123)
    sleep(2)
    pg.moveTo(1191,213)
    pg.click(1191,213)
    sleep(1.5)
    pg.moveTo(1168,230)
    pg.click(1168,230)

def get_away():
    """Handling going in zendesk chat away"""
    pg.moveTo(1162,120,2)
    pg.click(1162,120)
    sleep(3)
    pg.moveTo(1179,180,2)
    pg.click(1179,180)

def be_away():
    """set teams status to away"""
    pg.write('/away',0.5)
    pg.press('enter')
    sleep(3)

def be_offline():
    """Handling getting teams status to offline"""
    pg.write('/offline',0.2)
    pg.press('enter')
    sleep(3)

def get_offline():
    """Handling setting chat and agent availablity to offline"""
    pg.moveTo(1162,120,2)
    pg.click(1162,120)
    sleep(2)
    pg.moveTo(1176,209,2)
    pg.click(1176,209)
    sleep(2)
    pg.moveTo(1257,123,1)
    pg.click(1257,123)
    sleep(2)
    pg.moveTo(1174,214,1)
    pg.click(1174,214)
    sleep(1.5)
    pg.moveTo(1165,241,1)
    pg.click(1165,241)

def main():
    while True :
        x=str(input("Please enter your condition:")).lower() 
    
        if x=='morning':
            get_teams()
            be_available()
            write_in_chat()
            pg.write('Good morning',0.5)
            pg.press('enter')
            switch_chat()
            pg.write('Good morning',0.5)
            pg.press('enter')
            switch_back()
            get_browser()
            get_online()
            get_agent_available()

        elif x=='back':
            get_teams()
            be_available()
            write_in_chat()
            pg.write('Back',0.5)
            pg.press('enter')
            switch_chat()
            pg.write('Back',0.5)
            pg.press('enter')
            switch_back()
            get_browser()
            get_online()
   
        elif x=='lunch':
            get_teams()
            be_away()
            write_in_chat()
            pg.write('Lunch',0.5)
            pg.press('enter')
            switch_chat()
            pg.write('Lunch',0.5)
            pg.press('enter')
            switch_back()
            get_browser()
            get_away()
        
        elif x=='break':
            get_teams()
            be_away()
            write_in_chat()
            pg.write('break',0.5)
            pg.press('enter')
            switch_chat()
            pg.write('break',0.5)
            pg.press('enter')
            switch_back()
            get_browser()
            get_away()
   
        elif x=='night':
            get_teams()
            be_offline()
            write_in_chat()
            pg.write('Good Night',0.5)
            pg.press('enter')
            get_browser()
            get_offline()  

if __name__=="__main__":
    main()