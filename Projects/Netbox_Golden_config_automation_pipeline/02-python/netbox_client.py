#import moden HTTP client for Python

from urllib import response
import httpx

#setting Netbox URL, Token and device imput for variables
netboox_url = "http://localhost:8003/api/"
netbox_token = ""
device = input("Which device do you want from netbox?")

# setting headers for HTTP request to Netbox API

headers = {
    "Authorization": f"Token {netbox_token}",
    "Accept": "application/json",
}

def get_device():
    url = f"{netboox_url}dcim/devices/?name={device}"
    response = httpx.get(url, headers=headers)
    response.raise_for_status()
    data = response.json().get("results", [])
    print(data)


get_device()

