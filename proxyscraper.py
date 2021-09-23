import requests
import json


#Executing Status Request

#Executing API Request
ProxyStatus = requests.get("https://api.proxyscrape.com/v2/?request=proxyinfo&simplified=true")


proxystatusfile = open("proxiecountall.json", "w")
proxystatusfile.write(ProxyStatus.text)
proxystatusfile.close()



with open("proxiecountall.json") as file:
    ProxyStatus = json.load(file)

print(str(ProxyStatus["proxy_count"]) + " Proxies are avalible\n")


#Getting Values for Request
HTTPS=("yes")

TYPE = input("Which Type?: http,socks4,socks5,all: \n")

if TYPE == ("http"):
    HTTPS = input("Should the Proxys support https? (yes/no): \n")


if HTTPS == ("yes"):
    SSL=("all")
else:
    SSL= ""

TIMEOUT = input("Which Timeout?: \n")



#Executing API Request
ProxyAPI = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=" + TYPE + "&timeout=" + TIMEOUT +"&country=all&ssl=+" + SSL + "&anonymity=all")
print(ProxyAPI.text)

#Writing Proxies to File
outfile = open("proxies.txt", "w")
outfile.write(ProxyAPI.text)
outfile.close()

#Deleting Empty Lines in File

output = ""
with open("E:\PycharmProjects\FalixRestartV2\proxies.txt") as f:
    for line in f:
        if not line.isspace():
            output += line

f = open("proxies.txt", "w")
f.write(output)

print("Proxies have been saved to proxies.txt")
input("Press Enter to close")
