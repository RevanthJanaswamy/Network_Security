from datetime import datetime
import os
from NetworkSecurity.Constant import training_pipeline 

print(training_pipeline.ARTIFACT_DIR) #define some sort of constant (variables) to stramline this pipline
                                      #Constants are defined using capital letters 

# from NetworkSecurity.Logger.logger import logging 
# from NetworkSecurity.Exception.exception import NetworkSecurityException

class TrainingPipelineConfig:
      def __init__(self): 
            pass
           
class DataIngestionConfig:

    def __init__(self): 

        # try:
            pass 
        # except Exception as e:
        #   raise NetworkSecurityException(e,sys)

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
