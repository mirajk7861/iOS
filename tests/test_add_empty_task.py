
from pages.todo_page import TodoPage
import allure

@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Task Management")
@allure.story("Prevent adding empty task")
def test_empty_task_not_added(driver):
    todo = TodoPage(driver)
    with allure.step("Count tasks before attempting to add empty task"):
        initial_count = len(todo.get_tasks())

    with allure.step("Leave input empty and tap 'Add Task'"):
        todo.add_task("")


    with allure.step("Count tasks after tapping add button"):
        updated_count = len(todo.get_tasks())

    with allure.step("Verify task count remains same"):
        assert updated_count == initial_count, \
            f"Expected no new task, but found {updated_count - initial_count} added."
