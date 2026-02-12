from data_models import Device, Interface, IPAddress


def convert_to_device_model(device_json, interfaces_json, ips_json):
    hostname = device_json["name"]
    role = device_json["role"]["name"]
    site = device_json["site"]["name"]

    primary_ip = device_json.get("primary_ip4") or device_json.get("primary_ip")
    mgmt_ip = primary_ip["address"] if primary_ip else None

    interfaces = [
        Interface(
            name=iface["name"],
            enabled=iface["enabled"],
            description=iface.get("description")
        )
        for iface in interfaces_json
    ]

    ip_addresses = [
        IPAddress(
            address=ip["address"],
            interface_name=ip["assigned_object"]["name"]
        )
        for ip in ips_json
    ]

    return Device(
        hostname=hostname,
        role=role,
        site=site,
        mgmt_ip=mgmt_ip,
        interfaces=interfaces,
        ip_addresses=ip_addresses
    )