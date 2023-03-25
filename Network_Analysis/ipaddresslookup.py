from scapy.all import *
import requests
#you have to mention the interface ID from which you want to capture the traffic
interface = "Realtek RTL8821CE 802.11ac PCIe Adapter"
def print_packet(packet):
    ip_layer = packet.getlayer(IP) 
    #print("[!] New Packet: {src} -> {dst}".format(src=ip_layer.src,dst=ip_layer.dst)) # Printing Source Ip and destination IP from captured Packet
    ip=ip_layer.src
    url = "https://www.virustotal.com/api/v3/ip_addresses/"+ip
    headers = {
        "accept": "application/json",
        "x-apikey": "6af5be89e41374da5aff499f73e8337b0dd2f768f2c78067f9d8d3126f62fed5"
    }
    response = requests.get(url, headers=headers)
    print(response.text)
    ip=ip_layer.dst
    url = "https://www.virustotal.com/api/v3/ip_addresses/"+ip
    headers = {
        "accept": "application/json",
        "x-apikey": "6af5be89e41374da5aff499f73e8337b0dd2f768f2c78067f9d8d3126f62fed5"
    }
    response = requests.get(url, headers=headers)
    print(response.text)
    #packet.show() # Show the details of every packet
sniff(iface=interface, filter="ip", prn=print_packet) # sniff command used to capture the packets, iface= above defined inerface, here filtered IP address, called function 

