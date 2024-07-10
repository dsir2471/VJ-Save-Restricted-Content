import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "29015149"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "2eb6df7291e3adbc8e02ae230f5876ec")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://rhlkc9304:IwlPrP7KqboZCfXN@cluster0.5bjhh3o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
