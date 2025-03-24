from pages.todo_page import TodoPage
import allure

@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Task Management")
@allure.story("verify successful deletion of task")
def test_delete_task(driver):
    todo = TodoPage(driver)
    taskName = 'sample'
    with allure.step("Add new task"):
        todo.add_task(taskName)
    tasks = todo.get_tasks()
    with allure.step("Verify if task is added successfully"):
        assert any(taskName in task.text for task in tasks)

    with allure.step("Delete the newly added task"):
        todo.delete_task_with_task_name(taskName)
    tasks = todo.get_tasks()
    with allure.step("Verify that the task is deleted successfully"):
        assert not any(taskName in task.text for task in tasks), " Task still present after deletion!"

