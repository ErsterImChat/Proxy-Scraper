import json
import os
import requests

# Executing Status Request
ProxyStatus = requests.get("https://api.proxyscrape.com/v2/?request=proxyinfo&simplified=true")


OnlyPS = input("Do you want to use all Proxie Sources? (else only ProxieScrape) (yes/no): \n")

# Setting Up Proxie Counter

proxystatusfile = open("proxiecountall.json", "w")
proxystatusfile.write(ProxyStatus.text)
proxystatusfile.close()



with open("proxiecountall.json") as file:
    ProxyStatus = json.load(file)

# Printing Proxy Counter

print(str(ProxyStatus["proxy_count"]) + " Proxies are avalible from ProxieScrape, other Sources cant be counted before scraping.\n")

# Removing Proxie Counter File

if os.path.exists("proxiecountall.json"):
    os.remove("proxiecountall.json")


# Getting Values for Request
HTTPS = ("yes")

TYPE = input("Which Type?: http,socks4,socks5,all: \n")

if TYPE == ("http"):
    HTTPS = input("Should the Proxys support https? (yes/no): \n")

if HTTPS == ("yes"):
    SSL = ("all")
else:
    SSL = ""

TIMEOUT = input("Which Timeout?: \n")

# Executing API Request (ProxyScrape)
ProxyAPI = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=" + TYPE + "&timeout=" + TIMEOUT + "&country=all&ssl=+" + SSL + "&anonymity=all")
print(ProxyAPI.text)

# Writing ProxyScrape-Proxies to File
outfile = open("proxies.txt", "w")
outfile.write(ProxyAPI.text)
outfile.close()

# Executing API Request (openproxylist.xyz)

if TYPE == ("all"):

    ProxyAPI2 = requests.get("https://api.openproxylist.xyz/http.txt")
    print(ProxyAPI2.text)

else:

    ProxyAPI2 = requests.get("https://api.openproxylist.xyz/" + TYPE + ".txt")
    print(ProxyAPI2.text)

outfile = open("proxies.txt", "a")
outfile.write(ProxyAPI2.text)
outfile.close()

# Deleting Empty Lines in File

output = ""
with open("proxies.txt") as f:
    for line in f:
        if not line.isspace():
            output += line

f = open("proxies.txt", "w")
f.write(output)
f.close()

#Counting Lines in File
num_lines = sum (1 for line in open('proxies.txt'))

print(str(num_lines) + " Proxies have been saved to proxies.txt\n")

input("Press Enter to close")
