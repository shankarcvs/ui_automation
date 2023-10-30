*** Settings ***
Library    ems_ui_test_cases.test_case_class    WITH NAME   test_exct

*** Variables ***

*** Test Cases ***

TC_login
    [Documentation]  test the login to ems application
    ${TEST}  test_exct.login

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

TC_neg_tve_test_login_diff_user
    [Documentation]  test negative scenorio on login page different username
    ${TEST}  test_exct.neg_tve_test_login_diff_user

TC_neg_tve_test_login_diff_pswrd
    [Documentation]  test negative scenorio on login page different password
    ${TEST}  test_exct.neg_tve_test_login_diff_pswrd

TC_neg_tve_test_login_diff_both
    [Documentation]  test negative scenorio on login page different username and password
    ${TEST}  test_exct.neg_tve_test_login_diff_both

TC_Log_out
    [Documentation]  test log_out is working properly
    ${TEST}  test_exct.Log_out

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

*** comments ***


