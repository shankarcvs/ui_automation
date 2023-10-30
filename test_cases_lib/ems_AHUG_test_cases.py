import json
import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from ui_automation_lib import gui_handle as ui_lib
from nose import tools
import pyautogui
present_date=str(datetime.now())

with open("../duplicate/AHU.json",'r') as ahu:
    ahu_data=ahu.read()
ahu_data=json.loads(ahu_data)
ahu_data['updatedat']=present_date
print(ahu_data['updatedat'])
class AHUG_class(ui_lib):
    def __init__(self):
        self.ahu_data=ahu_data
    def refresh_path_AHUG(self,index,update_data):
        self.ahu_data["AHUGproperty"][index]["value"]=update_data
        ui_lib.AHU(self,data=self.ahu_data)
        xpath2 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select'
        xpath3 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select/option[3]'
        xpath4 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[3]/button/i'
        xpath5 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[2]/b[2]'
        result = ui_lib.device_property_lib(self)
        result.find_element(By.XPATH, xpath2).click()
        time.sleep(2)
        result.find_element(By.XPATH, xpath3).click()
        time.sleep(2)
        result.find_element(By.XPATH, xpath4).click()
        time.sleep(5)
        Results = result.find_element(By.XPATH, xpath5).text
        date = Results.split("T")
        tools.assert_in(str(date[0]),str(datetime.now()),  "Test case failed not updated datetime")
        return result

    def change_mode_to_manaul_AHUG(self):
        update_data='MANUAL'
        result=self.refresh_path_AHUG(index=0,update_data=update_data)
        xpath="/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[2]"
        updata=result.find_element(By.XPATH,xpath).text
        tools.assert_equal(update_data,updata,"change_mode_to_manaul_AHUG failed ")
        return "upadated to the manual mode"

    def change_mode_to_auto_AHUG(self):
        update_data='AUTO'
        result=self.refresh_path_AHUG(index=0,update_data=update_data)
        xpath="/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[2]"
        updata=result.find_element(By.XPATH,xpath).text
        tools.assert_equal(update_data,updata,"change_mode_to_auto_AHUG failed ")
        return "upadated to the auto mode"

    def neg_ve_TC_change_mode_to_AHUG(self):
        update_data=100
        result=self.refresh_path_AHUG(index=0,update_data=update_data)
        xpath="/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[2]"
        updata=result.find_element(By.XPATH,xpath).text
        tools.assert_not_equal(update_data,updata,"neg_ve_TC_change_mode_to_AHUG failed ")
        return "negative test on mode changing passed it does not updated"

    def neg_ve_TC_change_machine_status_to_AHUG(self):
        update_data=500
        result=self.refresh_path_AHUG(index=8,update_data=update_data)
        xpath='/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[2]/td[2]'
        updata=result.find_element(By.XPATH,xpath).text
        tools.assert_not_equal(update_data,updata,"neg_ve_TC_change_mode_to_AHUG failed ")
        return "negative test on mode changing passed it does not updated"

    def neg_ve_TC_change_AirSpeed_to_AHUG(self):
        update_data="Altiux"
        result=self.refresh_path_AHUG(index=8,update_data=update_data)
        xpath='/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[4]/td[2]'
        updata=result.find_element(By.XPATH,xpath).text
        tools.assert_not_equal(update_data,updata,"neg_ve_TC_change_mode_to_AHUG failed ")
        return "negative test on mode changing passed it does not updated"


if __name__ == "__main__":
    d=AHUG_class()
    d.change_mode_to_auto_AHUG()
