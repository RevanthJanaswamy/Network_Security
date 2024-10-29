from dataclasses import dataclass
#from NetworkSecurity.Constant import training_pipeline 


@dataclass
class DataIngestionArtifact:
      trained_file_path:str
      test_file_path:str

@dataclass
class DataValidationArtifact:
      validation_status: bool
      valid_train_file_path: str
      valid_test_file_path: str
      invalid_train_file_path: str
      invalid_test_file_path: str
      drift_report_file_path: str

      
@dataclass
class DataTransformationArtifact:
      def __init__(self): 
            pass

@dataclass
class ModelTrainerArtifact:
      def __init__(self): 
            pass
      
@dataclass
class ModelEvaluationArtifact:
      def __init__(self): 
            pass
@dataclass
class ModelPusherArtifact:
      def __init__(self): 
            pass

@dataclass
class ClassificationMetricArtifact:
      def __init__(self): 
            pass