
def show_metrics(metrics, ram_alert):
    print(f"\rCPU: {metrics.cpu_percent:5.1f}% | "
          f"RAM: {metrics.ram_percent:5.1f}%"
          f"({metrics.ram_used_gib:.2f}/{metrics.ram_total_gib:.2f}) GiB | "
          f"DISK: {metrics.disk_percent:5.1f}%"
          f"({metrics.disk_used_gib:.2f}/{metrics.disk_total_gib:.2f} GiB) | "
          f"{ram_alert}\033[K",
          end="",
          flush=True
          )
