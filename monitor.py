import psutil
from display import show_metrics
from history import save_metrics

UPDATE_INTERVAL = 1
RAM_ALERT_THRESHOLD = 80

def bytes_to_gib(value):
    return value / (1024 **3)

def get_ram_alert(ram_percent):
    if ram_percent >= RAM_ALERT_THRESHOLD:
        return "ATENÇÃO: USO ELEVADO DE RAM"
    return ""
    
def main():
    try:
        while True:
            #CPU
            cpu_usage = psutil.cpu_percent(interval=UPDATE_INTERVAL)

            #RAM
            memory = psutil.virtual_memory()
            memory_used = bytes_to_gib(memory.used)
            memory_total = bytes_to_gib(memory.total)
            ram_alert = get_ram_alert(memory.percent)

            #DISK
            disk = psutil.disk_usage("/")
            disk_used = bytes_to_gib(disk.used)
            disk_total = bytes_to_gib(disk.total)

            #Metrics
            show_metrics(
                cpu_usage, memory.percent,
                memory_used, memory_total,
                disk.percent, disk_used, disk_total,
                ram_alert
            )
            save_metrics(cpu_usage, memory.percent, disk.percent)

    except KeyboardInterrupt:
        print("\nMonitor Stopped")

if __name__ == "__main__":
    main()