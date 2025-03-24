import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TodoPage:
    def __init__(self, driver):
        self.driver = driver

    def add_task(self, task_name):
        element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Add a new task")
        element.click()
        try:
            self.driver.find_element("xpath", "//XCUIElementTypeButton[@name='Return']").click()
            safe_send_keys(self, element, task_name)
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Add Task").click()
        except Exception as e:
            print(e)



    def get_tasks(self):
        return self.driver.find_elements("xpath", "//*[contains(@name, 'Delete')]")


    def mark_task_completed(self, task_name):
        time.sleep(5)
        self.driver.find_element("xpath", "//XCUIElementTypeButton[@name='Return']").click()
        time.sleep(5)
        try:
            element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f'{task_name}')
            tap_element_with_actions(self.driver, element)
        except Exception as e:
            print(f"Failed to mark task done '{task_name}':", e)

    def delete_task_with_task_name(self, task_name):

        xpath = f"//XCUIElementTypeOther[.//XCUIElementTypeOther[@name='{task_name}']]//XCUIElementTypeButton[@name='Delete']"
        try:
            self.driver.find_element("xpath", "//XCUIElementTypeButton[@name='Return']").click()
            time.sleep(3)
            element = self.driver.find_element(AppiumBy.XPATH, xpath)
            tap_element_with_actions(self.driver, element)
        except Exception as e:
            try:
                print('keyboad not found', e)
                element = self.driver.find_element(AppiumBy.XPATH, xpath)
                tap_element_with_actions(self.driver, element)
            except Exception as ex:
                print(f"Failed to delete task '{task_name}':", ex)

    def is_task_completed(self, task_name: str) -> bool:
        """
        Checks whether a given task is marked as completed based on UI changes.
        Returns True if the label or accessibility name indicates completion.
        """
        try:
            task_elements = self.driver.find_elements(
                AppiumBy.IOS_PREDICATE,
                f'name CONTAINS "{task_name}"'
            )
            if not task_elements:
                raise Exception(f"Task '{task_name}' not found in list")

            task_el = task_elements[0]
            label = task_el.get_attribute("label") or ""
            name = task_el.get_attribute("name") or ""

            if label.lower() in name.lower():
                return True
            # Customize this condition when the app includes some indication for completed task
            # if "✓" in label or "(Completed)" in label or "done" in name.lower():
            #     return True

            return False

        except Exception as e:
            print(f"[DEBUG] Error checking completion state: {e}")
            return False



def tap_element_with_actions(driver, element):
    location = element.location
    size = element.size

    x = location['x'] + size['width'] / 2
    y = location['y'] + size['height'] / 2

    driver.execute_script("mobile: tap", {
        "x": x,
        "y": y
    })


def safe_send_keys(self, element, text, max_retries=3):
        for _ in range(max_retries):
            try:
                element = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable(element))
                element.clear()

                # Try normal send_keys first
                element.send_keys(text)
                return True

            except Exception:
                try:
                    # Fallback to JavaScript if UI fails
                    element = self.driver.find_element(*element)
                    self.driver.execute_script(
                        "arguments[0].value = arguments[1];",
                        element, text
                    )
                    return True
                except Exception as e:
                    print(f"Retry failed: {str(e)}")
                    time.sleep(1)
        return False





