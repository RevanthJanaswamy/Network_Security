import os
import sys
import pandas as pd
import numpy as np

"""
Defining common constant variable for training pipeline
"""
TARGET_COLUMN: str = "Result"
PIPELINE_NAME: str = "Network_Security"
ARTIFACT_DIR: str = "Artifacts"
FILE_NAME: str = "NetworkData.csv"


TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"
MODEL_FILE_NAME = "model.pkl"
SCHEMA_FILE_PATH = os.path.join("data_schema", "schema.yaml")
SCHEMA_DROP_COLS = "drop_columns"
SAVED_MODEL_DIR =os.path.join("saved_models")



"""
Data Ingestion related constants start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str = "NetworkData"
DATA_INGESTION_DATABASE_NAME: str = "KNAcademy"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2




"""
Data Validation related constants start with DATA_VALIDATION VAR NAME
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_VALID_DIR: str = "validated"
DATA_VALIDATION_INVALID_DIR: str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"


"""
Data Transformation related constants start with DATA_TRANSFORMATION VAR NAME
"""



"""
Model trainer related constants start with MODEL_TRAINER VAR NAME
"""


