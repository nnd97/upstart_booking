from application.extensions import apimanager

from .model import Exceptions

apimanager.create_api(
    Exceptions,
    methods = ["GET", "POST", "PUT", "DELETE"],
    url_prefix='/api',
    collection_name = "exception"
)
