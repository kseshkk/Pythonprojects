from dataclasses import dataclass

@dataclass
class City:
    name: str
    latitude: float
    longitude: float
    distance: float = 0