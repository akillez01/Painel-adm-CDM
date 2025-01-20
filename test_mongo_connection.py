import os
import django
from pymongo import MongoClient
from decouple import config

# Configurar o ambiente Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projeto.settings")
django.setup()

def test_mongo_connection():
    try:
        # Obter a URI do MongoDB a partir do arquivo .env
        mongo_uri = config('MONGO_URI')
        
        # Conectar ao MongoDB
        client = MongoClient(mongo_uri)
        
        # Listar as coleções no banco de dados
        db_name = config('MONGO_DB')
        db = client[db_name]
        collections = db.list_collection_names()
        
        print(f"Conectado ao MongoDB. Coleções no banco de dados '{db_name}': {collections}")
    except Exception as e:
        print(f"Erro ao conectar ao MongoDB: {e}")

if __name__ == "__main__":
    test_mongo_connection()