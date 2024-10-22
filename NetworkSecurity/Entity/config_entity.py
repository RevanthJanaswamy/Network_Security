from datetime import datetime
import os
from NetworkSecurity.Constant import training_pipeline 

print(training_pipeline.PIPELINE_NAME)
print(training_pipeline.ARTIFACT_DIR) #define some sort of constant (variables) to stramline this pipline
                                      #Constants are defined using capital letters 
                                      #ARTIFACT_DIR defined in __init__.py in training_pipeline folder

# from NetworkSecurity.Logger.logger import logging 
# from NetworkSecurity.Exception.exception import NetworkSecurityException

class TrainingPipelineConfig: #data_ingestion comes under training pipeline
      def __init__(self, timestamp = datetime.now()): 
            timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")
            self.pipeline_name=training_pipeline.PIPELINE_NAME
            self.artifact_name=training_pipeline.ARTIFACT_DIR

            self.artifact_dir = os.path.join(self.artifact_name, timestamp)

            self.timestamp: str = timestamp #object variable


           
class DataIngestionConfig:

    def __init__(self, training_pipeline_config:TrainingPipelineConfig): #training_pipeline_config is the object of  
                                                                         #TrainingPipelineConfig class

        """
        All the variables defined in capitals are constants defined in constants folder
        """    
        self.data_ingestion_dir: str = os.path.join(
                training_pipeline_config.artifact_dir, training_pipeline.DATA_INGESTION_DIR_NAME # DATA_INGESTION_DIR_NAME is a constant defined in 
                                                                                                  #constants folder (training_pipeline subfolder)
            )
        self.feature_store_file_path: str = os.path.join(
                self.data_ingestion_dir, training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR, training_pipeline.FILE_NAME
            )
        self.training_file_path: str = os.path.join(
                self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TRAIN_FILE_NAME
            )
        self.testing_file_path: str = os.path.join(
                self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TEST_FILE_NAME
            )
        self.train_test_split_ratio: float = training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION
        self.collection_name: str = training_pipeline.DATA_INGESTION_COLLECTION_NAME
        self.database_name: str = training_pipeline.DATA_INGESTION_DATABASE_NAME


        
         
class DataValidationConfig:
      def __init__(self): 
            pass
            
class DataTransformationConfig:
      def __init__(self): 
            pass

class ModelTrainerConfig:
      def __init__(self): 
            pass

class ModelEvaluationConfig:
      def __init__(self): 
            pass
      
class ModelPusherConfig:
      def __init__(self): 
            pass
