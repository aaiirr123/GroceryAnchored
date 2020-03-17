from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import re
import pandas as pd
import os
import time

#This code grabs the website in question
driver = webdriver.Chrome("C:/webdrivers/chromedriver")
url = "https://web.bcpa.net/BcpaClient/#/Commercial-Search"
driver.get(url)

#Allows for the creation of dataframe
totalObjectCount = 0

#input the range of cities in the county
range = input()


#This class holds the data for the stores
class Store:
    def __init__(self, owner, address, ID, year, SF):
        self.owner = owner
        self.address = address
        self.ID = ID
        self.year = year
        self.SF = SF
SL = []

#This loop switches between cities in the county
for i in range(1,range):

    

        


    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/ul/li[1]/a").click()
    
    time.sleep(2)
    #selects city
    element = driver.find_element_by_id("ddbComCity")
    drop1 = Select(element)
    drop1.select_by_index(i)
    #Selects use code
    element = driver.find_element_by_id("ddbUseCode")
    drop2 = Select(element)
    drop2.select_by_index(18)


    try:
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[2]/span").click()
        print("going thotouhg")
    except:
        print("Could not click on element")
    
    time.sleep(1)

    noWork = False

    #trys to get data three times if theres issues with search results
    for m in range(3):

        time.sleep(.5)

        try:                            
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/ul/li[2]/a").click()
        except:
            print("didnt work x :", m)
            if m == 2:
                print("Continued")
                noWork = True
                break
    if noWork == True:
        continue

    time.sleep(2)


    loops = []

    #Trys to get the number of stores
    while loops == []:
        time.sleep(1)
        loops = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div").text
        if loops == []:
            continue
        


    loops = loops.split()
    
    #Takes the looping number and turns it into an integer
    loopingNumber = int(loops[2])
    

        



    for j in range(1, loopingNumber):
        
    #trys to grab data from store locations

        time.sleep(3)
        try:
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[5]/div/div/table/tbody/tr[" + str(j) + "]/td[1]/div/a").click()
        except:
            print("Element not found")
            continue
        
        time.sleep(1)
        try:
            propertyOwner = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div[1]/div[7]/div[1]/table[1]/tbody/tr[1]/td[2]/div[1]").text
        except:
            print("No property owners")
            propertyOwner = 'NA'

        try:
            addy = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div[1]/div[7]/div[1]/table[2]/tbody/tr[1]/td[2]/div/span/a").text
        except:
            print("No address")
            addy = 'NA'

        try:
            idNumber = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div[1]/div[7]/div[1]/div[1]/table/tbody/tr/td[2]/div/span/a").text
        except:
            print("No ID")
            idNumber = 'NA'

        try:
            yearBuilt = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div[1]/div[7]/div[1]/table[3]/tbody/tr[6]/td[2]/div").text
        except:
            print("No year built")
            yearBuilt = "NA"

        try:
            SquareFootage = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div[1]/div[7]/div[1]/table[3]/tbody/tr[3]/td[2]/span[1]").text
        except:
            print("No square footage")
            SquareFootage = 'NA'

        prop = Store(propertyOwner, addy, idNumber, yearBuilt, SquareFootage)
        



        SL.append(prop)

        totalObjectCount+=1




        time.sleep(3)
    

        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/ul/li[2]/a").click()

Ow = []
Ad = []
I = []
Ye = []
Sf = []

for k in range(0,totalObjectCount):
    Ow.append(SL[k].owner)
    Ad.append(SL[k].address)
    I.append(SL[k].ID)
    Ye.append(SL[k].year)
    Sf.append(SL[k].SF)

Dataf = { "Owner" : Ow,  "Address" : Ad, "ID" : I, "Year" : Ye, "SF" : Sf}


df = pd.DataFrame(Dataf, columns = ['Owner', 'Address', 'ID', 'Year', 'SF'])


df.to_csv('StoreData.csv')                                
    
  
   
