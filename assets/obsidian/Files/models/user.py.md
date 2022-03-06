File that contains class `User` that inherits from `BaseModel`

```
#!/usr/bin/python3

"""Defines the User class."""

from models.base_model import BaseModel

class User(BaseModel):

"""Represent a User.

Attributes:

email (str): The email of the user.

password (str): The password of the user.

first_name (str): The first name of the user.

last_name (str): The last name of the user.

"""

email = ""

password = ""

first_name = ""

last_name = ""

```

-   Public class attributes:
    -   `email`: string - empty string
    -   `password`: string - empty string
    -   `first_name`: string - empty string
    -   `last_name`: string - empty string

[[models]]