import time

def background_task():
    time.sleep(5)
    print("Task completed using redis queue")