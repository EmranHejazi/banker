from pydantic import BaseModel
from typing import Optional

class Customer(BaseModel):
    id: int
    national_code: str
    full_name: Optional[str]
    mobile: Optional[str]
    age: Optional[int]
    city_name: Optional[str]
    province_name: Optional[str]
    birth_city: Optional[str]
    birth_province: Optional[str]
    gender: Optional[str]
