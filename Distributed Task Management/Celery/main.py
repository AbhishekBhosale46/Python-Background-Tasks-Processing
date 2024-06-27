from tasks import background_task

result = background_task.delay()

print("Task is running in the background")
print(result.get())