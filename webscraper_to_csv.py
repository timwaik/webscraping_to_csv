"""Testing webscraper. Headless browser version"""
from bs4 import BeautifulSoup
from selenium import webdriver
import ctypes
import itertools
import os
import sys
from datetime import datetime, timedelta

def main():
    #Configure chrome for headless
    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    #Filename of csv
    filename = "StockPrice.csv"
    #Price list
    price = []

    stock_name = [

                    "Maybank",
                    "CIMB Malaysia",
                    "RHB Bank",
                    "Hong Leong Bank",
                    "Ambank",
                    "Maxis",
                    "Digi" ,
                    "Axiata",
                    "Telekom Malaysia",
                    "Petronas Gas Bhd",
                    "Tenaga Nasional Bhd",
                    "British American Tobacco Malaysia",
                    "YTL",
                    "Astro Bhd" ,
                    "Genting",
                    "Gamuda",

                    ]

    webpage_list_dict = {

        "Maybank" : "https://www.google.com/search?q=maybank+stock",
        "CIMB Malaysia" : "https://www.google.com/search?q=cimb+malaysia+stock",
        "RHB Bank" : "https://www.google.com/search?q=rhb+stock",
        "Hong Leong Bank" : "https://www.google.com/search?q=hongleong+stock",
        "Ambank" : "https://www.google.com/search?q=ambank+stock",
        "Maxis" : "https://www.google.com/search?q=maxis+stock",
        "Digi" : "https://www.google.com/search?q=digi+stock",
        "Axiata" : "https://www.google.com/search?q=axiata+stock",
        "Telekom Malaysia" : "https://www.google.com/search?q=telekom+stock",
        "Petronas Gas Bhd" : "https://www.google.com/search?q=petronas+gas+stock",
        "Tenaga Nasional Bhd" : "https://www.google.com/search?q=tenaga+stock",
        "British American Tobacco Malaysia" : "https://www.google.com/search?q=bat+malaysia+stock",
        "YTL" : "https://www.google.com/search?q=ytl+stock",
        "Astro Bhd" : "https://www.google.com/search?q=astro+stock",
        "Genting" : "https://www.google.com/search?q=genting+stock",
        "Gamuda" : "https://www.google.com/search?q=gamuda+stock",

    }
    path = "C:\\Users\\khoo.timwai\\Documents\\My Own Documents\\Code\\python\\BeautifulSoup"
    #os.chdir(path)
    #print(os.cwd)

    #Get the current time to nearest half hour
    time_now = datetime.now()
    print("This is a record for time :")
    if time_now.minute >= 15 and time_now.minute <= 45:
        timestamp = time_now.replace(second=0, microsecond=0, minute=30)
        print(timestamp)
    elif time_now.minute <= 15:
        timestamp = time_now.replace(second=0, microsecond=0, minute=0)
        print(timestamp)
    elif time_now.minute >= 45:
        timestamp = (time_now.replace(second=0, microsecond=0, minute=0, hour=time_now.hour+1))
        print(timestamp)

    timestamp = timestamp.strftime("%d %m %Y - %H:%M:%S")
    print(timestamp)

    #Used selenium to load js scripts, which allows us to capture dynamic data loaded by js
    browser = webdriver.Chrome(executable_path = "C:\\Users\\khoo.timwai\\Documents\\My Own Documents\\chromedriver_win32\\chromedriver.exe",\
                               chrome_options = options)


    for name, webpage in webpage_list_dict.items():

        browser.get(webpage)
        browser.page_source

        #Parsing data from webpage using beautiful soup
        soup = BeautifulSoup(browser.page_source,"html.parser")
        price_box = soup.find("span", attrs={"class":"IsqQVc"})
        price.append(price_box.get_text())

        #Proof of concept
        #print("The price of the stock is: ",price_box.get_text())
    print("Stock successfully added")
    #Close browser
    browser.close()

    #Write to csv file
    if os.path.exists(filename):
        print("File exists! No need for headers..")
        for x in price:
            append_file = open(filename, "a")
            append_file.write(x + ",")
        append_file.write(timestamp)
        append_file.write("\n")
        append_file.close()
    else:
        print("File doesn't exist! Creating it now..")
        write_file = open(filename, "w")
        print("File created, writing headers..")
        for x in stock_name:
            write_file.write(x + ",")
        write_file.write("Time Stamp,")
        write_file.write("\n")
        write_file.close()
        print("Headers created! Adding data now..")
        for x in price:
            append_file = open(filename, "a")
            append_file.write(x + ",")
        append_file.write(timestamp)
        append_file.write("\n")
        append_file.close()

main()
