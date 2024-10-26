

from dataclasses import dataclass


@dataclass
class Client:
    id: int
    first_name: str
    full_name: str
    insurance_id: str
    