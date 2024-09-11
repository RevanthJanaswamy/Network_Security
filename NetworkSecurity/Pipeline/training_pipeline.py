import os
import sys

from NetworkSecurity.Exception.exception import NetworkSecurityException
from NetworkSecurity.Logger.logger import loggging

from NetworkSecurity.Components.data_ingestion import DataIngestion
from NetworkSecurity.Components.data_validation import DataValidation
from NetworkSecurity.Components.data_transformation import DataTransformation
from NetworkSecurity.Components.model_trainer import ModelTrainer
from NetworkSecurity.Components.model_evaluation import ModelEvaluation
from NetworkSecurity.Components.model_pusher import ModelPusher

from NetworkSecurity.Entity.config_entity import (
    TrainingPipeline,
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
        pass
    
    def start_training(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)