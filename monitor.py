import psutil
from dataclasses import dataclass
from display import show_metrics
from history import save_metrics

def bytes_to_gib(value: int) -> float:
    return value / (1024 **3)

@dataclass
class SystemMetrics:
    cpu_percent: float
    ram_percent: float
    ram_used_gib: float
    ram_total_gib: float
    disk_percent: float
    disk_used_gib: float
    disk_total_gib: float

class SystemMonitor:
    def __init__(self, update_interval: float = 1, ram_threshold: float = 80):
        if update_interval <= 0:
            raise ValueError("Update interval must be greater than zero.")
        if not 0 <= ram_threshold <= 100:
            raise ValueError("RAM threshold must be between 0 and 100.")

        self.update_interval = update_interval
        self.ram_threshold = ram_threshold

    def collect_metrics(self) -> SystemMetrics:
        cpu_usage = psutil.cpu_percent(interval=self.update_interval)
        ram = psutil.virtual_memory()
        disk = psutil.disk_usage("/")

        return SystemMetrics(
            cpu_percent= cpu_usage,
            ram_percent= ram.percent,
            ram_used_gib= bytes_to_gib(ram.used),
            ram_total_gib= bytes_to_gib(ram.total),
            disk_percent= disk.percent,
            disk_used_gib= bytes_to_gib(disk.used),
            disk_total_gib= bytes_to_gib(disk.total),
        )

    def get_ram_alert(self, ram_percent):
        if ram_percent >= self.ram_threshold:
            return "WARNING: HIGH RAM USAGE"
        return ""


def main():
    monitor = SystemMonitor()
    try:
        while True:

            #Metrics
            metrics = monitor.collect_metrics()
            ram_alert = monitor.get_ram_alert(metrics.ram_percent)

            show_metrics(metrics, ram_alert)
            save_metrics(
                metrics.cpu_percent,
                metrics.ram_percent,
                metrics.disk_percent,
            )

    except KeyboardInterrupt:
        print("\nMonitor Stopped")

if __name__ == "__main__":
    main()
