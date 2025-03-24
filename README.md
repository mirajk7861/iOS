**iOS App Automation for React Native To-Do App**
This project automates UI tests for a React Native iOS To-Do application using:
•	Appium + Python
•	Pytest for test execution
•	Allure for visual test reports
 
**Environment**
•	macOS: Ventura 15.3
•	Python: 3.9.6
•	Appium: Latest (installed via npm)
•	iOS Simulator: iPhone 15 (iOS 17.2)
•	Appium Inspector: Used for element discovery
 
**Features Covered**
Test Case	Description
test_add_task	Verifies tasks can be added
test_delete_task	Ensures tasks can be removed
test_mark_task_done	Marks a task as completed (strikeout)
test_empty_task_not_added	Negative test for empty task input

 **Test Summary**
Metric	Value
Total Tests	4
Passed	4 ✅
Failed	0 ❌
Environment	iOS Simulator
Report Tool	Allure
✍ Command Used
pytest --alluredir=allure-results
allure generate allure-results -o allure-report --clean
 
**Issues & Fixes**
Issue	Resolution
Allure report only showed "Loading..."	Installed Allure CLI via Homebrew and regenerated
App not launching in Simulator	Ensured .app path is correct and Simulator is booted
Unable to detect strike-through	Compared before/after element trees using Inspector
Keyboard blocked UI	Used driver.hide_keyboard() and tapped Return key
 
**Suggestions for Improvement**
1.	Better Accessibility IDs: Use accessibilityLabel or testID for React Native.
2.	Task Completion Attribute: Add clear attribute/state for completed tasks.
3.	Validation Message: Show feedback for empty input (toast or label).
4.	Test Coverage: 
 Editing tasks
 Bulk delete


 
**Run Locally**
1. Install Dependencies
pip install -r requirements.txt
2. Start Appium Server
appium server --use-drivers=xcuitest
3. Run Tests
pytest tests/
4. Generate Allure Report
pytest --alluredir=allure-results
allure generate allure-results -o allure-report --clean
open allure-report/index.html


 
**Folder Structure**


<img width="120" alt="image" src="https://github.com/user-attachments/assets/cea1df3b-97f9-4ee0-9737-5a421fa74ccf" />

 
**Sample Report**

 <img width="1432" alt="image" src="https://github.com/user-attachments/assets/5dac509f-8115-40eb-bf51-7433076780bc" />
