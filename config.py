import os
import logging
class Config:
    
    API_ID = int(os.environ.get("API_ID", "26796802"))
    API_HASH = os.environ.get("API_HASH", "b8cc96196eb105c33d8ce193e5efff5c")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6590624540:AAGOkHMG-k4ykdex2pz3LOOE6CGMZIU-c7s") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "Forward_BOT") 
    OWNER_ID = os.environ.get("OWNER_ID", "1474271232")
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Eln:Chaik2501@cipid.4whqkv9.mongodb.net/")
    DATABASE_NAME = os.environ.get("DATABASE_NAME","Eln")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Forward_data')
    SESSION = os.environ.get("SESSION", "Forward_Session")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001829851975"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", None)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
