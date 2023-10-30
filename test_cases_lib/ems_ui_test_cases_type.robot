*** Settings ***
Library    ems_ui_test_cases.test_case_class    WITH NAME   test_exct

*** Variables ***

*** Test Cases ***
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

TC_View_Device_list
    [Documentation]  To see the selected device properties
    ${TEST}  test_exct.View_Device_list

TC_edit_device_list
    [Documentation]  To edit the device name or device type
    ${TEST}  test_exct.edit_device_list

TC_Delete_device_list
    [Documentation]  To delete the selected device
    ${TEST}  test_exct.Delete_device_list

TC_Search_Device_list
    [Documentation]  To search the device name
    ${TEST}  test_exct.Search_Device_list

TC_device_property
    [Documentation]  Type of device list is showing
    ${TEST}  test_exct.device_property

TC_MyLoRA_101_parameter
    [Documentation]  Its showing MyLoRA_101_parameter list
    ${TEST}  test_exct.MyLoRA_101_parameter

TC_MyLoRA_102_parameter
    [Documentation]  Its showing MyLoRA_102_parameter list
    ${TEST}  test_exct.MyLoRA_102_parameter

TC_MyLoRA_103_parameter
    [Documentation]  Its showing MyLoRA_103_parameter list
    ${TEST}  test_exct.MyLoRA_103_parameter

TC_AHUG_Test_July_2023_parameter
    [Documentation]  Its showing AHUG_Test_July_2023_parameter list
    ${TEST}  test_exct.AHUG_Test_July_2023_parameter

TC_AHU_parameter
    [Documentation]  Its showing AHU_parameter list
    ${TEST}  test_exct.AHU_parameter

TC_DEV002_parameter
    [Documentation]  Its showing DEV002_parameter list
    ${TEST}  test_exct.DEV002_parameter

TC_MyCCN_parameter
    [Documentation]  Its showing MyCCN_parameter list
    ${TEST}  test_exct.MyCCN_parameter

TC_CO2_Simulater_parameter
    [Documentation]  Its showing CO2_Simulater_parameter list
    ${TEST}  test_exct.CO2_Simulater_parameter

TC_Smart_Meter_parameter
    [Documentation]  Its showing Smart_Meter_parameter list
    ${TEST}  test_exct.Smart_Meter_parameter

TC_Temperature_Device_parametery
    [Documentation]  Its showing Temperature_Device_parameters list
    ${TEST}  test_exct.Temperature_Device_parameter

TC_MyCCNL_parameter
    [Documentation]  Its showing MyCCNL_parameter list
    ${TEST}  test_exct.MyCCNL_parameter

TC_MyTCN_parameter
    [Documentation]  Its showing MyTCN_parameter list
    ${TEST}  test_exct.MyTCN_parameter

TC_EMMW_Gateway_parameter
    [Documentation]  Its showing EMMW_Gateway_parameter list
    ${TEST}  test_exct.EMMW_Gateway_parameter

TC_EMMW_Gateway_1_parameter
    [Documentation]  Its showing EMMW_Gateway_1_parameter list
    ${TEST}  test_exct.EMMW_Gateway_1_parameter

TC_EMG_parameter
    [Documentation]  Its showing EMG_parameter list
    ${TEST}  test_exct.EMG_parameter

TC_MyVCN_parameter
    [Documentation]  Its showing MyVCN_parameters list
    ${TEST}  test_exct.MyVCN_parameter

TC_AHU_17_Device
    [Documentation]  Its showing AHU_17_Device parameters list
    ${TEST}  test_exct.AHU_17_Device

TC_DEV_NAME_as
    [Documentation]  Its showing DEV_NAME_as parameters list
    ${TEST}  test_exct.DEV_NAME_as

TC_chiller
    [Documentation]  Its showing chiller parameters list
    ${TEST}  test_exct.chiller

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

*** Comments ***
