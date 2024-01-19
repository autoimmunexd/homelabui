import shutil

def storage():
    path = "/mnt/thevault"
    stat = shutil.disk_usage(path)
    total, used, free = stat
    total_gb = total / (1024 ** 3)
    used_gb = used / (1024 ** 3)
    free_gb = free / (1024 ** 3)
    storage_data = {
        "Total Space": f"{total_gb} GB",
        "Used Space": f"{used_gb} GB",
        "Free Space": f"{free_gb} GB"
        }
    
    return storage_data