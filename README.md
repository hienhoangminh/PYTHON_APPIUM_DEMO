# PYTHON_APPIUM_DEMO
How To
==============
## Dependencies
* Tested on Python 3.7, Appium python client 0.40.0
* pip install -r requirements.txt

## Run Syntax
* To run: right-click on Run Unittest for BeTest...
* For command line :
  * cd BeTestAppDemo
  * python3 -m unittest testcases/BeTestCases.py

## How to configure run environment
* Setup system env for PYTHON,APPIUM_URL, PLATFORM_VERSION
    * APPIUM_URL specifies the appium URL, by default, 'http://localhost:4723/wd/hub'
    * Python is installed and added to PATH variable
    

## Project Directories:
* drivers: it defines the way driver is instantiated and killed.
* locators: it defines all the locators.
* pageobjects: it defines all the screen in the application.
* testcases: it defines the test cases.

PLEASE NOTE : 
 - This is my sample project. It will be perfectionned and updated frequently.
 - I still can not handle the phase of get OTP, so test cases starts when user logged in successfully.

