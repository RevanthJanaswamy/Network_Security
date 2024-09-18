from NetworkSecurity.Exception.exception import NetworkSecurityException
from NetworkSecurity.Logger.logger import logging 

# Configuration of component and artifact generation
from NetworkSecurity.Entity.config_entity import DataIngestionConfig
from NetworkSecurity.Entity.artifact_entity import DataIngestionArtifact

import os
import sys
import pandas
import numpy
import pymongo
from typing import List

from dotenv import load_dotenv
load_dotenv()
MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

class DataIngestion:
    
    def __init__(self):
       
       try:
          pass
       
       except Exception as e:
          raise NetworkSecurityException(e,sys)
       
    def export_collection_as_dataframe(self):
       
       try:
          database_name= self.data_ingestion.config.database_name
          collection_name= self.data_ingestion.config.collection_name
          self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
       
       except Exception as e:
          raise NetworkSecurityException(e,sys)
       
    def export_data_into_feature_store(self):
       
       try:
          pass
       
       except Exception as e:
          raise NetworkSecurityException(e,sys)
       
    def split_data_as_train_test(self):
       
       try:
          pass
       
       except Exception as e:
          raise NetworkSecurityException(e,sys)
       
    def initiate_data_ingestino(self):
       
       try:
          pass
       
       except Exception as e:
          raise NetworkSecurityException(e,sys)  
