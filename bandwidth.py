import psutil
import time

def get_size(bytes):
    """
    Returns size of bytes in a nice format
    """
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024

def get_bandwidth():
    UPDATE_DELAY = 1  # in seconds

    # get the network I/O stats from psutil
    io = psutil.net_io_counters()
    # extract the total bytes sent and received
    bytes_sent, bytes_recv = io.bytes_sent, io.bytes_recv

    # create a dictionary to store bandwidth information
    bandwidth = {}

    while True:
        # sleep for `UPDATE_DELAY` seconds
        time.sleep(UPDATE_DELAY)
        # get the stats again
        io_2 = psutil.net_io_counters()
        # new - old stats get us the speed
        us, ds = io_2.bytes_sent - bytes_sent, io_2.bytes_recv - bytes_recv

        # store bandwidth information in the dictionary
        bandwidth['upload'] = get_size(io_2.bytes_sent)
        bandwidth['download'] = get_size(io_2.bytes_recv)
        bandwidth['upload_speed'] = get_size(us / UPDATE_DELAY) + '/s'
        bandwidth['download_speed'] = get_size(ds / UPDATE_DELAY) + '/s'

        # update the bytes_sent and bytes_recv for the next iteration
        bytes_sent, bytes_recv = io_2.bytes_sent, io_2.bytes_recv

        # return the bandwidth dictionary
        return bandwidth

# Uncomment the line below if you want to actually call the function
# bandwidth_info = get_bandwidth()
# print(bandwidth_info)
