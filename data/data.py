from dataclasses import dataclass
from datetime import date


@dataclass
class Person:
    full_name: str = None
    first_name: str = None
    last_name: str = None
    email: str = None
    gender_index: int = None
    gender: str = None
    mobile_number: int = None
    date_of_birth: date = None
    subjects: str = None
    hobbie_index: int = None
    hobbie: str = None
    picture: str = None
    state: str = None
    city: str = None
    age: int = None
    salary: int = None
    department: str = None
    current_address: str = None
    permanent_address: str = None

@dataclass
class Date:
    day: str = None
    month: str = None
    year: str = None
    time: str = None