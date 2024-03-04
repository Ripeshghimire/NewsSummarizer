from src.NewsSummarizer.logger import logging
import os
from src.NewsSummarizer.exception import CustomException
import urllib.request as request 
from pathlib import Path
class DataIngestionConfig:
    def __init__(self,data_ingestion_config):
        self.data_ingestion_config = data_ingestion_config
    def download_file(self):
