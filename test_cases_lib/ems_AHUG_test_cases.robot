*** Settings ***
Library    ems_AHUG_test_cases.AHUG_class    WITH NAME   test_exct

*** Variables ***

*** Test Cases ***
TC_change_mode_to_manaul_AHUG
    [Documentation]  change_mode_to_manaul_AHUG passed
    ${TEST}  test_exct.change_mode_to_manaul_AHUG