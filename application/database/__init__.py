from gatco_sqlalchemy import SQLAlchemy
import redis

db = SQLAlchemy()
redisdb = redis.StrictRedis(host='localhost', port=6379, db=5)

def init_database(app):
    db.init_app(app)
