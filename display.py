
def show_metrics(cpu, ram, ram_used, ram_total, disk, disk_used, disk_total, ram_alert):
    print(f"\rCPU: {cpu:5.1f}% | "
          f"RAM: {ram:5.1f}% ({ram_used:.2f}/{ram_total:.2f}) GiB | "
          f"DISK: {disk:5.1f}% ({disk_used:.2f}/{disk_total:.2f} GiB) | "
          f"{ram_alert}\033[K",
          end="",
          flush=True
          )
