from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import re
import pandas as pd
import os
import time

driver = webdriver.Chrome("C:/webdrivers/chromedriver")
url = "https://web.bcpa.net/BcpaClient/#/Commercial-Search"

class Store:
    def __init__(self, owner, address, ID, year, SF):
        self.owner = owner
        self.address = address
        self.ID = ID
        self.year = year
        self.SF = SF
SL = []

for i in range(1,20):

    

    driver.get(url)
    element = driver.find_element_by_id("ddbComCity")
    drop1 = Select(element)
    drop1.select_by_index(i)
    element = driver.find_element_by_id("ddbUseCode")
    drop2 = Select(element)
    drop2.select_by_index(18)

    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[2]/span").click()
    time.sleep(2)

    loops = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div").text
    loops = loops.split()
    
    loopingNumber = int(loops[2])

        



    for i in range(1, loopingNumber):

        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[5]/div/div/table/tbody/tr[" + str(i) + "]/td[1]/div/a").click()

        
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/ul/li[1]/a").click()

        propertyOwner = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div[1]/div[7]/div[1]/table[1]/tbody/tr[1]/td[2]/div[1]").text

        addy = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div[1]/div[7]/div[1]/table[2]/tbody/tr[1]/td[2]/div/span/a").text

        idNumber = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div[1]/div[7]/div[1]/div[1]/table/tbody/tr/td[2]/div/span/a").text

        yearBuilt = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div[1]/div[7]/div[1]/table[3]/tbody/tr[6]/td[2]/div").text

        SquareFootage = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div[1]/div[7]/div[1]/table[3]/tbody/tr[3]/td[2]/span[1]").text


        prop = Store(propertyOwner, addy, idNumber, yearBuilt, SquareFootage)

        



        SL.append(prop)



        for store in SL:
            print("Owner: ",store.owner)
            print("Address: ",store.address)
            print("ID: ",store.ID)
            print("SF: ",store.SF)
            print("Year: ",store.year)
            print(" ")
        
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/ul/li[2]/a").click()

        time.sleep(1)
    
  
   
