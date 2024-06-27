from redis import Redis
from rq import Queue
from task import background_task

q = Queue('my_queue', connection=Redis())
job = q.enqueue(background_task)

print("Task is enqueued")