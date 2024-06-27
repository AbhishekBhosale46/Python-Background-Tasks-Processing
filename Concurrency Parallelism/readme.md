Threading/Multiprocessing/Asyncio are used when you need simple, local concurrency and parallelism without involving external systems.

**1] Threading :** Threading allows us to run multiple threads (i.e smaller units of process) concurrently.

- Concurrency is achieved by running multiple threads within a single process.
- Suitable for I/O-bound tasks (e.g., network operations, file I/O).

**2] Multiprocessing :** Multiprocessing allows you to run multiple processes, which can take advantage of multiple CPU cores.

- Concurrency is achieved by running multiple processes, each with its own Python interpreter.
- Suitable for CPU-bound tasks (e.g., computation-heavy operations).

**3] Asyncio :** Asyncio is used for writing single-threaded concurrent code using coroutines, making it ideal for I/O-bound and high-level structured network code.

- Concurrency is achieved using asynchronous programming with coroutines.
- Suitable for I/O-bound tasks requiring high-level structured network code (e.g., web servers, web scraping).
- Efficiently handles thousands of I/O-bound operations without creating multiple threads/processes.