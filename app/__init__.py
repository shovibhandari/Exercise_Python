"""
Package initiaizer
"""
import configparser
from pathlib import Path

# Base path of Project
BASE = Path(__file__).parent.parent.absolute()

# Getting config parser
config = configparser.ConfigParser()
config.read(Path(BASE).joinpath('settings.ini'))
