from .model import Country, City

from application.extensions import apimanager


apimanager.create_api(
    Country,
    methods = ["GET", "POST", "PUT", "DELETE"],
    url_prefix='/api/v1',
    collection_name = "country"
)

apimanager.create_api(
    City,
    methods = ["GET", "POST", "PUT", "DELETE"],
    url_prefix='/api/v1',
    collection_name = "city"
)