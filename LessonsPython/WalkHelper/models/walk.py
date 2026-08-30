from dataclasses import dataclass
from datetime import datetime

@dataclass
class Walk:
    id: int
    user_id: int
    city_name: str
    place_name: str
    walk_date: datetime
    status: bool