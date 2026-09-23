import psutil

UPDATE_INTERVAL = 1

def show_metrics(cpu, ram, ram_used, ram_total, disk, disk_used, disk_total):
    print(f"\rCPU: {cpu:5.1f}% | "
          f"RAM: {ram:5.1f}% ({ram_used:.2f}/{ram_total:.2f}) GiB | "
          f"DISK: {disk:5.1f}% ({disk_used:.2f}/{disk_total:.2f} GiB)",
          end="",
          flush=True
          )

def bytes_to_gib(value):
    return value / (1024 **3)
    
def main():
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=UPDATE_INTERVAL)
            memory = psutil.virtual_memory()
            memory_used = bytes_to_gib(memory.used)
            memory_total = bytes_to_gib(memory.total)

            disk = psutil.disk_usage("/")
            disk_used = bytes_to_gib(disk.used)
            disk_total = bytes_to_gib(disk.total)

            show_metrics(
                cpu_usage, memory.percent,
                memory_used, memory_total,
                disk.percent, disk_used, disk_total
            )
    except KeyboardInterrupt:
        print("\nMonitor Stopped")

if __name__ == "__main__":
    main()