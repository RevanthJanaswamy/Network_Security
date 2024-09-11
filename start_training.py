import os
import sys

from NetworkSecurity.Exception.exception import NetworkSecurityException
from NetworkSecurity.Logger.logger import loggging

from NetworkSecurity.Pipeline.training_pipeline import TrainingPipline #class TrainingPipeline

def start_training():
    try:
        pass
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    
if __name__=='__main__':

    start_training()
