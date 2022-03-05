#!/usr/bin/python3
# File: __init__.py
# Authors: Imanol Asolo - Alex Arévalo
# email(s): <3848@holbertonschool.com>
#           <3915@holbertonschool.com>

"""Module of initialize for models package directory"""
from models.engine.file_storage import FileStorage

"""Space where attributes and methods are stored"""
storage = FileStorage()
storage.reload()
