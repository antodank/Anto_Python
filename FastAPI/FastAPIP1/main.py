
from fastapi import FastAPI, HTTPException
from datetime import datetime
import time
import platform
from models import ItemPayload


app = FastAPI()
grocery_list: dict[int, ItemPayload] = {
    1: ItemPayload(item_id=1000100, item_name="Lindt", quantity=10, description="Cocoa Rich", price=2.5),
    2: ItemPayload(item_id=1000101, item_name="Ferrero Rocher", quantity=6, description="Almond Rich", price=1.8),
    3: ItemPayload(item_id=1000102, item_name="Cadbury", quantity=4, description="Organic berries", price=3.0),
    4: ItemPayload(item_id=1000103, item_name="Toblerone", quantity=8, description="Fresh green grapes", price=2.2),
    5: ItemPayload(item_id=1000104, item_name="Godiva", quantity=5, description="Juicy oranges", price=2.8),
    6: ItemPayload(item_id=1000105, item_name="Hershey's", quantity=12, description="Sweet milk chocolate", price=1.5),
}

@app.get("/")
def read_root():
    return {"Message": "Hello World"}

@app.get("/getCurrentTimeZone")
def get_current_time_zone():
    """
    Get the current timezone of the system where the API is running.
    Works on both Windows and Linux systems.
    
    Returns:
        dict: Contains timezone name, UTC offset, and other timezone information
    """
    import os
    
    # Get timezone name
    current_time = datetime.now()
    
    # Try to get timezone from environment or system
    if os.name == 'nt':  # Windows
        timezone_name = time.tzname[time.daylight]
    else:  # Linux/Unix
        # Try TZ environment variable first
        timezone_name = os.environ.get('TZ', 'UTC')
        # If not set, try to get from /etc/timezone
        if timezone_name == 'UTC' and os.path.exists('/etc/timezone'):
            try:
                with open('/etc/timezone', 'r') as f:
                    timezone_name = f.read().strip()
            except:
                pass
        # Fallback to time module
        if timezone_name == 'UTC':
            timezone_name = time.tzname[0]
    
    # Get UTC offset in seconds
    utc_offset_seconds = time.timezone if time.daylight == 0 else time.altzone
    utc_offset_hours = -utc_offset_seconds / 3600
    
    return {
        "timezone_name": timezone_name,
        "utc_offset_hours": utc_offset_hours,
        "utc_offset_seconds": -utc_offset_seconds,
        "is_dst": bool(time.daylight),
        "current_time": current_time.isoformat(),
        "platform": platform.system(),
        "os_name": os.name
    }

@app.get("/items/{item_id}", 
         summary="Get item by ID",
         description="Retrieve a specific grocery item by its ID. " \
         "Optional field parameter to get specific fields only.",
         response_description="The requested grocery item")
def read_item(item_id: int, field: str | None = None):
    # Search for item by item_id field in the ItemPayload objects
    item = None
    
    for key, value in grocery_list.items():
        if value.item_id == item_id:
            item = value
            break
    
    # If item not found, raise exception
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found.")

    # Return only specific fields based on q parameter
    # Example: /items/1?q=price or /items/1?q=name
    if field == "price":
        return {"item_id": item_id, "price": item.price}
    elif field == "name":
        return {"item_id": item_id, "name": item.item_name}
    elif field == "summary":
        return {"item_id": item_id, "name": item.item_name, "price": item.price}
    
    # Return full item if no specific query
    return {"item": item}

# Route to list all items
@app.get("/items", summary="List all grocery items", response_description="A list of all grocery items")
def list_items() -> dict[str, dict[int, ItemPayload]]:
    return {"items": grocery_list}

# Route# Route to add a item
#@app.post("/items/addItem")
#def add_item(item: ItemPayload):
@app.post("/items/{item_name}/{quantity}/{price}", summary="Add a new grocery item", response_description="The added grocery item")
def add_item(item_name: str, quantity: int,price: float = 0.0):
    # Validate inputs
    if quantity <= 0:
        raise HTTPException(status_code=400, detail="Quantity must be greater than 0.")

    # Check if item already exists by item_name
    existing_item_key = None
    for key, value in grocery_list.items():
        if value.item_name.lower() == item_name.lower():
            existing_item_key = key
            break
    # If item exists, increase its quantity
    if existing_item_key is not None:
        grocery_list[existing_item_key].quantity += quantity
        if price != 0.0:
            grocery_list[existing_item_key].price = price  # Update price if needed
        return {"message": "Item quantity increased successfully", "item": grocery_list[existing_item_key]}
    else:
        new_id = max(grocery_list.keys()) + 1 if grocery_list else 1
        new_item = ItemPayload(
            item_id=new_id + 1000100,
            item_name=item_name,
            quantity=quantity,
            description="",
            price=price
        )
        grocery_list[new_id] = new_item

    return {"message": "Item added successfully", "item": new_item}

# Route to remove some quantity of a specific item by ID
@app.delete("/items/{item_id}/{quantity}", summary="Remove quantity of a grocery item", response_description="Result of the removal operation")
def remove_quantity(item_id: int, quantity: int):
    # Check if item already exists by item_name
    existing_item_key = None
    for key, value in grocery_list.items():
        if value.item_id == item_id:
            existing_item_key = key
            break
    # If item exists, increase its quantity
    if existing_item_key is not None:
        if grocery_list[existing_item_key].quantity > quantity:
            grocery_list[existing_item_key].quantity -= quantity
        else:
            raise HTTPException(status_code=400, detail="Insufficient quantity to remove.")
        
    else:
        raise HTTPException(status_code=404, detail="Item not found.")
    
    return {"result": f"For Item {item_id}, the quantity has been reduced by {quantity}."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
