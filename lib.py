#!/usr/bin/env python3

from os import path as path

class Config:
    """Store information about a settings config"""

    def __init__(self, name: str, locations: list[str]):
        """Create a new config"""
        self.name = name
        self.locations = locations

    def validate(self) -> bool:
        for location in self.locations:

    def update_repo_files(self):
        pass

    def install_local_files(self):
        pass

    def _copy_location(self, from_loc: str, to_loc: str):
        """Do not use this function directly
        Use `update_repo_files` or `install_local_files` instead"""
        pass

def get_configs() -> list[Config]:
    """Read all JSON files from `./configs/`"""


