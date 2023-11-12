#!/usr/bin/python3
"""Initializes the package."""

from models.engine.file_storage import FileStorage

def main():
    """Main function."""
    # Create an instance of FileStorage
    storage = FileStorage()

    # Reload data if available
    storage.reload()

if __name__ == "__main__":
    main()
