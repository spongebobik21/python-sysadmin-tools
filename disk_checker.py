import shutil

# Get disk usage information for the root directory "/" (in bytes)
total, used, free = shutil.disk_usage("/")

# Convert bytes to gigabytes for convenience (1GB = 1024^3 bytes)
total_gb = total / (1024 ** 3)
used_gb = used / (1024 ** 3)
used_percent = (used / total) * 100

# Display formatted information in the console
print("--- Disk Usage Check ---")
print(f"Total: {total_gb:.1f} GB")
print(f"Used: {used_gb:.1f} GB ({used_percent:.1f}%)")

# Check critical threshold (e.g., 90)
THRESHOLD = 90

if used_percent > THRESHOLD:
    print(f"[WARNING] Disk usage exceeds {THRESHOLD}%!")
else:
    print("[OK] Disk status is normal")