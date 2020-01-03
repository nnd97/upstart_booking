from application.extensions import apimanager
from .model import Booking
# from gatco.exceptions import ServerError
from application.components.base.view import verify_access

apimanager.create_api(Booking,
    methods=['GET', 'POST', 'DELETE', 'PUT'],
    url_prefix='/api',
    # preprocess=dict(GET_SINGLE=[verify_access],
    #                 GET_MANY=[verify_access],
    #                 POST=[verify_access],
    #                 PUT_SINGLE=[verify_access]),
    collection_name='booking')