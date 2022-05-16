from dataclasses import field
from marshmallow_dataclass import dataclass
from marshmallow.validate import Length

@dataclass
class InventoryItem:
  id: int 
  name: str

@dataclass
class InventoryCreateRequest:
  name: str = field(metadata={"validate": Length(min=1)})

@dataclass
class InventoryDeleteRequest:
  id: int

@dataclass
class InventoryUpdateRequest:
  id: int
  name: str = field(metadata={"validate": Length(min=1)})

@dataclass
class Warehouse:
  id: int 
  name: str

@dataclass
class WarehouseCreateRequest:
  name: str = field(metadata={"validate": Length(min=1)})

@dataclass
class WarehouseInventory:
  warehouse_id: int
  warehouse_name: str
  number: int

@dataclass
class AssignToWarehouseRequest:
  inventory_id: int
  warehouse_id: int
  number: int

@dataclass
class InventoryForWarehouse:
  inventory_id: int
  inventory_name: str
  number: int