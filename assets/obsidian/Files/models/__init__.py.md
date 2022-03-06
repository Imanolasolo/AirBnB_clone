- Initialization file for engine directory
- Usage: For file storage when they are created.

```
#!/usr/bin/python3

"""__init__ magic method for models directory"""

from models.engine.file_storage import FileStorage

storage = FileStorage()

storage.reload()

```

[[models]]