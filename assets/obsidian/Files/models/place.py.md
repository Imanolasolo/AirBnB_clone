File that contains class Place that inherits from BaseModel

```
#!/usr/bin/python3

"""Defines the Place class."""

from models.base_model import BaseModel

class Place(BaseModel):

"""Represent a place.

Attributes:

city_id (str): The City id.

user_id (str): The User id.

name (str): The name of the place.

description (str): The description of the place.

number_rooms (int): The number of rooms of the place.

number_bathrooms (int): The number of bathrooms of the place.

max_guest (int): The maximum number of guests of the place.

price_by_night (int): The price by night of the place.

latitude (float): The latitude of the place.

longitude (float): The longitude of the place.

amenity_ids (list): A list of Amenity ids.

"""

city_id = ""

user_id = ""

name = ""

description = ""

number_rooms = 0

number_bathrooms = 0

max_guest = 0

price_by_night = 0

latitude = 0.0

longitude = 0.0

amenity_ids = []

```

-   Public class attributes:
    -   `city_id`: string - empty string: it will be the `City.id`
    -   `user_id`: string - empty string: it will be the `User.id`
    -   `name`: string - empty string
    -   `description`: string - empty string
    -   `number_rooms`: integer - 0
    -   `number_bathrooms`: integer - 0
    -   `max_guest`: integer - 0
    -   `price_by_night`: integer - 0
    -   `latitude`: float - 0.0
    -   `longitude`: float - 0.0
    -   `amenity_ids`: list of string - empty list: it will be the list of `Amenity.id` later

[[models]]