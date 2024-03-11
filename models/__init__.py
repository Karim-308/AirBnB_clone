# models/__init__.py
""" models directory magic method  __init__"""
from models.engine.file_storage import FileStorage


FileStorage().reload()
