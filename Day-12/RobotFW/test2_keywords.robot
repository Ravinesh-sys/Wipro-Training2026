*** Settings ***
Library              SeleniumLibrary

*** Keywords ***
open application
    Open Browser         https://www.facebook.com/  edge
    Maximize Browser Window


*** Test Cases ***
test2.robot
    open application
    Close Browser
