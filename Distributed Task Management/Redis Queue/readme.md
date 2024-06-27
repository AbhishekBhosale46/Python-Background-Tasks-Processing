RQ is a simple Python library for queueing jobs and processing them in the background with workers. It is backed by Redis.

- Uses Redis to store task queues.
- Simple task queue management and background processing with workers.
- May not be suitable for very large-scale distributed systems.
- Works only with linux systems, cannot work on windows
- command to start worker : *rq worker queue_name*