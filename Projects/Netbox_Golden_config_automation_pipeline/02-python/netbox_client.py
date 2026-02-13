#import moden HTTP client for Python
from data_converter import convert_to_device_model
from urllib import response
import httpx


#setting Netbox URL, Token and device imput for variables
netbox_url = "http://localhost:8003/api/"
netbox_token = ""
device = input("Which device do you want from netbox?")

# setting headers for HTTP request to Netbox API

headers = {
    "Authorization": f"Token {netbox_token}",
    "Accept": "application/json",
}

def get_device():
    url = f"{netbox_url}dcim/devices/?name={device}"
    response = httpx.get(url, headers=headers)
    response.raise_for_status()
    results = response.json().get("results", [])
    print("\nRAW Netbox Response:")
    print("======================")
    print(results)
    return results[0] if results else None


get_device()



#raw_interfaces = get_interfaces(raw_device["id"])
#raw_ips = get_ip_addresses(raw_device["id"])

device = convert_to_device_model(raw_device, raw_interfaces, raw_ips)

print("\n==============================")
print(" Structured Pydantic Model")
print("==============================\n")
print(device)

print("\nHostname:", device.hostname)
print("Role:", device.role)
print("Site:", device.site)
print("Mgmt IP:", device.mgmt_ip)
