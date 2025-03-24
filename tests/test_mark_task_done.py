from pages.todo_page import TodoPage
import allure

@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Task Management")
@allure.story("verify successful deletion of task")

def test_mark_task_done(driver):
    todo = TodoPage(driver)
    taskName = 'Buy groceries'
    with allure.step("Add new task"):
        todo.add_task(taskName)
    tasks = todo.get_tasks()
    with allure.step("verify task is added successfully"):
        assert any(taskName in task.text for task in tasks)
    with allure.step("try to mark task done"):
        todo.mark_task_completed(taskName)
    with allure.step("Verify task is marked done "):
        assert todo.is_task_completed(taskName), "Task is not marked completed"
    todo.delete_task_with_task_name(taskName)
