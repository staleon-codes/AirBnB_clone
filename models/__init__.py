#!/usr/bin/python3
"""Script to initialize package"""
from models.engine import file_storage
storage = file_storage.FileStorage()
storage.reload()
