Celery is a powerful, production-ready asynchronous task queue/job queue based on distributed message passing. It's perfect for real-time operations but also supports scheduling.

- Distributed task queue framework that can use multiple brokers like Redis or RabbitMQ.
- Complex, large-scale distributed task management, supporting periodic tasks, retries, and chaining of tasks.
- Highly scalable, supports advanced features like task scheduling, result backend, monitoring.
- To run multiple workers on different machines the 'tasks.py' file must be present on each worker machine and the server itself
- command to start worker : *celery -A tasks worker --pool=solo -l info*