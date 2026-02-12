# settings.py
from pathlib import Path

# Notebook runs from repo root
BASE_DIR = Path().resolve()
print(BASE_DIR)

# Centralized data directory
DATASETS_DIR = BASE_DIR/"datasets"
print(DATASETS_DIR)

# Individual datasets
VEHICLE_EMISSIONS = DATASETS_DIR / "vehicle_emissions.csv"
DIABETES = DATASETS_DIR / "diabetes.csv"
HOUSING = DATASETS_DIR / "Housing.csv"
IRIS = DATASETS_DIR / "Iris.csv"
SPAM = DATASETS_DIR / "spam.csv"
WINE = DATASETS_DIR / "WineQT.csv"
TITANIC = DATASETS_DIR / "Titanic.csv"

print("settings file executed successfully")
