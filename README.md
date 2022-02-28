# 0x00. AirBnB clone - The console
<div style="text-align: justify">

Thank you for visiting this repository which contain the `first step` towards building first `full web application`: the `AirBnB clone`. 
<div style="text-align: justify">
	
The project currently only implements the back-end `console`. The goal of the project is to deploy on your server a simple copy of the `AirBnB website`.

![hbnb](https://github.com/Alexoat76/AirBnB_clone/blob/main/assets/hbnb-logo.png?raw=true)
	
# Getting Started :running:	
<div style="text-align: justify">
	
## Table of Contents
* [About](#about)
* [Requirements](#requirements)
* [Tasks](#tasks)
* [Credits](#credits)

	
## About
	
The tasks in this repository cover:
	
- Set up in place a `parent class` (called `BaseModel`) to take care of the `initialization`, `serialization` and `deserialization` of future instances.
- Create a simple flow of serialization/deserialization: Instance <-> `Dictionary` <-> `JSON string` <-> file.
- Create `all classes` used for AirBnB (`User`, `State`, `City`, `Place`…) that inherit from `BaseModel`.
- Create the first abstracted storage engine of the project: File `storage`.
- Create all `unittests` to `validate` all classes and storage engine.

	
## Requirements 

## Resources :books:

**Read or watch** :

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/80px-Google_2015_logo.svg.png)](https://www.google.com/search?q=AirBnB+clone+-+The+console&ei=eh8dYprkLtCawbkPs7uoCA&ved=0ahUKEwiaidyMjqP2AhVQTTABHbMdCgEQ4dUDCA4&uact=5&oq=AirBnB+clone+-+The+console&gs_lcp=Cgdnd3Mtd2l6EANKBAhBGAFKBAhGGABQAFgAYPYLaAFwAHgAgAEAiAEAkgEAmAEAwAEB&sclient=gws-wiz)

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Logo_of_YouTube_%282015-2017%29.svg/70px-Logo_of_YouTube_%282015-2017%29.svg.png)](https://www.youtube.com/playlist?list=PLlLHfkTcnvmPOp6jv_89tRpJUMFrP-Wbi)
	
	
- [Python packages](https://docs.python.org/3.4/tutorial/modules.html#packages)	
- [AirBnB clone](https://www.airbnb.com.co/?_set_bev_on_new_domain=1646059050_MmMwYzYwMzAyZmM4)	
- [Python abstract classes](https://blog.teclado.com/python-abc-abstract-base-classes/)
- [cmd module](https://docs.python.org/3.4/library/cmd.html)
- [uuid module](https://docs.python.org/3.4/library/uuid.html)
- [datetime](https://docs.python.org/3.4/library/datetime.html)	
- [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)	
- [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)	
- [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

	
## General :page_with_curl:
	
- Allowed editors: `vi`, `vim`, `emacs`.
- All files will be compiled on `Ubuntu 20.04` LTS using `python3`.
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/python3`.
- A `README.md` file, at the root of the folder of the project is mandatory.
- The `code` should use the `pycodestyle` (version 2.7.*)
- All files must be executable.
- The length of files will be tested using `wc`.	
- All modules should have a documentation `(python3 -c 'print(__import__("my_module").__doc__)')`
- All classes should have a documentation `(python3 -c 'print(__import__("my_module").MyClass.__doc__)')`
- All functions (inside and outside a class) should have a documentation `(python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')`

## Python Unit Tests :pushpin:
<div style="text-align: justify">

- Allowed editors: `vi`, `vim`, `emacs`.
- All files should end with a new line.	
- All test files should be inside a folder `tests`.
- You have to use the unittest module.
- All test files should be python files `(extension: .py)`.
- All test files and folders should start by `test_`.
- The file organization in the tests folder should be the same as your project.
- `e.g.`, For `models/base_model.py`, unit tests must be in: `tests/test_models/test_base_model.py`.
- `e.g.`, For `models/user.py`, unit tests must be in: `tests/test_models/test_user.py`.
- All tests should be executed by using this command: `python3 -m unittest discover tests`.
- You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base_model.py`.
- All modules should have a documentation `(python3 -c 'print(__import__("my_module").__doc__)')`.
- All classes should have a documentation `(python3 -c 'print(__import__("my_module").MyClass.__doc__)')`.
- All functions (inside and outside a class) should have a documentation `(python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')`.
	
## Installation :computer:
	
- Clone this repository: `git clone "https://github.com/Alexoat76/AirBnB_clone"`	
- Access AirBnb directory: `cd AirBnB_clone.`
	
## Usage :pushpin:
	
### Execution: :floppy_disk:
	
The shell should `work` like this in `interactive mode`:
	
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```	

But also in `non-interactive mode`:

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```	

	
## Console Commands :pushpin:
	
**`console.py`** - The console contains the entry point of the command interpreter. List of commands this console supports:
-   **`quit`**  - Exits console.
-   **`create`**  - Creates a new **`instance`** of `BaseModel`, saves it (to the `JSON` file) and prints the `id`.
-   **`destroy`**  - Deletes an **`instance`** based on the class name and `id` (save the change into the `JSON` file).
-   **`show`**  - Prints the string representation of an **`instance`** based on the class name and `id`.
-   **`all`**  - Prints all string representation of all **`instances`** based or not on the class name.
-   **`update`**  - Updates an **`instance`** based on the class name and id by adding or updating attribute (save the change into the `JSON` file).


## Credits

## Author(s):blue_book:

Work is owned and maintained by 
	**`Imanol Asolo`**  and **`Alex Arévalo`**.

<3848@holbertonschool.com>

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/25px-Octicons-mark-github.svg.png)](https://github.com/Imanolasolo)
[![M](https://upload.wikimedia.org/wikipedia/fr/thumb/c/c8/Twitter_Bird.svg/25px-Twitter_Bird.svg.png)](https://twitter.com/jjusturi)
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/25px-LinkedIn_logo_initials.png)](https://www.linkedin.com/in/imanol-asolo-5ba9b42a/)

<3915@holbertonschool.com>
	
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/25px-Octicons-mark-github.svg.png)](https://github.com/Alexoat76)
[![M](https://upload.wikimedia.org/wikipedia/fr/thumb/c/c8/Twitter_Bird.svg/25px-Twitter_Bird.svg.png)](https://twitter.com/aoarevalot)
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/25px-LinkedIn_logo_initials.png)](https://www.linkedin.com/in/Alexoat76/)


## Acknowledgments :mega: 

### **`Holberton School`** (*providing guidance*)
	
This program was written as part of the curriculum for Holberton School.
Holberton School is a campus-based full-stack software engineering program
that prepares students for careers in the tech industry using project-based
peer learning. For more information,  please visit [this link](https://www.holbertonschool.com/).
![Brand](https://assets.website-files.com/6105315644a26f77912a1ada/610540e8b4cd6969794fe673_Holberton_School_logo-04-04.svg)
