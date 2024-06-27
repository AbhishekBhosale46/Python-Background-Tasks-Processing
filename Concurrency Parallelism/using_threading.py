import threading
import time

def background_task():
    time.sleep(5)
    print("Task completed using threading")

def main():
    thread = threading.Thread(target=background_task)
    thread.start()
    print("Main thread continues to run...")

if __name__ == "__main__":
    main()