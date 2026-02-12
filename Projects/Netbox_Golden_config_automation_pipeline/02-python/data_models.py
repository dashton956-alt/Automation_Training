from pydantic import BaseModel
from typing import List, Optional

class Interface(BaseModel):
    name: str
    enabled: bool
    description: Optional[str]

class IPAddress(BaseModel):    
    address: str    
    interface_name: str

class device(BaseModel):
    hostname:str
    role:str
    site:str
    mgmt_ip:Optional[str]
    device_type: str
    interfaces: List[Interface]
    ip_addresses: List[IPAddress]