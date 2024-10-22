import os
import sys

from NetworkSecurity.Exception.exception import NetworkSecurityException
from NetworkSecurity.Logger.logger import logging

from NetworkSecurity.Pipeline.training_pipeline import TrainingPipeline #class TrainingPipeline

def start_training():
    try:
        model_training = TrainingPipeline()
        model_training.run_pipeline()
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    
if __name__=='__main__':

    start_training() 
