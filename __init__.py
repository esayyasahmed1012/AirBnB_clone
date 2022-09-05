#!/usr/bin/python3
""" init for class Storage """
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
