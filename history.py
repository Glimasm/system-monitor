import csv
from datetime import datetime
from pathlib import Path

HISTORY_FILE = Path(__file__).with_name("history.csv")

def save_metrics(cpu, ram, disk):
    needs_header = (
        not HISTORY_FILE.exists()
        or HISTORY_FILE.stat().st_size == 0
    )
    with HISTORY_FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if needs_header:
            writer.writerow(["timestamp", "cpu_percent", "ram_percent", "disk_percent"])

        writer.writerow([
            datetime.now().isoformat(timespec="seconds"),
            cpu,
            ram,
            disk,
        ])