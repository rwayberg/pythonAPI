from pydantic import BaseModel, Field

class Item(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float
    accepted: bool | None = False

class ItemUpdate(BaseModel):
    id: int
    name: str | None = None
    description: str | None = None
    price: float | None = None

    #@property
    #def ID(self) -> int:
    #    return self._id
    

# Testing Data
test_item_1 = Item(id=1, name="Test item 1", description="Test description 1", price=0.23, accepted=False)
test_item_2 = Item(id=2, name="Test item 2", description="Test description 2", price=35.67, accepted=False)
test_item_3 = Item(id=3, name="Test item 3", description="Test description 3", price=546.00, accepted=True)

test_items = [test_item_1, test_item_2, test_item_3]