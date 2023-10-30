import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from nose import tools
from mqtt_push import AHUGpro,data

url = "http://172.16.1.106:3000/"
web_driver_path="../drive_lib/chromedriver.exe"
with open("../config/config.conf","r") as conf:
  datas=conf.read()

data=data
class gui_handle(object):
  conf_data = json.loads(datas)
  def __init__(self,conf_data=conf_data):
    self.conf_data=conf_data

  def handler(self):
    try:
      service = Service(executable_path=web_driver_path)
      browser_handler=webdriver.Chrome(service=service)
      browser_handler.maximize_window()
      browser_handler.get(url)
      browser_handler.implicitly_wait(15)
      return browser_handler
    except Exception as err:
      return err


  def ems_login(self,username=conf_data["username"],password=conf_data["password"]):
    try:
      browser_handler=self.handler()
      xpath_user='//*[@id="root"]/div/div/div/div/div/div[1]/div/form/div[1]/input'
      browser_handler.find_element(By.XPATH,xpath_user).send_keys(username)
      xpath_pswrd='//*[@id="root"]/div/div/div/div/div/div[1]/div/form/div[2]/input'
      browser_handler.find_element(By.XPATH,xpath_pswrd).send_keys(password)
      xpath__ligin_button='//*[@id="root"]/div/div/div/div/div/div[1]/div/form/div[4]/div/button'
      browser_handler.find_element(By.XPATH,xpath__ligin_button).click()
      time.sleep(10)
      try:
        result=browser_handler.find_element(By.XPATH,'/html/body/div/div/footer/span[2]').text
        print("login successfully done")
      except:
        xpath = '/html/body/div/div/div/div/div/div/div[1]/div/form/div[3]/div/h6'
        result=browser_handler.find_element(By.XPATH,xpath).text
        print(result)
        print("login failed")
        tools.assert_equal(True,False,"login failed")
      return browser_handler
    except Exception as err:
       return [browser_handler,"login failed wrong username or password"]

  def Type_lib(self):
    xpath='/html/body/div/div/div/div/div/ul/li[2]/a'
    xpath1='/html/body/div/div/div/div/div/ul/li[2]/ul/li[1]/a'
    result=self.ems_login()
    result.find_element(By.XPATH,xpath).click()
    result.find_element(By.XPATH,xpath1).click()
    time.sleep(3)
    return result

  def Device_list_lib(self):
    xpath = '/html/body/div/div/div/div/div/ul/li[2]/a'
    xpath1 = '/html/body/div[1]/div/div/div/div/ul/li[2]/ul/li[2]/a'
    result = self.ems_login()
    result.find_element(By.XPATH, xpath).click()
    result.find_element(By.XPATH, xpath1).click()
    time.sleep(3)
    return result

  def device_property_lib(self):
    xpath = '/html/body/div/div/div/div/div/ul/li[2]/a'
    xpath1 = '/html/body/div/div/div/div/div/ul/li[2]/ul/li[3]/a'
    result = self.ems_login()
    result.find_element(By.XPATH, xpath).click()
    result.find_element(By.XPATH, xpath1).click()
    time.sleep(3)
    return result

  def AHU(self,data):
    AHUGpro.data1(self,data=data)


if __name__ == "__main__":
  obj=gui_handle()
  obj.AHU()
