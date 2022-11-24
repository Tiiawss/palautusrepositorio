*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go to Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Go to Register Page
    Set Username  k
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  Username should be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Password  1
    Set Password Confirmation  1
    Submit Credentials
    Register Should Fail With Message  Password should be at least 8 characters long

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  ellak123
    Submit Credentials
    Register Should Fail With Message  Passwords not matching

Login After Successful Registration
    Register With Credentials  kalle  kalle123  kalle123
    Register Should Succeed
    Go To Login Page
    Login Page Should Be Open
    Login With Credentials  kalle  kalle123
    Login Should Succeed

Login After Failed Registration
    Register With Credentials  kalle  k123  k123
    Register Should Fail With Message  Password must be at least 8 characters long and contain more than letters
    Go To Login Page
    Login Page Should Be Open
    Login With Credentials  kalle  k123
    Login Should Fail With Message  Invalid username or password

*** Keywords ***

Register With Credentials
    [Arguments]  ${username}  ${password}  ${password confirmation}
    Set Username  ${username}
    Set Password  ${password}
    Set Password Confirmation  ${password confirmation}
    Submit Credentials

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}