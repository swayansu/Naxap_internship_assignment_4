from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver  = webdriver.Chrome()
driver.get('https://www.google.com/')

# Enter your favourite song name here
songName = 'Imagine Dragons thunder'
searchBox = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
searchBox.send_keys(songName+ ' lyrics')
searchBox.send_keys(Keys.ENTER) 

lyrics = driver.find_elements_by_xpath('//*[@id="kp-wp-tab-default_tab:kc:/music/recording_cluster:lyrics"]/div[1]/div/div/div[2]/div/div/div/div/div/div/div[1]/div[2]')

# print(lyrics)
f = open('lyrics.txt','w')
for i in lyrics:
  f.write(i.text)
time.sleep(2)
driver.quit()