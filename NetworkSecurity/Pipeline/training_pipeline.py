import os
import sys

from NetworkSecurity.Exception.exception import NetworkSecurityException
from NetworkSecurity.Logger.logger import logging

from NetworkSecurity.Components.data_ingestion import DataIngestion
from NetworkSecurity.Components.data_validation import DataValidation
from NetworkSecurity.Components.data_transformation import DataTransformation
from NetworkSecurity.Components.model_trainer import ModelTrainer
from NetworkSecurity.Components.model_evaluation import ModelEvaluation
from NetworkSecurity.Components.model_pusher import ModelPusher


from NetworkSecurity.Entity.config_entity import (
    TrainingPipelineConfig,
    DataIngestionConfig, 
    DataValidationConfig, 
    DataTransformationConfig, 
    ModelTrainerConfig,
    ModelEvaluationConfig, 
    ModelPusherConfig
    )
                                                  
from NetworkSecurity.Entity.artifact_entity import (
    DataIngestionArtifact, 
    DataValidationArtifact, 
    DataTransformationArtifact, 
    ModelTrainerArtifact,
    ModelEvaluationArtifact, 
    ModelPusherArtifact
    )                                         


class TrainingPipeline:
    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()
    
    def start_data_ingestion(self):
        try:
            self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config) #DataIngestionConfig will come first when we start Data Ingestion
            logging.info("Starting Data Ingestion")
            data_ingestion=DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact= data_ingestion.initiate_data_ingestion()
            logging.info(f"Data ingestion completed and artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact


        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifact): #previous component output i.e artifact needs to be passed to current component
        try:
            data_validation_config = DataValidationConfig(training_pipeline_config=self.training_pipeline_config)
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact,data_validation_config=data_validation_config)
            data_validation_artifact = data_validation.initiate_data_validation()
            return data_validation_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def start_data_transformation(self, data_validation_artifact:DataValidationArtifact):#previous component output i.e artifact needs to be passed to current component
        try:
            data_transformation_config=DataTransformationConfig(training_pipeline_config=self.training_pipeline_config)
            data_transformation=DataTransformation(data_validation_artifact=data_validation_artifact, data_transformation_config=data_transformation_config)
            data_transformation_artifact=data_transformation.initiate_data_transformation()
            return data_transformation_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def start_model_trainer(self, data_transformation_artifact:DataTransformationArtifact)->ModelTrainerArtifact:
        try:
            self.model_trainer_config: ModelTrainerConfig = ModelTrainerConfig(
                training_pipeline_config=self.training_pipeline_config)
            
            model_trainer = ModelTrainer(
                data_transformation_artifact=data_transformation_artifact,
                model_trainer_config=self.model_trainer_config,
            )

            model_trainer_artifact = model_trainer.initiate_model_trainer()
            return model_trainer_artifact

        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def start_model_evaluation(self, data_validation_artifact: DataValidationArtifact, 
                               model_trainer_artifact: ModelTrainerArtifact):
        try:
            model_evaluation_config:ModelEvaluationConfig=ModelEvaluationConfig(training_pipeline_config=self.training_pipeline_config)
            model_eval=ModelEvaluation(model_evaluation_config,data_validation_artifact,model_trainer_artifact)
            model_eval_artifact=model_eval.initiate_model_evaluation()
            return  model_eval_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def start_model_pusher(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            #print(data_ingestion_artifact)
            data_validation_artifact=self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            #print(data_validation)
            data_transformation_artifact=self.start_data_transformation(data_validation_artifact=data_validation_artifact) #simple feature engineering
            #print(data_transformation_artifact)
            model_trainer_artifact = self.start_model_trainer(data_transformation_artifact=data_transformation_artifact)
            self.start_model_evaluation(model_trainer_artifact=model_trainer_artifact, )
        except Exception as e:
            raise NetworkSecurityException(e, sys)

       
        

