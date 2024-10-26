

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Location:
    id: int
    latitude: str
    longitude: str
    timestamp: datetime
    
        