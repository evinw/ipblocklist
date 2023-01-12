import socket

class BlockedIPError(Exception):
    pass

def is_ip_blocked(ip_address: str, block_list: list, whitelist: list) -> None:
    try:
        socket.inet_aton(ip_address)
        if ip_address in block_list:
            raise BlockedIPError(f"IP address {ip_address} is in the block list.")
        elif ip_address not in whitelist:
            whitelist.append(ip_address)
            print(f"IP address {ip_address} has been added to the whitelist.")
    except socket.error:
        raise ValueError("Invalid IP address.")

block_list = ["192.168.1.1", "10.0.0.1"]
whitelist = ["192.168.1.2", "10.0.0.2"]
ip_address = "192.168.1.3"

try:
    is_ip_blocked(ip_address, block_list, whitelist)
except BlockedIPError as e:
    print(e)
except ValueError as e:
    print(e)
