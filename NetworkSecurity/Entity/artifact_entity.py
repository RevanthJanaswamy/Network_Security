from dataclasses import dataclass
#from NetworkSecurity.Constant import training_pipeline 


@dataclass
class DataIngestionArtifact:
      trained_file_path:str
      test_file_path:str

@dataclass
class DataValidationArtifact:
      def __init__(self): 
            pass
      
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