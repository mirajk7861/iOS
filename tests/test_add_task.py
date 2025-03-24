
from pages.todo_page import TodoPage
import allure

@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Task Management")
@allure.story("verify task is added successfully ")


def test_add_task(driver):
    todo = TodoPage(driver)
    taskName = 'Buy groceries'
    with allure.step("Add new task"):
        todo.add_task(taskName)

    tasks = todo.get_tasks()
    with allure.step("verify the task is added successfully"):
        assert any(taskName in task.text for task in tasks)

    todo.delete_task_with_task_name(taskName)

