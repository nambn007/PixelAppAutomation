import json
from typing import List

from Genlogin import Genlogin
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

gen = Genlogin("")

data_gen = gen.getProfiles(0,30)
print("typeof->",type(data_gen))
filtered_profiles = []
# Lọc các hồ sơ có "profile_group_ids" chứa [17529]
for profile in data_gen['profiles']:
    if profile['profile_group_ids'] == [17529]:
        filtered_profiles.append(profile)

print(len(filtered_profiles))



profileID = gen.getProfiles(0,1)["profiles"][0]["id"]
wsEndpoint = gen.runProfile(profileID)["wsEndpoint"].replace("ws://","").split('/')[0]
print(type(wsEndpoint))
print(wsEndpoint)
#
chrome_driver = 'chromedriver.exe'
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", wsEndpoint)

service = Service(executable_path=r'chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)

print(type(driver))
driver.get("https://genlogin.com")
time.sleep(5)

