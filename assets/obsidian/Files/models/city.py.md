File containing class City that inherits from BaseModel

```
#!/usr/bin/python3

"""Defines the City class."""

from models.base_model import BaseModel

class City(BaseModel):

"""Represent a city.

Attributes:

state_id (str): The state id.

name (str): The name of the city.

"""

state_id = ""

name = ""
```

-   -   Public class attributes:
        -   `state_id`: string - empty string: it will be the `State.id`
        -   `name`: string - empty string

[[models]]
