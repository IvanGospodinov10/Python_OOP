from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task) -> str:
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str) -> str:
        for t in self.tasks:
            if t.name == task_name:
                t.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        # removed_tasks = 0
        # for t in self.tasks[:]:
        #     if t.completed:
        #         removed_tasks += 1
        #         self.tasks.remove(t)
        # return f"Cleared {removed_tasks} tasks."
        curr_t_len = len(self.tasks)
        self.tasks = [t for t in self.tasks if not t.completed]
        return f"Cleared {curr_t_len - len(self.tasks)} tasks."

    def view_section(self):
        result = [f"Section {self.name}:"]
        for task in self.tasks:
            result.append(task.details())
        return "\n".join(result)
