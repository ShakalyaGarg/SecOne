from socket import AF_INET
from socket import SOCK_STREAM
from socket import socket
from concurrent.futures import ThreadPoolExecutor
def test_port_number(host, port):
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.settimeout(3)
        try:
            sock.connect((host, port))
            return True
        except:
            return False
def port_scan(host, ports):
    print(f'Scanning {host}')
    with ThreadPoolExecutor(len(ports)) as executor:
        results = executor.map(test_port_number, [host]*len(ports), ports)
        for port,is_open in zip(ports,results):
            if is_open:
                print(f'> {host}:{port} open'
HOST = '127.0.0.1'
PORTS = range(8889)
port_scan(HOST, PORTS)
