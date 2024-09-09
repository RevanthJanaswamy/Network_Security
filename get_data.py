import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()
MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)



import certifi
ca = certifi.where()
import pandas as pd
import numpy as np 
import pymongo

from NetworkSecurity.Exception.exception import NetworkSecurityException

from NetworkSecurity.Logger.logger import logging 

class NetworkDataExtract:

    def __init__(self):

        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def csv_to_json_converter(self, file_path):

        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop= True, inplace= True)
            records=list(json.loads(data.T.to_json()).values())
            return records

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def pushing_data_to_mongodb(self,records,Database,Collection):

        try:
            self.Database=Database
            self.records=records
            self.Collection=Collection
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.Database = self.mongo_client[self.Database]
            self.Collection = self.Database[self.Collection]
            self.Collection.insert_many(self.records)
            return len(self.records)
        

        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
if __name__== '__main__':
    file_path = "./Network_Data/NetworkData.csv"
    Database="KNAcademy"
    Collection="NetworkData"
    networkobj= NetworkDataExtract()
    records = networkobj.csv_to_json_converter(file_path)
    noofrecords=networkobj.pushing_data_to_mongodb(records,Database,Collection)
    print(noofrecords)

        

        


    


        