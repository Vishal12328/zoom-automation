from selenium import webdriver
from cred import username,password,meetingid
import time

chrome = webdriver.Chrome()
time.sleep(1)

chrome.maximize_window()

chrome.get("https://zoom.us/profile")
time.sleep(4)

log_cl = chrome.find_element_by_xpath( '//*[@id="email"]')
log_cl.send_keys(username)


log_pas = chrome.find_element_by_xpath('//*[@id="password"]')
log_pas.send_keys(password)


log_sig = chrome.find_element_by_xpath(
    '//*[@id="login-form"]/div[4]/div/div[1]/button')
log_sig.click()
log_meet = chrome.find_element_by_xpath(
    '//*[@id="btnJoinMeeting"]')
log_meet.click()
time.sleep(4)
log_meet2 = chrome.find_element_by_xpath(
    '//*[@id="join-confno"]')
log_meet2.send_keys(meetingid)

log_meetbtn = chrome.find_element_by_xpath(
    '//*[@id="btnSubmit"]')
log_meetbtn.click()