#parts of following code have been taken form Santi Peñate-Vera 
#(https://stackoverflow.com/questions/207234/list-of-ip-addresses-hostnames-from-local-network-in-python)
import os
import socket    
import multiprocessing
import subprocess
import os
import nmap

def select_host(active_host):
    print(active_host)
    print("Tell which host you wish to connect to")
    x = int(input())
    return active_host[x-1]
    

def check_port(all_host,default_port):
    active = []
    nm = nmap.PortScanner()
    for host in all_host:
        nm.scan(str(host),str(default_port))
        if(nm[str(host)]['tcp'][default_port]['state']=='open'):
            active.append((host,socket.gethostbyaddr(str(host))[0]))
    return active


def pinger(job_q, results_q):
    """
    Do Ping
    :param job_q:
    :param results_q:
    :return:
    """
    DEVNULL = open(os.devnull, 'w')
    while True:

        ip = job_q.get()

        if ip is None:
            break

        try:
            subprocess.check_call(['ping', '-c1', ip],
                                  stdout=DEVNULL)
            results_q.put(ip)
        except:
            pass


def get_my_ip():
    """
    Find my IP address
    :return:
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket.setdefaulttimeout(1)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


def map_network(pool_size=255):
    """
    Maps the network
    :param pool_size: amount of parallel ping processes
    :return: list of valid ip addresses
    """

    ip_list = list()

    # get my IP and compose a base like 192.168.1.xxx
    ip_parts = get_my_ip().split('.')
    base_ip = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2] + '.'

    # prepare the jobs queue
    jobs = multiprocessing.Queue()
    results = multiprocessing.Queue()

    pool = [multiprocessing.Process(target=pinger, args=(jobs, results)) for i in range(pool_size)]

    for p in pool:
        p.start()

    # cue hte ping processes
    for i in range(1, 255):
        jobs.put(base_ip + '{0}'.format(i))

    for p in pool:
        jobs.put(None)

    for p in pool:
        p.join()

    # collect he results
    while not results.empty():
        ip = results.get()
        ip_list.append(ip)

    return ip_list


if __name__ == '__main__':

    print('Mapping...')
    #lst = map_network()
    selected_host = select_host(check_port(map_network(),12345))
    print("You have selected the following host: ",selected_host)
