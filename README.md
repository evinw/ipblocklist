# ipblocklist
Algorithm to detect blocked ip address and white list ips 

This algorithm uses he socket.inet_aton() function to check if the given IP address is a valid IPv4 address. If it is a valid IP address, it checks whether the address is in the block list. If it is in the block list, it raises a BlockedIPError exception, otherwise, it adds it to the whitelist. If the IP address is not a valid IPv4 address, it raises a ValueError exception.
