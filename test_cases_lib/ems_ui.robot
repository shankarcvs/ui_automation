*** Settings ***
Library    ems_ui_test_cases.test_case_class    WITH NAME   test_exct

*** Variables ***

*** Test Cases ***

TC_login
    [Documentation]  test the login to ems application
    ${TEST}  test_exct.login

TC_neg_tve_test_login_diff_user
    [Documentation]  test negative scenorio on login page different username
    ${TEST}  test_exct.neg_tve_test_login_diff_user

TC_neg_tve_test_login_diff_pswrd
    [Documentation]  test negative scenorio on login page different password
    ${TEST}  test_exct.neg_tve_test_login_diff_pswrd

TC_neg_tve_test_login_diff_both
    [Documentation]  test negative scenorio on login page different username and password
    ${TEST}  test_exct.neg_tve_test_login_diff_both

TC_neg_tve_test_login_empty_user
    [Documentation]  test negative scenorio on login page empty username
    ${TEST}  test_exct.neg_tve_test_login_diff_both

TC_neg_tve_test_login_empty_pswrd
    [Documentation]  test negative scenorio on login page empty password
    ${TEST}  test_exct.neg_tve_test_login_diff_both

TC_neg_tve_test_login_empty_both
    [Documentation]  test negative scenorio on login page empty username and password
    ${TEST}  test_exct.neg_tve_test_login_diff_both

TC_Log_out
    [Documentation]  test log_out is working properly
    ${TEST}  test_exct.Log_out

TC_total_sensors
    [Documentation]  display the total sensors count
    ${TEST}  test_exct.total_sensors

TC_active_sensors
    [Documentation]  display the active sensor count
    ${TEST}  test_exct.active_sensors

TC_in_active_sensors
    [Documentation]  display the in_active_sensors sensor count
    ${TEST}  test_exct.in_active_sensors

TC_alarms_list
    [Documentation]  display the alarm list
    ${TEST}  test_exct.alarms_list

TC_network_id
    [Documentation]  display the network id
    ${TEST}  test_exct.network_id

TC_check_profile
    [Documentation]  display the profile details
    ${TEST}  test_exct.check_profile

TC_Type_list
    [Documentation]  Type of device list is showing
    ${TEST}  test_exct.Type_list

TC_create_device_Type
    [Documentation]  it will create device type
    ${TEST}  test_exct.create_device_Type

TC_View_Device_Type
    [Documentation]  It will give the meta data of the selected type of device.
    ${TEST}  test_exct.View_Device_Type

TC_Edit_Device_type
    [Documentation]  Edit the device type meta data and device type info
    ${TEST}  test_exct.Edit_Device_type

TC_Delete_Device_type
    [Documentation]  To delete the device type
    ${TEST}  test_exct.Delete_Device_type

TC_AHUG_View_Device_Type
    [Documentation]  It will give the meta data of the AHUG type of device.
    ${TEST}  test_exct.AHUG_View_Device_Type

TC_CCN_View_Device_Type
    [Documentation]  It will give the meta data of the CCN type of device.
    ${TEST}  test_exct.CCN_View_Device_Type

TC_CO2_View_Device_Type
    [Documentation]  It will give the meta data of the CO2 type of device.
    ${TEST}  test_exct.CO2_View_Device_Type

TC_EMG_View_Device_Type
    [Documentation]  It will give the meta data of the EMG type of device.
    ${TEST}  test_exct.EMG_View_Device_Type

TC_EMMW_View_Device_Type
    [Documentation]  It will give the meta data of the EMMW type of device.
    ${TEST}  test_exct.EMMW_View_Device_Type

TC_Energy_Meter_View_Device_Type
    [Documentation]  It will give the meta data of the Energy Meter type of device.
    ${TEST}  test_exct.Energy_Meter_View_Device_Type

TC_LG_View_Device_Type
    [Documentation]  It will give the meta data of the LG type of device.
    ${TEST}  test_exct.LG_View_Device_Type

TC_TANDH_View_Device_Type
    [Documentation]  It will give the meta data of the TANDH type of device.
    ${TEST}  test_exct.TANDH_View_Device_Type

TC_TCN_View_Device_Type
    [Documentation]  It will give the meta data of the TCN type of device.
    ${TEST}  test_exct.TCN_View_Device_Type

TC_VCN_View_Device_Type
    [Documentation]  It will give the meta data of the VCN type of device.
    ${TEST}  test_exct.VCN_View_Device_Type

