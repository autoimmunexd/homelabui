import psutil
import time

def get_bandwidth():
    # Get the network interfaces
    interfaces = psutil.net_io_counters(pernic=True)

    # Sleep for a short time
    time.sleep(1)

    # Get the network interfaces again after sleeping
    interfaces_after = psutil.net_io_counters(pernic=True)

    # Calculate bandwidth usage for each interface
    bandwidth = {}
    for interface, stats_before in interfaces.items():
        stats_after = interfaces_after[interface]
        sent_bytes = stats_after.bytes_sent - stats_before.bytes_sent
        recv_bytes = stats_after.bytes_recv - stats_before.bytes_recv
        sent_speed = sent_bytes / 1024 / 1024  # Convert to MB
        recv_speed = recv_bytes / 1024 / 1024  # Convert to MB
        bandwidth[interface] = {'sent_speed': sent_speed, 'recv_speed': recv_speed}
    print(bandwidth)
    return bandwidth