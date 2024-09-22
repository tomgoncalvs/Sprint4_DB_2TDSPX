from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt

# Configuração compartilhada
mongo = PyMongo()
bcrypt = Bcrypt()
