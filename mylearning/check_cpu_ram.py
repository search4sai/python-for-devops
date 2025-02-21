import psutil

def get_resource_usage():
    """
    Retrieves and prints CPU, memory, and disk usage statistics.
    """

    # CPU usage
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_percent}%")

    # Memory usage
    virtual_memory = psutil.virtual_memory()
    print(f"Total Memory: {virtual_memory.total / (1024 ** 3):.2f} GB")
    print(f"Available Memory: {virtual_memory.available / (1024 ** 3):.2f} GB")
    print(f"Used Memory: {virtual_memory.used / (1024 ** 3):.2f} GB")
    print(f"Memory Usage Percentage: {virtual_memory.percent}%")

    # Disk usage
    disk_usage = psutil.disk_usage('/')  # Use '/' for root directory
    print(f"Total Disk Space: {disk_usage.total / (1024 ** 3):.2f} GB")
    print(f"Used Disk Space: {disk_usage.used / (1024 ** 3):.2f} GB")
    print(f"Free Disk Space: {disk_usage.free / (1024 ** 3):.2f} GB")
    print(f"Disk Usage Percentage: {disk_usage.percent}%")

if __name__ == "__main__":
    get_resource_usage()