TC_search_device_type
    [Documentation]  It will gives the selected device type
    ${TEST}  test_exct.search_device_type

TC_Dropdown_deviec_type
    [Documentation]  Display the all type of devices list.
    ${TEST}  test_exct.Dropdown_device_type

TC_device_list
    [Documentation]  Show the list of all devices.
    ${TEST}  test_exct.device_list

TC_Create_Device_list
    [Documentation]  To create the new device
    ${TEST}  test_exct.Create_Device_list

TC_Search_Device_list
    [Documentation]  To search the device name
    ${TEST}  test_exct.Search_Device_list


TC_View_Device_list
    [Documentation]  To see the selected device properties
    ${TEST}  test_exct.View_Device_list

TC_edit_device_list
    [Documentation]  To edit the device name or device type
    ${TEST}  test_exct.edit_device_list

TC_Delete_device_list
    [Documentation]  To delete the selected device
    ${TEST}  test_exct.Delete_device_list

TC_page_navigation_device_list
    [Documentation]  It will goto first page,second page,third page
    ${TEST}  test_exct.page_navigation_device_list

TC_device_property
    [Documentation]  Type of device list is showing
    ${TEST}  test_exct.device_property

TC_DEV002_parameter
    [Documentation]  Its showing DEV002_parameter list
    ${TEST}  test_exct.DEV002_parameter

TC_ahugdata_parameter
    [Documentation]  Its showing ahugdata_parameter list
    ${TEST}  test_exct.ahugdata_parameter

TC_ccndevice_parameter
    [Documentation]  Its showing ccndevice_parameter list
    ${TEST}  test_exct.ccndevice_parameter

TC_co2device_parameter
    [Documentation]  Its showing co2device_parameter list
    ${TEST}  test_exct.co2device_parameter

TC_emgdemo_parameter
    [Documentation]  Its showing emgdemo_parameter list
    ${TEST}  test_exct.emgdemo_parameter

TC_emmwdemo_parameter
    [Documentation]  Its showing emmwdemo_parameter list
    ${TEST}  test_exct.emmwdemo_parameter

TC_energymeterdevice_parameter
    [Documentation]  Its showing energymeterdevice_parameter list
    ${TEST}  test_exct.energymeterdevice_parameter

TC_lgdevice_parameter
    [Documentation]  Its showing lgdevice_parameter list
    ${TEST}  test_exct.lgdevice_parameter

TC_tandhdevice_parameter
    [Documentation]  Its showing tandhdevice_parameter list
    ${TEST}  test_exct.tandhdevice_parameter

TC_tcndevice_parameter
    [Documentation]  Its showing tcndevice_parameter list
    ${TEST}  test_exct.tcndevice_parameter

TC_vcndevice_parameter
    [Documentation]  Its showing vcndevice_parameter list
    ${TEST}  test_exct.vcndevice_parameter

TC_select_device_property_dropdown
    [Documentation]  Type of device list is showing
    ${TEST}  test_exct.select_device_property_dropdown

TC_Refresh_device_property
    [Documentation]   It will give the present time data based on the selected device.
    ${TEST}  test_exct.Refresh_device_property

TC_Update_device_property
    [Documentation]   It will update the desired value based on the selected device.
    ${TEST}  test_exct.Update_device_property

TC_Device_History
    [Documentation]   It will give previous data based on the selected device property.
    ${TEST}  test_exct.Device_History

TC_View_live_data
    [Documentation]   It will gives the selected device properties live data
    ${TEST}  test_exct.View_live_data

TC_Multi_live_data
    [Documentation]   It will give the multiple devices property values.
    ${TEST}  test_exct.Multi_live_data

TC_Compare_multi_data
    [Documentation]  Comparing the properties based on the selected device
    ${TEST}  test_exct.Compare_multi_data

TC_Compare_live_data
    [Documentation]  Selected devices common properties are displayed.
    ${TEST}  test_exct.Compare_live_data

TC_create_model
    [Documentation]  test creating model
    ${TEST}  test_exct.create_model

TC_get_model_info
    [Documentation]  test get model information
    ${TEST}  test_exct.get_model_info

TC_update_model_info
    [Documentation]  test update model information
    ${TEST}  test_exct.update_model_info

TC_delete_model_info
    [Documentation]  test delete model
    ${TEST}  test_exct.delete_model