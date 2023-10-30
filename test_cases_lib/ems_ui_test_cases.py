import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from ui_automation_lib import gui_handle as ui_lib
from nose import tools
import pyautogui

class test_case_class(ui_lib):
    def __init__(self):
        pass

    #TC_01
    #login to the ems page using credentials
    def login(self):
        #ui_lib.conf_data["username"]
        result=ui_lib.ems_login(self)
        if type(result)==list:
            tools.assert_not_in("login failed wrong username or password",result[1],result[1])
        return

    def total_sensors(self):
        result=ui_lib.ems_login(self)
        im1 = pyautogui.screenshot()
        im1.save("sensor_screenshot.png")
        total_text=result.find_element(By.XPATH,'//*[@id="style-15"]/div/h1').text
        active_text=active_text=result.find_element(By.XPATH,'/html/body/div/div/div/main/div/div/div[2]/div[2]/div/div[2]').text
        in_active_text=in_active_text=result.find_element(By.XPATH,'/html/body/div/div/div/main/div/div/div[2]/div[3]/div/div[2]/div/h1').text
        tools.assert_equal(int(active_text)+int(in_active_text),int(total_text),"total sensor details miss matching")
        print("total sensor",total_text)
        return [int(total_text),int(active_text),int(in_active_text)]


    def active_sensors(self):
        result=self.total_sensors()
        tools.assert_equal(result[0]-result[2],result[1],"active sensor details miss matching")
        return "active sensors :",result[1]

    def in_active_sensors(self):
        result=self.total_sensors()
        tools.assert_equal(result[0]-result[1],result[2],"in active sensor details are miss matching")
        return "inactive sensors :",result[2]

    def alarms_list(self):
        xpath='/html/body/div/div/div/main/div/div/div[3]/div/div/div[2]/center/h3'
        result=ui_lib.ems_login(self)
        data=result.find_element(By.XPATH,xpath).text
        tools.assert_equal("No records found!!",data,"alarms results failing")
        return data

    def network_id(self):
        xpath='/html/body/div/div/header/ul/li[1]/h6'
        result=ui_lib.ems_login(self)
        data=result.find_element(By.XPATH,xpath).text
        data1=data.split()
        tools.assert_equal(ui_lib.conf_data["username"],data1[2],"miss matching network id")
        return data

    def check_profile(self):
        xpath = '/html/body/div/div/header/ul/li[4]/a/i'
        xpath1 = '//*[@id="root"]/div/header/ul/li[4]/div/button[1]'
        xpath2 = '/html/body/div/div/div/main/div/div/div[2]/div/div/div[2]/form'
        result = ui_lib.ems_login(self)
        result.find_element(By.XPATH, xpath).click()
        result.find_element(By.XPATH, xpath1).click()
        time.sleep(3)
        im1 = pyautogui.screenshot()
        im1.save("check_profile_screenshot.png")
        out_data = result.find_element(By.XPATH, xpath2).text
        return out_data

    def neg_tve_test_login_diff_user(self):
        xpath = '/html/body/div/div/div/div/div/div/div[1]/div/form/div[3]/div/h6'
        data=ui_lib.ems_login(self,username="user",password=ui_lib.conf_data["password"])
        try:
            outdata=data[0].find_element(By.XPATH,xpath).text
            tools.assert_equal("username or password is incorrect",outdata,"login test case passed with different credentials")
        except:
            raise "login unsuccessfull element not found "
        return outdata

    def neg_tve_test_login_diff_pswrd(self):
        xpath = '/html/body/div/div/div/div/div/div/div[1]/div/form/div[3]/div/h6'
        data=ui_lib.ems_login(self,username=ui_lib.conf_data['username'],password="pasrd")
        try:
            outdata=data[0].find_element(By.XPATH,xpath).text
            tools.assert_equal("username or password is incorrect",outdata,"login test case passed with different credentials")
        except:
            raise "login unsuccessfull element not found "
        return outdata

    def neg_tve_test_login_diff_both(self):
        xpath='/html/body/div/div/div/div/div/div/div[1]/div/form/div[3]/div/h6'
        data=ui_lib.ems_login(self,username="user",password="pass")
        try:
            outdata=data[0].find_element(By.XPATH,xpath).text
            tools.assert_equal("username or password is incorrect",outdata,"login test case passed with different credentials")
        except:
            raise "login unsuccessfull element not found "
        return outdata

    def neg_tve_test_login_empty_user(self):
        xpath = '/html/body/div/div/div/div/div/div/div[1]/div/form/div[3]/div/h6'
        data=ui_lib.ems_login(self,username="",password=ui_lib.conf_data["password"])
        try:
            outdata=data[0].find_element(By.XPATH,xpath).text
            tools.assert_equal("username or password is incorrect",outdata,"login test case passed with different credentials")
        except:
            raise "login unsuccessfull element not found "
        return outdata

    def neg_tve_test_login_empty_pswrd(self):
        xpath = '/html/body/div/div/div/div/div/div/div[1]/div/form/div[3]/div/h6'
        data=ui_lib.ems_login(self,username=ui_lib.conf_data['username'],password="")
        try:
            outdata=data[0].find_element(By.XPATH,xpath).text
            tools.assert_equal("username or password is incorrect",outdata,"login test case passed with different credentials")
        except:
            raise "login unsuccessfull element not found "
        return outdata

    def neg_tve_test_login_empty_both(self):
        xpath='/html/body/div/div/div/div/div/div/div[1]/div/form/div[3]/div/h6'
        data=ui_lib.ems_login(self,username="",password="")
        try:
            outdata=data[0].find_element(By.XPATH,xpath).text
            tools.assert_equal("username or password is incorrect",outdata,"login test case passed with different credentials")
        except:
            raise "login unsuccessfull element not found "
        return outdata


    def Log_out(self):
        xpath = '/html/body/div/div/header/ul/li[4]/a/i'
        xpath1 = '/html/body/div/div/header/ul/li[4]/div/button[2]'
        xpath2 = '/html/body/div/div/div/div/div/div/div[1]/div/form/h1'
        result = ui_lib.ems_login(self)
        result.find_element(By.XPATH, xpath).click()
        result.find_element(By.XPATH, xpath1).click()
        Results = result.find_element(By.XPATH, xpath2).text
        tools.assert_equal("Login", Results, "log_out test case failed")
        return "logout successufully working"

    def Type_list(self):
        xpath2 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select/option[3]'
        xpath3='/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[2]'
        result = ui_lib.Type_lib(self)
        result.find_element(By.XPATH,xpath2).click()
        Results=result.find_element(By.XPATH,xpath3).text
        time.sleep(3)
        tools.assert_in("AHUG",Results,"Type_list test case failed")
        return Results


    def create_device_Type(self):
        xpath2 = '/html/body/div/div/div/main/div/div/div/div/div/div[1]/div/button/i'
        xpath3 = '/html/body/div[2]/div/div[1]/div/div/div[2]/div/div/div[2]/div/form/div[1]/div[2]/input'
        xpath4 = '/html/body/div[2]/div/div[1]/div/div/div[2]/div/div/div[2]/div/form/div[2]/div[2]/input'
        xpath5 = '/html/body/div[2]/div/div[1]/div/div/div[2]/div/div/div[2]/div/form/div[3]/div[2]/pre/textarea'
        xpath6 = '/html/body/div[2]/div/div[1]/div/div/div[3]/button[1]'
        xpath7 = '/html/body/div[2]/div/div/div/div[1]'
        result = ui_lib.Type_lib(self)
        result.find_element(By.XPATH, xpath2).click()
        result.find_element(By.XPATH, xpath3).send_keys("delete")
        result.find_element(By.XPATH, xpath4).send_keys("Air handling unit practice creation")
        result.find_element(By.XPATH, xpath5).send_keys('''{"deviceid": "","devicetype": "CO2","updatedat": "","NumberofProperties": 1,"properties": [{"property": "CO2 Level (ppm)","value type": "integer","mandatory": true,"editable": false,"unit": "ppm"}]}''')
        result.find_element(By.XPATH, xpath6).click()
        time.sleep(5)
        Results = result.find_element(By.XPATH, xpath7).text
        print((Results))
        time.sleep(5)
        tools.assert_equal("New type created successfully", Results, "Device Creation failed")
        return Results


    def View_Device_Type(self):
        xpath00 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select'
        xpath000 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select/option[3]'
        xpath0= '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[2]/input'
        xpath2 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[2]/table/tbody/tr/td[3]/strong/button[1]/i'
        xpath3 = '/html/body/div[3]/div/div[1]/div/div'
        result = ui_lib.Type_lib(self)
        result.find_element(By.XPATH, xpath00).click()
        result.find_element(By.XPATH, xpath000).click()
        time.sleep(2)
        result.find_element(By.XPATH, xpath0).send_keys("delete")
        time.sleep(3)
        result.find_element(By.XPATH, xpath2).click()
        time.sleep(3)
        Results=result.find_element(By.CLASS_NAME,'modal-content').text
        tools.assert_in("View Type", Results, "view device type failed")
        print(Results)

    def Edit_Device_type(self):
        xpath00 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select'
        xpath000 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select/option[3]'
        xpath2= '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[2]/input'
        xpath3= '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[2]/table/tbody/tr/td[3]/strong/button[2]/i'
        xpath4= '/html/body/div[2]/div/div[1]/div/div/div[3]/button[1]'
        xpath5 = '/html/body/div[2]/div/div/div/div[1]'
        result = ui_lib.Type_lib(self)
        result.find_element(By.XPATH, xpath00).click()
        result.find_element(By.XPATH, xpath000).click()
        result.find_element(By.XPATH, xpath2).send_keys("delete")
        time.sleep(5)
        result.find_element(By.XPATH,xpath3).click()
        time.sleep(3)
        result.find_element(By.XPATH,xpath4).click()
        time.sleep(3)
        Results = result.find_element(By.XPATH, xpath5).text
        time.sleep(5)
        tools.assert_equal("Device type updated successfully", Results, "Device type updated failed")
        return Results

    def Delete_Device_type(self):
        xpath00= '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select'
        xpath000= '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select/option[3]'
        xpath2 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[2]/input'
        xpath3 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[2]/table/tbody/tr/td[3]/strong/button[3]'
        xpath4= '/html/body/div[2]/div/div[1]/div/div/div[3]/button[1]'
        xpath5 = '/html/body/div[2]/div/div/div/div[1]'
        result = ui_lib.Type_lib(self)
        result.find_element(By.XPATH, xpath00).click()
        result.find_element(By.XPATH, xpath000).click()
        time.sleep(2)
        result.find_element(By.XPATH, xpath2).send_keys("delete")
        time.sleep(5)
        result.find_element(By.XPATH, xpath3).click()
        time.sleep(5)
        curser=pyautogui.position()
        time.sleep(3)
        pyautogui.moveTo(799, 292)
        pyautogui.click()
        time.sleep(3)
        Results =result.find_element(By.CLASS_NAME,'Toastify__toast-body').text
        print(Results)
        tools.assert_equal("Device type successfully deleted", Results, "device deletion failed")
        return Results

    def search_device_type(self):
        xpath2= '//*[@id="root"]/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[2]/input'
        xpath3= '//*[@id="root"]/div/div/main/div/div/div/div/div/div[2]/div[2]/table/tbody/tr/td[2]'
        result = ui_lib.Type_lib(self)
        time.sleep(2)
        result.find_element(By.XPATH,xpath2).send_keys("CCN")
        time.sleep(3)
        Results=result.find_element(By.XPATH,xpath3).text
        tools.assert_equal("CCN",Results,"Search function failed")
        return Results

    def Dropdown_device_type(self):
        xpath2= '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select'
        xpath3= '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select/option[3]'
        xpath4= '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]'
        result = ui_lib.Type_lib(self)
        result.find_element(By.XPATH,xpath2).click()
        time.sleep(2)
        result.find_element(By.XPATH,xpath3).click()
        Results=result.find_element(By.XPATH,xpath4).text
        time.sleep(3)
        tools.assert_in("EnergyMeter",Results,"Dropdown button not working")
        print(Results)

    def AHUG_View_Device_Type(self):
        xpath2 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select'
        xpath3 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select/option[3]'
        xpath4 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[2]/table/tbody[1]/tr/td[3]/strong/button[1]'
        xpath5 = '/html/body/div[3]/div/div[1]/div/div'
        result = ui_lib.Type_lib(self)
        result.find_element(By.XPATH, xpath2).click()
        result.find_element(By.XPATH, xpath3).click()
        time.sleep(2)
        result.find_element(By.XPATH, xpath4).click()
        time.sleep(2)
        Results = result.find_element(By.CLASS_NAME, "modal-content").text
        tools.assert_in("View Type",Results,"AHUG View device type not available")
        print(Results)

    def CCN_View_Device_Type(self):
        xpath2 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select'
        xpath3 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select/option[3]'
        xpath4 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[2]/table/tbody[2]/tr/td[3]/strong/button[1]/i'
        xpath5 = '/html/body/div[3]/div/div[1]/div/div'
        result = ui_lib.Type_lib(self)
        result.find_element(By.XPATH, xpath2).click()
        result.find_element(By.XPATH, xpath3).click()
        time.sleep(2)
        result.find_element(By.XPATH, xpath4).click()
        time.sleep(2)
        Results = result.find_element(By.CLASS_NAME, "modal-content").text
        tools.assert_in("View Type",Results,"CCN View device type not available")
        print(Results)

    def CO2_View_Device_Type(self):
        xpath2 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select'
        xpath3 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select/option[3]'
        xpath4 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[2]/table/tbody[3]/tr/td[3]/strong/button[1]/i'
        xpath5 = '/html/body/div[3]/div/div[1]/div/div'
        result = ui_lib.Type_lib(self)
        result.find_element(By.XPATH, xpath2).click()
        result.find_element(By.XPATH, xpath3).click()
        time.sleep(2)
        result.find_element(By.XPATH, xpath4).click()
        time.sleep(2)
        Results = result.find_element(By.CLASS_NAME, "modal-content").text
        tools.assert_in("View Type",Results,"C02 View device type not available")
        print(Results)

    def EMG_View_Device_Type(self):
        xpath2 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select'
        xpath3 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select/option[3]'
        xpath4 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[2]/table/tbody[4]/tr/td[3]/strong/button[1]/i'
        xpath5 = '/html/body/div[3]/div/div[1]/div/div'
        result = ui_lib.Type_lib(self)
        result.find_element(By.XPATH, xpath2).click()
        result.find_element(By.XPATH, xpath3).click()
        time.sleep(2)
        result.find_element(By.XPATH, xpath4).click()
        time.sleep(2)
        Results = result.find_element(By.CLASS_NAME, "modal-content").text
        tools.assert_in("View Type",Results,"EMG View device type not available")
        print(Results)

    def EMMW_View_Device_Type(self):
        xpath2 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select'
        xpath3 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select/option[3]'
        xpath4 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[2]/table/tbody[5]/tr/td[3]/strong/button[1]/i'
        xpath5 = '/html/body/div[3]/div/div[1]/div/div'
        result = ui_lib.Type_lib(self)
        result.find_element(By.XPATH, xpath2).click()
        result.find_element(By.XPATH, xpath3).click()
        time.sleep(2)
        result.find_element(By.XPATH, xpath4).click()
        time.sleep(2)
        Results = result.find_element(By.CLASS_NAME, "modal-content").text
        tools.assert_in("View Type",Results,"EMMW View device type not available")
        print(Results)

    def Energy_Meter_View_Device_Type(self):
        xpath2 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select'
        xpath3 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select/option[3]'
        xpath4 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[2]/table/tbody[6]/tr/td[3]/strong/button[1]/i'
        xpath5 = '/html/body/div[3]/div/div[1]/div/div'
        result = ui_lib.Type_lib(self)
        result.find_element(By.XPATH, xpath2).click()
        result.find_element(By.XPATH, xpath3).click()
        time.sleep(2)
        result.find_element(By.XPATH, xpath4).click()
        time.sleep(2)
        Results = result.find_element(By.CLASS_NAME, "modal-content").text
        tools.assert_in("View Type",Results,"Energy Meter View device type not available")
        print(Results)

    def LG_View_Device_Type(self):
        xpath2 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select'
        xpath3 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select/option[3]'
        xpath4 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[2]/table/tbody[7]/tr/td[3]/strong/button[1]/i'
        xpath5 = '/html/body/div[3]/div/div[1]/div/div'
        result = ui_lib.Type_lib(self)
        result.find_element(By.XPATH, xpath2).click()
        result.find_element(By.XPATH, xpath3).click()
        time.sleep(2)
        result.find_element(By.XPATH, xpath4).click()
        time.sleep(2)
        Results = result.find_element(By.CLASS_NAME, "modal-content").text
        tools.assert_in("View Type",Results,"LG View device type not available")
        print(Results)

    def TANDH_View_Device_Type(self):
        xpath2 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select'
        xpath3 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select/option[3]'
        xpath4 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[2]/table/tbody[9]/tr/td[3]/strong/button[1]/i'
        xpath5 = '/html/body/div[3]/div/div[1]/div/div'
        result = ui_lib.Type_lib(self)
        result.find_element(By.XPATH, xpath2).click()
        result.find_element(By.XPATH, xpath3).click()
        time.sleep(2)
        result.find_element(By.XPATH, xpath4).click()
        time.sleep(2)
        Results = result.find_element(By.CLASS_NAME, "modal-content").text
        tools.assert_in("View Type",Results,"TANDH View device type not available")
        print(Results)

    def TCN_View_Device_Type(self):
        # xpath = '/html/body/div/div/div/div/div/ul/li[2]/a'
        # xpath1 = '/html/body/div/div/div/div/div/ul/li[2]/ul/li[1]/a'
        xpath2 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select'
        xpath3 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select/option[3]'
        xpath4 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[2]/table/tbody[10]/tr/td[3]/strong/button[1]/i'
        xpath5 = '/html/body/div[3]/div/div[1]/div/div'
        result = ui_lib.Type_lib(self)
        # result = ui_lib.ems_login(self)
        # result.find_element(By.XPATH, xpath).click()
        # result.find_element(By.XPATH, xpath1).click()
        result.find_element(By.XPATH, xpath2).click()
        result.find_element(By.XPATH, xpath3).click()
        time.sleep(2)
        result.find_element(By.XPATH, xpath4).click()
        time.sleep(2)
        Results = result.find_element(By.CLASS_NAME, "modal-content").text
        tools.assert_in("View Type",Results,"TCN View device type not available")
        print(Results)

    def VCN_View_Device_Type(self):
        # xpath = '/html/body/div/div/div/div/div/ul/li[2]/a'
        # xpath1 = '/html/body/div/div/div/div/div/ul/li[2]/ul/li[1]/a'
        xpath2 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select'
        xpath3 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select/option[3]'
        xpath4 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[2]/table/tbody[11]/tr/td[3]/strong/button[1]/i'
        xpath5 = '/html/body/div[3]/div/div[1]/div/div'
        result = ui_lib.Type_lib(self)
        # result = ui_lib.ems_login(self)
        # result.find_element(By.XPATH, xpath).click()
        # result.find_element(By.XPATH, xpath1).click()
        result.find_element(By.XPATH, xpath2).click()
        result.find_element(By.XPATH, xpath3).click()
        time.sleep(2)
        result.find_element(By.XPATH, xpath4).click()
        time.sleep(2)
        Results = result.find_element(By.CLASS_NAME, "modal-content").text
        tools.assert_in("View Type",Results,"VCN View device type not available")
        print(Results)



    def device_list(self):
        # xpath = '/html/body/div/div/div/div/div/ul/li[2]/a'
        # xpath1= '/html/body/div[1]/div/div/div/div/ul/li[2]/ul/li[2]/a'
        xpath2= '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select'
        xpath3= '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select/option[3]'
        xpath4= '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[2]'
        result = ui_lib.Device_list_lib(self)
        # result = ui_lib.ems_login(self)
        # result.find_element(By.XPATH, xpath).click()
        # result.find_element(By.XPATH,xpath1).click()
        result.find_element(By.XPATH,xpath2).click()
        result.find_element(By.XPATH,xpath3).click()
        Device_list=result.find_element(By.XPATH,xpath4).text
        tools.assert_in("ccndevice",Device_list,"Device list not found")
        return Device_list


    def Create_Device_list(self):
        # xpath = '/html/body/div/div/div/div/div/ul/li[2]/a'
        # xpath1 = '/html/body/div[1]/div/div/div/div/ul/li[2]/ul/li[2]/a'
        xpath2= '/html/body/div[1]/div/div/main/div/div/div/div/div/div[1]/div/button'
        xpath3= '/html/body/div[2]/div/div[1]/div/div/div[2]/div/div/div[2]/div/form/div[1]/div[2]/input'
        xpath4= '/html/body/div[2]/div/div[1]/div/div/div[2]/div/div/div[2]/div/form/div[2]/div[2]/input'
        xpath5 = '/html/body/div[2]/div/div[1]/div/div/div[2]/div/div/div[2]/div/form/div[3]/div[2]/select'
        xpath6 = '/html/body/div[2]/div/div[1]/div/div/div[3]/button[1]'
        xpath7 = '/html/body/div[2]/div/div/div/div[1]'
        result = ui_lib.Device_list_lib(self)
        # result = ui_lib.ems_login(self)
        # result.find_element(By.XPATH, xpath).click()
        # result.find_element(By.XPATH, xpath1).click()
        result.find_element(By.XPATH, xpath2).click()
        time.sleep(3)
        result.find_element(By.XPATH, xpath3).send_keys("RevPi12")
        result.find_element(By.XPATH, xpath4).send_keys("Revolution pi")
        time.sleep(2)
        drp =Select(result.find_element(By.XPATH,xpath5))
        drp.select_by_visible_text("RevPi")
        result.find_element(By.XPATH, xpath6).click()
        time.sleep(3)
        Device_list = result.find_element(By.XPATH, xpath7).text
        print(Device_list)
        tools.assert_equal("Device created successfully", Device_list, "Device Creation failed")
        print(Device_list)

    def Search_Device_list(self):
        # xpath = '/html/body/div/div/div/div/div/ul/li[2]/a'
        # xpath1 = '/html/body/div[1]/div/div/div/div/ul/li[2]/ul/li[2]/a'
        xpath2 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select'
        xpath3 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select/option[3]'
        xpath4 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[2]/input'
        xpath5 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[2]/table'
        result = ui_lib.Device_list_lib(self)
        # result = ui_lib.ems_login(self)
        # result.find_element(By.XPATH, xpath).click()
        # result.find_element(By.XPATH, xpath1).click()
        time.sleep(2)
        result.find_element(By.XPATH, xpath2).click()
        time.sleep(3)
        result.find_element(By.XPATH, xpath3).click()
        time.sleep(2)
        result.find_element(By.XPATH,xpath4).send_keys("co2device")
        Results=result.find_element(By.XPATH,xpath5).text
        tools.assert_in("CO2",Results,"Search function failed")
        print(Results)

    def View_Device_list(self):
        # xpath = '/html/body/div/div/div/div/div/ul/li[2]/a'
        # xpath1 = '/html/body/div[1]/div/div/div/div/ul/li[2]/ul/li[2]/a'
        xpath2= '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select'
        xpath3= '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select/option[3]'
        xpath4 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[2]/input'
        #xpath4='/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[2]/table/tbody[17]/tr/td[7]/strong/button[2]/i'
        xpath5 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[2]/table/tbody/tr/td[7]/strong/button[1]/i'
        xpath6= '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[2]/table'
        result = ui_lib.Device_list_lib(self)
        # result = ui_lib.ems_login(self)
        # result.find_element(By.XPATH, xpath).click()
        # result.find_element(By.XPATH, xpath1).click()
        result.find_element(By.XPATH, xpath2).click()
        time.sleep(3)
        result.find_element(By.XPATH, xpath3).click()
        result.find_element(By.XPATH,xpath4).send_keys("RevPi12")
        time.sleep(3)
        result.find_element(By.XPATH,xpath5).click()
        time.sleep(3)
        View_Device=result.find_element(By.XPATH,xpath6).text
        tools.assert_in("CO2 Level (ppm)",View_Device,"View device list is failled")
        print(View_Device)

    def edit_device_list(self):
        # xpath = '/html/body/div/div/div/div/div/ul/li[2]/a'
        # xpath1 = '/html/body/div[1]/div/div/div/div/ul/li[2]/ul/li[2]/a'
        xpath2 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select'
        xpath3 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select/option[3]'
        xpath00= '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[2]/input'
        xpath4= '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[2]/table/tbody/tr/td[7]/strong/button[2]/i'
        xpath5= '/html/body/div[3]/div/div[1]/div/div/div[3]/button[1]'
        xpath6= '/html/body/div[2]/div/div/div/div[1]'
        result = ui_lib.Device_list_lib(self)
        # result = ui_lib.ems_login(self)
        # result.find_element(By.XPATH, xpath).click()
        # result.find_element(By.XPATH, xpath1).click()
        result.find_element(By.XPATH, xpath2).click()
        time.sleep(3)
        result.find_element(By.XPATH, xpath3).click()
        result.find_element(By.XPATH, xpath00).send_keys('RevPi12')
        time.sleep(5)
        result.find_element(By.XPATH, xpath4).click()
        time.sleep(3)
        curser = pyautogui.position()
        pyautogui.moveTo(962, 588)
        pyautogui.click()
        #result.find_element(By.XPATH, xpath5).click()
        time.sleep(2)
        Results=result.find_element(By.XPATH,xpath6).text
        print(Results)
        tools.assert_equal("Device Successfully updated",Results,"Device update failed")
        return Results

    def Delete_device_list(self):
        # xpath = '/html/body/div/div/div/div/div/ul/li[2]/a'
        # xpath1 = '/html/body/div[1]/div/div/div/div/ul/li[2]/ul/li[2]/a'
        xpath2 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select'
        xpath3 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select/option[3]'
        xpath4 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[2]/input'
        xpath5 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[2]/table/tbody/tr/td[7]/strong/button[3]'
        xpath6 = '/html/body/div[3]/div/div[1]/div/div/div[3]/button[1]'
        xpath7 = '/html/body/div[2]/div/div/div/div[1]'
        result = ui_lib.Device_list_lib(self)
        # result = ui_lib.ems_login(self)
        # result.find_element(By.XPATH,xpath).click()
        # result.find_element(By.XPATH,xpath1).click()
        time.sleep(2)
        result.find_element(By.XPATH,xpath2).click()
        time.sleep(3)
        result.find_element(By.XPATH,xpath3).click()
        time.sleep(5)
        result.find_element(By.XPATH,xpath4).send_keys("RevPi12")
        time.sleep(5)
        result.find_element(By.XPATH,xpath5).click()
        curser = pyautogui.position()
        time.sleep(3)
        pyautogui.moveTo(799, 292)
        pyautogui.click()
        #result.find_element(By.XPATH, xpath6).click()
        time.sleep(3)
        Delete_device=result.find_element(By.CLASS_NAME,'Toastify__toast-body').text
        tools.assert_equal("Device successfully deleted",Delete_device,"Device deletion failed")
        print(Delete_device)

    def page_navigation_device_list(self):
        # xpath = '/html/body/div/div/div/div/div/ul/li[2]/a'
        # xpath1 = '/html/body/div[1]/div/div/div/div/ul/li[2]/ul/li[2]/a'
        xpath2 = '//*[@id="1"]'
        xpath3 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[3]/ul/nav/nav/ul/nav[2]/ul/li/button'
        xpath4 = '//*[@id="3"]'
        xpath5 = '/html/body/div[1]/div/div/main/div/div/div'
        result = ui_lib.Device_list_lib(self)
        # result = ui_lib.ems_login(self)
        # result.find_element(By.XPATH, xpath).click()
        # result.find_element(By.XPATH, xpath1).click()
        result.find_element(By.XPATH, xpath2).click()
        time.sleep(5)
        result.find_element(By.XPATH, xpath3).click()
        time.sleep(5)
        r = result.find_element(By.XPATH, xpath4).click()
        time.sleep(3)
        print(r)
        print("page navigation is clickable")


    def device_property(self):
        # xpath = '/html/body/div/div/div/div/div/ul/li[2]/a'
        # xpath1 = '/html/body/div/div/div/div/div/ul/li[2]/ul/li[3]/a'
        xpath2 = '/html/body/div/div/div/main/div/div/div/div/div/div[1]/strong'
        result = ui_lib.device_property_lib(self)
        # result = ui_lib.ems_login(self)
        # result.find_element(By.XPATH, xpath).click()
        # result.find_element(By.XPATH,xpath1).click()
        time.sleep(2)
        Results=result.find_element(By.XPATH,xpath2).text
        time.sleep(2)
        tools.assert_equal("Device Property",Results,"Device property info not received")
        print(Results)

    def DEV002_parameter(self):
        # xpath = '/html/body/div/div/div/div/div/ul/li[2]/a'
        # xpath1 = '/html/body/div/div/div/div/div/ul/li[2]/ul/li[3]/a'
        xpath2 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select'
        xpath3 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[2]/table'
        result = ui_lib.device_property_lib(self)
        # result = ui_lib.ems_login(self)
        # result.find_element(By.XPATH, xpath).click()
        # result.find_element(By.XPATH, xpath1).click()
        time.sleep(2)
        dropdown = Select(result.find_element(By.XPATH, xpath2))
        dropdown.select_by_visible_text("DEV002")
        selected_option = dropdown.first_selected_option
        selected_option.click()
        time.sleep(8)
        im1 = pyautogui.screenshot()
        im1.save("Dev002_parameters_screenshot.png")
        time.sleep(2)
        Results = result.find_element(By.XPATH, xpath3).text
        Message = "No records found!!"
        if Results == Message:
            print("DEV002 parameters are not available ")
        else:
            print(Results)
        # tools.assert_in("Machine Status",Results,"Dev002_parameters are not available")
        # print(Results)

    def aghugdata_Mode(self):
        xpath2 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select'
        xpath0 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[1]'
        xpath3 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[2]/table'
        result = ui_lib.device_property_lib(self)
        time.sleep(2)
        dropdown = Select(result.find_element(By.XPATH, xpath2))
        dropdown.select_by_visible_text("ahugdata")
        selected_option = dropdown.first_selected_option
        selected_option.click()
        Resultsresult.find_element(By.XPATH,xpath0).text


    def ahugdata_parameter(self):
        # xpath = '/html/body/div/div/div/div/div/ul/li[2]/a'
        # xpath1 = '/html/body/div/div/div/div/div/ul/li[2]/ul/li[3]/a'
        xpath2 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select'
        xpath3 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[2]/table'
        result = ui_lib.device_property_lib(self)
        # result = ui_lib.ems_login(self)
        # result.find_element(By.XPATH, xpath).click()
        # result.find_element(By.XPATH, xpath1).click()
        time.sleep(2)
        dropdown = Select(result.find_element(By.XPATH, xpath2))
        dropdown.select_by_visible_text("ahugdata")
        selected_option = dropdown.first_selected_option
        selected_option.click()
        time.sleep(8)
        im1 = pyautogui.screenshot()
        im1.save("ahugdata_parameters_screenshot.png")
        time.sleep(2)
        Results = result.find_element(By.XPATH, xpath3).text
        Message = "No records found!!"
        if Results == Message:
            print("ahugdata parameters are not available ")
        else:
            print(Results)
        # tools.assert_in("Machine Status",Results,"Dev002_parameters are not available")
        # print(Results)

    def ccndevice_parameter(self):
        # xpath = '/html/body/div/div/div/div/div/ul/li[2]/a'
        # xpath1 = '/html/body/div/div/div/div/div/ul/li[2]/ul/li[3]/a'
        xpath2 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select'
        xpath3 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[2]/table'
        result = ui_lib.device_property_lib(self)
        # result = ui_lib.ems_login(self)
        # result.find_element(By.XPATH, xpath).click()
        # result.find_element(By.XPATH, xpath1).click()
        time.sleep(2)
        dropdown = Select(result.find_element(By.XPATH, xpath2))
        dropdown.select_by_visible_text("ccndevice")
        selected_option = dropdown.first_selected_option
        selected_option.click()
        time.sleep(8)
        im1 = pyautogui.screenshot()
        im1.save("ccndevice_parameters_screenshot.png")
        time.sleep(2)
        Results = result.find_element(By.XPATH, xpath3).text
        Message = "No records found!!"
        if Results == Message:
            print("ccndevice parameters are not available ")
        else:
            print(Results)
        # tools.assert_in("Machine Status",Results,"Dev002_parameters are not available")
        # print(Results)

    def co2device_parameter(self):
        # xpath = '/html/body/div/div/div/div/div/ul/li[2]/a'
        # xpath1 = '/html/body/div/div/div/div/div/ul/li[2]/ul/li[3]/a'
        xpath2 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select'
        xpath3 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[2]/table'
        result = ui_lib.device_property_lib(self)
        # result = ui_lib.ems_login(self)
        # result.find_element(By.XPATH, xpath).click()
        # result.find_element(By.XPATH, xpath1).click()
        time.sleep(2)
        dropdown = Select(result.find_element(By.XPATH, xpath2))
        dropdown.select_by_visible_text("co2device")
        selected_option = dropdown.first_selected_option
        selected_option.click()
        time.sleep(8)
        im1 = pyautogui.screenshot()
        im1.save("co2device_parameters_screenshot.png")
        time.sleep(2)
        Results = result.find_element(By.XPATH, xpath3).text
        Message = "No records found!!"
        if Results == Message:
            print("co2device parameters are not available ")
        else:
            print(Results)
        # tools.assert_in("Machine Status",Results,"Dev002_parameters are not available")
        # print(Results)

    def emgdemo_parameter(self):
        # xpath = '/html/body/div/div/div/div/div/ul/li[2]/a'
        # xpath1 = '/html/body/div/div/div/div/div/ul/li[2]/ul/li[3]/a'
        xpath2 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select'
        xpath3 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[2]/table'
        result = ui_lib.device_property_lib(self)
        # result = ui_lib.ems_login(self)
        # result.find_element(By.XPATH, xpath).click()
        # result.find_element(By.XPATH, xpath1).click()
        time.sleep(2)
        dropdown = Select(result.find_element(By.XPATH, xpath2))
        dropdown.select_by_visible_text("emgdemo")
        selected_option = dropdown.first_selected_option
        selected_option.click()
        time.sleep(8)
        im1 = pyautogui.screenshot()
        im1.save("emgdemo_parameters_screenshot.png")
        time.sleep(2)
        Results = result.find_element(By.XPATH, xpath3).text
        Message = "No records found!!"
        if Results == Message:
            print("emgdemo parameters are not available ")
        else:
            print(Results)
        # tools.assert_in("Machine Status",Results,"Dev002_parameters are not available")
        # print(Results)

    def emmwdemo_parameter(self):
        # xpath = '/html/body/div/div/div/div/div/ul/li[2]/a'
        # xpath1 = '/html/body/div/div/div/div/div/ul/li[2]/ul/li[3]/a'
        xpath2 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select'
        xpath3 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[2]/table'
        result = ui_lib.device_property_lib(self)
        # result = ui_lib.ems_login(self)
        # result.find_element(By.XPATH, xpath).click()
        # result.find_element(By.XPATH, xpath1).click()
        time.sleep(2)
        dropdown = Select(result.find_element(By.XPATH, xpath2))
        dropdown.select_by_visible_text("emmwdemo")
        selected_option = dropdown.first_selected_option
        selected_option.click()
        time.sleep(8)
        im1 = pyautogui.screenshot()
        im1.save("emmwdemo_parameters_screenshot.png")
        time.sleep(2)
        Results = result.find_element(By.XPATH, xpath3).text
        Message = "No records found!!"
        if Results == Message:
            print("emmwdemo parameters are not available ")
        else:
            print(Results)
        # tools.assert_in("Machine Status",Results,"Dev002_parameters are not available")
        # print(Results)

    def energymeterdevice_parameter(self):
        # xpath = '/html/body/div/div/div/div/div/ul/li[2]/a'
        # xpath1 = '/html/body/div/div/div/div/div/ul/li[2]/ul/li[3]/a'
        xpath2 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select'
        xpath3 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[2]/table'
        result = ui_lib.device_property_lib(self)
        # result = ui_lib.ems_login(self)
        # result.find_element(By.XPATH, xpath).click()
        # result.find_element(By.XPATH, xpath1).click()
        time.sleep(2)
        dropdown = Select(result.find_element(By.XPATH, xpath2))
        dropdown.select_by_visible_text("energymeterdevice")
        selected_option = dropdown.first_selected_option
        selected_option.click()
        time.sleep(8)
        im1 = pyautogui.screenshot()
        im1.save("energumeterdevice_parameters_screenshot.png")
        time.sleep(2)
        Results = result.find_element(By.XPATH, xpath3).text
        Message = "No records found!!"
        if Results == Message:
            print("energymeterdevice parameters are not available ")
        else:
            print(Results)
        # tools.assert_in("Machine Status",Results,"Dev002_parameters are not available")
        # print(Results)

    def lgdevice_parameter(self):
        # xpath = '/html/body/div/div/div/div/div/ul/li[2]/a'
        # xpath1 = '/html/body/div/div/div/div/div/ul/li[2]/ul/li[3]/a'
        xpath2 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select'
        xpath3 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[2]/table'
        result = ui_lib.device_property_lib(self)
        # result = ui_lib.ems_login(self)
        # result.find_element(By.XPATH, xpath).click()
        # result.find_element(By.XPATH, xpath1).click()
        time.sleep(2)
        dropdown = Select(result.find_element(By.XPATH, xpath2))
        dropdown.select_by_visible_text("lgdevice")
        selected_option = dropdown.first_selected_option
        selected_option.click()
        time.sleep(8)
        im1 = pyautogui.screenshot()
        im1.save("lgdevice_parameters_screenshot.png")
        time.sleep(2)
        Results = result.find_element(By.XPATH, xpath3).text
        Message = "No records found!!"
        if Results == Message:
            print("lgdevice parameters are not available ")
        else:
            print(Results)
        # tools.assert_in("Machine Status",Results,"Dev002_parameters are not available")
        # print(Results)

    def tandhdevice_parameter(self):
        # xpath = '/html/body/div/div/div/div/div/ul/li[2]/a'
        # xpath1 = '/html/body/div/div/div/div/div/ul/li[2]/ul/li[3]/a'
        xpath2 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select'
        xpath3 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[2]/table'
        result = ui_lib.device_property_lib(self)
        # result = ui_lib.ems_login(self)
        # result.find_element(By.XPATH, xpath).click()
        # result.find_element(By.XPATH, xpath1).click()
        time.sleep(2)
        dropdown = Select(result.find_element(By.XPATH, xpath2))
        dropdown.select_by_visible_text("tandhdevice")
        selected_option = dropdown.first_selected_option
        selected_option.click()
        time.sleep(8)
        im1 = pyautogui.screenshot()
        im1.save("tandhdevice_parameters_screenshot.png")
        time.sleep(2)
        Results = result.find_element(By.XPATH, xpath3).text
        Message = "No records found!!"
        if Results == Message:
            print("tandhdevice parameters are not available ")
        else:
            print(Results)
        # tools.assert_in("Machine Status",Results,"Dev002_parameters are not available")
        # print(Results)

    def tcndevice_parameter(self):
        # xpath = '/html/body/div/div/div/div/div/ul/li[2]/a'
        # xpath1 = '/html/body/div/div/div/div/div/ul/li[2]/ul/li[3]/a'
        xpath2 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select'
        xpath3 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[2]/table'
        result = ui_lib.device_property_lib(self)
        # result = ui_lib.ems_login(self)
        # result.find_element(By.XPATH, xpath).click()
        # result.find_element(By.XPATH, xpath1).click()
        time.sleep(2)
        dropdown = Select(result.find_element(By.XPATH, xpath2))
        dropdown.select_by_visible_text("tcndevice")
        selected_option = dropdown.first_selected_option
        selected_option.click()
        time.sleep(8)
        im1 = pyautogui.screenshot()
        im1.save("tcndevice_parameters_screenshot.png")
        time.sleep(2)
        Results = result.find_element(By.XPATH, xpath3).text
        Message = "No records found!!"
        if Results == Message:
            print("tcndevice parameters are not available ")
        else:
            print(Results)
        # tools.assert_in("Machine Status",Results,"Dev002_parameters are not available")
        # print(Results)

    def vcndevice_parameter(self):
        # xpath = '/html/body/div/div/div/div/div/ul/li[2]/a'
        # xpath1 = '/html/body/div/div/div/div/div/ul/li[2]/ul/li[3]/a'
        xpath2 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select'
        xpath3 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[2]/table'
        result = ui_lib.device_property_lib(self)
        # result = ui_lib.ems_login(self)
        # result.find_element(By.XPATH, xpath).click()
        # result.find_element(By.XPATH, xpath1).click()
        time.sleep(2)
        dropdown = Select(result.find_element(By.XPATH, xpath2))
        dropdown.select_by_visible_text("vcndevice")
        selected_option = dropdown.first_selected_option
        selected_option.click()
        time.sleep(8)
        im1 = pyautogui.screenshot()
        im1.save("vcndevice_parameters_screenshot.png")
        time.sleep(2)
        Results = result.find_element(By.XPATH, xpath3).text
        Message = "No records found!!"
        if Results == Message:
            print("vcndevice parameters are not available ")
        else:
            print(Results)
        # tools.assert_in("Machine Status",Results,"Dev002_parameters are not available")
        # print(Results)

    def select_device_property_dropdown(self):
        # xpath = '/html/body/div/div/div/div/div/ul/li[2]/a'
        # xpath1 = '/html/body/div/div/div/div/div/ul/li[2]/ul/li[3]/a'
        xpath2='/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select'
        xpath3='/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select/option[5]'
        xpath4='/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[2]/b[1]'
        result = ui_lib.device_property_lib(self)
        # result = ui_lib.ems_login(self)
        # result.find_element(By.XPATH, xpath).click()
        # result.find_element(By.XPATH, xpath1).click()
        result.find_element(By.XPATH,xpath2).click()
        time.sleep(2)
        result.find_element(By.XPATH,xpath3).click()
        time.sleep(2)
        Results=result.find_element(By.XPATH,xpath4).text
        tools.assert_equal("CO2demo",Results,"Selected device property info wrong")
        return Results

    def Refresh_device_property(self):
        # xpath = '/html/body/div/div/div/div/div/ul/li[2]/a'
        # xpath1 = '/html/body/div/div/div/div/div/ul/li[2]/ul/li[3]/a'
        xpath2 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select'
        xpath3 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select/option[5]'
        xpath4 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[3]/button/i'
        xpath5 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[2]/b[2]'
        result = ui_lib.device_property_lib(self)
        # result = ui_lib.ems_login(self)
        # result.find_element(By.XPATH, xpath).click()
        # result.find_element(By.XPATH, xpath1).click()
        result.find_element(By.XPATH, xpath2).click()
        time.sleep(2)
        result.find_element(By.XPATH, xpath3).click()
        time.sleep(2)
        result.find_element(By.XPATH, xpath4).click()
        time.sleep(5)
        Results = result.find_element(By.XPATH, xpath5).text
        date = Results.split("T")
        print(date)
        tools.assert_in(str(datetime.now()), date[0], "Test case failed not updated datetime")
        return Results

    def Update_device_property(self):
        # xpath = '/html/body/div/div/div/div/div/ul/li[2]/a'
        # xpath1 = '/html/body/div/div/div/div/div/ul/li[2]/ul/li[3]/a'
        xpath2 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select'
        xpath3 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[1]/select/option[3]'
        xpath4='/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[4]/td[4]/input'
        xpath5='//*[@id="root"]/div/div/main/div/div/div/div/div/div[2]/div[1]/div/div[4]/button'
        xpath6='/html/body/div[2]/div/div/div/div[1]'
        result = ui_lib.device_property_lib(self)
        # result = ui_lib.ems_login(self)
        # result.find_element(By.XPATH,xpath).click()
        # result.find_element(By.XPATH,xpath1).click()
        result.find_element(By.XPATH,xpath2).click()
        time.sleep(2)
        result.find_element(By.XPATH,xpath3).click()
        time.sleep(2)
        result.find_element(By.XPATH, xpath4).clear()
        time.sleep(3)
        result.find_element(By.XPATH, xpath4).send_keys("39.9")
        im1 = pyautogui.screenshot()
        im1.save("Update_device_property_screenshot.png")
        time.sleep(2)
        result.find_element(By.XPATH,xpath5).click()
        time.sleep(5)
        Results=result.find_element(By.XPATH,xpath6).text
        time.sleep(3)
        tools.assert_equal("Update parameter command sent to device.",Results,"Device properties not updated")
        print(Results)

    def Device_History(self):
        xpath = '/html/body/div/div/div/div/div/ul/li[2]/a'
        xpath1 = '/html/body/div[1]/div/div/div/div/ul/li[2]/ul/li[4]/a'
        xpath2 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div/div[1]/div[1]/select'
        xpath3 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div/div[1]/div[1]/select/option[3]'
        xpath4 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div/div[1]/div[2]/select'
        xpath5 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div/div[1]/div[2]/select/option[5]'
        xpath6 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div/div[1]/div[3]/input'
        xpath7 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div/div[1]/div[4]/input'
        xpath8 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div/div[1]/div[5]/button'
        xpath9 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div/div[2]/div/div/canvas'
        result = ui_lib.ems_login(self)
        result.find_element(By.XPATH, xpath).click()
        result.find_element(By.XPATH,xpath1).click()
        result.find_element(By.XPATH,xpath2).click()
        result.find_element(By.XPATH,xpath3).click()
        time.sleep(2)
        result.find_elements(By.XPATH,xpath4).clear()
        result.find_element(By.XPATH,xpath5).click()
        result.find_element(By.XPATH,xpath6).send_keys("02-08-2023")
        time.sleep(3)
        result.find_element(By.XPATH,xpath7).send_keys("05-09-2023")
        time.sleep(2)
        result.find_element(By.XPATH,xpath8).click()
        time.sleep(10)
        im1 = pyautogui.screenshot()
        im1.save("History_screenshot.png")
        data=result.find_element(By.XPATH,xpath9).text
        print(data)

    def View_live_data(self):
        xpath = '/html/body/div/div/div/div/div/ul/li[2]/a'
        xpath1 = '/html/body/div[1]/div/div/div/div/ul/li[2]/ul/li[5]/a'
        xpath2 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[1]/strong'
        xpath3 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div/div[1]/div/ul[1]/li/ul/li[2]/input'
        xpath4 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div/div[1]/div/ul[2]/li/ul/li[4]/input'
        xpath5 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div/div[1]/div/ul[2]/li/ul/li[6]/input'
        xpath6 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div/div[2]/div[1]'
        result = ui_lib.ems_login(self)
        result.find_element(By.XPATH, xpath).click()
        result.find_element(By.XPATH,xpath1).click()
        result.find_element(By.XPATH,xpath2).click()
        result.find_element(By.XPATH,xpath3).click()
        time.sleep(5)
        result.find_element(By.XPATH,xpath4).click()
        result.find_element(By.XPATH,xpath5).click()
        im1 = pyautogui.screenshot()
        im1.save("View_live_data_screenshot.png")
        time.sleep(2)
        data=result.find_element(By.XPATH,xpath6).text
        print(data)
        tools.assert_in("Air Speed (m/h",data,"Air Speed (m/h not found")
        tools.assert_in("Relay Status",data,"Relay Status not found")


    def Multi_live_data(self):
        xpath = '/html/body/div/div/div/div/div/ul/li[2]/a'
        xpath1 = '/html/body/div[1]/div/div/div/div/ul/li[2]/ul/li[6]/a'
        xpath2 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div[1]/select'
        xpath3 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div[1]/select/option[3]'
        xpath4 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[1]/div[2]/div/div/div'
        xpath5 = '//*[@id="root"]/div/div/main/div/div/div/div/div/div[2]/div[1]/div[2]/div/div/div/div'
        xpath6 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div[2]/div/div/div/div/span'
        xpath7 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[1]/div[3]/div/button'
        xpath8 = '/html/body/div/div/div/main/div/div/div/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/div/ul/li[4]/label'
        result = ui_lib.ems_login(self)
        result.find_element(By.XPATH, xpath).click()
        result.find_element(By.XPATH,xpath1).click()
        time.sleep(3)
        result.find_element(By.XPATH,xpath2).click()
        time.sleep(3)
        result.find_element(By.XPATH,xpath3).click()
        time.sleep(3)
        result.find_element(By.XPATH,xpath4).click()
        time.sleep(5)
        result.find_element(By.XPATH,xpath8).click()
        result.find_element(By.XPATH,xpath7).click()
        time.sleep(3)
        im1 = pyautogui.screenshot()
        im1.save("multi_live_data_screenshot.png")
        time.sleep(2)



    def Compare_multi_data(self):
        xpath = '/html/body/div/div/div/div/div/ul/li[2]/a'
        xpath1 = '/html/body/div[1]/div/div/div/div/ul/li[2]/ul/li[7]/a'
        xpath2 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[1]/div[1]/select'
        xpath3 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[1]/div[1]/select/option[3]'
        xpath4 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[1]/div[2]/select'
        xpath5 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[1]/div[2]/select/option[5]'
        xpath6 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[3]/div[2]/button[1]'
        xpath7 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[4]/div/div[1]/div/canvas'
        result = ui_lib.ems_login(self)
        result.find_element(By.XPATH, xpath).click()
        result.find_element(By.XPATH,xpath1).click()
        result.find_element(By.XPATH,xpath2).click()
        result.find_element(By.XPATH,xpath3).click()
        time.sleep(3)
        result.find_element(By.XPATH,xpath4).click()
        result.find_element(By.XPATH,xpath5).click()
        result.find_element(By.XPATH,xpath6).click()
        time.sleep(3)
        im1 = pyautogui.screenshot()
        im1.save("Compare_multi_data_screenshot.png")
        time.sleep(2)
        data = result.find_element(By.XPATH, xpath7)
        return "Graph Generated"
        #tools.assert_in("Air Speed (m/h", data, "Air Speed (m/h not found")

    def Compare_live_data(self):
        xpath = '/html/body/div/div/div/div/div/ul/li[2]/a'
        xpath1 = '/html/body/div[1]/div/div/div/div/ul/li[2]/ul/li[8]/a'
        xpath2 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div/div[1]/div/ul[1]/li/ul/li[2]/input'
        xpath3 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div/div[1]/div/ul[1]/li/ul/li[3]/input'
        xpath4 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[1]/div[2]/div/div/div'
        xpath5 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div/div[2]/canvas'
        result = ui_lib.ems_login(self)
        result.find_element(By.XPATH, xpath).click()
        result.find_element(By.XPATH, xpath1).click()
        result.find_element(By.XPATH, xpath2).click()
        result.find_element(By.XPATH, xpath3).click()
        result.find_element(By.XPATH, xpath4).click()
        time.sleep(3)
        result.find_element(By.XPATH,xpath4).send_keys("Air Speed")
        compare=result.find_element(By.XPATH,xpath5).text
        im1 = pyautogui.screenshot()
        im1.save("Compare_live_data_screenshot.png")
        return "Greph Generated"
        #tools.assert_equal("MYLORA103 ",compare,"Not found")

    def create_model(self):
        xpath = '/html/body/div[1]/div/div/div/div/ul/li[3]/a'
        xpath1 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[1]/div/button'
        xpath2 = '/html/body/div[2]/div/div[1]/div/div/div[2]/div/div/div[2]/div/form/div[1]/div[1]/select'
        #xpath3 = '/html/body/div[2]/div/div[1]/div/div/div[2]/div/div/div[2]/div/form/div[1]/div[1]/select/option[9]'
        xpath4 = '/html/body/div[2]/div/div[1]/div/div/div[2]/div/div/div[2]/div/form/div[1]/div[2]/input'
        xpath5 = '/html/body/div[2]/div/div[1]/div/div/div[3]/button[1]'
        xpath6 = '/html/body/div[2]/div/div/div/div[1]'
        result=ui_lib.ems_login(self)
        result.find_element(By.XPATH,xpath).click()
        result.find_element(By.XPATH, xpath1).click()
        #result.find_element(By.XPATH, xpath2).click()
        dropdown = Select(result.find_element(By.XPATH,xpath2))
        dropdown.select_by_value("RevPi")
        selected_option = dropdown.first_selected_option
        selected_option.click()
        time.sleep(3)
        result.find_element(By.XPATH, xpath4).clear()
        result.find_element(By.XPATH, xpath4).send_keys("RevPiModel")
        time.sleep(2)
        result.find_element(By.XPATH, xpath5).click()
        time.sleep(2)
        data=result.find_element(By.XPATH, xpath6).text
        tools.assert_in('Model info created successfully',data,"model failed to create")
        return data

    def get_model_info(self):
        xpath = '/html/body/div[1]/div/div/div/div/ul/li[3]/a'
        xpath1 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[1]/div[2]/div[1]/select'
        xpath2 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[1]/div[2]/div[1]/select/option[2]'
        xpath3 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[1]/div[2]/div[2]/select'
        xpath4 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[1]/div[2]/div[2]/select/option[2]'
        xpath5 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[1]/div[2]/div[3]/button'
        xpath6 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[2]/table'
        result = ui_lib.ems_login(self)
        result.find_element(By.XPATH, xpath).click()
        result.find_element(By.XPATH, xpath1).click()
        result.find_element(By.XPATH, xpath2).click()
        result.find_element(By.XPATH, xpath3).click()
        time.sleep(3)
        result.find_element(By.XPATH, xpath4).click()
        result.find_element(By.XPATH, xpath5).click()
        time.sleep(3)
        model = result.find_element(By.XPATH, xpath6).text
        tools.assert_in("NumberofProperties", model, "model information not found")
        return model

    def update_model_info(self):
        xpath = '/html/body/div[1]/div/div/div/div/ul/li[3]/a'
        xpath1 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[1]/div[2]/div[1]/select'
        xpath2 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[1]/div[2]/div[1]/select/option[2]'
        xpath3 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[1]/div[2]/div[2]/select'
        xpath4 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[1]/div[2]/div[2]/select/option[2]'
        xpath5 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[1]/div[2]/div[3]/button'
        xpath6 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[1]/div[2]/div[4]/button'
        xpath7 = '/html/body/div[3]/div/div[1]/div/div/div[3]/button[1]'
        xpath8 = '/html/body/div[2]/div/div/div/div[1]'
        result = ui_lib.ems_login(self)
        result.find_element(By.XPATH, xpath).click()
        result.find_element(By.XPATH, xpath1).click()
        result.find_element(By.XPATH, xpath2).click()
        result.find_element(By.XPATH, xpath3).click()
        time.sleep(3)
        result.find_element(By.XPATH, xpath4).click()
        result.find_element(By.XPATH, xpath5).click()
        time.sleep(3)
        result.find_element(By.XPATH, xpath6).click()
        pyautogui.moveTo(1167,327)
        time.sleep(2)
        pyautogui.scroll(-100)
        time.sleep(2)
        pyautogui.click(951,673)
        time.sleep(3)
        #result.find_element(By.XPATH, xpath7).click()
        model=result.find_element(By.XPATH, xpath8).text
        tools.assert_in("Model info updated successfully", model, "model information update failed")
        return model

    def delete_model(self):
        xpath = '/html/body/div[1]/div/div/div/div/ul/li[3]/a'
        xpath1 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[1]/div/button'
        xpath2 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[1]/div[2]/div[1]/select'
        xpath3 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[1]/div[2]/div[2]/select'
        xpath4 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[1]/div[2]/div[3]/button'
        xpath5 = '/html/body/div[1]/div/div/main/div/div/div/div/div/div[2]/div[1]/div[2]/div[5]/button'
        xpath6 = '/html/body/div[3]/div/div[1]/div/div/div[3]/button[1]'
        xpath7 = '/html/body/div[2]/div/div/div'
        result = ui_lib.ems_login(self)
        result.find_element(By.XPATH, xpath).click()
        #result.find_element(By.XPATH, xpath1).click()
        #result.find_element(By.XPATH, xpath2).click()
        dropdown = Select(result.find_element(By.XPATH, xpath2))
        dropdown.select_by_value("RevPi")
        selected_option = dropdown.first_selected_option
        selected_option.click()
        time.sleep(2)
        dropdown1 = Select(result.find_element(By.XPATH, xpath3))
        dropdown1.select_by_value("RevPiModel")
        selected_option = dropdown1.first_selected_option
        selected_option.click()
        result.find_element(By.XPATH, xpath4).click()
        time.sleep(3)
        result.find_element(By.XPATH, xpath5).click()
        time.sleep(6)
        pyautogui.click(817, 294,duration=1)
        time.sleep(3)
        #result.find_element(By.XPATH, xpath6).click()
        data=result.find_element(By.XPATH, xpath7).text
        print(data)
        tools.assert_in("Model info deleted successfully",data,"delete model test case failed")



if __name__ == "__main__":
    obj =test_case_class()
    obj.login()