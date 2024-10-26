
from dataclasses import dataclass


@dataclass
class Address:
    id: int
    client_id: str
    label: str
    cep: str
    address: str
    country: str
    state: str
    uf: str
    city: str
    number: str
    
    
    