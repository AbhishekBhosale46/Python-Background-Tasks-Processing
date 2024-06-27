import multiprocessing
import time

def background_task():
    time.sleep(5)
    print("Task completed using multiprocessing")

def main():
    process = multiprocessing.Process(target=background_task)
    process.start()
    print("Main process continues to run...")

if __name__ == "__main__":
    main()