import scapy.all as scapy

def scan(ip):
    # Create an ARP request packet
    arp_request = scapy.ARP(pdst=ip)
    
    # Create an Ethernet frame to encapsulate the ARP request
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    
    # Combine the Ethernet frame and ARP request
    arp_request_broadcast = broadcast/arp_request
    
    # Send the packet and receive the response
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    # List to store the results
    clients_list = []
    
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    
    return clients_list

def print_result(results_list):
    print("IP Address\t\tMAC Address\n-----------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])

# Get the target IP range from the user
target_ip = input("Enter the target IP range (e.g., 192.168.1.1/24): ")

# Perform the scan
scan_result = scan(target_ip)

# Print the results
print_result(scan_result)
