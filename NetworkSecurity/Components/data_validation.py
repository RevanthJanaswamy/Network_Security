from NetworkSecurity.Constant.training_pipeline import SCHEMA_FILE_PATH
from NetworkSecurity.Entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from NetworkSecurity.Entity.config_entity import DataValidationConfig
from NetworkSecurity.Exception.exception import NetworkSecurityException 
from NetworkSecurity.Logger.logger import logging 
from NetworkSecurity.Utils.main_utils.utils import read_yaml_file,write_yaml_file
from scipy.stats import ks_2samp #It will 2 samples of data and will tell you how much they are deviated from each other
import pandas as pd
import os,sys


class DataValidation    :
    def __init__(self):
        pass

    def validate_number_of_columns(self, dataframe: pd.DataFrame) ->bool:
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def is_numerical_column_exists(self,dataframe: pd.DataFrame) ->bool:
         try:
            pass
         except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    @staticmethod
    def read_data(file_path) -> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def detect_dataset_drift(self, base_df, current_df, threshold= 0.05) ->bool:
         try:
            pass
         except Exception as e:
            raise NetworkSecurityException(e,sys)
         
    def initiate_data_validation(self):
        try:
            self.read_data()
            self.validate_number_of_columns()
            self.is_numerical_column_exists()
            self.detect_dataset_drift()

        except Exception as e:
            raise NetworkSecurityException(e,sys)
            
        


        
    
