from application.extensions import apimanager

from .model import Port

apimanager.create_api(
    Port,
    methods = ["GET", "POST", "PUT", "DELETE"],
    url_prefix='/api',
    collection_name = "port"
)
