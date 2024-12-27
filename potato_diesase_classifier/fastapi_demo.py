from fastapi import FastAPI
from enum import Enum

### to create a direct ui of this code just type the /docs after the localhost


app = FastAPI()

@app.get("/hello/{name}")
async def hello(name):
    return f"fast api demo code {name}"

# get (read data order )
# post (create data order)
# put (update data)
# delete (delete data)


class AvailableCuisine(str,Enum):
    indian = "indian"
    american = "american"
    italian = "italian"
    
food_items = {
    'indian':["samosa","dal-chawal","pani puri"],
    "american":["hot dog"],
    "italian":["Raviol"]
}


coupon_code = {
    1:"10%",
    2:"20%",
    3:"30"
}


valid_cuisine = food_items.get("keys")
@app.get("/get_items/{cuisine}")
async def get_items(cuisine:AvailableCuisine):
    # # if we use flask then we use should like as 
    # if cuisine not in valid_cuisine:
    #     return f"SUpported cuisien are {valid_cuisine}"
    return food_items.get(cuisine)


@app.get("/get_coupon_code/{code}")
async def get_coupon_code(code:int):
    return {"discount_amount":coupon_code.get(code)}