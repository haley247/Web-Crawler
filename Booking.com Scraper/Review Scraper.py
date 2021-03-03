#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import time

import pandas as pd


# In[3]:


chromedriver = "/Users/hoaha/Documents/chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.get("https://booking.com")

time.sleep(2)
driver.find_element_by_css_selector("input[class*='sb-searchbox__input']").send_keys("Britannia International Hotel Canary Wharf")
driver.find_element_by_css_selector("button[type='submit']").click()
driver.find_element_by_xpath("//span[contains(text(),'Britannia International Hotel Canary Wharf')]").click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(3)
driver.find_element_by_css_selector('#show_reviews_tab').click() 

driver.switch_to.window(driver.window_handles[1])

Name = []
Country = []
Room_stayed = []
Date_stayed = []
Trip_type = []
Review_date = []
Review_title = []
Positive = []
Negative = []
Reviewer_score =[]

while True:
    room_info_eles = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div[itemprop='review']")))
    for element in room_info_eles:
        try:
            Name.append(element.find_element_by_class_name('bui-avatar-block__title').text)
        except:
            Name.append("Not Available")
            
        try:
            Country.append(element.find_element_by_class_name('bui-avatar-block__subtitle').text)
        except:
            Country.append("Not Available")
            
        try:
            Room_stayed.append(element.find_elements_by_class_name("bui-list__body")[0].text)
        except:
            Room_stayed.append("Not Available")
            
        try:
            Date_stayed.append(element.find_elements_by_class_name("bui-list__body")[1].text)
        except:
            Date_stayed.append("Not Available")
        
        try:
            Trip_type.append(element.find_elements_by_class_name("bui-list__body")[2].text)
        except:
            Trip_type.append("Not Available")
        
        try:
            Review_date.append(element.find_elements_by_class_name("c-review-block__date")[1].text)
        except:
            Review_date.append("Not Available")
        
        try:
            Review_title.append(element.find_elements_by_class_name("bui-grid__column-10")[0].text)
        except:
            Review_title.append("Not Available")
        
        try:
            Positive.append(element.find_elements_by_class_name("c-review__body")[0].text)
        except:
            Positive.append("Not Available")
        
        try:
            Negative.append(element.find_elements_by_class_name("c-review__body")[1].text)
        except:
            Negative.append("Not Available")
        
        try:
            Reviewer_score.append(element.find_elements_by_class_name("bui-review-score__badge")[0].text)
        except:
            Reviewer_score.append("Not Available")
        
    try:
        WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[class='pagenext']"))).click()
    except Exception: 
        break


# In[4]:


df = pd.DataFrame({"Name":Name,
                   "Country":Country,
                  "Room_stayed":Room_stayed,
                  "Date_stayed":Date_stayed,
                  "Trip_type":Trip_type,
                  "Review_date":Review_date,
                  "Review_title":Review_title,
                  "Positive":Positive,
                  "Negative":Negative,
                  "Reviewer_score":Reviewer_score})


# In[20]:


df.head(50)


# In[16]:


pd.set_option('display.max_colwidth', -1)


# In[23]:


df.loc[df['Name']=="Meng"]


# In[22]:


df.to_csv('Britannia International Hotel Canary Wharf.csv', encoding='utf-8')


# In[ ]:




