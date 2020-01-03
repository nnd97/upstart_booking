class Config(object):
    # DEV MODE
    DEBUG = True
    VERSION = "1.0.0"
    STATIC_URL = "static"
    SQLALCHEMY_DATABASE_URI = 'postgresql://portuser:123456abcA@localhost:5432/portdb'
    AUTH_LOGIN_ENDPOINT = 'login'
    AUTH_PASSWORD_HASH = 'bcrypt'
    AUTH_PASSWORD_SALT = 'add_salt'
    SECRET_KEY = 'acndef'
    SESSION_COOKIE_SALT = 'salt_key'

    # STATIC_URL = 'https://upstart.vn/static/monitor/' + VERSION

    SESSION_COOKIE_DOMAIN = '.upstart.vn'
    SESSION_REDIS_URI = "redis://localhost:6379/5"
