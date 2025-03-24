from appium.options.ios import XCUITestOptions
from appium.options.common.base import AppiumOptions

def get_ios_capabilities():
    options = AppiumOptions()
    options.load_capabilities({
            "platformName": "iOS",
            "appium:platformVersion": "18.3",
            "appium:deviceName": "iPhone 16 Pro",
            "appium:automationName": "XCUITest",
            "appium:app": "/Users/apple/Downloads/SimpleTodoApp/SimpleTodoApp.app",
            "appium:noReset": "true",
            "appium:includeSafariInWebviews": True,
            "appium:newCommandTimeout": 3600,
            "appium:connectHardwareKeyboard": True
        })
    return options
