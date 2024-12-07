import sys
from datetime import datetime as dt
import socket
import threading
import concurrent.futures
import os
import platform
from sys import platform

class UnsupportedPlatform(Exception):
    pass
#platform.system()
if "linux" in platform:
   print("linux")
elif "darwin" in platform:
   print("mac")
elif "win" in platform:
   print("windows")
else:
   raise UnsupportedPlatform

if len(sys.argv) == 2:
    try:
        ip = socket.gethostbyname_ex(sys.argv[1])
    except socket.gaierror:
        ip = []
else:
    print("You must enter a host to scan")
    print("Syntax: python3 scanner.py 127.0.0.1 or googl.com")
    sys.exit()


print (f"Found targets: {ip[2]}")
try:

    def portscan(host, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        try:
            result = s.connect_ex((host, port))
            if result == 0:
                openports.append(port)
            s.close()

        except KeyboardInterrupt:
            print(f"""User ended scan
Ports found so far:{openports}""")
            sys.exit()

        except socket.gaierror:
            print("Hostname could not be resolved")
            sys.exit()

        except socket.error:
            print("Could not connect to server")
            sys.exit()  

    for i in ip[2]:
        openports = []
        print("Scanning: "+i)
        def pscan(port):
            portscan(i, port)
        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            executor.map(pscan, range(0,8200))
        print(f"{i}:{openports}")

except KeyboardInterrupt:
    print("User ended scan")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()

except socket.error:
    print("Could not connect to server")
    sys.exit()
