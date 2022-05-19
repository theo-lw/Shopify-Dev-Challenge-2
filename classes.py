from dataclasses import field
from marshmallow_dataclass import dataclass
from marshmallow.validate import Length, Range
import requests
import os

@dataclass
class City:
  id: int 
  name: str
  longitude: float
  latitude: float
  weather: str

@dataclass
class InventoryItem:
  id: int 
  name: str
  city: City

@dataclass
class InventoryCreateRequest:
  name: str = field(metadata={"validate": Length(min=1)})
  city_id: int

@dataclass
class InventoryDeleteRequest:
  id: int

@dataclass
class InventoryUpdateRequest:
  id: int
  name: str = field(metadata={"validate": Length(min=1)})
  city_id: int

@dataclass
class CityCreateRequest:
  name: str = field(metadata={"validate": Length(min=1)})
  longitude: float = field(metadata={"validate": Range(min=-180, max=180)})
  latitude: float = field(metadata={"validate": Range(min=-90, max=90)})

class CityCreator:
  def __init__(self):
    self.cache = {}

  def create_city(self, id: int, name: str, longitude: float, latitude: float) -> City:
    if (longitude, latitude) not in self.cache:
      r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={os.getenv("API_KEY")}')
      self.cache[(longitude, latitude)] = r.json()['weather'][0]['description']
      
    return City(id, name, longitude, latitude, self.cache[(longitude, latitude)])
    