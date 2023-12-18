import random

#1
class RandomTaskGenerator:
    TASKS = [
        {"description": "Write a short poem", "time_estimate": 30},
        {"description": "Learn a new programming language", "time_estimate": 120},
        {"description": "Take a 30-minute walk", "time_estimate": 30},
        {"description": "Read a chapter of a book", "time_estimate": 45},
        {"description": "Cook a new recipe", "time_estimate": 60},
       
    ]

    def __init__(self, num_tasks=7):
        self.num_tasks = num_tasks

    def generate_random_tasks(self):
        random_tasks = random.sample(self.TASKS, min(self.num_tasks, len(self.TASKS)))
        return random_tasks


generator = RandomTaskGenerator(num_tasks=5)
random_tasks = generator.generate_random_tasks()

print("Random Tasks for the Week:")
for idx, task in enumerate(random_tasks, start=1):
    print(f"{idx}. {task['description']} (Approx. {task['time_estimate']} minutes)")
##############################################
    
#2
class WorkHoursCounter:
    def __init__(self):
        self.total_hours = 0
        self.tasks = []

    def add_task(self, task_name, hours_spent):
        self.tasks.append((task_name, hours_spent))
        self.total_hours += hours_spent

    def __iter__(self):
        self.current_task = 0
        return self

    def __next__(self):
        if self.current_task < len(self.tasks):
            task_name, hours_spent = self.tasks[self.current_task]
            self.current_task += 1
            return f"Task: {task_name}, Hours Spent: {hours_spent}"
        else:
            raise StopIteration

    def productivity_report(self):
        return f"Total Hours Spent: {self.total_hours}, Tasks Completed: {len(self.tasks)}"


work_counter = WorkHoursCounter()

work_counter.add_task("Coding", 3)
work_counter.add_task("Writing", 2)
work_counter.add_task("Meeting", 1)

for task in work_counter:
    print(task)

print(work_counter.productivity_report())    