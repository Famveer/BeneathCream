import os
from pydantic_settings import BaseSettings
import ast
from dotenv import load_dotenv
load_dotenv()

class Config(BaseSettings):

    DATA_PATH: str = os.getenv('DATA_PATH')
    MODEL_PATH: str = os.getenv('MODEL_PATH')
    
    PROCESS_TXT: bool = ast.literal_eval(os.getenv("PROCESS_TXT", "True"))
    CHUNK_SIZE: int = int(os.getenv('CHUNK_SIZE', "100000"))
    CSV_SEP: str = os.getenv("CSV_SEP", "\\")
    KEYWORD_SEP: str = os.getenv("KEYWORD_SEP", " FAMVEERFAMVEERFAMVEER ")
    TOPIC_SEARCH: str = os.getenv("TOPIC_SEARCH", "cve")
    ANY_FORMAT: bool = ast.literal_eval(os.getenv("ANY_FORMAT", "True"))
    
    RANDOM_STATE: int = int(os.getenv('RANDOM_STATE', "42"))
    TOP_K_FEATURES: int = int(os.getenv('TOP_K_FEATURES', "15"))
