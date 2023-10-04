import time


def callback(result):
    print(f"Async task completed with result: {result}")


def async_task(cb):
    # Simulate a long-running task
    time.sleep(10)
    cb("Task Done!")


if __name__ == "__main__":
    print("Starting async task...")
    async_task(callback)
    print("Continuing with other tasks...")
