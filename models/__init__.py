#!/usr/bin/python3
""" models directory magic method  __init__"""
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
