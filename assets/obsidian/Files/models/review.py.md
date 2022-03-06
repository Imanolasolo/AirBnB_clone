File that contains the class Review that inherits from BaseModel

```

#!/usr/bin/python3

"""Defines the Review class."""

from models.base_model import BaseModel

class Review(BaseModel):

"""Represent a review.

Attributes:

place_id (str): The Place id.

user_id (str): The User id.

text (str): The text of the review.

"""

place_id = ""

user_id = ""

text = ""
```

-   `Review` (`models/review.py`):
    -   Public class attributes:
        -   `place_id`: string - empty string: it will be the `Place.id`
        -   `user_id`: string - empty string: it will be the `User.id`
        -   `text`: string - empty string

[[models]]
